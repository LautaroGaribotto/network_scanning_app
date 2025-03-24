# ==============================
# Escáner de Red Local con Scapy

from scapy.all import sniff, IP
import sqlite3
from datetime import datetime

# Diccionario que traduce números de protocolo IP a nombres legibles
PROTOCOLOS = {
    6: "TCP",
    17: "UDP",
}

# Lista para almacenar los paquetes capturados en esta sesión
paquetes_capturados = []

# Conexión global a la base de datos
conexion_bd = None

def crear_bd():
    """
    Crea la base de datos 'paquetes.db' y la tabla 'paquetes' si no existen.
    """
    global conexion_bd
    conexion_bd = sqlite3.connect('paquetes.db')
    cursor = conexion_bd.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS paquetes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip_origen TEXT,
            ip_destino TEXT,
            protocolo TEXT,
            tamano INTEGER,
            fecha DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conexion_bd.commit()

def insertar_paquete(ip_origen, ip_destino, protocolo, tamano):
    """
    Inserta un paquete en la base de datos.
    """
    global conexion_bd
    cursor = conexion_bd.cursor()
    cursor.execute('''
        INSERT INTO paquetes (ip_origen, ip_destino, protocolo, tamano)
        VALUES (?, ?, ?, ?)
    ''', (ip_origen, ip_destino, protocolo, tamano))
    conexion_bd.commit()

def procesar_paquete(paquete):
    """
    Procesa cada paquete capturado:
    - Extrae IPs, protocolo y tamaño
    - Muestra info en consola
    - Guarda en memoria y en base de datos
    """
    if IP in paquete:
        capa_ip = paquete[IP]
        ip_origen = capa_ip.src
        ip_destino = capa_ip.dst
        numero_protocolo = capa_ip.proto
        nombre_protocolo = PROTOCOLOS.get(numero_protocolo, str(numero_protocolo))
        tamano_paquete = len(paquete)

        paquetes_capturados.append(paquete)
        insertar_paquete(ip_origen, ip_destino, nombre_protocolo, tamano_paquete)

        print(f"Paquete {len(paquetes_capturados)}:")
        print(f"  IP Origen: {ip_origen}")
        print(f"  IP Destino: {ip_destino}")
        print(f"  Protocolo: {nombre_protocolo}")
        print(f"  Tamaño: {tamano_paquete} bytes\n")

def guardar_resumen_en_txt(texto):
    """
    Guarda el resumen del escaneo en un archivo .txt con marca de tiempo.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo = f"resumen_captura_{timestamp}.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(texto)
    print(f"\nResumen guardado en: {nombre_archivo}")

def mostrar_estadisticas_locales():
    """
    Calcula estadísticas de la sesión actual:
    - Total de paquetes
    - Paquetes por protocolo
    - Top 5 IPs de origen y destino por tráfico
    Luego imprime y guarda el resumen en un .txt
    """
    resumen = "\n=== Estadísticas del escaneo ===\n"

    paquetes_por_protocolo = {}
    trafico_origen = {}
    trafico_destino = {}

    for paquete in paquetes_capturados:
        if IP in paquete:
            capa_ip = paquete[IP]
            ip_origen = capa_ip.src
            ip_destino = capa_ip.dst
            numero_protocolo = capa_ip.proto
            nombre_protocolo = PROTOCOLOS.get(numero_protocolo, str(numero_protocolo))
            tamano_paquete = len(paquete)

            paquetes_por_protocolo[nombre_protocolo] = paquetes_por_protocolo.get(nombre_protocolo, 0) + 1
            trafico_origen[ip_origen] = trafico_origen.get(ip_origen, 0) + tamano_paquete
            trafico_destino[ip_destino] = trafico_destino.get(ip_destino, 0) + tamano_paquete

    total_paquetes = len(paquetes_capturados)
    resumen += f"\nTotal de paquetes capturados: {total_paquetes}\n"

    resumen += "\nNúmero de paquetes por protocolo:\n"
    for protocolo, cantidad in paquetes_por_protocolo.items():
        resumen += f"  {protocolo}: {cantidad}\n"

    resumen += "\nTop 5 direcciones IP de origen con mayor tráfico:\n"
    for ip, total in sorted(trafico_origen.items(), key=lambda x: x[1], reverse=True)[:5]:
        resumen += f"  {ip}: {total} bytes\n"

    resumen += "\nTop 5 direcciones IP de destino con mayor tráfico:\n"
    for ip, total in sorted(trafico_destino.items(), key=lambda x: x[1], reverse=True)[:5]:
        resumen += f"  {ip}: {total} bytes\n"

    print(resumen)
    guardar_resumen_en_txt(resumen)

def iniciar_captura():
    """
    Inicia la captura de paquetes.
    Al presionar Ctrl+C, muestra estadísticas y pausa antes de cerrar.
    """
    print("Iniciando la captura de paquetes. Presiona Ctrl+C para detener...\n")
    try:
        sniff(prn=procesar_paquete, filter="ip")
    except KeyboardInterrupt:
        print("\nCaptura detenida por el usuario.")
    finally:
        mostrar_estadisticas_locales()
        if conexion_bd:
            conexion_bd.close()
        input("\nPresiona Enter para cerrar...")

if __name__ == "__main__":
    crear_bd()
    iniciar_captura()
