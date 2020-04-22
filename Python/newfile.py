import os, sys, shutil, stat
import subprocess as sp

# Programa para la creación de archivos .py, .sh, .src. 

# Pedimos el nombre del archivo. Este nombre tiene que tener su extensión es decir .py, .sh, etc.

nombre = input ('Introduzca el nombre del archivo. Recuerda que este debe llevar su extensión: ')

# Introducido el nombre con su extensión, lo primero que debemos hacer es guardarlo en su directorio correspondiente.
# Tenemos tres directorio uno para los archivos .py. otro para los archivos .sh y el último para los archivos .src.

guardado = []

def guardar_archivo():
    # Para guardar los archivos en su directorio lo prmiero que tenemos que hacer es sacar su extensión. 
    # Para ello utilizo la función endswith.
    if nombre.endswith('.py'):
        directorio_python = os.path.abspath('/home/alejandro/Documentos/python') # Creo la variable para usar la ruta varias veces.
        if not os.path.abspath(directorio_python):  # si no existe esta ruta la creo
            os.mkdir(directorio_python)             # creamos la ruta y guardamos el archivo en el.
            file = open(nombre, 'w')                # Guardamos el archivo
            file.close()                            # Cerramos el archivo
            guardado.append(shutil.move(nombre, directorio_python))  # Lo movemos a su carpeta correspondiente
            
        else:
            file = open(nombre, 'w')                # Si existe la ruta creamos el archivo.
            file.close()
            guardado.append(shutil.move(nombre, directorio_python))  # y por ultimo lo movemos al directorio correspondiente.
            
    elif nombre.endswith('.sh'):
        directorio_script = os.path.abspath('/home/alejandro/Documentos/script')
        if not os.path.abspath(directorio_script):
            os.mkdir(directorio_script)
            file = open(nombre, 'w') 
            file.close()
            os.chmod(nombre, stat.S_IXUSR+stat.S_IRUSR+stat.S_IWUSR) # Damos permiso de administrador.
            guardado.append(shutil.move(nombre, directorio_script))
            
        else:
            file = open(nombre, 'w') 
            file.close()
            os.chmod(nombre, stat.S_IXUSR+stat.S_IRUSR+stat.S_IWUSR)
            guardado.append(shutil.move(nombre, directorio_script))
            
    elif nombre.endswith('.src'):
        directorio_mikrotik = os.path.abspath('/home/alejandro/Documentos/mikrotik')
        if not os.path.abspath(directorio_mikrotik):
            os.mkdir(directorio_mikrotik)
            file = open(nombre, 'w') 
            file.close()
            guardado.append(shutil.move(nombre, directorio_mikrotik))
            
        else:
            file = open(nombre, 'w') 
            file.close()
            guardado.append(shutil.move(nombre, directorio_mikrotik))
            
    else:
        sys.exit('Por favor, introduzca solo archivos .py, .sh o .src') # Si por casualida el archivo introducido no coincide con 
                                                                        # ningún tipo mandará un error y se saldrá de la ejecución.
        

guardar_archivo()

# Con este bucle sacamos la ruta de la lista. Así podemos elegir la ruta a convenir.
for i in guardado:
   ruta_archivo_nuevo =  (i)

print (ruta_archivo_nuevo)

##############################################################################################################################################

print ('Elige un editor:')
print ('[1] Vim')
print ('[2] Code Visual Studio')
print ('[3] Nano')

opcion = int(input ('¿Que editor deseas usar? '))

def elegir_editor():
# Mostraremos un menú donde podremos elegir un editor con un número.
    if opcion == 1:
        sp.call(['vim', ruta_archivo_nuevo])
        exit()
    elif opcion == 2:
        sp.call(['code', ruta_archivo_nuevo, ' --user-data-dir'])
        exit()
    elif opcion == 3:
        sp.call(['nano', ruta_archivo_nuevo])
        exit()
    else:
        print ('El editor elegido no existe...')
   
elegir_editor()


        
    
