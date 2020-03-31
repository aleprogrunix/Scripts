#!/bin/bash

# Creación de un script que nos cree un archivo y nos lo abra directament con code sea cual sea su extension.

# Extensiones usadas en este script:
# python .py
# bash .sh
# mikrotik .rsc
# Cabe la posibilidad de incorporar mas extensiones en el futuro.

creacion_archivo() {

# Guardamos los directorios donde queremos que se guarden cada uno de los archivos diferentes. Así si alguien tiene que cambiarlo por sus propios directorios será mucho más facil.
	dir_sh='/home/alejandro/Documentos/script'
	dir_py='/home/alejandro/Documentos/python'
	dir_rsc='/home/alejandro/Documentos/mikrotik'

# Pedimos el nombre del archivo, el cual se tendra que escribir con su respectiva extensión.
	echo 'Introduzca nombre del archivo: ' 
        read nombre

# Ahora sacamos la extensión para poder enviarlo a sus directorio.
	extension="${nombre##*.}"
	extension=$([[  "$nombre"  = *.* ]] && echo "${nombre##*.}")

# Dependiendo de la extensión que tenga será creado en su respectivo directotio.
	if [ $extension == 'sh' ]; then 
		cd $dir_sh
		touch $nombre
	elif [ $extension == 'py' ]; then
		cd $dir_py
		touch $nombre
	elif [ $extension ==  'rsc' ]; then
		cd $dir_rsc
		touch $nombre
	fi
}

nombre=$creacion_archivo

editor(){
#vamos a pedir que dependiendo del numero ingresado abrira el archivo anterio mente creado con el editor que se ha elegido.
# Yo solo tengo code visual y vim pero podemos meter más.

echo 'Elige un editor: '
echo '[1] Vim'
echo '[2] Code Visual Studio'
echo '......................'

read numero
root=$(id -u)	

case $numero in
	1)
		if [ $root != 0  ]; then
			echo 'Necesitas privilegios: '
			sudo vim $nombre
		else
			vim $nombre
		fi
		;;
	2)
	    	if [ $root == 0  ]; then
		 	code $nombre --user-data-dir 
    		else
    			code $nombre
    		fi		    
		;;
esac
}


creacion_archivo
editor
