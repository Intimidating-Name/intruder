import pyttsx3
#import face_recognition
import cv2
video_capture = cv2.VideoCapture(0)
engine = pyttsx3.init()
engine.say('Sally sells seashells by the seashore.')
engine.say('The quick brown fox jumps over the lazy dog.')
engine.runAndWait()
