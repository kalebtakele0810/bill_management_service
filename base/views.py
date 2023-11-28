from django.shortcuts import render
from .models import Bill, Payment
from .forms import BillForm
from django.shortcuts import redirect
from loguru import logger

def home(request):
    # limit_value,offset_value
    payments = Payment.objects.all()[:10]
    bills = Bill.objects.filter(status='PENDING')
    label = 'Current Due Bills'
    count = bills.count()
    context = {'bills':bills, 'payments':payments, 'label' : label, 'count':count}
    
    return render(request,'base/home.html',context)

def bill(request,pk):  
    bill = Bill.objects.get(id=pk)
    context={'bill':bill} 
    return render(request,'base/bill.html',context)

def createBill(request):
    # if request.user.roles.filter(name='Biller').exists():
        form = BillForm()
        if request.method == 'POST':
            form = BillForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        context = {'form' : form}
        return render(request,'base/bill_form.html',context)

def updateBill(request,pk):
    # if request.user.roles.filter(name='Biller').exists():
        bill = Bill.objects.get(id=pk)
        form = BillForm(instance=bill)
        if request.method == 'POST':
            form = BillForm(request.POST, instance=bill)
            if form.is_valid():
                form.save()
                return redirect('home')
        context = {'form':form}
        return render(request,'base/bill_form.html',context)

def latestPayments(request):
    # if request.user.role.filter(name='Biller').exists():
        payments = Payment.objects.all()
        context = {'payments':payments}
        return render(request,'base/latest_payments.html',context)

def overDueBillsList(request):
    # if request.user.roles.filter(name='Biller').exists():
        payments = Payment.objects.all()[:10]
        bills = Bill.objects.filter(status='OVERDUE')
        label = 'Unpaid bills'
        count = bills.count()
        context = {'bills':bills, 'payments':payments, 'label' : label , 'count': count}
        return render(request,'base/home.html',context)
