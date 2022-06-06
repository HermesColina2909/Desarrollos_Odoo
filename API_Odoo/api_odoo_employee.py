#Importando librerias
import xmlrpc.client

#Conexion con la base de datos
url = 'https://yummy-careers-pruebas-5052211.dev.odoo.com'                  #Dominio o IP de la base de datos
db = 'yummy-careers-pruebas-5052211'                                        #Nombre de la base de datos
username = 'admin'                                                          #Usuario de la base de datos
password = '123'                                                            #Contraseña de usuario

#iniciando sesion
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))       #Proporciona metallamadas que no requieren autentificacion
version_db = common.version()                                              #Asignar common a una variable para imprimir
uid = common.authenticate(db, username, password, {})                      #Identificador de usuario utilizado en las metallamadas autentificadas
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))       #Imprimir variable version_db para mostrar datos de la base de datos
print(version_db)

#Extraer registros de la base de datos
res = models.execute_kw(db, uid, password, 'hr.employee', 'search_read', [[['department_id', '!=', False]]], {'fields': [
    'name', 
    'work_phone', 
    'work_email', 
    'department_id'
    ], 
    'limit': 100
    }
)
employee_num = len(res)
print(res)
print('Numero de empleados en yummy: {}'.format(employee_num))
comentario = input('Comentario: ')