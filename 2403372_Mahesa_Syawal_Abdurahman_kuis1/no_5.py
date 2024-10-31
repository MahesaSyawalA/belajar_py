# nama : mahesa syawal abdurahman
# nim : 2403372
# kelas : 1 C
import locale 

locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

# dikonversi menjadi meter terlebih dahulu
Panjang = 8;
Lebar = 10;
Tinggi = 4;


rumus_luas = 2 * (Panjang * Tinggi) + 2 * (Lebar * Tinggi) 

nilai = rumus_luas*520000;

format_idr = locale.currency(nilai, grouping=True)

print(f'total luasnya {rumus_luas} dengan total biaya : RP. { format_idr}');