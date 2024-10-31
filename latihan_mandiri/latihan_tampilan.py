import curses
from curses import wrapper
# from tabulate import tabulate

# data = [
#     {"id": 1, "nama": "Budi Santoso", "nik": "1234567890123456"},
#     {"id": 2, "nama": "Siti Nurhaliza", "nik": "1234567890123457"},
#     {"id": 3, "nama": "Ahmad Fauzan", "nik": "1234567890123458"},
#     {"id": 4, "nama": "Rina Sari", "nik": "1234567890123459"},
#     {"id": 5, "nama": "Tono Wirawan", "nik": "1234567890123460"},
# ];

# # print(('Testing print data nasabah').rjust(40, '-'));
# headers = ["id", "nama", "nik"]
# table_data = [[item["id"], item["nama"], item["nik"]] for item in data]
# print(tabulate(table_data, headers=headers, numalign='left',tablefmt='rounded_outline'))

# def main(stdscr):
#     stdscr.clear();
#     stdscr.addstr('Hello World');
#     stdscr.refresh();
#     stdscr.getch();


# wrapper(main);

# data = [1, 2, 2, 3, 4, 4, 5]

# # Menghapus duplikasi dengan mengubah ke set, lalu kembali ke list
# data_unique = set(data)

# print(data_unique)

nilai = [85, 90, 78, 92, 88, 76, 95]

print(max(nilai))
print(sum(nilai))
print(min(nilai))

print(len(nilai))
print(f'rata rta { sum(nilai)/len(nilai) : .0 }')

# for i in range(nilai):
#     i
