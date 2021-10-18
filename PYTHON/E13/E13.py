#KEILA SOFÍA CABALLERO RAMOS
#GILBERTO EDUARDO GALVÁN GARCÍA
#MARCO ARTURO CANTÚ VIVANCO

import subprocess

pag = input("Ingresa la página web: ")
comando = "nmap.exe " + pag + " | Out-File -FilePath 'Nmap.txt' "
#print(comando)
lineaPS = "powershell -Executionpolicy ByPass -Command " + comando
runningProcesses = subprocess.check_output(lineaPS)
print(runningProcesses.decode())
