import cv2
import pandas as pd
import os
from PIL import Image, ImageDraw,ImageFont
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
        df = pd.read_excel('./Cyber_workshp.xlsx')
        names = df["Name"]
        cnt = 0
        for name in names:
            cnt += 1
            name = name.strip()
            template = cv2.imread('Certificate_template.jpg')
            x, y = 100, 290
            email = df[df['Name'] == name].iloc[0]['Email']

            template_rgb = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(template_rgb)

            # Write text on the image using PIL
            draw = ImageDraw.Draw(pil_image)
            font = ImageFont.truetype("arial.ttf", 36)  # You can adjust font type and size 
            draw.text((52, 290), name, fill=(0, 0, 0), font=font)

            # Convert back to OpenCV format
            template_with_text = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

            output_folder = 'Generated_Certificates/'
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            output_file_name = os.path.join(output_folder, f'{email}.pdf')
            convert_image_to_pdf(template_with_text, output_file_name, name)
            print(cnt)
    except Exception as e:
        print(f"cenrticficate not done for {name} , {email}, {e}")

generate_certs()
