import sys
from scapy.all import sniff, IP
import time

PUERTO = 8085  # Puerto que deseas monitorear

# Función para manejar cada paquete capturado
def manejar_paquete(paquete):
    global ips_conectadas

    if IP in paquete:
        direccion_ip = paquete[IP].src
        ips_conectadas.add(direccion_ip)

# Conjunto para almacenar las direcciones IP únicas
ips_conectadas = set()

while True:
    # Reiniciar el conjunto de direcciones IP
    ips_conectadas.clear()

    # Filtrar y capturar paquetes en el puerto especificado durante 5 segundos
    tiempo_inicial = time.time()  # Obtiene el tiempo actual

    while time.time() - tiempo_inicial <= 5:
        sniff(filter=f"tcp port {PUERTO}", prn=manejar_paquete, count=1, timeout=1)

    # Imprimir la cantidad de direcciones IP únicas conectadas
    print(f"Número de IPs conectadas: {len(ips_conectadas)}")
