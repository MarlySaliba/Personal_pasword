class Password:
    def __init__(self, password=''):  
        self._password = password

    def password_setting(self):
        while True:
            self._password = input("Enter your password: ")  # How you enter your password
            counter = 0
            specials = 0
            uppers = 0
            
            special_characters = "!@#$%^&*'()-_+=<>?/\""  # The special characters that are possible in a password

            # Password analysis & validation
 
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

            # If there are messages, print them and ask for the password again
            if messages:
                print("\n".join(messages))  # Print all validation messages
            else:
                return "You have entered a valid password."  # Return the valid if all conditions are met


# Instantiate the Password class
password_check = Password()

# Call the password_setting method to set a password
password_input = password_check.password_setting()

# Print the result
print(f"{password_input}")
