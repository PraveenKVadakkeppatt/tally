from email import message
from email.policy import default
from locale import currency
from symtable import Symbol
from django.db import models


# Create your models here.

class Companies(models.Model):
    d_path=models.CharField(max_length=100,null=True)
    name=models.CharField(max_length=100,null=True)
    mailing_name=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)
    pincode=models.IntegerField(null=True)
    telephone=models.IntegerField(null=True)
    mobile=models.IntegerField(null=True)
    fax=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    website=models.CharField(max_length=100,null=True)
    fin_begin=models.DateField(blank=True,null=True)
    books_begin=models.DateField(blank=True,null=True)
    currency_symbol=models.CharField(max_length=100,null=True)
    formal_name=models.CharField(max_length=100,null=True)
    fin_end = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    status=models.BooleanField(default=False)

class tally_group(models.Model):
    group_name = models.CharField(max_length=255)
    group_alias = models.CharField(max_length=255)
    group_under = models.CharField(max_length=255)
    nature = models.CharField(max_length=255,null=True)
    gross_profit = models.CharField(max_length=255 ,null=True)
    sub_ledger = models.CharField(max_length=255)
    debit_credit = models.CharField(max_length=255)
    calculation = models.CharField(max_length=255)
    invoice = models.CharField(max_length=255)


class cost_center(models.Model):
    c_name = models.CharField(max_length=255)
    cost_alias = models.CharField(max_length=255)
    under = models.CharField(max_length=255)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)

class currencyAlteration(models.Model):
    Symbol = models.CharField(max_length=255)
    FormalName = models.CharField(max_length=255)
    ISOCurrency = models.CharField(max_length=255)
    DecimalPlace = models.CharField(max_length=255,default='')
    showAmount = models.CharField(max_length=255)
    suffixSymbol = models.CharField(max_length=255)
    AddSpace = models.CharField(max_length=255)
    wordRep = models.CharField(max_length=255)
    DecimalWords = models.CharField(max_length=255)


class Currency_alt(models.Model):
    currencyAlteration=models.ForeignKey(currencyAlteration, on_delete=models.CASCADE, null=True)
    stddate=models.CharField(max_length=255,blank=True,null=True)
    stdrate=models.CharField(max_length=255,default='null')
    selldate=models.CharField(max_length=255,blank=True,null=True)
    selvorate=models.CharField(max_length=255,default='null')
    sellrate=models.CharField(max_length=255,default='null')
    buydate=models.CharField(max_length=255,blank=True,null=True)
    buyvorate=models.CharField(max_length=255,default='null')
    buyrate=models.CharField(max_length=255,default='null')


class Voucher(models.Model):
    voucher_name=models.CharField(max_length=255)
    alias=models.CharField(max_length=255)
    voucher_type=models.CharField(max_length=255)
    abbreviation=models.CharField(max_length=255)
    voucherActivate=models.CharField(max_length=255)
    voucherNumber=models.CharField(max_length=255)
    preventDuplicate=models.CharField(max_length=255)
    advance_con=models.CharField(max_length=255)
    voucherEffective=models.CharField(max_length=255)
    transaction=models.CharField(max_length=255)
    make_optional=models.CharField(max_length=255)
    voucherNarration=models.CharField(max_length=255)
    provideNarration=models.CharField(max_length=255)
    manu_jrnl=models.CharField(max_length=255,default='null')
    track_purchase=models.CharField(max_length=255)
    enable_acc=models.CharField(max_length=255)
    prnt_VA_save=models.CharField(max_length=255)
    jurisdiction=models.CharField(max_length=255,default='null')
    pos_invoice=models.CharField(max_length=255)
    msg_1=models.CharField(max_length=255)
    msg_2=models.CharField(max_length=255)
    default_bank=models.CharField(max_length=255)
    title_print=models.CharField(max_length=255)
    setAlter=models.CharField(max_length=255)

class rateofexchange(models.Model):
    date_ROE=models.CharField(max_length=255,default='null')
    currencyName=models.CharField(max_length=255,default='null')
    stdrate=models.CharField(max_length=255,default='null')
    sell_voucher_rate=models.CharField(max_length=255,default='null')
    sell_specified_rate=models.CharField(max_length=255,default='null')
    buy_voucher_rate=models.CharField(max_length=255,default='null')
    buy_specified_rate=models.CharField(max_length=255,default='null')
    currencyAlteration=models.ForeignKey(currencyAlteration, on_delete=models.CASCADE, null=True)






class tally_ledger(models.Model):
    name=models.CharField(max_length=255,default='null')
    alias=models.CharField(max_length=255,default='null')
    under=models.CharField(max_length=255,default='null')
    mname=models.CharField(max_length=255,default='null')
    address=models.CharField(max_length=255,default='null')
    state=models.CharField(max_length=255,default='')
    country=models.CharField(max_length=255,default='')
    pincode=models.CharField(max_length=255,default='null')
    pan_no=models.CharField(max_length=255,default='null')
    bank_details=models.CharField(max_length=255,default='null')
    registration_type=models.CharField(max_length=255,default='null')
    gst_uin=models.CharField(max_length=255,default='null')
    opening_blnc=models.CharField(max_length=255,default='null')
    set_odl=models.CharField(max_length=255,default='null')
    ac_holder_nm=models.CharField(max_length=255,default='null')
    acc_no=models.CharField(max_length=255,default='null')
    ifsc_code=models.CharField(max_length=255,default='null')
    swift_code=models.CharField(max_length=255,default='null')
    bank_name=models.CharField(max_length=255,default='null')
    branch=models.CharField(max_length=255,default='null')
    SA_cheque_bk=models.CharField(max_length=255,default='null')
    Echeque_p=models.CharField(max_length=255,default='null')
    SA_chequeP_con=models.CharField(max_length=255,default='null')
    group_name=models.ForeignKey(tally_group,on_delete=models.CASCADE,blank=True,null=True)


class ledger_cheque_book(models.Model):
    chq_range=models.CharField(max_length=255,default='null')
    from_num=models.CharField(max_length=255,default='null')
    to_no=models.CharField(max_length=255,default='null')
    no_chq=models.CharField(max_length=255,default='null')
    nm_chq=models.CharField(max_length=255,default='null')

class ledger_cheque_demension(models.Model):
    cheque_config= models.CharField(max_length=100,null=True)
    cheque_width = models.IntegerField(null=True)
    cheque_height = models.IntegerField(null=True)
    startL_leftEdge = models.IntegerField(null=True)
    startL_topEdge = models.IntegerField(null=True)
    distancel_leftEdge = models.IntegerField(null=True)
    distancel_topEdge = models.IntegerField(null=True)
    date_style = models.CharField(max_length=100,blank=True,null=True)
    date_seperator = models.CharField(max_length=10,blank=True,null=True)
    separator_width = models.IntegerField(null=True)
    character_distance = models.FloatField(null=True)
    Pdistancel_leftEdge = models.IntegerField(null=True)
    Pdistancel_topEdge = models.IntegerField(null=True)
    area_width = models.IntegerField(null=True)
    secondL_DTE = models.IntegerField(null=True)
    secondfirstL_height = models.IntegerField(null=True)
    firstL_dTE = models.IntegerField(null=True)
    sl_fisrtl_LE = models.IntegerField(null=True)
    sl_secondl_LE = models.IntegerField(null=True)
    amount_widtharea = models.IntegerField(null=True)
    currencyFNM_print = models.CharField(max_length=10,null=True)
    df_TE = models.IntegerField(null=True)
    startL_LE = models.IntegerField(null=True)
    amt_widtharea = models.IntegerField(null=True)
    currencyS_print = models.CharField(max_length=10,null=True)
    company_name = models.CharField(max_length=10,null=True)
    print_CN = models.CharField(max_length=10,null=True)
    salutation_Fsign = models.CharField(max_length=100,null=True)
    salutation_Ssign = models.CharField(max_length=100,null=True)
    top_Edistance = models.IntegerField(null=True)
    startLF_leftE = models.IntegerField(null=True)
    width_sign_area = models.IntegerField(null=True)
    height_sign_area = models.IntegerField(null=True)

class bank_details(models.Model):
    bank_de=models.CharField(max_length=10,null=True)
    trans_type=models.CharField(max_length=10,null=True)
    cros_using=models.CharField(max_length=10,null=True)
    acnt_no=models.CharField(max_length=10,null=True)
    ifs=models.CharField(max_length=10,null=True)
    bank_name=models.CharField(max_length=10,null=True)
    




class Features(models.Model):
    co_name=models.CharField(max_length=100,null=True)
    maintain_acconts=models.CharField(max_length=100,null=True)
    bill_wise_entry=models.CharField(max_length=100,null=True)
    cost_centers=models.CharField(max_length=100,null=True)
    interest_calc=models.CharField(max_length=100,null=True)
    maintain_inventory=models.CharField(max_length=100,null=True)
    integrate_accounts=models.CharField(max_length=100,null=True)
    multiple_price_level=models.CharField(max_length=100,null=True)
    batches=models.CharField(max_length=100,null=True)
    expirydate_batches=models.CharField(max_length=100,null=True)
    joborder_processing=models.CharField(max_length=100,null=True)
    cost_tracking=models.CharField(max_length=100,null=True)
    job_costing=models.CharField(max_length=100,null=True)
    discount_invoices=models.CharField(max_length=100,null=True)
    Billed_Quantity=models.CharField(max_length=100,null=True)
    gst=models.CharField(max_length=100,null=True)
    tds=models.CharField(max_length=100,null=True)
    tcs=models.CharField(max_length=100,null=True)
    vat=models.CharField(max_length=100,null=True)
    excise=models.CharField(max_length=100,null=True)
    servicetax=models.CharField(max_length=100,null=True)
    payroll=models.CharField(max_length=100,null=True)
    multiple_addrss=models.CharField(max_length=100,null=True)
    vouchers=models.CharField(max_length=100,null=True)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)



class GST(models.Model):
    company_name=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    reg_type=models.CharField(max_length=100,null=True)
    assessee=models.CharField(max_length=100,null=True)
    gst_applicable=models.CharField(max_length=100,null=True)
    gstin=models.CharField(max_length=100,null=True)
    periodicity=models.CharField(max_length=100,null=True)
    flood_cess=models.CharField(max_length=100,null=True)
    applicable_form1=models.CharField(max_length=100,null=True)
    gst_rate_details=models.CharField(max_length=100,null=True)
    advance_receipts=models.CharField(max_length=100,null=True)
    reverse_charge=models.CharField(max_length=100,null=True)
    gst_classification=models.CharField(max_length=100,null=True)
    bond_details=models.CharField(max_length=100,null=True)
    tax_rate=models.CharField(max_length=100,null=True)
    tax_calc=models.CharField(max_length=100,null=True)
    tax_purchase=models.CharField(max_length=100,null=True)
    eway_bill=models.CharField(max_length=100,null=True)
    applicable_form=models.CharField(max_length=100,null=True)
    threshold_includes=models.CharField(max_length=100,null=True)
    threshold_limit=models.CharField(max_length=100,null=True)
    intrastate=models.CharField(max_length=100,null=True)
    threshold_limit2=models.CharField(max_length=100,null=True)
    print_eway=models.CharField(max_length=100,null=True)
    e_invoice=models.CharField(max_length=100,null=True)
    app_form=models.CharField(max_length=100,null=True)
    billfrom_place=models.CharField(max_length=100,null=True)
    dperiod=models.CharField(max_length=100,null=True)
    send_ewaybill=models.CharField(max_length=100,null=True)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)


class Tds_Details(models.Model):
    company_name=models.CharField(max_length=100,null=True)
    tan_regno=models.CharField(max_length=100,null=True)
    tan=models.CharField(max_length=100,null=True)
    deductor_type=models.CharField(max_length=100,null=True)
    deductor_branch=models.CharField(max_length=100,null=True)
    person_details=models.CharField(max_length=100,null=True)
    ignore_it=models.CharField(max_length=100,null=True)
    active_tds=models.CharField(max_length=100,null=True)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)


class tds_person(models.Model):
    name=models.CharField(max_length=100,null=True)
    son_daughter=models.CharField(max_length=100,null=True)
    designation=models.CharField(max_length=100,null=True)
    pan=models.CharField(max_length=100,null=True)
    flat_no=models.CharField(max_length=100,null=True)
    building=models.CharField(max_length=100,null=True)
    street=models.CharField(max_length=100,null=True)
    area=models.CharField(max_length=100,null=True)
    town=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    pincode=models.CharField(max_length=100,null=True)
    mobile=models.CharField(max_length=100,null=True)
    std=models.CharField(max_length=100,null=True)
    telephone=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)

    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)

class gst_taxability(models.Model):
    taxability=models.CharField(max_length=100,null=True)
    integrated_tax=models.CharField(max_length=100,null=True)
    cess=models.CharField(max_length=100,null=True)
    flood_cess=models.CharField(max_length=100,null=True)

class gst_lutbond(models.Model):
    lutbond=models.CharField(max_length=100,null=True)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    validity_from = models.CharField(max_length=100,null=True)
    validity_to =models.CharField(max_length=100,null=True)


    
    
   #payroll
class emp_category(models.Model):
    cat_name= models.CharField(max_length=225)
    cat_alias= models.CharField(max_length=225)
    revenue_items=models.CharField(max_length=225)
    non_revenue_items=models.CharField(max_length=225)

class Create_employeegroup(models.Model):
    name =models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    define_salary=models.CharField(max_length=225) 

class Employee(models.Model):

    name = models.CharField(max_length=225)
    alias= models.CharField(max_length=225)
    under= models.CharField(max_length=225)
    date_join = models.DateField()
    defn_sal = models.CharField(max_length=225)
    emp_name = models.CharField(max_length=225)
    emp_desg = models.CharField(max_length=225)
    fnctn = models.CharField(max_length=225)
    location = models.CharField(max_length=225)
    gender= models.CharField(max_length=225)
    dob = models.DateField()
    blood = models.CharField(max_length=225)
    parent_name =models.CharField(max_length=225)
    spouse_name =models.CharField(max_length=225)
    address =models.CharField(max_length=225)
    number =models.CharField(max_length=225)
    email =models.CharField(max_length=225)
    inc_tax_no =models.CharField(max_length=225)
    aadhar_no=models.CharField(max_length=225)
    uan =models.CharField(max_length=225)
    pfn =models.CharField(max_length=225)
    pran =models.CharField(max_length=225)
    esin =models.CharField(max_length=225)
    bankdtls=models.CharField(max_length=225)


class add_bank(models.Model):
    employee_id= models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    Acount_No=models.CharField(max_length=225)
    IFSC_code=models.CharField(max_length=225)
    Bank_name=models.CharField(max_length=225)
    Branch_name=models.CharField(max_length=225)
    Transaction_type=models.CharField(max_length=225)


class E_found_trasfer(models.Model):
    employee_id= models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    Acount_No=models.CharField(max_length=225)
    IFSC_code=models.CharField(max_length=225)
    Bank_name=models.CharField(max_length=225)
    Cheque=models.CharField(max_length=225)

class create_payhead(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    pay_type=models.CharField(max_length=225)
    income_type=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    affect_net=models.CharField(max_length=225)
    payslip=models.CharField(max_length=225)
    calculation_of_gratuity=models.CharField(max_length=225)
    cal_type=models.CharField(max_length=225)
    calculation_period=models.CharField(max_length=225)
    leave_withpay=models.CharField(max_length=225)
    leave_with_out_pay=models.CharField(max_length=225)
    production_type=models.CharField(max_length=225)
    opening_balance=models.CharField(max_length=225)

class compute_information(models.Model):
    Pay_head_id = models.ForeignKey(create_payhead, on_delete=models.CASCADE, null=True, blank=True)
    compute=models.CharField(max_length=225,default="Null")
    effective_from=models.CharField(max_length=225,default="NULL")
    amount_greater=models.CharField(max_length=225,default="NULL")
    amount_upto=models.CharField(max_length=225,default="NULL")
    slab_type=models.CharField(max_length=225,default="NULL")
    value=models.CharField(max_length=225,default="NULL")



class Rounding(models.Model):
    pay_head_id = models.ForeignKey(create_payhead, on_delete=models.CASCADE, null=True, blank=True)
    Rounding_Method =models.CharField(max_length=225,default="Null",blank=True)
    Round_limit = models.CharField(max_length=22,default="Null",blank=True)


class gratuity(models.Model):
    pay_head_id=models.ForeignKey(create_payhead, on_delete=models.CASCADE, null=True, blank=True)
    days_of_months=models.CharField(max_length=225)
    number_of_months_from=models.CharField(max_length=225)
    to=models.CharField(max_length=225)
    calculation_per_year=models.CharField(max_length=225)





class salary(models.Model):
    name=models.CharField(max_length=225)
    under=models.CharField(max_length=225) 
    effective=models.CharField(max_length=225)
    payhead=models.CharField(max_length=225)
    rate=models.CharField(max_length=225)
    per=models.CharField(max_length=225)
    pay_type=models.CharField(max_length=225)
    cal_type=models.CharField(max_length=225)


class units(models.Model):
    type= models.CharField(max_length=225)
    symbol=models.CharField(max_length=225)
    formal_name=models.CharField(max_length=225)
    number_of_decimal_places=models.CharField(max_length=225)
    first_unit=models.CharField(max_length=225)
    conversion=models.CharField(max_length=225)
    second_unit=models.CharField(max_length=225)

class Create_attendence(models.Model):
    name =models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    type =models.CharField(max_length=225)
    period=models.CharField(max_length=225,default='null',blank=True)
    units=models.CharField(max_length=225,default='null',blank=True)   
    
class create_VoucherModels(models.Model):
    voucher_name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225)
    voucher_type = models.CharField(max_length=225)
    abbreviation = models.CharField(max_length=225)
    active_this_voucher_type =  models.CharField(max_length=225)
    method_voucher_numbering = models.CharField(max_length=225)
    use_adv_conf = models.CharField(max_length=225,blank=True)
    prvnt_duplictes = models.CharField(max_length=225,default="Null",blank=True)
    use_effective_date =  models.CharField(max_length=225,default="Null")
    allow_zero_value_trns =  models.CharField(max_length=225)
    allow_naration_in_voucher =  models.CharField(max_length=225)
    make_optional =  models.CharField(max_length=225)
    provide_naration =  models.CharField(max_length=225)
    print_voucher = models.CharField(max_length=225)
  
