import random

class CipherManager:
    def __init__(self, original_text, characters):
        self.original_text = original_text
        self.text = original_text
        self.characters = characters
        self.cipher = {}
        self.letters_distribution: dict = {}
        self.confirmed_letters = set()

    def randomize_cipher(self):
        self.confirmed_letters = set()
        available_characters = list(self.characters)
        for character in self.characters:
            self.cipher[character] = random.choice(available_characters)
            available_characters.remove(self.cipher[character])

    def set_cipher_default(self):
        for character in self.characters:
            self.cipher[character] = character

    def substitute(self):
        temp_text = list(self.original_text)
        for (index, letter) in enumerate(temp_text):
            if letter in self.cipher:
                temp_text[index] = self.cipher[letter]

        self.text = ''.join(temp_text)

    def encrypt(self):
        self.randomize_cipher()
        self.substitute()

    def decrypt(self):
        if self.cipher == {}:
            self.set_cipher_default()
        self.substitute()

    def calc_letter_distribution(self):
        self.letters_distribution = {}
        temp_text = list(self.text)
        text_lenght = len(temp_text)

        for letter in temp_text:
            if letter not in self.letters_distribution:
                self.letters_distribution[letter] = 1
            else:
                self.letters_distribution[letter] += 1

        self.letters_distribution = dict(sorted(self.letters_distribution.items(), key=lambda x:x[1], reverse=True))

        for letter in self.letters_distribution:
            self.letters_distribution[letter] *= 100 / text_lenght
            self.letters_distribution[letter] = str(self.letters_distribution[letter]) + "%"

        if self.letters_distribution != {} and len(self.confirmed_letters) == 0 and self.characters != None:
            for key in self.letters_distribution:
                if key not in self.characters:
                    self.confirmed_letters.add(key)

        confirmed_percentage = len(self.confirmed_letters) / len(self.letters_distribution) * 100

        print(f"\nConfirmed letters {confirmed_percentage}%")

        self.display_letter_distribution()

    def display_letter_distribution(self):
        for distribution in self.letters_distribution.items():
            print(distribution)
    
    def swap_letters(self, a, b):
        x = None
        for key, value in self.cipher.items():
            if value == a:
                x = key
                break
        else:
            print(f"Letter {a} not found in cipher")
            return None

        y = None
        for key, value in self.cipher.items():
            if value == b:
                y = key
                break
        else:
            print(f"Letter {b} not found in cipher")
            return None

        self.cipher[x] = b
        self.cipher[y] = a

    def modify_confirmed(self, letter):
        if len(letter)!=1:
            print("Incorrect value for confirmation")
            return None
        
        if letter in self.confirmed_letters:
            self.confirmed_letters.remove(letter)
            return None
        self.confirmed_letters.add(letter)

    def printText(self):
        print('\n')
        for character in self.text:
            if character in self.confirmed_letters:
                print('\033[92m' + character + '\033[0m', end='')
            else:
                print(character, end='')