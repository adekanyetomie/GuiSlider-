from tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)


red = GPIO.PWM(2,500)
red.start(100)
blue = GPIO.PWM(3,500)
blue.start(100)
green = GPIO.PWM(4, 500)
green.start(100)


class app:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		Label(frame, text = 'Red').grid(row = 0, column = 0)
		Label(frame, text = 'Green').grid(row = 1, column = 0)
		Label(frame, text = 'Blue').grid(row = 2, column = 0)
		scaleRed = Scale(frame, from_ = 0, to = 100, orient = HORIZONTAL, command = self.updateRed)
		scaleRed.grid(row = 0, column = 1)
		scaleGreen = Scale(frame, from_ = 0, to = 100, orient = HORIZONTAL, command = self.updateGreen)
		scaleGreen.grid(row = 1, column = 1)
		scaleBlue = Scale(frame, from_ = 0, to = 100, orient = HORIZONTAL, command = self.updateBlue)
		scaleGreen.grid(row = 2,  column = 1)
	def updateRed(self, duty):
		red.ChangeDutyCycle(float(duty))
	def updateGreen(self, duty):
		green.ChangeDutyCycle(float(duty))
	def updateBlue(self, duty):
		blue.ChangeDutyCycle(float(duty))

root = Tk()
root.wm_title('RGB LED CONTROL')
app = app(root)
root.geometry('200x150+0+0')
root.mainloop()
