# import subprocess

# PUERTO = 3724  # Puerto que deseas monitorear

# # Ejecutar tcpdump en segundo plano para capturar el tráfico en el puerto especificado
# proceso_tcpdump = subprocess.Popen(['tcpdump', '-i', 'ens3', 'port', str(PUERTO)], stdout=subprocess.PIPE)

# print(f'Monitoreando el puerto {PUERTO}...')

# # Leer la salida de tcpdump línea por línea
# for linea in iter(proceso_tcpdump.stdout.readline, b''):
    # linea = linea.decode().strip()
    # if 'IP' in linea:  # Filtrar líneas que contengan información de IP (puedes ajustar el filtro según tus necesidades)
        # print('Se recibió una petición en el puerto 3724. Enviando mensaje...')
        # # Código para enviar el mensaje aquí
        
        
# import subprocess

# PUERTO = 3724  # Puerto que deseas monitorear
# NUM_PETICIONES = 10  # Número de peticiones requeridas antes de enviar el mensaje

# # Ejecutar tcpdump en segundo plano para capturar el tráfico en el puerto especificado
# proceso_tcpdump = subprocess.Popen(['tcpdump', '-i', 'ens3', 'port', str(PUERTO)], stdout=subprocess.PIPE)

# print(f'Monitoreando el puerto {PUERTO}...')

# # Variables de control
# contador_peticiones = 0

# # Leer la salida de tcpdump línea por línea
# for linea in iter(proceso_tcpdump.stdout.readline, b''):
    # linea = linea.decode().strip()
    # if 'IP' in linea:  # Filtrar líneas que contengan información de IP (puedes ajustar el filtro según tus necesidades)
        # contador_peticiones += 1
        # print(f'Se recibió una petición en el puerto {PUERTO}. ({contador_peticiones}/{NUM_PETICIONES})')

        # if contador_peticiones == NUM_PETICIONES:
            # print('Se recibieron 10 peticiones. Enviando mensaje...')
            # # Código para enviar el mensaje aquí

            # # Reiniciar el contador de peticiones
            # contador_peticiones = 0
            
# from scapy.all import *

# PUERTO = 8085  # Puerto que deseas monitorear
# NUM_PETICIONES = 100  # Número de peticiones requeridas antes de enviar el mensaje

# # Función para manejar cada paquete capturado
# def manejar_paquete(paquete):
    # global contador_peticiones

    # if IP in paquete:
        # contador_peticiones += 1
        # # print(f'Se recibió una petición en el puerto {PUERTO}. ({contador_peticiones}/{NUM_PETICIONES})')

        # # Obtener la dirección IP de origen
        # direccion_ip = paquete[IP].src
        # print(f'Dirección IP de origen: {direccion_ip}')

        # if contador_peticiones == NUM_PETICIONES:
            # print('Se recibieron 100 peticiones. Enviando mensaje...')

            # # Código para enviar el mensaje aquí, incluyendo la dirección IP de origen

            # # Reiniciar el contador de peticiones
            # contador_peticiones = 0

# # Variables de control
# contador_peticiones = 0

# # Filtrar y capturar paquetes en el puerto especificado
# sniff(filter=f"tcp port {PUERTO}", prn=manejar_paquete)

# from scapy.all import sniff, IP
# import time

# PUERTO = 8085  # Puerto que deseas monitorear

# while True:
    # # Función para manejar cada paquete capturado
    # def manejar_paquete(paquete):
        # if IP in paquete:
            # direccion_ip = paquete[IP].src
            # if direccion_ip not in direcciones_ip:
                # direcciones_ip[direccion_ip] = 1
            # else:
                # direcciones_ip[direccion_ip] += 1

    # # Variables de control
    # direcciones_ip = {}

    # # Filtrar y capturar paquetes en el puerto especificado de forma continua
    # while True:
        # sniff(filter=f"tcp port {PUERTO}", prn=manejar_paquete, count=1, timeout=1)

        # # Imprimir el conteo de direcciones IP únicas
        # print("Conteo de direcciones IP únicas:")
        # for ip, count in direcciones_ip.items():
            # print(f"Dirección IP: {ip}, Cantidad: {count}")

        # # Realizar una pausa antes de capturar el siguiente paquete
        # time.sleep(1)

from scapy.all import sniff, IP
import time

PUERTO = 8085  # Puerto que deseas monitorear

# Función para manejar cada paquete capturado
def manejar_paquete(paquete):
    global contador_peticiones

    if IP in paquete:
        contador_peticiones += 1
        # direccion_ip = paquete[IP].src
        # print(f'Dirección IP de origen: {direccion_ip}')

# Variables de control
contador_peticiones = 0

while True:
    # Reiniciar el contador de peticiones
    contador_peticiones = 0

    # Filtrar y capturar paquetes en el puerto especificado durante 10 segundos
    tiempo_inicial = time.time()  # Obtiene el tiempo actual

    while time.time() - tiempo_inicial <= 10:
        sniff(filter=f"tcp port {PUERTO}", prn=manejar_paquete, count=1, timeout=1)

    # Imprimir el conteo de peticiones
    print(f"Conteo de peticiones: {contador_peticiones}")
