from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


red = LED(17)
blue = LED(14)
yellow = LED(26)

MORSE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

def dot():
    
        red.on()
        blue.on()
        yellow.on()
        time.sleep(0.4)
        red.off()
        blue.off()
        yellow.off()
        time.sleep(0.4)
    
def dash():
        red.on()
        blue.on()
        yellow.on()
        time.sleep(1)
        red.off()
        blue.off()
        yellow.off()
        time.sleep(0.4)
        
def Word():
    wordinput = userinput.get()
    for letters in wordinput:
        for char in MORSE[letters.upper()]:
            if char == '-':
                dash()
            elif char == '.':
                dot()
            else: 
                time.sleep(0.5)
        time.sleep(0.5)
        
        
def close():
      win.destroy()
        
 


win = Tk()
win.title("Blink Morse Code")
myFont = tkinter.font.Font(family = 'Helvetica',
                            size = 12, weight = "bold")

button = Button(win, text = 'Blink', font = myFont,
                    command = Word, bg = 'green',height = 1,
                    width = 8)
button.grid(row = 1, column = 1)


userinput = Entry(win, width = 18, bg= 'white')
userinput.grid(row = 0, column = 1)

Label(win, text ='Enter a word').grid(row = 0, column = 0)

ExitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'red', height = 1, width = 7)
ExitButton.grid(row=3, column=1)
