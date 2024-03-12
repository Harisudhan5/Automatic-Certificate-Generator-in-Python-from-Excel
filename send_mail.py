'''import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Replace 'your_actual_password' with your Gmail account password
password = 'jwow dlvq llrf lytj'

# Replace 'your_actual_email@gmail.com' with your Gmail email address
email_address = 'harisudhans574@gmail.com'

# Replace 'your_actual_quote_of_the_day' with the desired quote
quote_of_the_day = 'your_actual_quote_of_the_day'

# Replace 'path/to/your/file.pdf' with the actual path to your PDF file
pdf_file_path = 'Files/file.pdf'

# Create a MIMEMultipart object
message = MIMEMultipart()
message['From'] = email_address
message['To'] = 'speaktoharisudhan@gmail.com'
message['Subject'] = 'Working Day'

# Attach the text message
message.attach(MIMEText(quote_of_the_day, 'plain'))

# Attach the PDF file
with open(pdf_file_path, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={pdf_file_path}')
    message.attach(part)

# Connect to the SMTP server and send the email
connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=email_address, password=password)
connection.sendmail(from_addr=email_address, to_addrs='speaktoharisudhan@gmail.com', msg=message.as_string())
connection.close()
'''

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Function to extract email address from the filename
def extract_email(filename):
    return filename[:-4]

# Replace 'your_actual_password' with your Gmail account password
password = 'jwow dlvq llrf lytj'

# Replace 'your_actual_email@gmail.com' with your Gmail email address
email_address = 'harisudhans574@gmail.com'

# Path to the folder containing PDF files
folder_path = 'Generated_Certificates'

# Connect to the SMTP server
try:
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=email_address, password=password)

    # Iterate through the files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            # Extract email address from the filename
            recipient_email = extract_email(filename)
            print(recipient_email)
            # Create a MIMEMultipart object
            message = MIMEMultipart()
            message['From'] = email_address
            message['To'] = recipient_email
            message['Subject'] = 'This is a mail Automation '

            # Attach the PDF file
            with open(os.path.join(folder_path, filename), 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={filename}')
                message.attach(part)

            # Send the email
            connection.sendmail(from_addr=email_address, to_addrs=recipient_email, msg=message.as_string())
            print(f"Email sent to {recipient_email} successfully!")

    print("All emails sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    connection.quit()
