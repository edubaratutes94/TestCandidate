import subprocess


def run_command(command):
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error


# Correr el comando git pull
output, error = run_command('git pull')
print(output.decode())
if error:
    print("Error aquii con el GITPULL ", error.decode())
else:
    print("SALIO BIEN EL GIT PULL", output.decode())

# Activar el entorno virtual
output, error = run_command(
    'C:/Mio/Trabajo/MyVenv/Scripts/activate.bat')
print(output.decode())
if error:
    print("Error aquii con el source ", error.decode())
else:
    print("SALIO BIEN EL ACTIVATE", output.decode())


# Correr las migraciones
# output, error = run_command('python manage.py migrate')
# print(output.decode())
# if error:
#    print("Error aquii con el migrate ", error.decode())
# else:
#    print("SALIO BIEN EL MIGRATE", output.decode())


# Correr collect static
# output, error = run_command('python manage.py collectstatic')
# print(output.decode())
# if error:
#    print(error.decode())

# Desactivar el entorno virtual
# output, error = run_command('deactivate')
# print(output.decode())
# if error:
#    print("Error aquii con el desactivar ", error.decode())
# else:
#    print("SALIO BIEN EL DESACTIVATE", output.decode())
# Reiniciar nginx
# output, error = run_command('sudo service nginx restart')
# print(output.decode())
# if error:
#    print(error.decode())

# Reiniciar gunicorn
# output, error = run_command('sudo service gunicorn restart')
# print(output.decode())
# if error:
#    print(error.decode())
