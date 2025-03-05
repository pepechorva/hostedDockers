#!/bin/bash

# Default net name
NET_NAME="serversNET"

# docker-compose folders
MARIADB_DIR="./mariadb"
PHPMYADMIN_DIR="./phpmyadmin"
PARTDB_DIR="./partdb"
HEIMDALL_DIR="./heimdall"
PORTAINER_DIR="./portainer"

# help function to show the script usage
show_help() {
  echo "Uso: $0 [-h] [-u [nombre_red]] [-d] [-c nombre_red] [-r nombre_red] [-l] [-a] [-s]"
  echo "  -h  Muestra esta ayuda"
  echo "  -l  Lista los contenedores"
  echo "  -a  [nombre_red] Inicia todos los contenedores y crea la red especificada"
  echo "  -s  [nombre_red] Detiene todos los contenedores y elimina la red especificada"
  echo "  -u  [container] inicia el contenedor especificado"
  echo "  -d  [container] detiene el contenedor especificado"
  echo "  -n  [nombre_red] Crea una red con el nombre especificado"
  echo "  -e  [nombre_red] Elimina la red con el nombre especificado"
  }

#START CONTAINERS
# all containers
up_containers() {
  # check if network exists
  if docker network ls | grep -q "$NET_NAME"; then
    echo "La red $NET_NAME ya existe."
  else
    echo "Creando la red $NET_NAME..."
    docker network create "$NET_NAME"
  fi

  # start containers
  start_container "heimdall"
  start_container "mariadb"
  start_container "phpmyadmin"
  start_container "partdb"
  start_container "portainer"

  echo "Contenedores iniciados."
}

#start container by name
start_container() {
  local name="$1"
  if [ -d "$name" ]; then
    echo "Iniciando $name..."
    docker-compose -f "$name/docker-compose.yml" up -d
  else
    echo "El directorio de $name ($name) no existe."
  fi
}

#STOP CONTAINERS
# Función para detener y eliminar contenedores
stop_containers() {
  stop_container "heimdall"
  stop_container "mariadb"
  stop_container "phpmyadmin"
  stop_container "partdb"
  stop_container "portainer"
  
  echo "Contenedores detenidos y eliminados."
}

#stop container by name
stop_container() {
  local name="$1"
  if [ -d "$name" ]; then
    echo "Deteniendo $name..."
    docker-compose -f "$name/docker-compose.yml" down
  fi
}

# Process command line arguments
while getopts ":h:l:asudne" opt; do
  case $opt in
    h)
      show_help
      exit 0
      ;;
    l)
      docker ps -a
      exit 0
      ;;
    a)
      if [ -n "$OPTARG" ]; then
        NET_NAME="$OPTARG"
      fi
      up_containers
      exit 0
      ;;
    s)
      if [ -n "$OPTARG" ]; then
        NET_NAME="$OPTARG"
      fi
      stop_containers
      exit 0
      ;;
    u)
      if [ -n "$OPTARG" ]; then
        start_container "$OPTARG"
      else
        echo "Debe especificar el nombre del contenedor."
      fi
      exit 0
      ;;
    d)
      if [ -n "$OPTARG" ]; then
        stop_container "$OPTARG"
      else
        echo "Debe especificar el nombre del contenedor."
      fi
      exit 0
      ;;
    n)
      if [ -n "$OPTARG" ]; then
        NET_NAME="$OPTARG"
      fi
      docker network create "$NET_NAME"
      exit 0
      ;;
    e)
      if [ -n "$OPTARG" ]; then
        NET_NAME="$OPTARG"
      fi
      docker network rm "$NET_NAME"
      exit 0
      ;;
    \?)
      echo "Opción inválida: -$OPTARG" >&2
      show_help
      exit 1
      ;;
  esac
done

# if no arguments are passed, show help
if [ $# -eq 0 ]; then
  show_help
  exit 0
fi



echo "Script finalizado."