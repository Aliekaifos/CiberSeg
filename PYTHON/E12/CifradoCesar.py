# KEILA SOFÍA CABALLERO RAMOS
#GILBERTO EDUARDO GALVÁN GARCÍA
#MARCO ARTURO CANTÚ VIVANCO

import detectEnglish
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-modo", dest="modo", help="Tarea a realizar: (cifrar/descifrar/crack)",default="cifrar",
                    required=True)
parser.add_argument("-msj", dest="msj", help="Mensaje a: (cifrar/descifrar/crack)",
                    required=True)
parser.add_argument("-key", dest="key", help="Tarea a realizar: (cifrar/descifrar/crack)")

params = parser.parse_args()
parametro = str(params.modo)
parametro1 = str(params.msj)
parametro2 = str(params.key)

def cifrarcesar(message,clave):
    espacios = 1
    while espacios > 0:

        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex + key
            # print(translatedIndex)
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol
    print(translated)


def desifrarcesar(clave, message):
    espacios = 1
    while espacios > 0:
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key
            # print(translatedIndex)
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
    print(translated)

def crackcesar(message):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    for key in range(len(SYMBOLS)):
        translated = ''
        for symbol in message:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key
                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)
                translated = translated + SYMBOLS[translatedIndex]
            else:
                translated = translated + symbol
        #print('Key #%s: %s' % (key, translated))

        if detectEnglish.isEnglish(translated):
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, translated))
            print()
            print('Enter D if done, anything else to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return symbol


#LspeAgsqAiwxewC

if parametro=="cifrar":
    message = parametro1
    clave = parametro2
    cifrarcesar(message, clave)

elif parametro=="descifrar":
    message = parametro1
    clave = parametro2
    desifrarcesar(clave, message)
elif parametro=="crack":
    message = parametro1
    crackcesar(message)
else:
    print("syntax error")


