import random

def get_answer(answer_number):
    responses = {
        1: ['It is certain', 'Absolutely!'],
        2: ['It is decidedly so', 'Yes, definitely!'],
        3: ['Yes', 'Indeed!'],
        4: ['Reply hazy, try again', 'Not clear, try again'],
        5: ['Ask again later', 'I’ll need to ponder that one'],
        6: ['Concentrate and ask again', 'Focus and ask once more'],
        7: ['My reply is no', 'Nope'],
        8: ['Outlook not so good', 'Things don’t look promising'],
        9: ['Very doubtful', 'Unlikely']
    }
    
    # Choose a random response from the list
    if answer_number in responses:
        return random.choice(responses[answer_number])
    else:
        return 'Error: Invalid answer number.'

def main():
    print("Welcome to the Magic Teller!")
    
    while True:
        input('Ask a yes or no question (or type "quit" to exit): ')
        
        # Generate a random number between 1 and 9
        r = random.randint(1, 9)
        
        # Get the answer based on the random number
        fortune = get_answer(r)
        
        # Display the answer
        print(f"Magic Teller says: {fortune}")
        
        # Check if the user wants to continue or quit
        if input('Do you want to ask another question? (yes/no): ').strip().lower() != 'yes':
            print('Goodbye! Have a magical day!')
            break

if __name__ == '__main__':
    main()
