# nama : mahesa syawal abdurahman
# nim : 2403372
# kelas : 1 C

nilai  = [10, 20, 20, 30, 40, 50, 50, 60];

# karena set tidak mendukung nilai duplikat maka akan otomatis menghapus duplikasi
# lalu di kembalikan lagi variable nya menjadi list 
nilai_tanpa_duplikat_set = set(nilai);
print(nilai_tanpa_duplikat_set);

nilai_tanpa_duplikat = list(nilai_tanpa_duplikat_set);
print(nilai_tanpa_duplikat);

# agar terilhat lebih rapi mari kita urutkan
nilai_tanpa_duplikat.sort()
print(nilai_tanpa_duplikat);



