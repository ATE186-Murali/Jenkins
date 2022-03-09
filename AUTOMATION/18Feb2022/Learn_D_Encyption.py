from cryptography.fernet import Fernet

password="murali"

keys=Fernet.generate_key()

print(password)

print(keys)

presencecode=password.encode()

print(presencecode)

encryption=Fernet(keys).encrypt(presencecode)

print(encryption)

decryption=Fernet(keys).decrypt(encryption)

print(decryption.decode())
