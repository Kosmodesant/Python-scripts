from email.message import EmailMessage

message = EmailMessage()
sender = "example@example.com"
recipient = "example@example.com"
body = """Hey there!
...
... I'm learning to send emails using Python!"""


message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
message.set_content(body)


import os.path
attachment_path = (r"example.jpg")
attachment_filename = os.path.basename(attachment_path)
import mimetypes
mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)

mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)

print(mime_subtype)



with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename=os.path.basename(attachment_path))
print(message)

import smtplib
mail_server = smtplib.SMTP_SSL('smtp.example.com')
mail_server.set_debuglevel(1)

import getpass
mail_pass = getpass.getpass('Password? ')
mail_server.login(sender, mail_pass)
mail_server.send_message(message)
