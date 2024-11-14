import africastalking
from django.conf import settings


def send_sms(phone_numbers: list, message):
    
    africastalking.initialize(username=settings.AFR_TKG_USERNAME, api_key=settings.AFR_TKG_API_KEY)
    sms = africastalking.SMS
    try:
        response = sms.send(message, phone_numbers)
        if response['SMSMessageData']['Recipients'][0]['status'] != 'Success':
            return False, 'Sending of message has failed.'
    except Exception as e:
        print(e)
        return False, f'Sending message to user failed'
    
    return True, response
