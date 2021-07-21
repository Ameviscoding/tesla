from tkinter import *
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
        fileMenu = Menu(menu)

        # adds a command to the menu option
        fileMenu.add_command(label="Change tail-lights color")
        fileMenu.add_command(label="Change head-lights color")
        menu.add_cascade(label="Choose lights color", menu=fileMenu)

        configMenu = Menu(menu)
        configMenu.add_command(label="Birdeye view", command = self.showImgBird)
        configMenu.add_command(label="Side view")
        configMenu.add_command(label="Tail view")
        configMenu.add_command(label="Front view")
        menu.add_cascade(label="New configuration")

        helpMenu = Menu(menu)
        helpMenu.add_command(label="About")
        helpMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="Help", menu=helpMenu)
        
    def showImgBird(self):
        load = Image.open("birdeye.jpg")
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
