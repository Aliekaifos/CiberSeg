#!/bin/bash

#api cfccfca8a55b497f9f3c5b22a9cd132a

function api_pwned(){
  echo "Ingresa tu API Key"
  read -s HIBPKEY
  echo "Ingresa el archivo con los emails"
  read emails
  for email in $(cat $emails)
  do
    echo $email
    curl -s -o breach.json "https://haveibeenpwned.com/api/v3/breachedaccount/$email" -H "hibp-api-key:$HIBPKEY"
    curl -s -o pasteacc.json "https://haveibeenpwned.com/api/v3/pasteaccount/$email" -H "hibp-api-key:$HIBPKEY"
    echo  -e "You Have Been Pwned at :"
    jq ".[]" breach.json  
    jq ".[]" pasteacc.json  
    echo "---"
    sleep 3
  done
  exit 0
}
api_pwned