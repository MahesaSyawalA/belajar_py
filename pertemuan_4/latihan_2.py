# nama : mahesa syawal abdurahman
# nim : 2403372
# kelas : 1 C

students = {
    "Alice": "Computer Science",
    "Bob": "Mathematics",
    "Charlie": "Physics",
    "David": "Computer Science",
    "Eva": "Mathematics"
}

# deklarasi dulu variabel untuk hasil count nanti
count_math = 0; 
count_comp = 0;
count_phys = 0;

# melakukan looping pada dictionary berdasarkan value nya 
for matkul in students.values():
    # memberikan kondisi untuk menambahkan nilai 1 pada variabel count yang telah di buat
    if "Mathematics" in matkul :
        count_math += 1
    elif "Computer Science" in matkul:
        count_comp += 1
    else :
        count_phys += 1



print(f'prodi computer science sebanyak {count_comp}');
print(f'prodi mathematics sebanyak {count_math}');
print(f'prodi physics sebanyak {count_phys}');

