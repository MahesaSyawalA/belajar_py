# nama : mahesa syawal abdurahman
# nim : 2403372
# kelas : 1 C
    
jumlah_barang = int(input('berapa jumlah barang yang ingin anda beli : '));

count = 0;
harga_satuan = 0;

if(jumlah_barang < 100 ) :
    if(jumlah_barang <= 0):
        print('tidak ada barang yang di jumlahkan')
    else:
        count = jumlah_barang * 5000;
        harga_satuan = 5000;
elif(jumlah_barang >= 100 ) :
    count = jumlah_barang * 4000;
    harga_satuan = 4000;
elif(jumlah_barang > 150 ) :
    count = jumlah_barang * 2500;
    harga_satuan = 2500;

print(f'total harga berdasarkan pesanan yang di inginkan sebanyak {jumlah_barang} dengan harga satuan {harga_satuan} adalah Rp.{count}')

