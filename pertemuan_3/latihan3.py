# nama : mahesa syawal abdurahman
# nim : 2403372
# kelas : 1 C

nilai_mahasiswa = [88,75,63,97,82,74,91,80,81,63];
nilai_hasil_sort = nilai_mahasiswa.sort()
nilai_mahasiswa.reverse();
nilai_minimum = min(nilai_mahasiswa);
nilai_maksimum = max(nilai_mahasiswa);
nilai_rata_rata = sum(nilai_mahasiswa) / len(nilai_mahasiswa);

print(f'nilai paling besar : {nilai_maksimum}')
print(f'nilai paling kecil : {nilai_minimum}')
print(f'nilai Rata-Rata : {nilai_rata_rata}')
print(f'nilai kedua terbesar : {nilai_mahasiswa[1]}')


