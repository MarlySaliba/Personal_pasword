import random
import string
class Password_generator:
    # Initiating all my variables - in this case there is only the generated password
    def __init__(self, generated_password=''):
        self._generated_password = generated_password

    # This is the definition in charge of generating and validating the password
    def generator(self):
        letters = string.ascii_letters 
        digits = string.digits                        #String of all the letters and digits 
        special_characters = "!@#$%^&*'-_+<>?/\""     #String of all acceptable characters
        all_characters = letters + digits + special_characters

        # Ensure at least one lowercase letter, one uppercase letter, one digit, and one special character
        password = [
            random.choice(string.ascii_lowercase),  # At least one lowercase letter
            random.choice(string.ascii_uppercase),  # At least one uppercase letter
            random.choice(string.digits),           # At least one digit
            random.choice(special_characters)       # At least one special character
        ]

        # Fill the remaining characters to make it 8 characters long
        password_length = random.randint(8, 12)  # Random length between 8 and 12
        password += random.choices(all_characters, k=password_length - len(password))

        # Shuffle the password to randomize the positions of the characters
        random.shuffle(password)

        # Convert the list to a string (8 characters long)
        random_string = ''.join(password)
        
        # Return the password that you got
        return random_string
    
password = Password_generator()

print(password.generator())



C:\Users\marly\OneDrive\Documents\Personnal projects in python\Personal_pasword\Password_generator.py