# nama : mahesa syawal abdurahman
# nim : 2403372
# kelas : 1 C

data_mobil = {
    'Merk': 'Honda',
    'Tipe': 'HRV',
    'Tahun': '2018',
    'Warna': 'Hitam',
    'NoPolisi': 'D 1234 ABC',
    'Bensin':'Pertalite',
    'Tranmisi': 'Manual',
}
print(f' data mobil lama {data_mobil}');

input_kondisi = str(input('apakah anda ingin mengupdate data ? ya/tidak : '))

if input_kondisi == 'ya':
    input_merk = str(input('masukan merek mobil untuk di update : '));
    input_tipe = str(input('masukan tipe mobil untuk di update : '));
    input_tahun = str(input('masukan tahun mobil untuk di update : '));
    input_warna = str(input('masukan warna mobil untuk di update : '));
    input_nopol = str(input('masukan NoPolisi mobil untuk di update : '));
    input_bensin = str(input('masukan bensin mobil untuk di update : '));
    input_transmisi = str(input('masukan tranmisi mobil untuk di update : '));

    data_mobil['Merk'] = input_merk;
    data_mobil['tipe'] = input_tipe;
    data_mobil['Tahun'] = input_tahun;
    data_mobil['Warna'] = input_warna;
    data_mobil['NoPolisi'] = input_nopol;
    data_mobil['Bensin'] = input_bensin;
    data_mobil['Tranmisi'] = input_transmisi;
    print(f'data yang telah di update {data_mobil}');





