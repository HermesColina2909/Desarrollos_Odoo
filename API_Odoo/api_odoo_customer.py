#Importando librerias
import xmlrpc.client

#Conexion con la base de datos
url = 'https://psstore-prueba-4772395.dev.odoo.com'                     #Dominio o IP de la base de datos
db = 'psstore-prueba-4772395'                                           #Nombre de la base de datos
username = 'hermes@gmail.com'                                           #Usuario de la base de datos
password = '123'                                                        #Contraseña de usuario

#iniciando sesion
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))    #Proporciona metallamadas que no requieren autentificacion
version_db = common.version()                                           #Asignar common a una variable para imprimir
uid = common.authenticate(db, username, password, {})                   #Identificador de usuario utilizado en las metallamadas autentificadas              
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))    #Proporciona metallamadas a los modelos
print(version_db)                                                       #Mostrar informacion de la base de datos

#Metodos de llamada
#Buscar y leer datos de una tabla
res = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', False]]], {
    'fields': [
        'display_name',
        'phone', 
        'email', 
        'city'], 
        'limit': 100
        }
    )
print(res)

#Listar registros
lista = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', False]]])
print(lista)

#Paginacion
pagina = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', False]]], {'offset': 1, 'limit': 5})
print(pagina)

#contar registros
registro = models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['is_company', '=', False]]])
print(registro)

#Campos de registros - lista
campo = models.execute_kw(db, uid, password, 'res.partner', 'fields_get', [], {'attributes': ['string', 'help', 'type']})
cam = len(campo)
print(cam)

#Crear registros
print('<===== Crear nuevo cliente en Odoo =====>')
nombre = input('Nombre: ')
ciudad = input('Ciudad: ')
telefono = input('Telefono: ')
crear = models.execute_kw(db, uid, password, 'res.partner', 'create', 
    [{
        'name': nombre, 
        'city': ciudad, 
        'phone': telefono
    }]
)
print(crear)

print('<===== Crear nuevo producto en Odoo =====>')
producto = input('Nombre: ')
precio = input('Precio: ')
referencia = input('Referencia interna: ')
coste = input('Coste: ')
productos_odoo = models.execute_kw(db, uid, password, 'product.template', 'create', 
    [{
        'name': producto,
        'list_price': precio,
        'default_code': referencia,
        'standard_price': coste
    }]
)
print(productos_odoo)

#Confirmar ordenes de venta
borrador = models.execute_kw(db, uid, password, #Determinar cuales ordenes de venta estan en borrador
'sale.order', 
'search', 
[[['state', '=', 'draft']]])
confirmar = models.execute_kw(db, uid, password, #Confirmar las ordenes de venta en borrador
'sale.order', 
'action_confirm', 
[borrador])
print('Confirmar ordenes de venta: {}'.format(confirmar))
comentario = input('Comentario: ')