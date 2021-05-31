import sys
import os
import img2pdf

klasor_yolu = "fotograflar"
if os.path.isdir(klasor_yolu):
	with open("fotograflar.pdf","wb") as pdf_dosya:
		fotograflar = []
		for dosya_adi in os.listdir(klasor_yolu):
			if dosya_adi.endswith(".jpg"):
				yol = os.path.join(klasor_yolu,dosya_adi)
				fotograflar.append(yol)
		pdf_dosya.write(img2pdf.convert(fotograflar))

elif os.path.isfile(klasor_yolu):
	if klasor_yolu.endswith(".jpg"):
		with open("fotograflar_2.pdf","wb") as pdf_dosya:
			pdf_dosya.write(img2pdf.convert(klasor_yolu))

else:
	print("lütfen jpg uzantılı bir dosya veya içerisinde jpg uzantılı dosya olan klasor giriniz")