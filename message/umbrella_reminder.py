"""Check the weather forecast and text an umbrella reminder if it's raining."""

import requests
from bs4 import BeautifulSoup
from twilio.rest import Client  # Updated import

def rain_check():
    """Check weather.com to see if it is likely to rain today."""
    url = 'https://weather.com/en-GB/'
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        weather_elem = soup.select_one('#styles-xz0ANuUJ_nowBlurb_17gst')  # Use select_one for a single element
        if weather_elem:
            weather = weather_elem.get_text()
            return 'rain' in weather.lower()
    except Exception as e:
        print(f"An error occurred while checking the weather: {e}")
    return False

def text_myself(message):
    """Use Twilio to text the message argument to your phone."""
    try:
        client = Client(account_sid, auth_token)  # Updated to use the new Twilio Client
        client.messages.create(
            body=message,
            from_=twilio_number,
            to=my_number
        )
    except Exception as e:
        print(f"An error occurred while sending the text: {e}")

# Twilio credentials and phone numbers
account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
my_number = '+15559998888'
twilio_number = '+15552225678'

if rain_check():
    text_myself('Remember to take an umbrella.')
