# nama : mahesa syawal abdurahman
# nim : 2403372
# kelas : 1 C

ordo = int(input('Input ordo yang ingin dibuat : '))

isi = 1

for baris in range(ordo):
    for kolom in range(ordo):
        print(f'{isi}', end=' ')
        isi += 1
    print()