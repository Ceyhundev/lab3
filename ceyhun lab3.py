import random

def printList(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print(lst[i][j], end='    ')
        print()

# Matris boyutları
n = 4
m = 4

# Rastgele değerlerle matris oluşturma
a = [[random.randint(10, 20) for _ in range(m)] for _ in range(n)]
print("Oluşturulan matris:")
printList(a)
print()

# Baş diagonaldeki elemanların toplamını hesaplama
diagonal_sum = 0
for i in range(n):
    diagonal_sum += a[i][i]

print("Baş diagonaldeki elemanların toplamı:", diagonal_sum)
