import tkinter
top = tkinter.Tk()
top.mainloop()

while True:
    try:
        #import tkinter
        #tkinter.Message("Hello there!")
        Cent = int(input ("enter value in fahrenheit: "))
        Faren = ((5/9)*(Cent-32))
        print (str (Cent) + " in fahrenheit is " + str(Faren))
        break
    except:
        print ("please enter a number!")
