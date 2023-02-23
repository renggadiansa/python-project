#looping / perulangan
angka = [1,2,3,4,5,6,7,8,9,10]
for i in angka:
    print(f"angka i sekarang {i}")
print("end program 1")

#range index default (0)
angka_range = range(5)
for i in angka_range:
    print(f"nilai i sekarang {i}")
print("end program 2")

#range index custom (1)
angka_range = range(1,5)
for i in angka_range:
    print(f"nilai i sekarang {i}")
print("end program 3")

#using string
data_str = "i handsome"
for i in data_str:
    print(f"nilai i sekarang {i}")
print("end program 4")
