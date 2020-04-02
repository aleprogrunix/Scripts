# Una conexión SSH se inicializa con la creación de un objeto SSHClient
import paramiko 
import os
import pysftp
import time

# Datos del cliente al que nos queremos conectar
ssh_cliente = '192.168.88.1'
ssh_usuario = 'admin'
ssh_clave = ''
ssh_puerto = 22     # En este caso usamos el 22, pero se puede usar el necesario.

# Creamos esta variable que nos permitirá abrir las conexiones ssh.
ssh_client = paramiko.SSHClient()

# Función que nos permitirá conectarnos por ssh
def conectando():
    try:
            # Para pasar el archivo por SFTP tenemos que tener anterior mente una conexión por SSH.
             # ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=ssh_cliente, port=ssh_puerto, username=ssh_usuario, password=ssh_clave)

            print ('¡Conexión establecida satisfactoria!')
            
    except EnvironmentError:

            print ('Conexión fallida... ')
    

# Función que nos permitirá subir el archivo a la antena.
def upload():
    # Una vez conectado tenemos que elegir que archivo vamos a pasar de nuestra ruta local a la ruta remota.
    localPath = '/home/alejandro/Documentos/Python/Ejercicios/configfile-v-6.43.rsc' # Ruta local y archivo a enviar.
    remotePath= '/configfile-v-6.43.rsc' # Ruta remota a donde quiero ingresar el archivo elegido.
    try:
            # abrimos conexion sftp.
            subida = ssh_client.open_sftp()
            # Cargando archivo
            subida.put(localPath, remotePath)
            print ('¡Archivo subido con exito!')
        
    except EnvironmentError:
            print ('Lo sentimos, hubo un error al subir el archivo')    

##########EJECUTAMOS LAS FUNCIONES###################
conectando()
upload()
#####################################################

# Ejecutamos el comando de forma remota para borrar los parametros capturando entrada, salida y error estándar
entrada, salida, error = ssh_client.exec_command('system reset-configuration run-after-reset=configfile-v-6.43.rsc')

# Mostramos la salida estándar en pantalla
print (salida.read())

print ('Reiniciando...')  
time.sleep(60)

# Cerramos la conexión
ssh_client.close()
