# nama : mahesa syawal abdurahman
# nim : 2403372
# kelas : 1 C

my_list = ['apel','jeruk','ceri','durian','apel','mangga'];
print(f'data awal : {my_list}');

my_list[2] = 'cherry';
print(f'hasil ubah data ceri : {my_list}');

input_index = int(input('masukan no index yang ingin anda tambahkan data : '));
input_data = str(input('masukan data yang ingin anda input : '));
print(f'index yang anda input {input_index}, dan data yang ingin anda masukan adalah {input_data}');

my_list.insert(input_index , input_data);
print(f'hasil dari inputan anda : {my_list}');

my_list.sort();
print(f'hasil sort adalah : {my_list}');


