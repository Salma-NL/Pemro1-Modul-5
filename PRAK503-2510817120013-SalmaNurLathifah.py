def maksimal(a, b):
    if a > b:
        return a
    else:
        return b

def minimal(a, b):
    if a < b:
        return a
    else:
        return b

jumlah_bilangan = int(input())

maks = -100000
minim = 100000

bilangan = list(map(int, input().split()))

batas = 0
while batas < jumlah_bilangan:
    nilai = bilangan[batas]
    maks = maksimal(maks, nilai)
    minim = minimal(minim, nilai)
    batas += 1

print(maks, minim)