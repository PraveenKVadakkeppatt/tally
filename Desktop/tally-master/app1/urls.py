from django.urls import path,include
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    # path('index',views.index,name='index'),
    path('demo',views.demo,name='demo'),
    path('list_of_groups',views.list_of_groups,name='list_of_groups'),
    path('load_create_groups/<int:pk>',views.load_create_groups,name='load_create_groups'),

    path('load_alter_groups',views.load_alter_groups,name="load_alter_groups"),
    # path('branch',views.branch,name='branch'),
    # path('ledger',views.ledger,name='ledger'),
    path('list_of_ledger',views.list_of_ledger,name='list_of_ledger'),
    path('load_ledger_alter/<int:pk>',views.load_ledger_alter,name='load_ledger_alter'),

    path('ledger_gst_details',views.ledger_gst_details,name='ledger_gst_details'),
    path('load_create_ledger',views.load_create_ledger,name='load_create_ledger'),
    path('ledger_chequebook',views.ledger_chequebook,name='ledger_chequebook'),
    path('ledger_bank_details',views.ledger_bank_details,name='ledger_bank_details'),
    path('ledger_cheque_dimenssion',views.ledger_cheque_dimenssion,name='ledger_cheque_dimenssion'),

    path('load_create_ledger2',views.load_create_ledger2,name='load_create_ledger2'),
    path('list_of_currency',views.list_of_currency,name='list_of_currency'),
    path('load_currency',views.load_currency,name='load_currency'),
    path('list_of_companies',views.list_of_companies,name='list_of_companies'),
    path('create_company',views.create_company,name='create_company'),
    path('company_feature_form/<int:pk>',views.company_feature_form,name='company_feature_form'),
    path('companies_feature',views.companies_feature,name='companies_feature'),
    path('companyCreate',views.companyCreate,name='companyCreate'),
    path('create_company',views.create_company,name='create_company'),
    path('select_company',views.select_company,name='select_company'),
    path('shut_company',views.shut_company,name='shut_company'),
    path('shut/<int:pk>',views.shut,name="shut"),
    path('enable/<int:pk>',views.enable,name="enable"),
    # path('shut_card',views.shut_card,name='shut_card'),



    path('load_rates_of_exchange',views.load_rates_of_exchange,name='load_rates_of_exchange'),
    path('create_currency',views.create_currency,name='create_currency'),
    path('load_alter_currency',views.load_alter_currency,name='load_alter_currency'),
    path('currency_alteraion/<int:pk>',views.currency_alteraion,name='currency_alteraion'),

    path('gst_details/<int:pk>',views.gst_details,name='gst_details'),
    path('gst_details_of_company',views.gst_details_of_company,name='gst_details_of_company'),
    path('lutbond/<int:pk>',views.lutbond,name='lutbond'),


    path('tds_detuctor/<int:pk>',views.tds_detuctor,name='tds_detuctor'),
    path('tds_personal/<int:pk>',views.tds_personal,name='tds_personal'),




    # path('primary',views.primary,name='primary'),
    # path('costcat',views.costcat,name='costcat'),
    # path('costcentr',views.costcentr,name='costcentr'),
    # path('voucher',views.voucher,name='voucher'),
    path('list_of_voucher_type',views.list_of_voucher_type,name='list_of_voucher_type'),
    path('load_voucher_type/<int:pk>',views.load_voucher_type,name='load_voucher_type'),
    path('voucher_type_alteration_secondary',views.voucher_type_alteration_secondary,name='voucher_type_alteration_secondary'),
    path('load_create_voucher',views.load_create_voucher,name='load_create_voucher'),
    # path('vouchpage',views.vouchpage,name='vouchpage'),

    path('list_of_cost_centers',views.list_of_cost_centers,name='list_of_cost_centers'),
    path('load_cost_centers/<int:pk>',views.load_cost_centers,name="load_cost_centers"),
    path('alter_cost_create',views.alter_cost_create,name="alter_cost_create"),



#payroll masters

    path('empgroup',views.emp_grp,name='emp_grp'),
    path('addemp_grp',views.addemp_group,name='addemp_group'),
    path('employee',views.employee,name='employee'),
    path('addemployee',views.addemployee,name='addemployee'),
    path('salary',views.salary1,name='salary1'),
    path('load',views.load,name='load'),
    path('load_calculation',views.load_calculation,name='load_calculation'),
    path('payhead2',views.payhead2,name='payhead2'),
    path('stunits',views.stunits,name='stunits'),
    path('add_units',views.add_units,name='add_units'),
    path('attendence',views.attendence,name='attendence'),
    path('emp_attendence',views.emp_attendence,name='emp_attendence'),
    path('payheads',views.payheads,name='payheads'),
    path('add_pay_head',views.add_payhead,name='add_payhead'),
    path('payvoucher',views.payvoucher,name='payvoucher'),
    path('employe_category',views.employe_category,name='employe_category'),
    path('employe_category_form',views.employe_category_form,name='employe_category_form'),

#secondary
    path('empgroup2',views.emp_grp2,name='emp_grp2'),
    path('addemp_grp2',views.addemp_group2,name='addemp_group2'),
    path('attendence2',views.attendence2,name='attendence2'),
    
]
