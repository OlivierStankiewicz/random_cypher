from CipherManager import CipherManager

cipherManager = None
with open("original_file.txt") as file:
    cipherManager = CipherManager(file.read().upper(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

cipherManager.encrypt()

with open("cyphered_file.txt", "w") as file:
    file.write(cipherManager.text)