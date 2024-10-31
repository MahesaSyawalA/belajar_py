print("hello dunia")
my_list = ['aple','mangga','cau','gedang'];
print(my_list[1:3]);
my_list.append('jambu');
print(my_list);
my_list.insert(1,'cau');
# my_list()
print(my_list);
# menghapus berdasarkan index
my_list.pop(1);
# menghapus berdasarkan itemnya
my_list.remove('mangga');
print(my_list);
# my_list.clear();
# print(my_list);

# latihan tuple 
#  jika menggunakan tuple data tidak bisa dirubah atau bersifat fixed sedangkan
# ketika data berupa list maka data bisa di ubah sesuai kebutuhan 
my_tuple=('kardus','buku','print');
print(my_tuple);
my_new_list = list(my_tuple);
print(my_new_list);
my_new_tuple = tuple(my_list);
print(my_new_tuple);

