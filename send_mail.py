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

            # Create a MIMEMultipart object 
            message = MIMEMultipart()
            message['From'] = email_address
            message['To'] = recipient_email
            message['Subject'] = 'MLSC Cloud Security Workshop Participation Certificate'

            # Attach the PDF file
            with open(os.path.join(folder_path, filename), 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={filename}')
                message.attach(part)

            # Add body to the email
            body = '''
Hey folks !!
Thank you for paying attention through out the workshop .Here is your certificate .
Stay tuned for upcoming for upcoming events and workshops 

Follow the links and join our community on regular updates of events of our MLSC community, Microsoft events and Microsoft Learn Challenges and more opportunities....
Follow this link to join my WhatsApp group: https://lnkd.in/gPqf-vi7

Follow the MLSC official LinkedIn page for more updates:

https://lnkd.in/gDksfiux


https://lnkd.in/g8NKX4Un 
'''
            message.attach(MIMEText(body, 'plain'))

            # Send the email
            connection.sendmail(from_addr=email_address, to_addrs=recipient_email, msg=message.as_string())
            print(f"Email sent to {recipient_email} successfully!")

    print("All emails sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    connection.quit()
