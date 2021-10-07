# -*- encoding: utf-8 -*-
# Keila Sofía Caballero Ramos

from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import os

def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        # Parse geo references.
        Nsec = exif['GPSInfo'][2][2]
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][3] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        exif['GPSInfo'] = {"Lat": Lat, "Lng": Lng}
        #input()  # Se eliminto el input


def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    retof = [{"GPSInfo": ret["GPSInfo"]},
             {"Modelo": ret["Make"]},         # Se simplifica la info que se obtendra del diccionario
             {"Fecha": ret["DateTimeOriginal"]}]
    return retof  # Se retorna la variable retof simplificada


def printMeta():
    ruta = input("Ruta de imágenes: ")
    os.chdir(ruta)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
            print("[+] Metadata for file: %s " % (name))
            #input()  # se elimina el input
            try:
                exifData = {}
                exif = get_exif_metadata(name)
                for metadata in exif:
                    for x,y in metadata.items():   #se buscan las nuevas claves y valores correspondientes
                        print("Metadata: %s - Value: %s " %(x, y)) #se agregan las nuevas claves y valores
                print("\n")
            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)
printMeta()