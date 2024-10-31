# nama : mahesa syawal abdurahman
# nim : 2403372
# kelas : 1 C

jumlah = 0
index = 0
stringOutput = ''
# print('test')

while index < 10 :
    index += 1 
    jumlah = jumlah + index
    
    if index < 10:
        stringOutput += str(index) + '+'
    else: 
        stringOutput += str(index)

print(f'{stringOutput} = {jumlah}')   

for i in range(10, -6, -2):
    print (f'{i}')