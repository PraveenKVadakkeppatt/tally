from urllib import request
from django.shortcuts import render
from django.contrib import messages

from app1.models import GroupModel

# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'home.html')

def group(request):
    grp = GroupModel.objects.all()
    context={'grp':grp}
    return render(request,'groups.html',context)

def branch(request):
    return render(request, 'branch.html')

def ledger(request):
    return render(request, 'ledger.html')

def primary(request):
    return render(request, 'primarycost.html')

def costcat(request):
    return render(request, 'costcat.html')

def costcentr(request):
    return render(request, 'costcentr.html')

def voucher(request):
    return render(request, 'voucher.html')

def vouchpage(request):
    return render(request, 'vouchpage.html')

def list_of_ledger(request):
    return render(request,'list_of_ledger.html')


def list_of_groups(request):
    return render(request,'list_of_groups.html')

def load_create_ledger(request):
    return render(request,'load_create_ledger.html')

def create_group(request):
    if request.method == 'POST':
        gname = request.POST['gname']
        alia = request.POST['alia']
        under = request.POST['und']
        gp = request.POST['subled']
        naturee = request.POST['nature']
        gross_profitt = request.POST['gross_profit']
        nett = request.POST['nee'] 
        calc = request.POST['cal']
        meth = request.POST['meth']

        mdl = GroupModel(
            name=gname,
            alias=alia,
            under=under,
            nature_of_group=naturee,
            does_it_affect=gross_profitt,
            gp_behaves_like_sub_ledger=gp,
            nett_debit_credit_bal_reporting=nett,
            used_for_calculation=calc,
            method_to_allocate_usd_purchase=meth,
        )
        mdl.save()
        grp = GroupModel.objects.all()
        context={'grp':grp}
        messages.info(request,'GROUP CREATED SUCCESSFULLY')
        return render(request,'groups.html',context)
        



