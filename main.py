import cv2
import pandas as pd
import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import img2pdf 

def convert_image_to_pdf(image, output_file_name, name):
    try:
        temp_image_path = "Temp/temp.jpg"
        cv2.imwrite(temp_image_path, image)
        with open(temp_image_path, "rb") as f:
            pdf_bytes = img2pdf.convert(f.read())
        with open(output_file_name, "wb") as f:
            f.write(pdf_bytes)
        print(f"PDF generated for {name} at {output_file_name}")
        os.remove(temp_image_path)
    except Exception as e:
        print(f"Error converting {name} to PDF: {e}")

def generate_certs():
    try:
        df = pd.read_excel('e.xlsx')  # Assuming the Excel file name is 'e.xlsx'
        print(df)
        names = df["Name"]
        cnt = 0
        for name in names:
            print(name)
            cnt += 1
            name = name.strip()
            template = cv2.imread('./template.jpg')
            x, y = 980, 647
            
            # Print information to understand the data
            print(f"Name: {name}")
            print("Unique Names in DataFrame:", df['Name'].unique())
            
            # Locate the row based on the name and extract the email
            email = df.loc[df['Name'] == name, 'Email'].iloc[0]
            print(f"Email: {email}")

            template_rgb = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(template_rgb)
            # Write text on the image using PIL
            draw = ImageDraw.Draw(pil_image)
            font = ImageFont.truetype("arial.ttf", 50)  # adjust font type and size  
            draw.text((60, 267), name, fill=((25, 151, 251)), font=font)

            # Convert back to OpenCV format
            template_with_text = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

            output_folder = 'Generated_Certificates/'
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            output_file_name = os.path.join(output_folder, f'{email}.pdf')
            convert_image_to_pdf(template_with_text, output_file_name, name)
            print(cnt)
    except Exception as e:
        print(f"Certificate not generated for {name}, {email}. Error: {e}")

generate_certs()
