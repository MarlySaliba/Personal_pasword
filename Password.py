class Password:
    def __init__(self, password=''):  
        self._password = password

    def password_setting(self):
        while True:
            self._password = input("Enter your password: ") 
            
            special_characters = "!@#$%^&*'()-_+=<>?/\""  # Special characters possible in password
 
            messages = []
            # Check for sufficient numbers
            if not any(char.isdigit() for char in self._password):
                messages.append("You do not have sufficient numbers in your password.")
                
            # Check for sufficient special characters
            if not any(char in special_characters for char in self._password):
                messages.append("You need to include a special character in your password.")
                
            # Check for uppercase letters
            if not any(char.isupper() for char in self._password):
                messages.append("You need at least 1 uppercase letter in your password.")

            if len(self._password) < 8:
                messages.append("Your password needs to be at least 8 characters long.")
            if ' ' in self._password:  # Check for spaces
                messages.append("Your password must not contain spaces.")

            if messages:
                print("\n".join(messages))
            else:
                return "You have entered a valid password." 

password_check = Password()

password_input = password_check.password_setting()

print(f"{password_input}")

