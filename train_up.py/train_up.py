# Nama : Mahesa Syawal Abdurahman
# Kelas : 1C Rekayasa Perangkat Lunak
# Kode Peserta : NI09

sisi_awal = { 
  "perempuan": ["p1", "p2", "p3"],
"laki_laki": ["l1", "l2", "l3"] 
}
sisi_akhir = {}

print(f'berikut data entitas yang ada pada sisi awal : {sisi_awal}')

for i in range(3):
    key = f"balikan_{i+1}"
    sisi_akhir[key] = [sisi_awal["perempuan"][i],sisi_awal["laki_laki"][i]];

print(f'berikut data entitas yang ada setelah di sebrangkan ke sisi akhir : {sisi_akhir}')