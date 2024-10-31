buah = ['apel','mangga','cau']
angka = [1,2]
hewan = ['curut','kecoa']
for i in buah:
    for x in angka:
        for k in hewan :
            print(f'{i} ke {x} hewannya {k}')

for i in buah:
    print(i)

list_baru = []
for t in buah:
    list_baru.append(t.capitalize())

print(list_baru)