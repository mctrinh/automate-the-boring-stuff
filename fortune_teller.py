import random

def get_magic_response():
    messages = [
        'It is certain',
        'It is decidedly so',
        'Yes, definitely',
        'Reply hazy, try again',
        'Ask again later',
        'Concentrate and ask again',
        'My reply is no',
        'Outlook not so good',
        'Very doubtful'
    ]
    return random.choice(messages)

def main():
    print("Welcome to the Magic Teller!")
    print("Ask me a yes or no question, and I will give you an answer.")
    
    while True:
        question = input('What is your question? (or type "quit" to exit): ')
        if question.lower() == 'quit':
            print('Goodbye! May the odds be ever in your favor!')
            break
        
        # Get and print the Magic 8-Ball response
        response = get_magic_response()
        print(f"Magic Teller says: {response}")

if __name__ == '__main__':
    main()
