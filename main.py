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

known_people = ["Fred Rogers", "Tom Hanks"]

fred = face_recognition.load_image_file("fred.jpg")
tom = face_recognition.load_image_file("tom.jpg")
known_encodings = [face_recognition.face_encodings(fred)[0], face_recognition.face_encodings(tom)[0]]

engine.say("Scanning.")
engine.runAndWait()


while True:
    camera.capture(output, format="rgb")

    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)
    for face_encoding in face_encodings:
          matches = face_recognition.compare_faces(known_encodings, face_encoding)
          found = False
          for index, value in enumerate(matches):
              if value:
                  print(value)
                  engine.say("Hello {}".format(known_people[index]))
                  engine.runAndWait()
                  found = True

          if not found:
              print("INTRUDER!")
              engine.say("HALT!")
              engine.say("INTRUDER!")
              engine.runAndWait()




