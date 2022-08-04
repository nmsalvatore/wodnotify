from twilio.rest import Client
from dotenv import load_dotenv
from generator import Workout

import os, schedule, time

load_dotenv()

client = Client(
    os.environ['TWILIO_SID'],
    os.environ['TWILIO_AUTH_TOKEN']
)

def send_new_workout():
    twilio_phone_number = os.environ['TWILIO_PHONE_NUMBER']
    my_phone_number = os.environ['PERSONAL_PHONE_NUMBER']
    workout = Workout()

    message = client.messages.create(
        body=workout,
        from_=twilio_phone_number,
        to=my_phone_number
    )

    print(message.sid)

print('\nRunning wodnotify...\n')
schedule.every().day.at('07:00').do(send_new_workout)
while True:
    schedule.run_pending()
    time.sleep(1)
