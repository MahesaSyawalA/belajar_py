# nama : mahesa syawal abdurahman
# nim : 2403372
# kelas : 1 C

input_umur = int(input('masukan umur : '));

if( input_umur >= 18 and input_umur <= 25 ):
    print('umur anda sesuai kriteria');
    input_iq = int(input('masukan IQ : '));
    if( input_iq >= 130 ):
        print('IQ anda sesuai kriteria');
        input_tinggi = int(input('masukan tinggi badan : '));
        input_jk = str(input('gender anda L/P : '))
        if(input_jk == 'L' and input_tinggi >= 175):
            print(f'anda dapat menjadi model Pria');
        elif(input_jk == 'L' and input_tinggi <= 175):
            print(f'tinggi badan anda tidak memenuhi kriteria model pria');
        if (input_jk == 'P' and input_tinggi >= 170):
            print(f'anda dapat menjadi model Wanita');
        elif (input_jk == 'P' and input_tinggi <= 170):
            print(f'tinggi badan anda tidak memenuhi kriteria model wanita');
    else:
        print('Iq anda tidak sesuai dengan kriteria');
else:
    print('umur anda tidak sesuai dengan kriteria');