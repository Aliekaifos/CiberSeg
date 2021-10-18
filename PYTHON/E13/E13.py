#KEILA SOFÍA CABALLERO RAMOS
#GILBERTO EDUARDO GALVÁN GARCÍA
#MARCO ARTURO CANTÚ VIVANCO

import subprocess

pag = input("Ingresa la página web: ")
#print(comando)
comando = "powershell -Executionpolicy ByPass -File NmapE13.ps1 -website " + pag
runningProcesses = subprocess.check_output(comando)
print(runningProcesses.decode())
