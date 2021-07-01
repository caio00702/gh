import hashlib

string = input("Digite: ")

menu = int(input('Escolha um tipo de encode'
             '\n1 MD5'
             '\n2 SHA1'
             '\n3 SHA256'
             '\n4 SHA512'))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print("O Hash da String", string, " é: ", resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print("O Hash da String", string, " é: ", resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print("O Hash da String", string, " é: ", resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print("O Hash da String", string, " é: ", resultado.hexdigest())
else:
    print('Meeeee')