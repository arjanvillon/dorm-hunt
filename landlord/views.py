from django.http import JsonResponse
from django.contrib import messages
from django.utils.html import escape

from datetime import date
import datetime


from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, CreateView, DetailView)
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist



# SECTION Import Forms
from landlord.forms import PropertyForm, ReminderForm, AddTenantForm, AddExpenseForm

#SECTION Import Models
from landlord.models import Property, Reminder, AddTenant, Expenses, History
from user.models import User, UserProfile
from tenant.models import Application, MessageRoom

# Create your views here.
class LandlordListView(ListView):
    template_name = 'landlord/landlord_home.html'
    model = Property

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['property_numbers'] = Property.objects.all().filter(owner=self.request.user).count()
        return context

    def get_queryset(self):
        return Property.objects.all().filter(owner=self.request.user)

class LandlordProperties(TemplateView):
    template_name = 'landlord/landlord_properties.html'

class PropertyCreateView(CreateView):
    form_class = PropertyForm
    model = Property

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.slots = form.instance.capacity
        return super().form_valid(form)

class PropertyDetailView(DetailView):
    model = Property

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        this_property = get_object_or_404(Property, pk=pk)
        try:
            room = MessageRoom.objects.get(dorm=this_property)
        except ObjectDoesNotExist:
            room_name = this_property.name.replace(' ', '').lower()
            print(room_name)

            room = MessageRoom.objects.create(name=room_name, dorm=this_property)
            room.members.add(this_property.owner)

        context = super().get_context_data(**kwargs)
        context["room"] = room 
        return context
    


class LandlordMessages(ListView):
    template_name = 'landlord/landlord_messages.html'
    model = Property

    def get_queryset(self):
        return Property.objects.all().filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        properties = self.request.user.property_set.all()

        application_list = []
        active_applications = []
        room_list = []

        try:
            for p in properties:
                # applications = Application.objects.filter(dorm=p, is_approved=False, is_disapproved=False)
                applications = p.application_set.filter(is_approved=False, is_disapproved=False)

                if len(applications) > 0:
                    active_applications.append(p.name)
                    print(active_applications)

                # room_list.append(room)
                for application in applications:
                    application_list.append(application)
            room_list = MessageRoom.objects.filter(members=self.request.user)
            print(room_list)
            application_count = len(application_list)
        except ObjectDoesNotExist:
            application_list = ''
            active_applications = ''
            application_count = 0
            room_list = 0

        context = super().get_context_data(**kwargs)
        context["application_list"] = application_list
        context["active_applications"] = active_applications
        context["application_count"] = application_count
        context["room_list"] = room_list
        return context

def approve_application(request, pk):
    application = get_object_or_404(Application, pk=pk)
    application.approve()
    return redirect('landlord:landlord_messages')

def disapprove_application(request, pk):
    application = get_object_or_404(Application, pk=pk)
    application.disapprove()
    return redirect('landlord:landlord_messages')


class LandlordIndividualMessages(TemplateView):
    template_name = 'landlord/landlord_ind_messages.html'

# Reminders

class ReminderCreateView(CreateView):
    form_class = ReminderForm
    model = Reminder

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        property_list = Property.objects.filter(owner=self.request.user)
        context['property_list'] = property_list
        
        return context
    
    def form_valid(self, form):
        # print('hello')
        return super().form_valid(form)


# Add to Tenant
class TenantAddCreateView(CreateView):
    model = AddTenant
    form_class = AddTenantForm

    def get_context_data(self, **kwargs):
        properties = Property.objects.filter(owner=self.request.user)

        context = super(TenantAddCreateView, self).get_context_data(**kwargs)
        context['properties'] = properties
        return context
    

    def form_valid(self, form):        
        try:
            query = User.objects.get(email=form.instance.account_user)
            print(query)

            try:
                tenant = AddTenant.objects.get(account_user=form.instance.account_user)
                messages.add_message(self.request, messages.INFO, 'The email you entered is already a part of a dormitory.')
                return redirect('landlord:add_tenant')
            except ObjectDoesNotExist:
                form.instance.account = query
                this_property = Property.objects.get(pk=form.instance.dorm.pk)
                this_property.slots -= 1
                this_property.save()
                room = MessageRoom.objects.get(dorm=this_property)
                room.members.add(query)
                print(this_property)
                print(room.members.all())

        except ObjectDoesNotExist:
            messages.add_message(self.request, messages.INFO, 'The email you entered is not yet a user of this application. Do advise your tenant to sign up to our application for your convenience. Thank you!')
            return redirect('landlord:add_tenant')
        return super().form_valid(form)

# NOTE for viewing purposes only
class Payment(TemplateView):
    template_name = 'landlord/payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        properties = Property.objects.filter(owner=user)
        tenants = AddTenant.objects.all()
        month_today = datetime.datetime.now().strftime("%B")
        # now=datetime.datetime.now()
        # now_formatted = now.strftime("%Y-%m-%d")
        
        expenses = Expenses.objects.all()

        for expense in expenses:
            for tenant in tenants:
                if tenant.dorm == expense.property_name:
                    if expense.repeat == True:
                        tenant.expense_balance = expense.amount
                        tenant.expense_is_paid = False
                        print('HEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
                        tenant.save()
                    else:     
                        print('FAAAALSEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
            expense.repeat = False
            expense.save()

        context['expenses'] = expenses
        context['property_numbers'] = properties.count()
        context['property_list'] = properties
        context['tenants'] = tenants
        context['month_today'] = month_today

        return context

def mark_tenant_paid(request, pk):
    tenant = get_object_or_404(AddTenant, pk=pk)
    if request.method == "POST":
        amount = request.POST.get('amount')
        tenant.paid(int(amount))

        history = History.objects.create(tenant=tenant.account, dorm=tenant.dorm, amount=amount)

    # tenant.paid(tenant.dorm.price)
    return redirect('landlord:payment')


def due_date(request):
    properties = Property.objects.filter(owner=request.user)

    for p in properties:
        tenants = p.addtenant_set.all()
        for tenant in tenants:
            tenant.unpaid(p.price)
    
    return redirect('landlord:landlord_messages')

def remove_tenant(request, pk):
    tenant = get_object_or_404(AddTenant, pk=pk)
    room = MessageRoom.objects.get(dorm=tenant.dorm)
    dorm = Property.objects.get(pk=tenant.dorm.pk)

    if room.members.filter(pk=tenant.account.pk).exists():
        room.members.remove(tenant.account)
    else:
        print('none')
        
    dorm.slots += 1
    dorm.save()
    print(dorm.slots)
    tenant.delete()

    return redirect('landlord:landlord_home')

# class AddExpenseView(TemplateView):
#     template_name = 'landlord/add_expense.html'

class AddExpenseCreateView(CreateView):
    
    form_class = AddExpenseForm
    model = Expenses
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        print('valid')
        tenants = AddTenant.objects.filter(dorm=form.instance.property_name)
        
        for tenant in tenants:
            tenant.expense_balance += form.instance.amount
            tenant.expense_is_paid = False
            
            if tenant.is_inclusive == 'Inclusive':
                tenant.expense_balance = 0
                tenant.expense_is_paid = True
                
            if tenant.wallet > 0:
                tenant.expense_balance -= tenant.wallet
                if tenant.expense_balance <= 0:
                    tenant.wallet = (-1) * tenant.expense_balance
                    tenant.expense_balance = 0
                    tenant.expense_is_paid = True
                else:
                    tenant.wallet = 0
                
            tenant.save()
        return super().form_valid(form)

class HistoryListView(ListView):
    template_name = "landlord/payment_history.html"

    def get_queryset(self):
        pk = self.kwargs['pk']
        tenant = AddTenant.objects.get(pk=pk)
        return History.objects.filter(tenant=tenant.account).order_by('-date_paid')