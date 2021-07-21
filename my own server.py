from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("The Server App")
window.geometry("800x600")
window.resizable(True,True)
font_header = ('Arial',15)
font_entry = ('Arial',12)
font_label = ('Arial',11)
base_padding = {'padx':10,'pady':8}
header_padding = {'padx':10,'pady':12}
def clicked():
    username = username_entry.get()
    password = password_entry.get()
    avatar = avatar.load()
    messagebox.showinfo('''Welcome to the car server. Here you can think of a car and get the resources for the car that you are thinking of.
                        So the first thing is that you will be put into creative mode so that you can see the resources and how they look like.
                        Then you can go into survival and go mining and because you know how they look like you can mine the ore with a iron picaxe or
                        above and the crafting recipies will be in the crafting book. Enjoy!''',{username},{password})
main_label = Label(window,text = 'The car server',font = font_header,justify = CENTER)
main_label.pack()
username_label = Label(window,text = 'login',font = label_font)
username_label.pack()
password_label = Label(window,text = 'password',font = label_font)
username_entry = Entry(window,bg = '#00ff00',tg = '#000000',bg = '#0000ff')
#C:\Users\amevs\OneDrive\Desktop\this folder is for coding
username_entry.pack()
password_entry.pack()
send_btn = Button(window,text = 'enter the only car server in minecraft',command = clicked)
send_btn.pack(**base_padding)
window.mainloop()
number_mods = 3
mod1 = 'crafting'
mod2 = 'create car'
mod3 = 'gas station'
def crafting(name,materials,number):
    name = [tesla,BMW,lamborgini,Toyota,Audi,ferrari,buggati,mercedes,rolls royce,TATA,hyundai,Nissan,LEXUS,opel,chevorlet,ford,mitsubishi,vw,skoda,renault,fiat,Honda,geely,peugeot,pininfarina,porche,dodge,'range' rover,land rover,kia,bently,cadilac,crysler,suzuki,maruti,volvo,maserati,mazda,apura,alfa romeo,infiniti,mini cooper,Jeep,aston martin,pontiac,citron,maybach,daewoo,hummer,haval,GMC,Morris Garages,mahindra,cherry,datsun,]
materials = [iron ingot,leather,glass,wool,glass pane,dye]
materials2 = [plastic,carbon fiber,wires,wheel,seats,lamps,rubber,rods,aluminum,titanium,neon,]
