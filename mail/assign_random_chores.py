"""Assign randomized chores to people and email them their appointed tasks."""

import random
import smtplib
from email.mime.text import MIMEText

def get_chore(email, last_chore):
    """Randomly selects a chore that isn't the last chore the person had."""
    available_chores = [chore for chore in chores if chore != last_chore]
    if available_chores:
        new_chore = random.choice(available_chores)
        chore_assignments[email] = new_chore
        chores.remove(new_chore)
    else:
        print(f'No new chores available for {email}. Reshuffling needed.')

def send_chore(email, chosen_chore):
    """Emails the address with chore details."""
    subject = 'This Week\'s Chore'
    body = f'You have been randomly assigned {chosen_chore}. You will not receive this chore next time.'
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'Example@Email.com'
    msg['To'] = email
    
    try:
        smtp_obj.sendmail('Example@Email.com', email, msg.as_string())
    except Exception as e:
        print(f'Failed to send email to {email}: {e}')

def main():
    with open('last_chores.txt') as f:
        last_chores = [line.strip() for line in f.readlines()]

    global chores
    global chore_assignments

    EMAILS = ['Recipient1@email.com', 'Recipient2@email.com', 'Recipient3@email.com', 'Recipient4@email.com']
    chore_assignments = {}

    # Ensure there are enough chores for the number of people
    if len(EMAILS) > len(set(chores)):
        print("Not enough unique chores for the number of people.")
        return

    while len(chore_assignments) < len(EMAILS):
        chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
        for email, last_chore in zip(EMAILS, last_chores):
            get_chore(email, last_chore)

    smtp_obj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_obj.login('Example@Email.com', 'Password')

    for address, chore in chore_assignments.items():
        send_chore(address, chore)

    smtp_obj.quit()

    with open('last_chores.txt', 'w') as f:
        for email in EMAILS:
            f.write(chore_assignments.get(email, '') + '\n')

    print('Everyone has been emailed their latest chore. Program will now close.')

if __name__ == "__main__":
    main()
