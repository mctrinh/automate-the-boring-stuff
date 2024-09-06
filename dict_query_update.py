# Dictionary to store names and their birthdays
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

def main():
    while True:
        # Prompt the user to enter a name or leave blank to quit
        name = input('Enter a name (or press Enter to quit): ').strip()

        if name == '':
            print('Exiting the birthday database.')
            break

        # Check if the name is in the birthday database
        if name in birthdays:
            print(f"{name}'s birthday is on {birthdays[name]}.")
        else:
            print(f"I do not have birthday information for {name}.")
            # Prompt for the birthday and update the database
            bday = input('What is their birthday? ').strip()
            birthdays[name] = bday
            print('Birthday database updated.')

if __name__ == '__main__':
    main()
