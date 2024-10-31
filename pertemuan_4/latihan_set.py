my_set = {'apel', 'mangga', 'nanas', 'apel'};
my_set_2 = {'jeruk','kiwi'};
print('apel' in my_set);

# set tidak bisa di ganti hanya bisa di tambahkan data nya dan di gabungkan dengan set lain
my_set.add('nanas');
print(my_set);
# my_set.update(my_set_2);
# print(my_set);

# lalu metode lain ketika ingin menggabungkan kedua set 
# namun tidak mengganti variable pertama dan membuat variable baru 
d = my_set.union(my_set_2);
print(f'ini hasil dari union {d}');

# lalu ada function untuk memfilter data yang ada pada dua variable set 
a = {'jeruk','apel'};
b = {'apel','mangga'};

a.intersection_update(b);
# membuat variable baru
g = a.intersection(b);
print(a);
print(g);
