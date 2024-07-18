#company_code_manager/__manifest__.py
{
    'name': 'Company Code Manager',
    'version': '1.0',
    'summary': 'Manage unique company codes for organizations',
    'author': 'Anand VM',
    'license': 'AGPL-3',
    'company': 'Catalist ERP',
    'depends': ['base', 'web'],
    'data': [
        'views/res_company_views.xml',
        'views/res_company_search_view.xml',
    ],

    'installable': True,
    'application': False,
}
