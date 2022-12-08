import random

def password():
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    c = ['1','2','3','4','5','6','7','8','9','0']
    otvet = ''
    for i in range(11):
        otvet += random.choice(a + c)
    return otvet

d = password()
print('Password:', d)
