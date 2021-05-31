
import os
import zipfile
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--ziplidosya", required=True)
args = vars(parser.parse_args())

zipli_dosya = args['ziplidosya']

if os.path.exists(zipli_dosya) == False:
    sys.exit("Böyle bir dosya yok")

def cikar(zipli_dosya):
    dosya_adi = zipli_dosya.split(".zip")[0]  #deneme.zip -> deneme
    if zipli_dosya.endswith(".zip"):
        yeni_klasor = os.getcwd() + "/" + dosya_adi
        with zipfile.ZipFile(zipli_dosya, "r") as zip_objesi:
            zip_objesi.extractall(yeni_klasor)
        print("çıkarma işlemi tamamlandı...")
    else:
        print("bu bir zip dosyası degil..")

cikar(zipli_dosya)