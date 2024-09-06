import re
import pyperclip

# Strong Password Regexes
pass_length_regex = re.compile(r'.{8,}')       # Minimum 8 characters
pass_upper_regex = re.compile(r'[A-Z]')        # Contains an uppercase letter
pass_lower_regex = re.compile(r'[a-z]')        # Contains a lowercase letter
pass_digit_regex = re.compile(r'[0-9]')        # Contains a digit

def is_strong_password(password):
    return (pass_length_regex.search(password) and
            pass_upper_regex.search(password) and
            pass_lower_regex.search(password) and
            pass_digit_regex.search(password))

def main():
    # Retrieve password from clipboard
    password = pyperclip.paste().strip()
    print(password)

    # Check password strength and print relevant message
    if is_strong_password(password):
        print("That's a strong password. Remember to use it for one site only.")
    else:
        print("That's a weak password. I wouldn't recommend using it.")

if __name__ == '__main__':
    main()

