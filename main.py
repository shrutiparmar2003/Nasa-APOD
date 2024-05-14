import webbrowser
import requests
import json
from PIL import Image
from io import BytesIO
import smtplib

DEMO_KEY = 'Your API Key'
url = 'https://api.nasa.gov/planetary/apod'
params = {
    'date': '2024-05-14',
    'api_key': DEMO_KEY,
    'thumbs': 'True',

}


response = requests.get(url, params=params)
json_data = response.json()
image_url = json_data['url']
print(json_data)
if response.status_code == 200:
        try:
            json_data = response.json()
            image_url = json_data['url']

            image_data = requests.get(image_url).content
            with open(f"apod_date.jpg", 'wb') as f:
                f.write(image_data)
            print(f"Image saved as apod_date.jpg")
        except KeyError:
            print("Error: Unexpected JSON format.")
else:
    print("Error: Failed to fetch data from NASA APOD API.")
webbrowser.open(image_url)
print("Press 1 for yes and 0 for no")
mail= int(input("Do you want this APOD to be sent to you in your mail : "))

if mail==1:
    email = input("SENDER EMAIL : ")
    receiver = input("Receiver email : ")
    subject = input("SUBJECT : ")
    message = json_data
    text = f"subject : {subject}\n\n{message}"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, "Your App password")
    server.sendmail(email, receiver, text)
print("Email has been sent to " + receiver)
