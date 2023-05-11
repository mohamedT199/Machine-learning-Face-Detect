import html
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import face_recognition
import cv2
import numpy as np
import os
import serial
import smtplib
import imghdr
import requests
from requests.structures import CaseInsensitiveDict
from email.message import EmailMessage
import smtplib, ssl
import html
import mimetypes
from email.headerregistry import Address
from email.message import EmailMessage
from email.utils import make_msgid
from pathlib import Path

# s = serial.Serial('COM1',9600)
CurrentFolder = os.getcwd()  # Read current folder path
# can't use Logos
image = CurrentFolder + '\\download.jpg'
image2 = CurrentFolder + '\\Diff.jpg'
image3 = CurrentFolder + '\\Test_Image.jpg'

video_capture = cv2.VideoCapture(0)
url = "http://192.168.1.3/api/alert"
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"
data = '{"user_id": "1"}'

# Load a sample picture and learn how to recognize it.
Rahul_image = face_recognition.load_image_file(image3)
Rahul_face_encoding = face_recognition.face_encodings(Rahul_image)[0]

# Load a second sample picture and learn how to recognize it.
Pranali_image = face_recognition.load_image_file(image3)
Pranali_face_encoding = face_recognition.face_encodings(Pranali_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    Rahul_face_encoding,
    Pranali_face_encoding
]
known_face_names = [
    "Rahul_Jadhav",
    "Pranali_Jadhav"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


def check_image(imagee):
    if process_this_frame:
        Mohamed = face_recognition.load_image_file(imagee)
        Mohamed_encoding = face_recognition.face_encodings(Mohamed)[0]
        matches = face_recognition.compare_faces(known_face_encodings, Mohamed_encoding)
        if True in matches:

            Sender_Email2 = os.environ.get("MAIL_USER")
            Reciever_Email = "mt724047@gmail.com"

            Password2 = os.environ.get("MAIL_PASS")
            port = 587  # For starttls
            smtp_server = "smtp.gmail.com"
            message2 = "hello this is test mail "
            context = ssl.create_default_context()

            message = MIMEMultipart()
            message['From'] = Sender_Email
            message['To'] = Reciever_Email
            message['Subject'] = 'A test mail sent by Python. It has an attachment.'
            message.attach(MIMEText(message2, 'plain'))
            attach_file_name = 'download.jpg'
            attach_file = open(attach_file_name, 'rb')  # Open the file as binary mode
            payload = MIMEBase('application', 'octate-stream')
            payload.set_payload((attach_file).read())
            encoders.encode_base64(payload)  # encode the attachment
            payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
            message.attach(payload)
            text = message.as_string()
            newMessage = EmailMessage()
            newMessage['Subject'] = "Confirm Your Email Address for Bahga.com"
            newMessage['From'] = Sender_Email
            newMessage['To'] = Reciever_Email
            newMessage.set_content("""
            Dear Mohamed,

Thank you for registering at bahga.systems. To complete your registration, please click on the following link to verify your email address:

https://bahga.systems

Once you have verified your email address, you will be able to log in to your account and start using our services. If you did not register at Bahga, please ignore this email.

If you have any questions or concerns about your account, please do not hesitate to contact us.

Best regards,
Bahga Support Team
            """)
            with open("Diff.jpg", 'rb') as imeg:
                file_data = imeg.name
                file_type = imghdr.what(imeg.name)
                file_name = imeg.name

            newMessage.add_attachment(file_data, subtype=file_type, filename=file_name)
            # newMessage.set_payload(payload)
            newMessage2 = newMessage.as_string()
            print("message have data")
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(Sender_Email, Password)
                print("server si login")
                # server.sendmail(Sender_Email, Reciever_Email, message2)
                # setup2 message for user
                server.sendmail(Sender_Email, Reciever_Email, newMessage2)
                print("server sent mail")
                server.quit()

            # with smtplib.SMTP_SSL('smtp.gmail.com', 587) as smtp:
            #     smtp.login(Sender_Email, Password)
            #     smtp.send_message(newMessage)
            return "yes it's working"

        else:
            return "it's also working"

# if process_this_frame:
#     Mohamed = face_recognition.load_image_file(image)
#     Mohamed_encoding = face_recognition.face_encodings(Mohamed)[0]
#     matches = face_recognition.compare_faces(known_face_encodings, Mohamed_encoding)
#     if True in matches:
#         print("yes it's Working")

# while True:
#     print("waiting for bell input")
#     #serial_data = s.read()
#     if(b'a' == b'a'):
#         while(1):
#             # Grab a single frame of video
#             ret, frame = video_capture.read()
#
#             # Resize frame of video to 1/4 size for faster face recognition processing
#             small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
#
#             # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
#             #rgb_small_frame = small_frame[:, :, ::-1]
#             rgb_small_frame = cv2.cvtColor(small_frame , cv2.COLOR_BGR2RGB)
#
#             # Only process every other frame of video to save time
#             if process_this_frame:
#                 # Find all the faces and face encodings in the current frame of video
#                 face_locations = face_recognition.face_locations(rgb_small_frame)
#                 face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
#
#                 print('hellllo')
#                 face_names = []
#                 for face_encoding in face_encodings:
#                     # See if the face is a match for the known face(s)
#                     matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#                     name = "Tymor Aya Amer"
#
#                     # # If a match was found in known_face_encodings, just use the first one.
#                     # if True in matches:
#                     #     first_match_index = matches.index(True)
#                     #     name = known_face_names[first_match_index]
#
#                     # Or instead, use the known face with the smallest distance to the new face
#                     face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#                     best_match_index = np.argmin(face_distances)
#                     print(name)
#                     if matches[best_match_index]:
#                         name = known_face_names[best_match_index]
#
#                     face_names.append(name)
#                     if(name == "Tymor Aya Amer"):
#                         #s.write(b'0')
#                         print(name)
#                         i = 0
#                         #serial_data = s.read()
#                         if("serial_data" == b'p'):
#                             print(" Memebers present inside home no need to send image")
#                             print(name)
#                         elif( b'q' == b'q'):
#                             print(name)
#                             while i < 10:
#                                 resp = requests.post(url, headers=headers, data=data)
#                                 print(resp.status_code)
#                                 print("sending image on mail")
#                                 # return_value, image = video_capture.read()
#                                 # cv2.imwrite('opencv.png', image)
#                                 i += 1
#                                 # Sender_Email = "mh3451882@gmail.com"
#                                 # Reciever_Email = "mt724047@gmail.com"
#                                 # Password = "Mohamed_3451882" #type your password here
#                                 # newMessage = EmailMessage()
#                                 # newMessage['Subject'] = "Alert Theft inside your home"
#                                 # newMessage['From'] = Sender_Email
#                                 # newMessage['To'] = Reciever_Email
#                                 # newMessage.set_content('Let me know what you think. Image attached!')
#                                 # with open('opencv.png', 'rb') as f:
#                                 #     image_data = f.read()
#                                 #     image_type = imghdr.what(f.name)
#                                 #     image_name = f.name
#                                 # newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
#                                 # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#                                 #     smtp.login(Sender_Email, Password)
#                                 #     smtp.send_message(newMessage)
#                     elif((name == "Rahul_Jadhav") or (name == "Pranali_Jadhav")):
#                         print('it he')
#                         #s.write(b'1')
#
#             process_this_frame = not process_this_frame
#
#
#             # Display the results
#             for (top, right, bottom, left), name in zip(face_locations, face_names):
#                 # Scale back up face locations since the frame we detected in was scaled to 1/4 size
#                 top *= 4
#                 right *= 4
#                 bottom *= 4
#                 left *= 4
#
#                 # Draw a box around the face
#                 cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#
#                 # Draw a label with a name below the face
#                 cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#                 font = cv2.FONT_HERSHEY_DUPLEX
#                 cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
#
#             # Display the resulting image
#             cv2.imshow('Video', frame)
#
#             # Hit 'q' on the keyboard to quit!
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#
# # Release handle to the webcam
# video_capture.release()
# cv2.destroyAllWindows()
