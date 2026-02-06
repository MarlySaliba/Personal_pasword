import random
import string
class Password_generator:
    def __init__(self, generated_password=''):
        self._generated_password = generated_password

    def generator(self):
        letters = string.ascii_letters 
        digits = string.digits                        #String of all the letters and digits 
        special_characters = "!@#$%^&*'-_+<>?/\""     #String of all acceptable characters
        all_characters = letters + digits + special_characters

        # Ensure at least one lowercase letter, one uppercase letter, one digit, and one special character
        password = [
            random.choice(string.ascii_lowercase), 
            random.choice(string.ascii_uppercase),  
            random.choice(string.digits),           
            random.choice(special_characters)       
        ]

        password_length = random.randint(8, 12) 
        password += random.choices(all_characters, k=password_length - len(password))

        random.shuffle(password)

        random_string = ''.join(password)
        
        return random_string
    
password = Password_generator()

print(password.generator())




C:\Users\marly\OneDrive\Documents\Personnal projects in python\Personal_pasword\Password_generator.py
