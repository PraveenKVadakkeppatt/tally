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
    obj=GroupModel.objects.all().filter(under ='curntasts1')
    return render(request, 'groups.html')

def branch(request):
    context={ 'name':'Branch/Division' }
    return render(request, 'branch.html',context)

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

def list_of_voucher_type(request):
    return render(request,'list_of_voucher_type.html')

def list_of_currency(request):
    return render(request,'list_of_currency.html')

def list_of_companies(request):
    return render(request,'list_of_companies.html')

def load_create_ledger(request):
    return render(request,'load_create_ledger.html')

def load_create_groups(request):
    return render(request,'load_create_groups.html')
    

def load_create_ledger2(request):
    return render(request,'load_create_ledger2.html')

def load_voucher_type(request):
    return render(request,'load_voucher_type.html')

def load_currency(request):
    return render(request,'load_currency.html')

def create_company(request):
    return render(request,'create_company.html')

def company_feature_form(request):
    return render(request,'company_feature_form.html')

def load_rates_of_exchange(request):
    return render(request,'load_rates_of_exchange.html')

def create_currency(request):
    return render(request,'create_currency.html')

def load_alter_currency(request):
    return render(request,'load_alter_currency.html')

def gst_details(request):
    return render(request,'gst_details.html')

def tds_detuctor(request):
    return render(request,'tds_detuctor.html')





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
        


