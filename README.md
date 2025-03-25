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
	  - $ pip install scapy

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
