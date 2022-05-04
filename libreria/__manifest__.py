# -*- coding utf-8 -*-

{

    'name': "Libreria Odoo",
    'description': "Este modulo se usa para gestionar libros en Odoo",
    'summary': "Este modulo se usa para gestionar una tabla de libros en Odoo. Esto se puede instalar en odoo sh y odoo community",
    'author': 'Ing. Hermes Colina',
    'Category': 'Geenral',
    'Version': '1.0',
    'depends':['hr'],
    'data':[

            'views/menu_view.xml',
            'views/libros_view.xml',
            'views/hr_employee_view.xml',
            'security/libreria_security.xml',
            'security/ir.model.access.csv',
        ],
    

}
