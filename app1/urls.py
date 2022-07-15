from django.urls import path,include
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    path('index',views.index,name='index'),
    path('group',views.group,name='group'),
    path('list_of_groups',views.list_of_groups,name='list_of_groups'),
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

    path('primary',views.primary,name='primary'),
    path('costcat',views.costcat,name='costcat'),
    path('costcentr',views.costcentr,name='costcentr'),
    path('voucher',views.voucher,name='voucher'),
    path('list_of_voucher_type',views.list_of_voucher_type,name='list_of_voucher_type'),
    path('load_voucher_type',views.load_voucher_type,name='load_voucher_type'),
    path('vouchpage',views.vouchpage,name='vouchpage'),




    
]