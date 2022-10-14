firstname=input("Введите имя: ")
lastname=input("Введите фамилию: ")
yearofbirth=int(input("Введите год рождения: "))
A=firstname
B=lastname
C=yearofbirth
D=("")
print(A, end="_")
print(B, end="_")
print(C)
D=A
A=B
B=D
C+=60
print(A, end="_")
print(B, end="_")
print(C)