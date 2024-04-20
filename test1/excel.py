import os
import random
from datetime import datetime
from openpyxl import Workbook
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def generate_excel_file():
    wb = Workbook()
    ws = wb.active
    ws.title = "TDSheet"

    ws.append(["Имя", "Текущая дата", "Текущее время"])

    for _ in range(10):
        name = generate_random_name()
        current_date = datetime.now().date()
        current_time = datetime.now().time().strftime("%H:%M:%S")
        ws.append([name, current_date, current_time])

    file_name = generate_file_name()

    save_dir = os.path.join(os.path.expanduser("~"), "Documents", "skcu")
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    save_path = os.path.join(save_dir, file_name)

    wb.save(save_path)
    
    return save_path

def generate_random_name():
    names = ["Aкылбек", "Aсылбек", "Болатбек", "Диас", "Макс", "Саня", "Саша", "Ора", "Тора", "Дора"]
    return random.choice(names)

def generate_file_name():
    current_date = datetime.now().strftime("%Y-%m-%d")
    random_number = random.randint(100, 999)
    file_name = f"Aslanbek_{current_date}_{random_number}.xlsx"
    return file_name

def send_email_with_attachment(file_path, recipient_email):
    sender_email = "mukhambetaliev.aslanbek@gmail.com" 
    sender_password = "cyis hwpm jwfy rwid"  

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Excel File"

    with open(file_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(file_path)}")
    msg.attach(part)

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
    print("Email sent successfully!")

try:
    excel_file_path = generate_excel_file()
    recipient_email = "de0th.po@gmail.com"  
    send_email_with_attachment(excel_file_path, recipient_email)
except Exception as e:
    print(f"Failed to send email: {e}")
