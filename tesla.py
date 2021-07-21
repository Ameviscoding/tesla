from tkinter import *
from tkinter import colorchooser
from PIL import Image, ImageTk #pip install Pillow
class Window(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

        #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Tesla App")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        # create Choose lights color object)
        fileMenu = Menu(menu, tearoff=0)

        # adds a command to the menu option
        fileMenu.add_command(label="Change tail-lights color",command=self.changeTlc)
        fileMenu.add_command(label="Change head-lights color", command=self.changeHlc)
        menu.add_cascade(label="Choose lights color", menu=fileMenu)

        configMenu = Menu(menu, tearoff=0)
        configMenu.add_command(label="Birdeye view", command=self.showImgBird)
        configMenu.add_command(label="Side view", command=self.showImg)
        configMenu.add_command(label="Tail view", command=self.showImgTail)
        configMenu.add_command(label="Front view", command=self.showImgFront)
        menu.add_cascade(label="New configuration", menu=configMenu)

        helpMenu = Menu(menu, tearoff=0)
        helpMenu.add_command(label="About", command=self.showText)
        helpMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="Help", menu=helpMenu)
        
    def showImg(self):
        load = Image.open("tesla.png")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def showImgFront(self):
        load = Image.open("front of tesla.jpg")
        front = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=front)
        img.image = front
        img.place(x=0, y=0)

    def showImgTail(self):
        load = Image.open("for the tail lights of tesla.jpg")
        tail = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=tail)
        img.image = tail
        img.place(x=0, y=0)

    def changeHlc(self):
        #self.master.title("Headlights color")
        color_code = colorchooser.askcolor(title ="Choose color of headlights")
        print(color_code)
        type(color_code)
        lime =['#80ff80', '#80ff00', '#00ff00', '#00ff80', '#00ff40']
        yellow = ['#ffff00', '#ffff80']
        peach = ['#ff8080']
        red = ['#ff0000']
        brown = ['#804040', '#800000', '#000000', '#400000', '#804000']
        orange = ['#ff8040', '#ff8000']
        olive = ['#808000', '#808040']
        grey=['#808080', '#c0c0c0']
        green=['#008000', '#004000', '#008080', '#008040', '#004040', '#408080']
        blue=['#80ffff', '#00ffff', '#004080', '#0000ff', '#000080', '#0080ff', '#0080c0','#0000a0', '#000040']
        violet=['#8080ff', '#8080c0', '#800040', '#800080', '#400040', '#8000ff', '#400080']
        white=['#ffffff']

        if color_code[1] in yellow:
            load = Image.open("front of teslayellow.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in peach:
            load = Image.open("front of teslaff8080.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in red:
            load = Image.open("front of teslared.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in brown:
            load = Image.open("front of teslabrown.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in orange:
            load = Image.open("front of teslaorange.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in olive:
            load = Image.open("front of teslaolive.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in grey:
            load = Image.open("front of teslagrey.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in lime:
            load = Image.open("front of teslalime.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in green:
            load = Image.open("front of teslagreen.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in blue:
            load = Image.open("front of teslablue.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in violet:
            load = Image.open("front of teslaviolet.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in white:
            load = Image.open("front of teslawhite.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        else:
            load = Image.open("front of teslapink.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
    def changeTlc(self):
        #self.master.title("Headlights color")
        color_code = colorchooser.askcolor(title ="Choose color of headlights")
        print(color_code)
        type(color_code)
        lime =['#80ff80', '#80ff00', '#00ff00', '#00ff80', '#00ff40']
        yellow = ['#ffff00', '#ffff80']
        peach = ['#ff8080']
        red = ['#ff0000']
        brown = ['#804040', '#800000', '#000000', '#400000', '#804000']
        orange = ['#ff8040', '#ff8000']
        olive = ['#808000', '#808040']
        grey=['#808080', '#c0c0c0']
        green=['#008000', '#004000', '#008080', '#008040', '#004040', '#408080']
        blue=['#80ffff', '#00ffff', '#004080', '#0000ff', '#000080', '#0080ff', '#0080c0','#0000a0', '#000040']
        violet=['#8080ff', '#8080c0', '#800040', '#800080', '#400040', '#8000ff', '#400080']
        white=['#ffffff']

        if color_code[1] in yellow:
            load = Image.open("for the tail lights of teslayellow.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in peach:
            load = Image.open("front of teslaff8080.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in red:
            load = Image.open("front of teslared.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in brown:
            load = Image.open("front of teslabrown.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in orange:
            load = Image.open("front of teslaorange.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in olive:
            load = Image.open("front of teslaolive.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in grey:
            load = Image.open("front of teslagrey.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in lime:
            load = Image.open("front of teslalime.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in green:
            load = Image.open("front of teslagreen.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in blue:
            load = Image.open("front of teslablue.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in violet:
            load = Image.open("front of teslaviolet.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        elif color_code[1] in white:
            load = Image.open("front of teslawhite.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        else:
            load = Image.open("front of teslapink.jpg")
            tail = ImageTk.PhotoImage(load)

            # labels can be text or images
            img = Label(self, image=tail)
            img.image = tail
            img.place(x=0, y=0)
        
            

        

        
        

        
            

        

        
        

    def showImgBird(self):
        load = Image.open("birdeye.jpg")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)


    def showText(self):#multi-line text
        load = Image.open("about.jpg")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def exitProgram(self):
        exit()
        
root = Tk()

#creation of an instance
root.geometry('700x700')
app = Window(root)
#print(im.format, im.size, im.mode)
#image = ImageTk.PhotoImage(pilImage)
#imagesprite = canvas.create_image(698, 305, image=image)
root.iconbitmap('tesla.ico') 
root.mainloop()
