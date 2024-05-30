# import re

# with open('Berita.txt', 'r') as file:
#     teks_berita = file.read()
# pola = r'\b[A-Z][a-z]*\b'
# hasil = re.findall(pola, teks_berita)
# print(hasil)

# import re


# teks = "Ini adalah contoh teks. Teks ini akan dipisah berdasarkan spasi."
# pola = r'\s+'
# hasil_tanpa_batas = re.split(pola, teks)
# hasil_dengan_batas = re.split(pola, teks, maxsplit=3)

# print("Hasil tanpa batasan jumlah pemisahan:", hasil_tanpa_batas)
# print("Hasil dengan batasan jumlah pemisahan (3 kali):", hasil_dengan_batas)


import re
teks = "Ini adalah contoh teks. Teks ini akan diganti. Teks ini juga akan diganti."
pola = r'Teks'
pengganti = 'Kalimat'
hasil_tanpa_batas = re.sub(pola, pengganti, teks)
hasil_dengan_batas = re.sub(pola, pengganti, teks, count=2)

print("Hasil tanpa batasan jumlah penggantian:", hasil_tanpa_batas)
print("Hasil dengan batasan jumlah penggantian (2 kali):", hasil_dengan_batas)
