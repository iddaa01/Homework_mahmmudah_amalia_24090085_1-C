# Program Pengembangan Anak

# Input Data Pribadi Anak
nama = input('Masukkan nama: ')
usia = int(input('Masukkan usia: '))
tempat_tinggal = input('Masukkan tempat tinggal: ')
no_hp = input('Masukkan no handphone orang tua: ')
pekerjaan_orang_tua = input('Masukkan pekerjaan orang tua: ')
penghasilan_orang_tua = float(input('Masukkan penghasilan orang tua (dalam Rupiah): '))

# Kriteria dan Syarat Kelengkapan
kewarganegaraan = input('Masukkan kewarganegaraan: ')
sekolah_universitas = input('Masukkan sekolah atau universitas: ')
nim = input('Masukkan nomor NIM (jika ada): ')
no_kk = input('Masukkan nomor KK: ')

# Kriteria
if (usia < 18) and (kewarganegaraan == 'WNI') and (pekerjaan_orang_tua not in ['TNI', 'ASN', 'Polri']) and (penghasilan_orang_tua <= 2000000):
    print(f'{nama}, Usia: {usia}, Tempat Tinggal: {tempat_tinggal}, No HP Orang Tua: {no_hp}')
    print('Anak tersebut berhak mendapatkan program bantuan.')
else:
    print(f'{nama}, Anak tersebut tidak berhak mendapatkan program bantuan.')
