def main():
    while True:
        # Ask for the user's name
        name = input('Who are you? ').strip()
        if name != 'Trinh':
            print('Access denied. Try again.')
            continue
        
        # Ask for the password
        password = input('Hello, Trinh. What is the password? ').strip()
        if password == 'indiehacker':
            print('Access granted.')
            break
        else:
            print('Incorrect password. Try again.')

if __name__ == '__main__':
    main()
