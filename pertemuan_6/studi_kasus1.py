# nama : mahesa syawal abdurahman
# nim : 2403372
# kelas : 1 C

nilai = int(input('masukan nilai mahasiswa : '));

grade = '';
if (nilai >= 0 ):
    if( nilai >= 90):
        grade = 'A' ;
    elif( nilai < 90 and nilai >= 80 ):
        grade = 'B';
    elif( nilai < 80 and nilai >= 70 ):
        grade = 'C';
    else:
        grade = 'D';
    print(f'Grade yang di dapat dari nilai {nilai} adalah {grade}'); 
else:
    print('nilai tidak tepat');
