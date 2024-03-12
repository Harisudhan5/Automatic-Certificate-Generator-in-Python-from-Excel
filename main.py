import cv2
import pandas as pd
import os
from PIL import Image
import img2pdf 

def convert_image_to_pdf(image,output_file_name,name):
    try:
        gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        temp_image_path = "Temp/temp.jpg"
        cv2.imwrite(temp_image_path,gray_img)
        with open(temp_image_path,"rb") as f:
            pdf_bytes = img2pdf.convert(f.read())
        with open(output_file_name,"wb") as f:
            f.write(pdf_bytes)
        os.remove(temp_image_path)
        return f"Generated PDF {name}"
    except:
        return f"An Error Occured for {name}"

def get_centered_value(name,x):
    text_size = cv2.getTextSize(name, cv2.FONT_HERSHEY_SIMPLEX, 2.5, 5)[0]
    x_centered = x - (text_size[0] // 2)
    return 

def generate_certs():
    df = pd.read_excel('Untitled spreadsheet.xlsx')
    names = df["Name"]
    for name in names:
        name = name.strip()
        template = cv2.imread('Blue Simple Achievement Certificate.png')
        x, y = 980,650

        x_centered = get_centered_value(name,x)
        
        email = df[df['Name'] == name].iloc[0]['Email']
        cv2.putText(template, name, (x_centered, y), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 0, 0), 5, cv2.LINE_AA)
        #cv2.imwrite(f'Generated_Certificates/{name}.jpg', template)
        output_file_name = f'Generated_Certificates/{email}.pdf'
        convert_image_to_pdf(template, output_file_name,name)

generate_certs()
