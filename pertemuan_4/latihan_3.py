# nama : mahesa syawal abdurahman
# nim : 2403372
# kelas : 1 C

student_info = {
    "Alice": {"age": 20, "major": "Computer Science"},
    "Bob": {"age": 21, "major": "Mathematics"},
    "Charlie": {"age": 19, "major": "Physics"}
}

# untuk menampilkan key nama yang ada
for key in student_info.keys():
    print(key)

# input nama dari user harus sesuai dengan nama yang ada tidak boleh berbeda bahkan huruf besar kecilnya
input_name = str(input('Inputkan nama siswa : '));

selected_data = student_info[input_name];

print (f'Umur {input_name} adalah {selected_data['age']} dan Prodi nya adalah {selected_data['major']}');