# KEILA SOFÍA CABALLERO RAMOS
# GILBERTO EDUARDO GALVÁN GARCÍA
# MARCO ARTURO CANTÚ VIVANCO

<#
.synopsis
Nmap to WebSite

- User Specified WebSite

.Description
The script will create a file with the result of the Nmap analysis.

.parameter website
Specifies the website 

.example
NmapE13 -website google.com
#>


param([Parameter(Mandatory)][string] $website)

nmap.exe $website | Out-File -FilePath 'Nmap.txt'
Write-Host Ejecución Exitosa
