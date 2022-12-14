import tkinter as tk
from tkinter import ttk
  


  
class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        windowWidth = 350
        windowHeight = 250

        offsetLeft = int( (self.winfo_screenwidth() - windowWidth) / 2 )
        offsetTop  = int( (self.winfo_screenheight() - windowHeight) / 2 )

        self.geometry('{}x{}+{}+{}'.format(windowWidth, windowHeight, offsetLeft, offsetTop))

        self.title('Konwerter systemów liczbowych') 

        self.minsize(300, 250)
        self.maxsize(300, 250)

        container = tk.Frame(self, relief="ridge", width=300, height=250)
        container.pack(expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 3)        

        self.frames = {} 

        for F in (StartPage, Decy, decBin, decOkt, decHex, Binar, binDec, binOkt, binHex, Oktal, oktDec, oktBin, oktHex, Hexal, hexDec, hexBin, hexOkt):
  
            frame = F(container, self)

            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Wybierz system do którego", justify='center')
        label.grid(padx=75)   
        label = ttk.Label(self, text ="należy Twoja liczba.")
        label.grid(padx=75) 
  
        button1 = ttk.Button(self, text ="Decymalny",
        command = lambda : controller.show_frame(Decy))
        button1.grid(padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Binarny",
        command = lambda : controller.show_frame(Binar))
        button2.grid(padx = 5, pady = 5)

        button3 = ttk.Button(self, text ="Oktalny",
        command = lambda : controller.show_frame(Oktal))
        button3.grid(padx = 5, pady = 5)

        button4 = ttk.Button(self, text ="Heksadecymalny",
        command = lambda : controller.show_frame(Hexal))
        button4.grid(padx = 5, pady = 5)

        label = ttk.Label(self, text ="Patryk Bekier", font=('Helvatical bold',5))
        label.grid() 
        label = ttk.Label(self, text ="Akademia Nauk Stosowanych w Łomży", font=('Helvatical bold',5))
        label.grid() 
        label = ttk.Label(self, text ="Wydział Nauk Informatyczno-technologicznych", font=('Helvatical bold',5))
        label.grid() 
        label = ttk.Label(self, text ="Semestr I", font=('Helvatical bold',5))
        label.grid() 
  

class Decy(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Wybierz system na jaki chcesz")
        label.grid(padx=75) 
        label1 = ttk.Label(self, text =" przekowertować swoją liczbę.")
        label1.grid(padx=75)

        button1 = ttk.Button(self, text ="Binarny",
                            command = lambda : controller.show_frame(decBin))
        button1.grid(padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Oktalny",
                            command = lambda : controller.show_frame(decOkt))
        button2.grid(padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Heksadecymalny",
                            command = lambda : controller.show_frame(decHex))    
        button2.grid(padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Powrót",
                            command = lambda : controller.show_frame(StartPage))     
        button2.grid(padx = 5, pady = 5)
  

class decBin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)       
            
        label = ttk.Label(self, text ="Wprowadź liczbę i zatwierdź.")
        label.grid(padx=75)
  
        wpis = ttk.Entry(self)
        wpis.grid(padx=75)   

        def oblicz():        
            dec = wpis.get()
            dec = int(dec)
            dec = bin(dec)
            label1.config(text=dec[2:])
             
        label1 = ttk.Label(self, text="")
        label1.grid(row = 2)

        button1 = ttk.Button(self, text="Konwertuj", command = oblicz)
        button1.grid(row = 3, padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Powrót", command = lambda : controller.show_frame(StartPage))
        button2.grid(row = 4, padx = 5, pady = 5)


class decOkt(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)       
            
        label = ttk.Label(self, text ="Wprowadź liczbę i zatwierdź.")
        label.grid(padx=75)
  
        wpis = ttk.Entry(self)
        wpis.grid(padx=75)   

        def oblicz():
            decnum = wpis.get()
            decnum = int(decnum)
            decnum = oct(decnum)                   
            label1.config(text=decnum[2:])
             
        label1 = ttk.Label(self, text="")
        label1.grid(row = 2)

        button1 = ttk.Button(self, text="Konwertuj", command = oblicz)
        button1.grid(row = 3, padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Powrót", command = lambda : controller.show_frame(StartPage))
        button2.grid(row = 4, padx = 5, pady = 5)  


class decHex(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)       
            
        label = ttk.Label(self, text ="Wprowadź liczbę i zatwierdź.")
        label.grid(padx=75)
  
        wpis = ttk.Entry(self)
        wpis.grid()   

        def oblicz(padx=75):
            decnum = wpis.get()
            decnum = int(decnum)
            decnum = hex(decnum)                   
            label1.config(text=decnum[2:].upper())
             
        label1 = ttk.Label(self, text="")
        label1.grid(row = 2)

        button1 = ttk.Button(self, text="Konwertuj", command = oblicz)
        button1.grid(row = 3, padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Powrót", command = lambda : controller.show_frame(StartPage))
        button2.grid(row = 4, padx = 5, pady = 5)  


class Binar(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Wybierz system na jaki chcesz")
        label.grid(padx=75) 
        label1 = ttk.Label(self, text =" przekowertować swoją liczbę.")
        label1.grid(padx=75)

        button1 = ttk.Button(self, text ="Decymalny",
                            command = lambda : controller.show_frame(binDec))
        button1.grid(padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Oktalny",
                            command = lambda : controller.show_frame(binOkt))
        button2.grid(padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Heksadecymalny",
                            command = lambda : controller.show_frame(binHex))    
        button2.grid(padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Powrót",
                            command = lambda : controller.show_frame(StartPage))     
        button2.grid(padx = 5, pady = 5)


class binDec(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)       
            
        label = ttk.Label(self, text ="Wprowadź liczbę i zatwierdź.")
        label.grid(padx=75)
  
        wpis = ttk.Entry(self)
        wpis.grid(padx=75)   

        def oblicz():
            bnum = wpis.get()
            bnum = int(bnum)
            dnum = 0
            i = 1
            while bnum!=0:
                rem = bnum%10
                dnum = dnum + (rem*i)
                i = i*2
                bnum = int(bnum/10)                  
            label1.config(text=dnum)
             
        label1 = ttk.Label(self, text="")
        label1.grid(row = 2)

        button1 = ttk.Button(self, text="Konwertuj", command = oblicz)
        button1.grid(row = 3, padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Powrót", command = lambda : controller.show_frame(StartPage))
        button2.grid(row = 4, padx = 5, pady = 5)  


class binOkt(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)       
            
        label = ttk.Label(self, text ="Wprowadź liczbę i zatwierdź.")
        label.grid(padx=75)
  
        wpis = ttk.Entry(self)
        wpis.grid(padx=75)   

        def oblicz():
            bnum = wpis.get()
            bnum = int(bnum)
            odig = 0
            mul = chk = 1
            onum = ""
            while bnum!=0:
                rem = bnum % 10
                odig = odig + (rem * mul)
                if chk%3==0:
                    onum = onum + str(odig)
                    mul = chk = 1
                    odig = 0
                else:
                    mul = mul*2
                    chk = chk+1
                bnum = int(bnum / 10)

            if chk!=1:
                onum = onum + str(odig)                 
            label1.config(text=onum[::-1])
             
        label1 = ttk.Label(self, text="")
        label1.grid(row = 2)

        button1 = ttk.Button(self, text="Konwertuj", command = oblicz)
        button1.grid(row = 3, padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Powrót", command = lambda : controller.show_frame(StartPage))
        button2.grid(row = 4, padx = 5, pady = 5)  


class binHex(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)       
            
        label = ttk.Label(self, text ="Wprowadź liczbę i zatwierdź.")
        label.grid(padx=75)
  
        wpis = ttk.Entry(self)
        wpis.grid(padx=75)   

        def oblicz():
            bnum = wpis.get()
            bnum = int(bnum, 2)
            hdnum = hex(bnum)     
            label1.config(text=hdnum[2:].upper())
             
        label1 = ttk.Label(self, text="")
        label1.grid(row = 2)

        button1 = ttk.Button(self, text="Konwertuj", command = oblicz)
        button1.grid(row = 3, padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Powrót", command = lambda : controller.show_frame(StartPage))
        button2.grid(row = 4, padx = 5, pady = 5)


class Oktal(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Wybierz system na jaki chcesz")
        label.grid(padx=75) 
        label1 = ttk.Label(self, text =" przekowertować swoją liczbę.")
        label1.grid(padx=75)

        button1 = ttk.Button(self, text ="Decymalny",
                            command = lambda : controller.show_frame(oktDec))
        button1.grid(padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Binarny",
                            command = lambda : controller.show_frame(oktBin))
        button2.grid(padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Heksadecymalny",
                            command = lambda : controller.show_frame(oktHex))    
        button2.grid(padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Powrót",
                            command = lambda : controller.show_frame(StartPage))     
        button2.grid(padx = 5, pady = 5)


class oktDec(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)       
            
        label = ttk.Label(self, text ="Wprowadź liczbę i zatwierdź.")
        label.grid(padx=75)
  
        wpis = ttk.Entry(self)
        wpis.grid(padx=75)   

        def oblicz():
            onum = wpis.get()
            onum = int(onum)
            chk = 0
            i = 0
            decnum = 0
            while onum!=0:
                rem = onum%10
                if rem>7:
                    chk = 1
                    break
                decnum = decnum + (rem * (8 ** i))
                i = i+1
                onum = int(onum/10)
     
            label1.config(text=decnum)
             
        label1 = ttk.Label(self, text="")
        label1.grid(row = 2)

        button1 = ttk.Button(self, text="Konwertuj", command = oblicz)
        button1.grid(row = 3, padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Powrót", command = lambda : controller.show_frame(StartPage))
        button2.grid(row = 4, padx = 5, pady = 5)


class oktBin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)       
            
        label = ttk.Label(self, text ="Wprowadź liczbę i zatwierdź.")
        label.grid(padx=75)
  
        wpis = ttk.Entry(self)
        wpis.grid(padx=75)   

        def oblicz():
            onum = wpis.get()
            onum = int(onum)
            rev = 0
            chk = 0
            while onum!=0:
                rem = onum%10
                if rem>7:
                    chk = 1
                    break
                rev = rem + (rev*10)
                onum = int(onum/10)

            if chk == 0:
                onum = rev
                binnum = ""

                while onum!=0:
                    rem = onum%10
                    if rem==0:
                        binnum = binnum + "000"
                    elif rem==1:
                        binnum = binnum + "001"
                    elif rem==2:
                        binnum = binnum + "010"
                    elif rem==3:
                        binnum = binnum + "011"
                    elif rem==4:
                        binnum = binnum + "100"
                    elif rem==5:
                        binnum = binnum + "101"
                    elif rem==6:
                        binnum = binnum + "110"
                    elif rem==7:
                        binnum = binnum + "111"
                    onum = int(onum/10)     
            label1.config(text=binnum)
             
        label1 = ttk.Label(self, text="")
        label1.grid(row = 2)

        button1 = ttk.Button(self, text="Konwertuj", command = oblicz)
        button1.grid(row = 3, padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Powrót", command = lambda : controller.show_frame(StartPage))
        button2.grid(row = 4, padx = 5, pady = 5)


class oktHex(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)       
            
        label = ttk.Label(self, text ="Wprowadź liczbę i zatwierdź.")
        label.grid(padx=75)
  
        wpis = ttk.Entry(self)
        wpis.grid(padx=75)   

        def oblicz():
            onum = wpis.get()
            onum = int(onum)
            chk = i = dnum = 0
            while onum!=0:
                rem = onum % 10
                if rem>7:
                    chk = 1
                    break
                dnum = dnum + (rem * (8 ** i))
                i = i+1
                onum = int(onum / 10)

            if chk == 0:
                hnum = ""
                while dnum != 0:
                    rem = dnum % 16
                    if rem < 10:
                        rem = rem + 48
                    else:
                        rem = rem + 55
                    rem = chr(rem)
                    hnum = hnum + rem
                    dnum = int(dnum / 16)
                hnum = hnum[::-1]     
            label1.config(text=hnum)
             
        label1 = ttk.Label(self, text="")
        label1.grid(row = 2)

        button1 = ttk.Button(self, text="Konwertuj", command = oblicz)
        button1.grid(row = 3, padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Powrót", command = lambda : controller.show_frame(StartPage))
        button2.grid(row = 4, padx = 5, pady = 5)


class Hexal(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Wybierz system na jaki chcesz")
        label.grid(padx=75) 
        label1 = ttk.Label(self, text =" przekowertować swoją liczbę.")
        label1.grid(padx=75)

        button1 = ttk.Button(self, text ="Decymalny",
                            command = lambda : controller.show_frame(hexDec))
        button1.grid(padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Binarny",
                            command = lambda : controller.show_frame(hexBin))
        button2.grid(padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Oktalny",
                            command = lambda : controller.show_frame(hexOkt))    
        button2.grid(padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Powrót",
                            command = lambda : controller.show_frame(StartPage))     
        button2.grid(padx = 5, pady = 5)


class hexDec(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)       
            
        label = ttk.Label(self, text ="Wprowadź liczbę i zatwierdź.")
        label.grid(padx=75)
  
        wpis = ttk.Entry(self)
        wpis.grid(padx=75)   

        def oblicz():
            hnum = wpis.get()            
            dnum = int(hnum, 16)
            label1.config(text=dnum)
             
        label1 = ttk.Label(self, text="")
        label1.grid(row = 2)

        button1 = ttk.Button(self, text="Konwertuj", command = oblicz)
        button1.grid(row = 3, padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Powrót", command = lambda : controller.show_frame(StartPage))
        button2.grid(row = 4, padx = 5, pady = 5)


class hexBin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)       
            
        label = ttk.Label(self, text ="Wprowadź liczbę i zatwierdź.")
        label.grid(padx=75)
  
        wpis = ttk.Entry(self)
        wpis.grid(padx=75)   

        def oblicz():
            hnum = wpis.get()            
            hnum = int(hnum, 16)
            bnum = bin(hnum)
            label1.config(text=bnum[2:])
             
        label1 = ttk.Label(self, text="")
        label1.grid(row = 2)

        button1 = ttk.Button(self, text="Konwertuj", command = oblicz)
        button1.grid(row = 3, padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Powrót", command = lambda : controller.show_frame(StartPage))
        button2.grid(row = 4, padx = 5, pady = 5)


class hexOkt(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)       
            
        label = ttk.Label(self, text ="Wprowadź liczbę i zatwierdź.")
        label.grid(padx=75)
  
        wpis = ttk.Entry(self)
        wpis.grid(padx=75)   

        def oblicz():
            hnum = wpis.get()            
            hnum = int(hnum, 16)
            onum = oct(hnum)
            label1.config(text=onum[2:])
             
        label1 = ttk.Label(self, text="")
        label1.grid(row = 2)

        button1 = ttk.Button(self, text="Konwertuj", command = oblicz)
        button1.grid(row = 3, padx = 5, pady = 5)

        button2 = ttk.Button(self, text ="Powrót", command = lambda : controller.show_frame(StartPage))
        button2.grid(row = 4, padx = 5, pady = 5)


app = tkinterApp()
app.mainloop()