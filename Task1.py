# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1



N = int(input("Введите размер массива: "))

X = int(input("Введите число Х: "))

A = []
for i in range(N):
    A.append(int(input()))



i = 0
count = 0
for i in range(N):
    if (A[i] == X):
        count += 1
    i +=1

print(N)
print(A)
print(X)
print(count)