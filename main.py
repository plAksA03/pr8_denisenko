import random

def password():
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    otvet = ''
    for i in range(11):
        otvet += random.choice(a)
    return otvet

d = password()
print('Password:', d)
