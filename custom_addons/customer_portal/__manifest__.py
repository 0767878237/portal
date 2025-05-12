{
    'name': 'Customer Portal',
    'version': '1.0',
    'summary': 'Customer Portal for customers to view personal info',
    'category': 'Website',
    'depends': ['portal', 'website', 'contacts'],
    'data': [
        'security/customer_portal_security.xml',
        'security/ir.model.access.csv',
        'views/portal_templates.xml',
    ],
    'installable': True,
    'application': False,
}
