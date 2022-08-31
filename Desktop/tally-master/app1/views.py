from cgi import print_arguments
import datetime
from doctest import master
from multiprocessing import context
from symtable import Symbol
from unicodedata import name
from urllib import request
from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import timedelta

from app1.models import *


# Create your views here.

def base(request):
    return render(request, 'base.html')
def demo(request):
    return render(request, 'demo.html')
# def index(request):
#     return render(request, 'home.html')

# def group(request):
#     obj=GroupModel.objects.all().filter(under ='curntasts1')
#     return render(request, 'groups.html')

# def branch(request):
#     context={ 'name':'Branch/Division' }
#     return render(request, 'branch.html',context)

# def ledger(request):
#     return render(request, 'ledger.html')

# def primary(request):
#     return render(request, 'primarycost.html')

# def costcat(request):
#     return render(request, 'costcat.html')

# def costcentr(request):
#     return render(request, 'costcentr.html')

# def voucher(request):
#     return render(request, 'voucher.html')

# def vouchpage(request):
#     return render(request, 'vouchpage.html')

def list_of_ledger(request):
    led=tally_ledger.objects.all()
    context={'led':led}
    return render(request,'list_of_ledger.html',context)


def list_of_groups(request):
    grup=tally_group.objects.all()
    context={'grup':grup}
    return render(request,'list_of_groups.html',context)

def list_of_voucher_type(request):
    vou=Voucher.objects.all()
    context={'vou':vou}
    return render(request,'list_of_voucher_type.html',context)

def list_of_currency(request):
    curr=currencyAlteration.objects.all()
    context={'curr':curr}
    return render(request,'list_of_currency.html',context)

def companyCreate(request):
    return render(request,'create_companys.html')

def create_company(request):
    if request.method=='POST':
        dp=request.POST.get('dpath')
        cn=request.POST.get('name')
        mn=request.POST.get('mailing_name')
        ca=request.POST.get('address1')
        cs=request.POST.get('state')
        cc=request.POST.get('country')
        pin=request.POST.get('pincode')
        tel=request.POST.get('telephone')
        mob=request.POST.get('mobile')
        fax=request.POST.get('fax')
        email=request.POST.get('email')
        web=request.POST.get('website')
        fy=request.POST.get('fin_begin')
        bks=request.POST.get('books_begin')
        bc=request.POST.get('currency_symbol')
        fr=request.POST.get('formal_name')
        cmp=Companies.objects.filter(name=cn)
        out=datetime.datetime.strptime (fy,'%Y-%m-%d')+timedelta (days=364) 
        print(out)
        a=out.date()
        print(a)
        if cmp:
            messages.info(request,'Company name already exists!!')
        else:
            com=Companies(d_path=dp,
                                name=cn,
                                mailing_name=mn,
                                address=ca,
                                state=cs,
                                country=cc,
                                pincode=pin,
                                telephone=tel,
                                mobile=mob,
                                fax=fax,
                                email=email,
                                website=web,
                                fin_begin=fy,
                                books_begin=bks,
                                currency_symbol=bc,
                                formal_name=fr,
                                fin_end=a,)
            com.save()
            
                        
            return render(request,'company_feature_form.html',{'com':com})
    return render(request,'create_companys.html')



    

def companies_feature(request):
    return render(request,'company_feature_form.html')

def list_of_companies(request):
    return render(request,'list_of_companies.html')

def select_company(request):
    comp=Companies.objects.all()
    
    return render(request,'select_company.html',{'comp1':comp})

def shut_company(request):
	com=Companies.objects.all() 
	return render(request, 'shut_company.html',{'com':com})

def shut(request,pk):
    c=Companies.objects.get(id=pk)
    c.status=False
    c.save()
    return redirect('shut_company') 

def enable(request,pk):
    c=Companies.objects.get(id=pk)
    c.status=True
    c.save()
    return redirect('shut_company')



def list_of_cost_centers(request):
    cst=cost_center.objects.all()
    return render(request,'list_of_cost_centers.html',{'cst':cst})

# def shut_card(request):
#     return render(request,'shut_card.html')

def load_ledger_alter(request,pk):
    led=tally_ledger.objects.get(id=pk)
    lga=tally_group.objects.all()
    if request.method=='POST':
        led.name=request.POST.get('name')
        led.alias=request.POST.get('alias')
        led.under=request.POST.get('under')
        led.mname=request.POST.get('mailingname')
        led.address=request.POST.get('address')
        led.state=request.POST.get('state')
        led.country=request.POST.get('country')
        led.pincode=request.POST.get('pincode')
        led.pan_no=request.POST.get('pan_no')
        led.bank_details=request.POST.get('bank_details')
        led.registration_type=request.POST.get('registration_type')
        led.gst_uin=request.POST.get('gst_uin')
        led.opening_blnc=request.POST.get('opening_blnc')

        led.set_odl=request.POST.get('set_odl')
        led.aac_holder_nm=request.POST.get('ac_holder_nm')
        led.acc_no=request.POST.get('acc_no')
        led.ifsc_code=request.POST.get('ifsc_code')
        led.swift_code=request.POST.get('swift_code')
        led.bank_name=request.POST.get('bank_name')
        led.branch=request.POST.get('branch')
        led.SA_cheque_bk=request.POST.get('SA_cheque_bk')
        led.Echeque_p=request.POST.get('Echeque_p')
        led.SA_chequeP_con=request.POST.get('SA_chequeP_con')
        led.save()
        print("added")
        return redirect('/')
    return render(request,'load_ledger_alter.html',{'i':led,'lga':lga})


def load_create_ledger(request):
    lg=tally_group.objects.all()
    if request.method=='POST':
        nm=request.POST.get('name')
        als=request.POST.get('alias')
        under=request.POST.get('under')
        mname=request.POST.get('mailingname')
        adr=request.POST.get('address')
        st=request.POST.get('state')
        cntry=request.POST.get('country')
        pin=request.POST.get('pincode')
        pno=request.POST.get('pan_no')
        bdetls=request.POST.get('bank_details')
        rtype=request.POST.get('registration_type')
        gst_uin=request.POST.get('gst_uin')
        opnbn=request.POST.get('opening_blnc')

        spdl=request.POST.get('set_odl')
        achnm=request.POST.get('ac_holder_nm')
        acno=request.POST.get('acc_no')
        ifsc=request.POST.get('ifsc_code')
        scode=request.POST.get('swift_code')
        bn=request.POST.get('bank_name')
        brnch=request.POST.get('branch')
        sacbk=request.POST.get('SA_cheque_bk')
        ecp=request.POST.get('Echeque_p')
        sacpc=request.POST.get('SA_chequeP_con')
        
        ldr=tally_ledger(name=nm,alias=als,under=under,mname=mname,address=adr,state=st,country=cntry,
						pincode=pin,pan_no=pno,bank_details=bdetls,registration_type=rtype,gst_uin=gst_uin,
						opening_blnc=opnbn,set_odl=spdl,ac_holder_nm=achnm,acc_no=acno,ifsc_code=ifsc,swift_code=scode,
						bank_name=bn,branch=brnch,SA_cheque_bk=sacbk,Echeque_p=ecp,SA_chequeP_con=sacpc)
		
        ldr.save()
        return redirect('/')
    
    return render(request,'load_create_ledger.html',{'lg':lg})

def ledger_gst_details(request):
    return render(request,'ledger_gst_details.html')

def ledger_chequebook(request):
    if request.method=='POST':
        cr=request.POST.get('ccon')
        fnum=request.POST.get('from_no')
        tnum=request.POST.get('to_no')
        nchq=request.POST.get('no_chq')
        nachq=request.POST.get('nm_chq')
        chqbk=ledger_cheque_book(chq_range=cr,
                                from_num=fnum,
                                to_no=tnum,
                                no_chq=nchq,
                                nm_chq=nachq,
                
                                    )
        
        chqbk.save()
        print("added")
        return redirect('ledger_chequebook')
    return render(request,'ledger_cheque_book.html')




    
def ledger_bank_details(request):
    if request.method=='POST':
        bdt=request.POST['bankde']
        tt=request.POST['trans']
        cu=request.POST['cros']
        an=request.POST['acnt']
        ifs=request.POST['ifs']
        bn=request.POST['bank']
        bd=bank_details(bank_de=bdt,
                        trans_type=tt,
                        cros_using=cu,
                        acnt_no=an,
                        ifs=ifs,
                        bank_name=bn,)
        
        bd.save()
        print("added")
    return render(request,'ledger_bank_details.html')


def load_create_groups(request,pk):
    grup=tally_group.objects.get(id=pk)
    if request.method=='POST':
        grup.group_name=request.POST['gname']
        grup.group_alias=request.POST['alias']
        grup.group_under=request.POST['group']
        grup.nature=request.POST['group_nature']
        grup.gross_profit=request.POST['gorss_profit']
        grup.sub_ledger=request.POST['ledger']
        grup.debit_credit=request.POST['debit/credit']
        grup.calculation=request.POST['calculation']
        grup.invoice=request.POST['invoice']
                 
        grup.save()
        print("added")
        return redirect('/')
    return render(request,'load_create_groups.html',{'i':grup})

def load_alter_groups(request):
    return render(request,'load_create_groups.html')
    

def load_create_ledger2(request):
    if request.method=='POST':
        gname=request.POST['gname']
        galias=request.POST['alias']
        under=request.POST['group']
        nature=request.POST['group_nature']
        gross=request.POST['gorss_profit']
        ledg=request.POST['ledger']
        cred=request.POST['debit/credit']
        calc=request.POST['calculation']
        invc=request.POST['invoice']
        grp=tally_group(group_name=gname,
                group_alias=galias,
                group_under=under,
                nature=nature,
                gross_profit=gross,
                sub_ledger=ledg,
                debit_credit=cred,
                calculation=calc,
                invoice=invc,
                )          
        grp.save()
        print("added")
        return redirect('/')
    return render(request,'load_create_ledger2.html')


def load_voucher_type(request,pk):
    vou=Voucher.objects.get(id=pk)
    if request.method=='POST':
        vou.voucher_name=request.POST['vname']
        vou.alias=request.POST['valias']
        vou.voucher_type=request.POST['vtype']
        vou.abbreviation=request.POST['vabbre']
        vou.voucherActivate=request.POST['vactive']
        vou.voucherNumber=request.POST['vnum']
        vou.preventDuplicate=request.POST['vprev']
        vou.advance_con=request.POST['advcon'] 
        vou.voucherEffective=request.POST['effct']
        vou.transaction=request.POST['trans']
        vou.make_optional=request.POST['opt']
        vou.voucherNarration=request.POST['narrate']
        vou.provideNarration=request.POST['provide']
        vou.manu_jrnl=request.POST['journal']
        vou.track_purchase=request.POST['purchase']
        vou.enable_acc=request.POST['allocate']
        vou.prnt_VA_save=request.POST['vprint']
        vou.jurisdiction=request.POST['juri']
        vou.pos_invoice=request.POST['pos']
        vou.msg_1=request.POST['msg1']
        vou.msg_2=request.POST['msg2']
        vou.default_bank=request.POST['vbank']
        vou.title_print=request.POST['vtitle']
        vou.setAlter=request.POST['vsetalt']
        
        
        
        vou.save()
        print("added")
        return redirect('/')
    return render(request,'load_voucher_type.html',{'i':vou})

def voucher_type_alteration_secondary(request):
    return render(request,'voucher_type_alteration_secondary.html')

def load_create_voucher(request):
    if request.method=='POST':
        vouchername=request.POST['vname']
        voucheralias=request.POST['valias']
        vouchertype=request.POST['vtype']
        abbreviation=request.POST['vabbre']
        vactive=request.POST['vactive']
        vnumber=request.POST['vnum']
        vprevent=request.POST['vprev']
        vadvcon=request.POST['advcon'] 
        veffective=request.POST['effct']
        vtrans=request.POST['trans']
        voptional=request.POST['opt']
        vnarration=request.POST['narrate']
        vprovide=request.POST['provide']
        vjournal=request.POST['journal']
        vpurchase=request.POST['purchase']
        vallocate=request.POST['allocate']
        vprint=request.POST['vprint']
        vjuri=request.POST['juri']
        vpos=request.POST['pos']
        vmsg1=request.POST['msg1']
        vmsg2=request.POST['msg2']
        vbank=request.POST['vbank']
        vtitle=request.POST['vtitle']
        vsetalt=request.POST['vsetalt']
        
        
        vouch=Voucher(voucher_name=vouchername,
                              alias=voucheralias,
                              voucher_type=vouchertype,
                              abbreviation=abbreviation,
                              voucherActivate=vactive,
                              voucherNumber=vnumber,
                              preventDuplicate=vprevent,
                              advance_con=vadvcon,
                              voucherEffective=veffective,
                              transaction=vtrans,
                              make_optional=voptional,
                              voucherNarration=vnarration,
                              provideNarration=vprovide,
                              manu_jrnl=vjournal,
                              track_purchase= vpurchase,
                              enable_acc=vallocate,
                              prnt_VA_save=vprint,
                              jurisdiction=vjuri,
                              pos_invoice=vpos,
                              msg_1=vmsg1,
                              msg_2=vmsg2,
                              default_bank=vbank,
                              title_print=vtitle,
                              setAlter=vsetalt,
                             )
        vouch.save()
        print("added")
        return redirect('/')
    return render(request,'load_create_voucher.html')

def load_currency(request):
    return render(request,'load_currency.html')


def company_feature_form(request,pk):
    id=Companies.objects.get(id=pk)
    print(id)

    if request.method=='POST':
        coname=request.POST['name']
        ma=request.POST['main']
        bw=request.POST['bill']
        ecc=request.POST['cost']
        eic=request.POST['inter']
        mi=request.POST['inven']
        iawi=request.POST['intac']
        empl=request.POST['mulpri']
        eb=request.POST['enbat']
        medb=request.POST['mained']
        ejop=request.POST['ejob']
        ect=request.POST['ecost']
        ejc=request.POST['ejoco']
        udci=request.POST['used']
        usa=request.POST['uact']
        gst=request.POST['gst']
        tds=request.POST['tds']
        tcs=request.POST['tcs']
        vat=request.POST['vat']
        enex=request.POST['exci']
        est=request.POST['extax']
        mp=request.POST['mai']
        # eps=request.POST['enpa']
        ema=request.POST['enad']
        mmv=request.POST['mark']
        fc=Features(co_name=coname,
                          maintain_acconts=ma,
                          bill_wise_entry=bw,
                          cost_centers=ecc,
                          interest_calc=eic,
                          maintain_inventory=mi,
                          integrate_accounts=iawi,
                          multiple_price_level=empl,
                          batches=eb,
                          expirydate_batches=medb,
                          joborder_processing=ejop,
                          cost_tracking=ect,
                          job_costing=ejc,
                          discount_invoices=udci,
                          Billed_Quantity=usa,
                          gst=gst,
                          tds=tds,
                          tcs=tcs,
                          vat=vat,
                          excise=enex,
                          servicetax=est,
                          payroll=mp,
                        #   enb_pay=eps,
                          multiple_addrss=ema,
                          vouchers=mmv,
                          company=id,)
        fc.save()
        print("added")
    return render(request,'company_feature_form.html',{'com':id})

def load_rates_of_exchange(request):
    curcc=currencyAlteration.objects.all()
    rat=rateofexchange.objects.all()
    if request.method=='POST':
        
        curncy=request.POST['curname']
        
        cstdrate=request.POST['stdr']
        csrate=request.POST['sr']
        bsrate=request.POST['sr2']
        raex=rateofexchange(
                          
                          stdrate=cstdrate,
                          sell_specified_rate=csrate,
                          buy_specified_rate=bsrate,
                          currencyName=curncy,)
        raex.save()
        print("added")
        return redirect('/')
    return render(request,'load_rates_of_exchange.html',{'curcc':curcc,'rat':rat})

def create_currency(request):
    
    
    return render(request,'create_currency.html')



def load_cost_centers(request,pk):
    cst=cost_center.objects.get(id=pk)
    ccst=cost_center.objects.all()
    if request.method=='POST':
        cst.c_name=request.POST['cname']
        cst.cost_alias=request.POST['calias']
        cst.under=request.POST['cunder']
        
        cst.save()
        print("added")
        return redirect('/')
    return render(request,'load_cost_centers.html',{'i':cst,'ccst':ccst})

def alter_cost_create(request):
    ccst=cost_center.objects.all()
    if request.method=='POST':
        cname=request.POST['cname']
        calias=request.POST['calias']
        cunder=request.POST['cunder']
        cost=cost_center(c_name=cname,
                cost_alias=calias,
                under=cunder,
                )
        cost.save()
        print("added")
        return redirect('alter_cost_create')
    return render(request,'alter_cost_create.html',{'ccst':ccst})


def load_alter_currency(request):
    if request.method=='POST':
        casymbol=request.POST['symbol']
        caname=request.POST['name']
        caiso=request.POST['iso']
        canumdec=request.POST['numdec']
        caamount=request.POST['amount']
        casuffix=request.POST['suffix']
        casymam=request.POST['symam']
        caamodec=request.POST['amodec']
        cadecwo=request.POST['decwo']
        ca=currencyAlteration(Symbol=casymbol,
                              FormalName=caname,
                              ISOCurrency=caiso,
                              DecimalPlace=canumdec,
                              showAmount=caamount,
                              suffixSymbol=casuffix,
                              AddSpace=casymam,
                              wordRep=caamodec,
                              DecimalWords=cadecwo)
        ca.save()
        print("hi")
        return redirect('list_of_currency')
    return render(request,'load_alter_currency.html')



        

    


def currency_alteraion(request,pk):
    calt=currencyAlteration.objects.get(id=pk)
    if request.method=='POST':
        calt.Symbol=request.POST.get('symbol')
        calt.FormalName=request.POST.get('name')
        calt.ISOCurrency=request.POST.get('iso')
        calt.DecimalPlace=request.POST.get('numdec')
        calt.showAmount=request.POST.get('amount')
        calt.suffixSymbol=request.POST.get('suffix')
        calt.AddSpace=request.POST.get('symam')
        calt.wordRep=request.POST.get('amodec')
        calt.DecimalWords=request.POST.get('decwo')
        

        stadate=request.POST.get('standate')
        starate=request.POST.get('stdrate')
        seldate=request.POST.get('selldate')
        selvrate=request.POST.get('selvrate')
        selrate=request.POST.get('selsrate')
        buydate=request.POST.get('buydate')
        buyvrate=request.POST.get('buyvrate')
        buyrate=request.POST.get('buysrate')

        al=Currency_alt(stddate=stadate,
                        stdrate=starate,
                        selldate=seldate,
                        selvorate=selvrate,
                        sellrate=selrate,
                        buydate=buydate,
                        buyvorate=buyvrate,
                        buyrate=buyrate,
                        currencyAlteration_id=pk,)
       
        
        al.save()
        calt.save()
        print("added")
        return redirect('list_of_currency')
    return render(request,'currency_alteraion.html',{'i':calt})

def gst_details(request,pk):
    id=Companies.objects.get(id=pk)
    company=Companies.objects.get(id=pk)

    if request.method=='POST':
        cmp=request.POST.get('cmpname')
        state=request.POST.get('cstate')
        reg=request.POST.get('creg')
        gapp=request.POST.get('cgapp')
        uin=request.POST.get('cuin')
        peri=request.POST.get('cperi')
        fl=request.POST.get('cflood')
        apf=request.POST.get('capf')
        grate=request.POST.get('cgrate')
        adr=request.POST.get('cadr')
        rev=request.POST.get('crev')
        gclass=request.POST.get('cgclass')
        lut=request.POST.get('clut')
        tv=request.POST.get('ctv')
        tc=request.POST.get('ctc')
        tp=request.POST.get('ctp')
        eway=request.POST.get('ceway')
        appform=request.POST.get('cappform')
        liin=request.POST.get('cliin')
        thr=request.POST.get('cthr')
        intra=request.POST.get('cintra')
        thre=request.POST.get('cthre')
        ewayb=request.POST.get('cewayb')
        einv=request.POST.get('ceinv')
        appli=request.POST.get('cappli')
        billf=request.POST.get('cbillf')
        dper=request.POST.get('cdper')
        snd=request.POST.get('csnd')
        gd=GST(company_name=cmp,
              state=state,
              reg_type=reg,
              gst_applicable=gapp,
              gstin=uin,
              periodicity=peri,
              flood_cess=fl,
              applicable_form1=apf,
              gst_rate_details=grate,
              advance_receipts=adr,
              reverse_charge=rev,
              gst_classification=gclass,
              bond_details=lut,
              tax_rate=tv,
              tax_calc=tc,
              tax_purchase=tp,
              eway_bill=eway,
              applicable_form=appform,
              threshold_includes=liin,
              threshold_limit=thr,
              intrastate=intra,
              threshold_limit2=thre,
              print_eway=ewayb,
              e_invoice=einv,
              app_form=appli,
              billfrom_place=billf,
              dperiod=dper,
              send_ewaybill=snd,
              company=id,)
        gd.save()
        print("added")
    return render(request,'gst_details.html',{'id':id,'companies':company})

def lutbond(request,pk):
    id=Companies.objects.get(id=pk)
    if request.method=='POST':
        lbn=request.POST.get('lbn')
        afrom=request.POST['application_from']
        ato=request.POST['application_to']
        lb=gst_lutbond(lutbond=lbn,
                        validity_from = afrom,
                        validity_to = ato,
                        company=id,)
        lb.save()

    return render(request,'lutbond.html',{'id':id})

def gst_details_of_company(request):
    if request.method=='POST':

        ta=request.POST.get('gta')
        it=request.POST.get('git')
        ce=request.POST.get('gce')
        fc=request.POST.get('gfc')
        gdc=gst_taxability(Taxability=ta,
                            integrated_tax=it,
                            cess=ce,
                            flood_cess=fc,)
        gdc.save()
        return redirect('gst_details_of_company')
    return render(request,'gst_details_of_company.html')

def tds_detuctor(request,pk):
    id=Companies.objects.get(id=pk)

    if request.method=='POST':
        cmp=request.POST.get('tcmpname')
        tr=request.POST.get('ttr')
        tx=request.POST.get('ttx')
        dr=request.POST.get('tdr')
        drb=request.POST.get('tdrb')
        sad=request.POST.get('tsad')
        ii=request.POST.get('tii')
        at=request.POST.get('tat')
        td=Tds_Details(company_name=cmp,
                tan_regno=tr,
                tan=tx,
                deductor_type=dr,
                deductor_branch=drb,
                person_details=sad,
                ignore_it=ii,
                active_tds=at,
                company=id)
        td.save()
        print("added")
    return render(request,'tds_detuctor.html',{'id':id})

def tds_personal(request,pk):
    id=Companies.objects.get(id=pk)
    if request.method=="POST":
        name=request.POST.get('tpname')
        sd=request.POST.get('tpsd')
        dn=request.POST.get('tpdn')
        pn=request.POST.get('tppn')
        ft=request.POST.get('tpft')
        ps=request.POST.get('tpps')
        st=request.POST.get('spst')
        ln=request.POST.get('spln')
        dt=request.POST.get('spdt')
        se=request.POST.get('tpse')
        pin=request.POST.get('tppin')
        mb=request.POST.get('spmb')
        std=request.POST.get('spstd')
        te=request.POST.get('spte')
        el=request.POST.get('spel')
        tp=tds_person(name=name,
                        son_daughter=sd,
                        designation=dn,
                        pan=pn,
                        flat_no=ft,
                        building=ps,
                        street=st,
                        area=ln,
                        town=dt,
                        state=se,
                        pincode=pin,
                        mobile=mb,
                        std=std,
                        telephone=te,
                        email=el,
                        company=id)
        tp.save()
        messages.info(request,'tds personal details added..!!')
    return render(request,'tds_personal.html',{'id':id})

def ledger_cheque_dimenssion(request):

    if request.method == 'POST':
            cc=request.POST.get('ccon')
            cw= request.POST.get('cheque_width')
            ch= request.POST.get('cheque_height')
            sle= request.POST.get('startL_leftEdge')
            slte= request.POST.get('startL_topEdge')
            dlle= request.POST.get('distancel_leftEdge')
            dlte= request.POST.get('distancel_topEdge')
            ds= request.POST.get('date_style')
            dts= request.POST.get('date_seperator')
            sw= request.POST.get('separator_width')
            cd= request.POST.get('character_distance')
            pdle= request.POST.get('Pdistancel_leftEdge')
            pdlte= request.POST.get('Pdistancel_topEdge')
            aw= request.POST.get('area_width')
            sldte= request.POST.get('secondL_DTE')
            sflh= request.POST.get('secondfirstL_height')
            fldte= request.POST.get('firstL_dTE')
            slfle= request.POST.get('sl_fisrtl_LE')
            slsle= request.POST.get('sl_secondl_LE')
            awa= request.POST.get('amount_widtharea')
            cfnmp= request.POST.get('currencyFNM_print')
            dfte= request.POST.get('df_TE')
            sle= request.POST.get('startL_LE')
            amwa= request.POST.get('amt_widtharea')
            csp= request.POST.get('currencyS_print')
            cn= request.POST.get('company_name')
            pcn= request.POST.get('print_CN')
            sfs= request.POST.get('salutation_Fsign')
            sss= request.POST.get('salutation_Ssign')
            tes= request.POST.get('top_Edistance')
            slfl= request.POST.get('startLF_leftE')
            wsa= request.POST.get('width_sign_area')
            hsa= request.POST.get('height_sign_area')

            cld= ledger_cheque_demension(cheque_config=cc,cheque_width=cw,cheque_height=ch,startL_leftEdge=sle,startL_topEdge=slte,distancel_leftEdge=dlle,
                                        distancel_topEdge=dlte,date_style=ds,date_seperator=dts,separator_width=sw,character_distance=cd,
                                        Pdistancel_leftEdge=pdle,Pdistancel_topEdge=pdlte,area_width=aw,secondL_DTE=sldte,secondfirstL_height=sflh,
                                        firstL_dTE=fldte,sl_fisrtl_LE=slfle,sl_secondl_LE=slsle,amount_widtharea=awa,currencyFNM_print=cfnmp,
                                        df_TE=dfte,startL_LE=sle,amt_widtharea=amwa,currencyS_print=csp,company_name=cn,print_CN=pcn,
                                        salutation_Fsign=sfs,salutation_Ssign=sss,top_Edistance=tes,startLF_leftE=slfl,width_sign_area=wsa,
                                        height_sign_area=hsa)

            cld.save()
            return redirect('ledger_cheque_dimenssion')
    return render(request,'ledger_cheque_dimenssion.html')



# payroll masters

def emp_grp(request):
    std=Create_employeegroup.objects.all()
    return render(request,'employegroup.html',{'std':std})


def addemp_group(request):
    empc=emp_category.objects.all()
    if request.method == 'POST':
        name= request.POST['name']
        alias = request.POST['alias']
        under = request.POST['under']
        sal= request.POST['sal']

        std= Create_employeegroup(
            name =name,
            alias=alias,
            under=under,
            define_salary=sal,   
        )
        std.save()
       # messages.success(request,'employee group add successfully !!!')
        return redirect('emp_grp')
    return render(request,'employegroup.html',{'empc':empc})


def emp_grp2(request):
    std=Create_employeegroup.objects.all()
    return render(request,'employegroup_secondary.html',{'std':std})


def employee(request):
    std=Create_employeegroup.objects.all()
    return render(request,'employe.html',{'std':std})   


def addemployee(request):
    if request.method=='POST':
        
        namee = request.POST['name']
        aliass = request.POST['alias']
        underr = request.POST['under']
        join = request.POST['join']
        sal = request.POST['sal']
        empname = request.POST['empname']
        desig = request.POST['desig']
        fn = request.POST['fn']
        loc = request.POST['loc']
        gen = request.POST['gen']
        dob = request.POST['dob']
        bloodd = request.POST['blood']
        prnts = request.POST['prnts']
        spouse = request.POST['spouse']
        adrs = request.POST['adrs']
        phone = request.POST['phone']
        email = request.POST['email']
        taxno = request.POST['taxno']
        aadhar = request.POST['aadhar']
        uan = request.POST['uan']
        pfn = request.POST['pfn']
        pran = request.POST['pran']
        esin = request.POST['esin']
        bank = request.POST['bank']
        #Bank
        acount=request.POST['acount']
        ifsc_code=request.POST['ifsc']
        bankname=request.POST['bank_name']
        branch=request.POST['branch_name']
        transaction_type=request.POST['Transaction_type']
        #E-found transfer
        acount_num=request.POST['acnumber']
        ifsc=request.POST['ifsccode']
        bankname2=request.POST['bank_name2']
        cheque=request.POST['cheque']


        
        
        std = Employee(

            name =namee,
            alias=aliass,
            under=underr,
            date_join=join,
            defn_sal =sal,
            emp_name = empname,
            emp_desg=desig ,
            fnctn = fn,
            location =loc,
            gender =gen,
            dob =dob,
            blood=bloodd,
            parent_name =prnts,
            spouse_name = spouse,
            address = adrs,
            number = phone,
            email = email,
            inc_tax_no = taxno,
            aadhar_no = aadhar,
            uan = uan,
            pfn = pfn,
            pran = pran,
            esin = esin,
            bankdtls = bank,
            
            



        )

        std.save()
        idd=std

        std2=add_bank(employee_id=idd,
                      Acount_No=acount,
                      IFSC_code=ifsc_code,
                      Bank_name=bankname,
                      Branch_name=branch,
                      Transaction_type=transaction_type,
        )
        std2.save()

        std3=E_found_trasfer(employee_id=idd,
                             Acount_No=acount_num,
                             IFSC_code=ifsc,
                             Bank_name=bankname2,
                             Cheque=cheque 
        )
        std3.save()
        return render(request,'employe.html')


def addemp_group2(request):
    std=Create_employeegroup.objects.all()
    if request.method == 'POST':
        name= request.POST['name']
        alias = request.POST['alias']
        under = request.POST['under']
        sal= request.POST['sal']

        std= Create_employeegroup(
            name =name,
            alias=alias,
            under=under,
            define_salary=sal,   
        )
        std.save()
        #messages.success(request,'employee group add successfully !!!')
        return redirect('employee')
    return render(request,'emp_group3.html',{'std':std})   


def salary1(request):
    pk=create_payhead.objects.all()
    if request.method=='POST':
        name1=request.POST['name']
        under=request.POST['under']
        effect=request.POST['effective']
        pay=request.POST['payhead']
        rate=request.POST['rate']
        per=request.POST['per']
        payhead=request.POST['payheaad_type']
        calculation=request.POST['calculation_type']
        #save salary
        std=salary(name=name1,
                   under=under,
                   effective=effect,
                   payhead=pay,
                   rate=rate,
                   per=per,
                   pay_type=payhead,
                   cal_type=calculation,
        )
        std.save()
        return redirect('salary1')
    return render(request,'salary.html',{'pk':pk}) 

def load(request):
    did=request.GET.get("id")
    obj=create_payhead.objects.get(name=did)
    return render(request,"load.html",{"obj":obj})

def load_calculation(request):
    did=request.GET.get("id")
    obj=create_payhead.objects.get(name=did)
    return render(request,"load_calculation.html",{"obj":obj})

def payhead2(request):
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        pay_head_type=request.POST['payhead']
        income_type=request.POST['income']
        under=request.POST['under']
        affect_net_salary=request.POST['netsalary']
        payslip=request.POST['payslip']
        calculation_of_gratuity=request.POST['caltype']
        calculation_period=request.POST['ctype']
        calculation_type=request.POST['caltype']
        attendence_leave_withpay=request.POST['attendence with pay']
        attendence_leave_with_outpay=request.POST['Attendance with out pay']
        production_type=request.POST['ptype']
        opening_balance=request.POST['balance']

        #compute information
        compute=request.POST['compute']
        effective_from=request.POST['effective_from']
        # amount_greaterthan=request.POST['', False]
        amount_upto=request.POST['amount_upto']
        slabtype=request.POST['slab_type']
        value=request.POST['value']

        #Rounding
        round_method=request.POST['roundmethod']
        limit=request.POST['limit']

        #Gratuity
        days_of_months=request.POST['days_of_months']
        from_date=request.POST['from']
        to=request.POST['to']
        calculation_per_year=request.POST['eligiibility']

        std=create_payhead(name=name,
                           alias=alias,
                           pay_type=pay_head_type,
                           income_type=income_type,
                           under=under,
                           affect_net=affect_net_salary,
                           payslip=payslip,
                           calculation_of_gratuity=calculation_of_gratuity,
                           cal_type=calculation_type,
                           calculation_period=calculation_period,
                           leave_withpay=attendence_leave_withpay,
                           leave_with_out_pay=attendence_leave_with_outpay,
                           production_type=production_type,
                           opening_balance=opening_balance,
                           
        )
        std.save()
        idd=std

        std2=compute_information(Pay_head_id=idd,
                                 compute=compute,
                                 effective_from=effective_from,
                                #  amount_greater=amount_greaterthan,
                                 amount_upto=amount_upto,
                                 slab_type=slabtype,
                                 value=value,
        )
        std2.save()

        std3=Rounding(pay_head_id=idd,
                     Rounding_Method=round_method,
                     Round_limit=limit,
        )
        std3.save()

        std4=gratuity(pay_head_id=idd,
                     days_of_months=days_of_months,
                     number_of_months_from=from_date,
                     to=to,
                     calculation_per_year=calculation_per_year,
        )
        std4.save()
        messages.success(request,'successfully Added !!!')
        return redirect('salary1')
    return render(request,'payhead_secondary.html')     


def stunits(request):
    ps=units()
    return render(request,'stunits.html',{'ps':ps}) 

def add_units(request):
    if request.method=='POST':
        std=units()
        std.type=request.POST.get('type')
        std.symbol=request.POST.get('symbol')  
        std.formal_name=request.POST.get('formal')
        std.number_of_decimal_places=request.POST.get('decimal') 
        std.first_unit=request.POST.get('ft')
        std.conversion=request.POST.get('con')
        std.second_unit=request.POST.get('sec')  
        std.save()
        return redirect('stunits')

def attendence(request):
    std=Create_attendence.objects.all()
    pk=units.objects.all()
    return render(request,'attendence.html',{'std':std,'pk':pk})   

def emp_attendence(request):
    if request.method == 'POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under=request.POST['under']
        type=request.POST['type']
        period=request.POST['period']
        units1=request.POST['units']
        
        std=Create_attendence(
            name =name,
            alias=alias,
            under=under,
            type=type,
            period=period,
            units=units1,
           )
        std.save()
        messages.success(request,'successfully Added !!!')
        return redirect('attendence')

def attendence2(request):
    std=Create_attendence.objects.all()
    pk=units.objects.all()
    return render(request,'attendence_secondary.html',{'std':std,'pk':pk}) 

def add_payhead(request):
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        pay_head_type=request.POST['payhead']
        income_type=request.POST['income']
        under=request.POST['under']
        affect_net_salary=request.POST['netsalary']
        payslip=request.POST['payslip']
        calculation_of_gratuity=request.POST['caltype']
        calculation_period=request.POST['ctype']
        calculation_type=request.POST['caltype']
        attendence_leave_withpay=request.POST['attendence with pay']
        attendence_leave_with_outpay=request.POST['Attendance with out pay']
        production_type=request.POST['ptype']
        opening_balance=request.POST['balance']

        #compute information
        compute=request.POST['compute']
        effective_from=request.POST['effective_from']
        # amount_greaterthan=request.POST['', False]
        amount_upto=request.POST['amount_upto']
        slabtype=request.POST['slab_type']
        value=request.POST['value']

        #Rounding
        round_method=request.POST['roundmethod']
        limit=request.POST['limit']

        #Gratuity
        days_of_months=request.POST['days_of_months']
        from_date=request.POST['from']
        to=request.POST['to']
        calculation_per_year=request.POST['eligiibility']

        std=create_payhead(name=name,
                           alias=alias,
                           pay_type=pay_head_type,
                           income_type=income_type,
                           under=under,
                           affect_net=affect_net_salary,
                           payslip=payslip,
                           calculation_of_gratuity=calculation_of_gratuity,
                           cal_type=calculation_type,
                           calculation_period=calculation_period,
                           leave_withpay=attendence_leave_withpay,
                           leave_with_out_pay=attendence_leave_with_outpay,
                           production_type=production_type,
                           opening_balance=opening_balance,
                           
        )
        std.save()
        idd=std

        std2=compute_information(Pay_head_id=idd,
                                 compute=compute,
                                 effective_from=effective_from,
                                #  amount_greater=amount_greaterthan,
                                 amount_upto=amount_upto,
                                 slab_type=slabtype,
                                 value=value,
        )
        std2.save()

        std3=Rounding(pay_head_id=idd,
                     Rounding_Method=round_method,
                     Round_limit=limit,
        )
        std3.save()

        std4=gratuity(pay_head_id=idd,
                     days_of_months=days_of_months,
                     number_of_months_from=from_date,
                     to=to,
                     calculation_per_year=calculation_per_year,
        )
        std4.save()
        messages.success(request,'successfully Added !!!')
        return redirect('payheads')

def payheads(request):
    std=Create_attendence.objects.all()
    return render(request,'payheads.html',{'std':std})   


def payvoucher(request):
    return render(request,'payroll.html')   

def add_voucher(request):
    if request.method == 'POST':
        Vname = request.POST['name']
        alias = request.POST['alias']
        vtype = request.POST['type']
        abbre = request.POST['abber']
        activ_vou_typ = request.POST['active']  
        meth_vou_num = request.POST['numbering']
        useadv = request.POST.get('config', False)
        prvtdp = request.POST.get('prevent', False)
       
        use_effct_date = request.POST['effect']  
        allow_zero_trans = request.POST['trans']  
        allow_naration_in_vou = request.POST['narr']  
        optional = request.POST['optical'] 
        provide_narr = request.POST['ledg']  
        print = request.POST['print']  
        
        std = create_VoucherModels(voucher_name=Vname ,
            alias=alias,
            voucher_type=vtype,
            abbreviation=abbre,
            active_this_voucher_type=activ_vou_typ,
            method_voucher_numbering=meth_vou_num,
            use_effective_date=use_effct_date,
            use_adv_conf = useadv,
            prvnt_duplictes =prvtdp,
            allow_zero_value_trns=allow_zero_trans,
            allow_naration_in_voucher=allow_naration_in_vou,
            make_optional=optional,
            provide_naration=provide_narr,
            print_voucher=print,

        )
        std.save()
        return redirect('payvoucher')

    return render(request, 'payroll.html')  

def employe_category(request):
    return render(request,'employe_category.html')   

def employe_category_form(request):
    if request.method == 'POST':
        name= request.POST['name']
        alias = request.POST['alias']
        relocate = request.POST['locate']
        relocate= request.POST['locate2']

        std= emp_category(
            cat_name =name,
            cat_alias=alias,
            revenue_items=relocate,
            non_revenue_items=relocate,   
        )
        std.save()
       # messages.success(request,'employee group add successfully !!!')
        return redirect('emp_grp')