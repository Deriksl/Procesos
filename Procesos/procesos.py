import psutil

def listar_procesos():
    # Obtener la lista de procesos en ejecución
    procesos = psutil.process_iter(attrs=['pid', 'name', 'status', 'num_threads'])

    print(f"{'PID':<10} {'Nombre':<30} {'Estado':<15} {'Hilos':<10}")
    print("=" * 65)

    for proceso in procesos:
        try:
            # Obtener información del proceso
            pid = proceso.info['pid']
            nombre = proceso.info['name']
            estado = proceso.info['status']
            hilos = proceso.info['num_threads']

            # Imprimir información del proceso
            print(f"{pid:<10} {nombre:<30} {estado:<15} {hilos:<10}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            # Manejar el caso donde el proceso ya no existe o no se tiene permiso
            continue

# Llamar a la función directamente
listar_procesos()

# python procesos.py