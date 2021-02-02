from django.contrib.auth.models import User, Group, Permission
from django.core.management import execute_from_command_line
from django.core.management import call_command
from users.models import Profile



print('Truncando base de datos')
execute_from_command_line(["manage.py", "flush", "--no-input"])
print('Finaliza operación de truncado')

print('Inicia Migración')
execute_from_command_line(["manage.py", "migrate"])
print('Finaliza Migración')



print('Registrando productos')
call_command('loaddata', 'dev_tools/defaultData.json')
print('Productos registrados')
print('Creando usuarios administradores por defecto')

usuario, cu = User.objects.get_or_create(username='Admin1')
usuario.id = 1
usuario.is_superuser = True
usuario.first_name = 'Admin1'
usuario.last_name = ''
usuario.email = 'Admin1@correo.udistrial.edu.co'
usuario.is_staff = True
usuario.is_active = True
usuario.set_password('admin#123_')

usuario.save()

usuario, cu = User.objects.get_or_create(username='Admin2')
usuario.id = 1
usuario.is_superuser = True
usuario.first_name = 'Admin2'
usuario.last_name = ''
usuario.email = 'Admin2@correo.udistrial.edu.co'
usuario.is_staff = True
usuario.is_active = True
usuario.set_password('admin#123_')

usuario.save()

usuario, cu = User.objects.get_or_create(username='Admin3')
usuario.id = 1
usuario.is_superuser = True
usuario.first_name = 'Admin3'
usuario.last_name = ''
usuario.email = 'Admin3@correo.udistrial.edu.co'
usuario.is_staff = True
usuario.is_active = True
usuario.set_password('admin#123_')

usuario.save()

print('-----------------------------------')
print('-- Usuario      : Admin1          --')
print('-- Clave        : admin#123_     --')
print('-----------------------------------')
print('-- Usuario      : Admin2        --')
print('-- Clave        : admin#123_     --')
print('-----------------------------------')
print('-- Usuario      : Admin3      --')
print('-- Clave        : admin#123_     --')
print('-----------------------------------')

print('Base de datos actualizada')
