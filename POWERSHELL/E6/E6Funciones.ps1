## Keila Sofía Caballero Ramos/ Gilberto Eduardo Galván García/ Marco Arturo Cantú Vivanco ##

do{ 
    switch($opc){
    1 {
       try{
           Ver-StatusPerfil
       } catch{
        Write-Host "Ocurrió un error" 
       }  
    }
    2 { 
       Set-Status1 -ErrorAction SIlentlyContinue
    }
    3 { 
       Ver-PerfilRedActual 
    }
    4 { 
       Cambiar-PerfilRedActual  
    }
    5 { 
       Ver-ReglasBloqueo 
    }
    6 { 
       Agregar-ReglasBloqueo 
    }
    7 { 
       Eliminar-ReglasBloqueo
    }
    default { 
        Write-Host "Opción no válida"
    }
    }
    $opc = Read-Host -Prompt "`nQué función desea realizar? `n[1] Ver Status `n[2] Cambiar Status `n[3] Ver Perfil de Red Actual`n[4] Cambiar Perfil de Red Actual `n[5] Ver Reglas de Bloqueo `n[6] Agregar Reglas de Bloqueo `n[7] Eliminar Reglas de Bloqueo `n[8] Salir `n"
}while($opc -ne 8)