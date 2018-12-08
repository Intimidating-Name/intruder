import face_recognition
import pyttsx3
import picamera
import numpy as np

# Get a reference to the Raspberry Pi camera.
# If this fails, make sure you have a camera connected to the RPi and that you
# enabled your camera in raspi-config and rebooted first.
camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)
face_locations = []
face_encodings = []

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('rate', 130)
engine.setProperty('voice', 'english')

known_people = {
    'fred2.jpg': "Fred Rogers",
    'tom2.jpg': "Tom Hanks"
}

known_image = face_recognition.load_image_file("fred2.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

print('Comparing...')
while True:
    camera.capture(output, format="rgb")

    face_locations = face.recognition.face_recognition(output)
    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)
    for face_encoding in face_encodings:
          match = face_recognition.compare_faces([known_encoding], face_encoding)
          if match[0]:
              engine.say("Hello")
              engine.runAndWait()
          else:
              print("INTRUDER!")
              engine.say("HALT!")
              engine.say("INTRUDER!")
              engine.runAndWait()




