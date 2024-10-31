# nama : mahesa syawal abdurahman
# nim : 2403372
# kelas : 1 C

data_barang_bulan_juli = ['T-Shirt', 'Blouse', 'Kemeja', 'Celana Panjang', 'Rok', 'Baju Renang', 'Tas', 'Topi', 'Sepatu','Sendal'];
print(f'data barang bulan juli adalah : {data_barang_bulan_juli}' );
print(f'dengan total barang bulan juli: {data_barang_bulan_juli.__len__()}')

data_barang_bulan_juli.remove('Baju Renang')
data_barang_bulan_juli.insert(5,'Gamis');

data_barang_bulan_juli.append('Ikat Rambut');
data_barang_bulan_juli.append('Kerudung');


print(f'data barang bulan ini : {data_barang_bulan_juli} ');
print(f'dengan total barang bulan ini  : {data_barang_bulan_juli.__len__()}')

