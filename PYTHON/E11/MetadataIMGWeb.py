# -*- encoding: utf-8 -*-

from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import os, glob
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import argparse

#https://www.uanl.mx/eventos/
parser = argparse.ArgumentParser()  
parser.add_argument("-url", dest='url', help="Ingresa la url de donde quieres obtener las imagenes")
params = parser.parse_args()  
url = str(params.url)
print("Url: " + url)

def descargaimg():
    try:
        os.makedirs("Imgs Descargadas")
    except:
        pass  
    #url = input("Ingresa la url de donde quieres obtener las imagenes: ")
    folder = ("Imgs Descargadas")
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        name = image['alt']
        link = image['src']
        with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
    print("Imagenes Descargadas")



def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        #Parse geo references.
        print(exif['GPSInfo'])
        input("...")
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
        exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}
        input()

 
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
    return ret
    
def printMeta():
    IMGs = []
    #ruta = "Imgs Descargada"
    #os.chdir(ruta)
    for img in glob.glob("*.jpg"):
        IMGs.append(img)
    for img in glob.glob(".jpg"):
        IMGs.append(img)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in IMGs:
            fileimg = open(name+".txt", "a") 
            file1 = open("imgdescargadas.txt", "a")
            file1.write(name+"\n")
            #print(os.path.join(root, name))
            fileimg.write("[+] Metadata for file: " + (name) + '\n')
            #print ("[+] Metadata for file: %s " %(name))
            #input()
            try:
                exifData = {}
                exif = get_exif_metadata(name)
                for metadata in exif:
                    fileimg.write("Metadata: " +str(metadata) + " - Value:  " + str(exif[metadata]) + "\n")
                    #print ("Metadata: " +str(metadata) + " - Value:  " + str(exif[metadata]))
                    #print ("\n")
            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)
    print("Metadata Guardada")
descargaimg()                   
printMeta()


