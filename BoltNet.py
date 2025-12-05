from tkinter import *
from tkinter import ttk
root = Tk()
root.config(cursor="rtl_logo")
root.title("BOLTNET")
root.geometry("300x300")
enabled = IntVar() 
reba = IntVar()
def boltconn():
            root4 = Tk()
            s = ['B0Ltapb_Hy6L0', 'AbybApb', '4y-4yx_4y-4yx', 'Bouны_Bceленнoй']
            root4.title("BOLT Connecter")
            root4.config(bg="purple", cursor="umbrella")
            import random
            rnd = random.choice(s)
            Label(root4, text=f"Accesible server: {rnd}", bg="purple", fg="white").pack()
            Label(root4, text="Accesible net: B0Lt@pb_B_DD", bg="purple", fg="white").pack()
            def change():
                import random
                d = random.choice(s)
                ass = Label(root4, text=f"Accesible server: {d}",  bg="purple", fg="white").pack()
                def connect():
                    t = Tk()
                    t.config(bg="blue", cursor="man")
                    t.title("connected!")
                    t.geometry("300x250")
                    Label(t, text=f"You are connected to {d}").pack()
                    from PIL import Image, ImageTk
                Button(root4, text="Connect", command=connect, bg="blue", fg="white").pack()
                def film(): 
                        import tkinter as tk  
                        import pyglet
                        r = Tk()
                        r.title("Serie 1")
                        r.config(cursor="man")  # воспроизведение видео  
                        MediaLoad = pyglet.media.load(r"C:\Users\alena\Downloads\mixkit-little-cats-lying-on-an-armchair-32471-hd-ready.mp4")
                        pyglet.player.queue(MediaLoad)
                        pyglet.player.play().pack()
                        r.mainloop() 
            Button(root4, text="Change", command=change).pack() 
            mainloop()
def ddn():
    root2 = Tk()
    root2.geometry("300x300")
    root2.config(cursor="pirate")
    root2.title('DDN52 Connecter')
    radiobutton_variable = IntVar()
    w = ttk.Button(root2, cursor="left_tee").pack()
    Radiobutton(root2, text="Common",  variable = radiobutton_variable, value=1).pack()
    Radiobutton(root2, text="Reborn", variable = radiobutton_variable, value=2).pack()
    Radiobutton(root2, text="Dacha",  variable = radiobutton_variable, value=3).pack()
    Radiobutton(root2, text="Warfight",   variable = radiobutton_variable, value=4).pack()
    vari = IntVar()
    dira = IntVar()
    ttk.Checkbutton(root2, text="Dynamic mode", variable=vari).pack()
    ttk.Checkbutton(root2, text="Connect from servers", variable=dira).pack()
    dd = IntVar()
    Radiobutton(root2, text="Film", variable=dd, value=1).pack()
    Radiobutton(root2, text="Game", variable=dd, value=2).pack()
    def search():
        root3 = Tk()
        root3.title("Connecter found!")
        root3.config(cursor="hand1")
        ll = Label(root3, text="B0Ltn1K_d@tD0M@").pack()
        Label(root3, text="Status: Universal\n").pack()
        s = ['B0Ltapb_Hy6L0', 'AbybApb', '4y-4yx_4y-4yx', 'Bouны_Bceленнoй']
        import random
        ww = random.choice(s)
        Label(root3, text=ww).pack()
        Label(root3, text="Status: Certain").pack()
        def conn():
            t2 = Tk()
            t2.config(bg="blue", cursor="man")
            t2.title("connected!")
            t2.geometry("300x250")
            d = random.choice(s)
            Label(t2, text=f"You are connected to {ww}", bg="blue",fg="white", font="TkMenuFont", compound=BOTTOM).pack()
        Button(root3, text="Connect", command=conn, bg="green").pack()
    Button(root2, text="Connect", command=search).pack()

k = Button(root, text='DDN52', command=ddn, bg="green", cursor="question_arrow")
k.pack() 
bb = Button(root, text="Connect to BOLT", command=boltconn, bg="yellow", cursor="watch").pack()


root.mainloop()
