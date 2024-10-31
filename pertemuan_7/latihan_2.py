# nama : mahesa syawal abdurahman
# nim : 2403372
# kelas : 1 C

count = 0
index = 0 
stringOutput = ''

while index >= 0:
    user = int(input('input nilai jika ingin berhenti berikan nilai - : '))  
    index = user
    if user >= 0:
        count += user
        stringOutput += str(user) + '+'

print(f'{stringOutput[:-1]} = {count}')
