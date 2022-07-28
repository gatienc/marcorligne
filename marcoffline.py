from logging import exception
import tkinter as tk
from tkinter import ttk

from matplotlib.pyplot import text

def keyPressed(event):
        """
        Key pressed event listener
        Used to handle RFID reader that is considered like a Keyboard
        When a RFID card is detected, the RFID will write the id of the card
        (acting like a keyboard), and end it with the 'Return' char

        DEBUG TIP: when using a dev environement with a dev database, 
        the keyboard can be used as a fake RFID reader
        """
        
        global rfidBuf
        global id

        print(event.char)
        print(rfidBuf)
        if event.keysym == 'Return':
            try:
                id = int(rfidBuf)
                affid['text']='id:'+str(id)
                affid1['text']='id:'+str(id)
                affid2['text']='id:'+str(id)
            except Exception:
                print(rfidBuf)
                print("erreur dans le texte",rfidBuf," (pas un int)")
            rfidBuf = ""
        else:
            rfidBuf += event.char
            print(rfidBuf)
def update():
    print ('id updated')
def validerpayer(cout,controller):
    if cout<0:
        print("erreur nombre négatif")
    else:
        f=open("HistoMarcoHS.txt","a")
        f.write(str(id)+" "+str(cout)+"\n")
        f.close()
        controller.show_frame(StartPage)

def ajoutcout(part):
    global cout
    global prix
    cout=(int((cout+part)*10))/10
    
    prix['text']=str(cout)+'euro'

LARGEFONT =("Verdana", 25)

class tkinterApp(tk.Tk):
    
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        
        
        self.bind("<Key>", keyPressed)
        self.geometry("800x500")
        # creating a container
        
        container = tk.Frame(self,background="blue")
        container.pack(side = "top", fill = "both", expand = True)
        

        
        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
            frame.grid(row = 0, column = 0,sticky ="nsew")
        
        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()
    

# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label of frame Layout 2
        label = ttk.Label(self, text ="Startpage",background='red', font = LARGEFONT)
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 4, padx = 40, pady = 40)

        button1 = ttk.Button(self, text ="Payer",
        command = lambda : controller.show_frame(Page1))
    
        # putting the button in its place by
        # using grid
        button1.grid(row = 4, column = 3, padx = 40, pady = 40,sticky="s")

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Recharger", 
        command = lambda : controller.show_frame(Page2))
    
        # putting the button in its place by
        # using grid
        button2.grid(row = 4, column = 4, padx = 40, pady = 40,sticky="s")
        global affid
        textid="id:"+id
        affid=tk.Label(self,text=textid,justify='center')
        affid.grid(row = 5, column = 3, padx = 40, pady = 40,sticky="s")
        


# second window frame page1:payer       
class Page1(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Payer", font = LARGEFONT)
        
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
    
        # putting the button in its place
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Recharger",
                            command = lambda : controller.show_frame(Page2) )
        
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        global cout
        global prix
        cout=0
        prix= ttk.Label(self,text=str(cout)+"euro",font=LARGEFONT)
        prix.grid(row=1,column=5,padx=10,pady=10)
        euro= ttk.Label(self,text="1 euro",font=LARGEFONT)
        euro.grid(row=2,column=2,padx=10,pady=10)
        europlus = ttk.Button(self,text="+", command = lambda : ajoutcout(1) )
        europlus.grid(row = 1, column = 2, padx = 10, pady = 10)
        euromoins = ttk.Button(self,text="-", command = lambda : ajoutcout(-1) )
        euromoins.grid(row = 3, column = 2, padx = 10, pady = 10)

        cinquantes= ttk.Label(self,text="0,5 euro",font=LARGEFONT)
        cinquantes.grid(row=2,column=3,padx=10,pady=10)
        cinquantesplus = ttk.Button(self,text="+", command = lambda : ajoutcout(0.5) )
        cinquantesplus.grid(row = 1, column = 3, padx = 10, pady = 10)
        cinquantesmoins = ttk.Button(self,text="-", command = lambda : ajoutcout(-0.5) )
        cinquantesmoins.grid(row = 3, column = 3, padx = 10, pady = 10)

        dix= ttk.Label(self,text="0,1 euro",font=LARGEFONT)
        dix.grid(row=2,column=4,padx=10,pady=10)
        dixplus = ttk.Button(self,text="+", command = lambda : ajoutcout(0.1) )
        dixplus.grid(row = 1, column = 4, padx = 10, pady = 10)
        dixmoins = ttk.Button(self,text="-", command = lambda : ajoutcout(-0.1) )
        dixmoins.grid(row = 3, column = 4, padx = 10, pady = 10)

        global affid1
        textid="id:"+id
        affid1=tk.Label(self,text=textid,justify='center')
        affid1.grid(row = 5, column = 3, padx = 40, pady = 40,sticky="s")

        valid=ttk.Button(self,text="✅", command = lambda : validerpayer(cout,controller)) 
        valid.grid(row = 5, column = 4, padx = 40, pady = 40,sticky="s")


# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Recharger", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Payer",
                            command = lambda : controller.show_frame(Page1))
    
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(StartPage))
    
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        button3 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(Page2))

        global affid2
        textid="id:"+id
        affid2=tk.Label(self,text=textid,justify='center')
        affid2.grid(row = 5, column = 3, padx = 40, pady = 40,sticky="s")

# Driver Code
id=''
rfidBuf=""
app = tkinterApp()
app.title("marchorsligne")


app.mainloop()
