def hitung(nilai1, nilai2):
    hasil = nilai1 - nilai2
    if hasil < 0:
        return -hasil
    else:
        return hasil

def mutlak(angka):
    if angka < 0:
        return -angka
    else:
        return angka

a, b, c, d = map(int, input().split())
hasil = hitung(a, c) + hitung(b, d)
print(mutlak(hasil))