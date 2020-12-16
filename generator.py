import random
print ('generator hard pass')
print('автор @DAN SAD')
a = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
length = input('длина пароля?'+ "\n")
n = input('Сколько всего нужно паролей'+ "\n")
n = int(n)
length = int(length)
for n in range(n):
    password =''
    for i in range(length):
        password += random.choice(a)
    print(password)
