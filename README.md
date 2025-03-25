ESCÁNER DE RED - Aplicación de Captura y Análisis de Tráfico
---------------------------------------------------------------

Esta herramienta permite capturar paquetes en tiempo real en tu red local y generar un resumen automático en pantalla y en un archivo ".txt", con estadísticas de tráfico por protocolo y por dirección IP.

ARCHIVOS
---------------------------------------------------------------


network_scanning_app.exe - Ejecutable para Windows

network_scanning_app.py - Código fuente en python para revisar o correr desde consola

Instructivo .txt

FUNCIONALIDAD
---------------------------------------------------------------


✔ Captura paquetes desde la red local

✔ Muestra información de cada paquete en consola

✔ Guarda los datos en una base de datos SQLite ("paquetes.db")

✔ Genera automáticamente un archivo ".txt" con el resumen

✔ El resumen incluye:
   - Total de paquetes capturados
   - Paquetes por protocolo
   - Top 5 IPs de origen con mayor tráfico (en bytes)
   - Top 5 IPs de destino con mayor tráfico

REQUISITOS POR SISTEMA OPERATIVO
---------------------------------------------------------------

🪟 WINDOWS
---------------------------------------------------------------
1. Instalar Npcap:
   - Descargar desde: https://npcap.com/#download (Npcap 1.81 installer for Windows 7/2008R2, 8/2012, 8.1/2012R2, 10/2016, 2019, 11 (x86, x64, and ARM64))
   - Durante la instalación, marcar:
     ✅ “Install Npcap in WinPcap API-compatible Mode”

2. Ejecutar la app:
   - Ejecutar como administrador (clic derecho → "Ejecutar como administrador")

3. Uso:
   - Al ejecutarse la app, dejar correr el tiempo que le parezca
   - Presionar Ctrl+C para detener la captura
   - El resumen se mostrará en pantalla y se guardará automáticamente como ".txt"

🐧 LINUX
---------------------------------------------------------------

1. Tener Python 3 instalado:
	  - $ python3 --version

2. Instalar Scapy:
	  - $ pip install scapy (utilizar el gestor de paquetes según tu distribución de linux)

3. Ejecutar el script como superusuario:
	  - $ sudo python3 network_scanning_app.py

4. Al finalizar (Ctrl+C), se generará un archivo ".txt" con el resumen

🍎 MACOS
---------------------------------------------------------------

1. Tener Python 3 instalado:
 	 - $ python3 --version

3. Instalar Scapy:
	  - $ pip install scapy

4. Dar permisos de red a Python si macOS los solicita:
 	 - Preferencias del sistema → Seguridad y privacidad → Red

5. Ejecutar el script como superusuario:
	  - $ sudo python3 network_scanning_app.py

6. Al finalizar (Ctrl+C), se generará un archivo ".txt" con el resumen


CONSULTAR LA BASE DE DATOS (paquetes.db)
---------------------------------------------------------------
Todos los paquetes capturados se almacenan automáticamente en una base de datos
local llamada "paquetes.db", utilizando SQLite. Esto permite hacer consultas,
análisis posteriores o visualizar la información capturada con herramientas externas.

REQUISITO - tener instalado sqlite3 en el equipo

1. Abrir una terminal (cmd, PowerShell, bash, etc.)
2. Ir a la carpeta donde está "paquetes.db"
3. Ingresar al cliente SQLite:

   En Windows:
   > sqlite3 paquetes.db

   En Linux/macOS:
   $ sqlite3 paquetes.db

4. Realizar consultas SQL, por ejemplo:

   - Ver todos los paquetes:
     - SELECT * FROM paquetes;
     

   - Contar paquetes por protocolo:
     - SELECT protocolo, COUNT(*) FROM paquetes GROUP BY protocolo;
     

   - Ver los 10 paquetes más grandes:
     - SELECT * FROM paquetes ORDER BY tamano DESC LIMIT 10;

5. Para salir del cliente SQLite:
   .exit
