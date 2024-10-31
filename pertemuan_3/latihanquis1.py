# nama : mahesa syawal abdurahman
# nim : 2403372
# kelas : 1 C

my_tuple = ('pulpen','pena','penghapus');
print(f'data awal : {my_tuple}');
my_list = list(my_tuple);
my_list.insert(1,'tipex');
print( f'hasil insert dengan index 1 {my_list}' );
my_list.append('penggaris');
print(f'hasil append data harus nya berada di paling akhir : {my_list}');
my_list.pop(1);
print(f'hasil pop dengan index 1 : {my_list}');
my_new_tuple = tuple(my_list);
print(f'data akhir setelah di modifikasi : {my_new_tuple}');