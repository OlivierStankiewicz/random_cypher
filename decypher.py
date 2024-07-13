from CipherManager import CipherManager

cipherManager = None

with open("cyphered_file.txt", "r") as file:
    cipherManager = CipherManager(file.read(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

while True:
    cipherManager.decrypt()

    cipherManager.calc_letter_distribution()

    cipherManager.printText()

    print('''\nInput two characters to be swapped (x=y)
Q to quit
"randomize" to shuffle the cypher randomly
"confirm" to mofify confirmed letters''')

    usr_input = input(">")
    if usr_input.lower() == 'q':
        break

    if usr_input.lower() == "randomize":
        cipherManager.randomize_cipher()
        continue

    if usr_input.lower() == "confirm":
        while True:
            print("\nConfirmation mode")
            print("Currently confirmed:")
            print(cipherManager.confirmed_letters)
            print('Type in a letter to toggle ("exit" to exit)')
            usr_input = input('>')
            if usr_input.lower() == "exit":
                break
            cipherManager.modify_confirmed(usr_input)
        continue


    if len(usr_input) != 3:
        print("Wrong format, try again")
        continue

    usr_input = list(usr_input)

    cipherManager.swap_letters(usr_input[0], usr_input[2])

print('Decrypted text:')
cipherManager.printText()

with open("decyphered_file.txt", "w") as file:
    file.write(cipherManager.text)