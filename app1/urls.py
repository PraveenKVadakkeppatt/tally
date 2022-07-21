from django.urls import path,include
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    path('index',views.index,name='index'),
    path('group',views.group,name='group'),
    path('list_of_groups',views.list_of_groups,name='list_of_groups'),
    path('load_create_groups',views.load_create_groups,name='load_create_groups'),

    path('create_group',views.create_group,name="create_group"),
    path('branch',views.branch,name='branch'),
    path('ledger',views.ledger,name='ledger'),
    path('list_of_ledger',views.list_of_ledger,name='list_of_ledger'),
    path('load_create_ledger',views.load_create_ledger,name='load_create_ledger'),
    path('load_create_ledger2',views.load_create_ledger2,name='load_create_ledger2'),
    path('list_of_currency',views.list_of_currency,name='list_of_currency'),
    path('load_currency',views.load_currency,name='load_currency'),
    path('list_of_companies',views.list_of_companies,name='list_of_companies'),
    path('create_company',views.create_company,name='create_company'),
    path('company_feature_form',views.company_feature_form,name='company_feature_form'),
    path('select_company',views.select_company,name='select_company'),
    path('shut_company',views.shut_company,name='shut_company'),
    path('shut_card',views.shut_card,name='shut_card'),



    path('load_rates_of_exchange',views.load_rates_of_exchange,name='load_rates_of_exchange'),
    path('create_currency',views.create_currency,name='create_currency'),
    path('load_alter_currency',views.load_alter_currency,name='load_alter_currency'),
    path('currency_alteraion',views.currency_alteraion,name='currency_alteraion'),

    path('gst_details',views.gst_details,name='gst_details'),
    path('tds_detuctor',views.tds_detuctor,name='tds_detuctor'),



    path('primary',views.primary,name='primary'),
    path('costcat',views.costcat,name='costcat'),
    path('costcentr',views.costcentr,name='costcentr'),
    path('voucher',views.voucher,name='voucher'),
    path('list_of_voucher_type',views.list_of_voucher_type,name='list_of_voucher_type'),
    path('load_voucher_type',views.load_voucher_type,name='load_voucher_type'),
    path('vouchpage',views.vouchpage,name='vouchpage'),




    
]