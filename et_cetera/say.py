# import cowsay
import pyttsx3

engine = pyttsx3.init()
# this = input("What's this? ")
# cowsay.cow(this)
students = ["John", "James", "Monica", "Isaac"]

silicon_valley_characters = ["Richard Hendricks", "Erlich Bachman", "Bertram Gilfoyle", "Dinesh Chugtai", "Jared Dunn", "Gavin Belson", "Monica Hall", "Peter Gregory", "Jian Yang", "Laurie Bream", "Russ Hanneman", "Jack Barker"]


for student in sorted(silicon_valley_characters):
  engine.say(student)
  engine.runAndWait()