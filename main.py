import face_recognition
import pyttsx3
engine = pyttsx3.init()

known_people = {
    "known/tomhanks1.jpeg":"tom hanks",
    "known/fredrogersstamp1.png":"fred rogers",
    "you.jpeg":"me.self",
    "a":"jim"
}

known_image = face_recognition.load_image_file("known/tomhanks1.jpeg")
unknown_image = face_recognition.load_image_file("known/fredrogersstamp1.png")
tom_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
results = face_recognition.compare_faces([tom_encoding], unknown_encoding)

if results[0] is True:
    engine.say("Hello")
    print("Hello " + known_people[known_image])
else:
    engine.say("Goodbyeasdfyuhkjasdrfrgur")
    print("Goodbye")

#engine.runAndWait()




