import smtplib
from email.message import EmailMessage
from string import Template

email = EmailMessage()
email['from'] = 'Vijay Bhatt'
email['to'] = 'vjbhatt760@gmail.com'
email['subject'] = 'You won a million dollar'

with open('index.html', 'r') as file:
    text = Template(file.read())
    email.set_content(text.substitute(name='Vijay'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('vjbhatt760@gmail.com', 'uefwfcfnjizfcjng')
    smtp.send_message(email)
    print('all looks good')
