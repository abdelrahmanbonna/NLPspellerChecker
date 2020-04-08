#Importing packages
from tkinter import *
import checker

#Creating GUI and setting it's properties
app = Tk()
app.title("English Spelling Checker")
app.geometry("1024x600")
app.resizable(0,0)
app.configure(background="limegreen")

#Variables
result=StringVar(app)
result.set("Typo:-----")
brain=checker.SpellerChecker


#Text areas
insertedText=Text(app, width=60, height=30,wrap=WORD)
insertedText.place(x=3,y=25)
outText=Text(app, height=30, width=60, wrap=WORD)
outText.place(x=535,y=25)


#labels
insertLable =Label(app,text="Insert Text:",bg="limegreen").place(x=3,y=3)
outLable =Label(app,text="Output:",bg="limegreen").place(x=535,y=3)
resultLabel=Label(app,textvariable=result,bg="limegreen").place(x=160,y=570)

#Functions to use in Buttons
def corrects():
    outText.delete('1.0', END)
    outText.insert(INSERT,brain.correctTypos(insertedText.get("1.0",END)))

def checks():
    result.set(brain.check(insertedText.get("1.0",END)))
    
#Buttons
checkButton=Button(app,text="Check",width=20,command=checks).place(x=3,y=570)
correctButton=Button(app,text="Correct",width=20,command=corrects).place(x=535,y=570)


#Creating the main loop to draw the app
app.mainloop()
