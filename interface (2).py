
from tkinter import *
from tkinter import messagebox
import rsa


def generer(Labele, Labeln, Labeld, p, q):
    try:
        e, n, d = rsa.generate_keypair(p, q)
        print("e = ", e)
        print("n = ", n)
        print("d = ", d)
        Te = StringVar()
        Tn = StringVar()
        Td = StringVar()
        Te.set("e = " + str(e))
        Tn.set("n = " + str(n))
        Td.set("d = " + str(d))
        Labele['textvariable'] = Te
        Labeln['textvariable'] = Tn
        Labeld['textvariable'] = Td
        Labele.pack(side=LEFT, padx=5, pady=5)
        Labeln.pack(side=LEFT, padx=5, pady=5)
        Labeld.pack(side=LEFT, padx=5, pady=5)
    except ValueError as erreur:
        messagebox.showerror("Mauvais choix", erreur)

def chiffrer(LabelResultat, e, n, message):
    Texte = StringVar()
    Texte.set(str(rsa.encrypt(e.get(), n.get(), message.get())))
    LabelResultat['textvariable'] = Texte
    LabelResultat.pack(side=LEFT, padx=5, pady=5)

def chiffrerAleatoire(LabelResultat, message):
    e, n, d = rsa.generate_random_keypair()
    Texte = StringVar()
    Texte.set(str(rsa.encrypt(e, n, message.get())))
    LabelResultat['textvariable'] = Texte
    LabelResultat.pack(side=LEFT, padx=5, pady=5)

    print("e= ",e," - n= ", n, " - d= ",d)

def dechiffrer(LabelResultat, d, n, message):
    Texte = StringVar()
    Texte.set(str(rsa.decrypt(d.get(), n.get(), message.get())))
    LabelResultat['textvariable'] = Texte
    LabelResultat.pack(side=LEFT, padx=5, pady=5)

def dechiffrerCRT(LabelResultat, d, p, q, code):
    Texte = StringVar()
    Texte = StringVar()
    Texte.set(str(rsa.decryptCRT(d.get(), p.get(), q.get(), code.get())))
    LabelResultat['textvariable'] = Texte
    LabelResultat.pack(side=LEFT, padx=5, pady=5)

def wiener(LabelR, Labeld, e, n, code):
    msg, d = rsa.attack_wiener(e.get(),n.get(),code.get())
    Td = StringVar()
    Texte = StringVar()
    Td.set("d = " + str(d))
    Texte.set(msg)
    Labeld['textvariable'] = Td
    Labeld.pack(side=LEFT, padx=5, pady=5)
    LabelR['textvariable'] = Texte
    LabelR.pack(side=LEFT, padx=5, pady=5)

def hastad(LabelR, y, e, listn, listcode):
    y += 35
    Texte = StringVar()
    msg = rsa.attack_hastad(e, listn, listcode)
    print(msg)
    Texte.set(msg)
    LabelR['textvariable'] = Texte
    LabelR.place(x=30, y=y)






def RSAgenerate():

    Mafenetre.title("Générer les clés de RSA")

    for ele in Mafenetre.winfo_children():
        ele.destroy()
    menu()

    p = IntVar()
    q = IntVar()

    Tp = StringVar()
    Tp.set("p :")
    Labelp = Label(Mafenetre, textvariable=Tp, fg='black').pack(side=LEFT)
    cp = Entry(Mafenetre, textvariable=p, bg='bisque', fg='maroon')
    cp.focus_set()
    cp.pack(side=LEFT, padx=5, pady=5)

    Tq = StringVar()
    Tq.set("q :")
    Labelq = Label(Mafenetre, textvariable=Tq, fg='black').pack(side=LEFT)
    cq = Entry(Mafenetre, textvariable=q, bg='bisque', fg='maroon')
    cq.focus_set()
    cq.pack(side=LEFT, padx=5, pady=5)

    Labele = Label(Mafenetre, fg='black')
    Labeln = Label(Mafenetre, fg='black')
    Labeld = Label(Mafenetre, fg='black')

    boutonchiffrer = Button(Mafenetre, text='Génerer', command=lambda: generer(Labele, Labeln, Labeld, p.get(), q.get()))

    boutonchiffrer.pack(side=LEFT, padx=5, pady=5)

    BoutonQuitter = Button(Mafenetre, text='Quitter', command=Mafenetre.destroy)
    BoutonQuitter.pack(side=LEFT, padx=5, pady=5)






def RSAsahl():

    Mafenetre.title("RSA avec une cle choisie")

    for ele in Mafenetre.winfo_children():
        ele.destroy()
    menu()

    message = StringVar()
    e = IntVar()
    n = IntVar()

    Te = StringVar()
    Te.set("e :")
    Labele = Label(Mafenetre, textvariable=Te, fg='black').pack(side=LEFT)
    ce = Entry(Mafenetre, textvariable=e, bg='bisque', fg='maroon')
    ce.focus_set()
    ce.pack(side=LEFT, padx=5, pady=5)

    Tn = StringVar()
    Tn.set("n :")
    Labeln = Label(Mafenetre, textvariable=Tn, fg='black').pack(side=LEFT)
    cn = Entry(Mafenetre, textvariable=n, bg='bisque', fg='maroon')
    cn.focus_set()
    cn.pack(side=LEFT, padx=5, pady=5)

    Tm = StringVar()
    Tm.set("message :")
    Labelp = Label(Mafenetre, textvariable=Tm, fg='black').pack(side=LEFT)
    cmsg = Entry(Mafenetre, textvariable=message, bg='bisque', fg='maroon')
    cmsg.focus_set()
    cmsg.pack(side=LEFT, padx=5, pady=5)

    LabelResultat = Label(Mafenetre, fg='black', bg='yellow')
    boutonchiffrer= Button(Mafenetre, text='Chiffrer', command=lambda: chiffrer(LabelResultat, e, n, message))

    boutonchiffrer.pack(side=LEFT, padx=5, pady=5)

    BoutonQuitter = Button(Mafenetre, text='Quitter', command=Mafenetre.destroy)
    BoutonQuitter.pack(side=LEFT, padx=5, pady=5)









def RSAaleat():
    for ele in Mafenetre.winfo_children():
        ele.destroy()
    menu()

    Mafenetre.title("RSA avec une cle aleatoire")

    message = StringVar()
    Tm = StringVar()
    Tm.set("Votre message :")
    Labelm = Label(Mafenetre, textvariable=Tm, fg='black').pack(side=LEFT)
    cmsg = Entry(Mafenetre, textvariable=message, bg='bisque', fg='maroon')
    cmsg.focus_set()
    cmsg.pack(side=LEFT, padx=5, pady=5)

    LabelResultat = Label(Mafenetre, fg='black', bg='yellow')
    boutonchiffrer = Button(Mafenetre, text='Chiffrer', command=lambda: chiffrerAleatoire(LabelResultat, message))

    boutonchiffrer.pack(side=LEFT, padx=5, pady=5)

    BoutonQuitter = Button(Mafenetre, text='Quitter', command=Mafenetre.destroy)
    BoutonQuitter.pack(side=LEFT, padx=5, pady=5)







def RSAdechiff():
    for ele in Mafenetre.winfo_children():
        ele.destroy()
    menu()

    Mafenetre.title("Déchiffrement RSA")

    code = StringVar()
    d = IntVar()
    n = IntVar()

    Td = StringVar()
    Td.set("d :")
    Labeld = Label(Mafenetre, textvariable=Td, fg='black').pack(side=LEFT)
    cd = Entry(Mafenetre, textvariable=d, bg='bisque', fg='maroon')
    cd.focus_set()
    cd.pack(side=LEFT, padx=5, pady=5)

    Tn = StringVar()
    Tn.set("n :")
    Labeln = Label(Mafenetre, textvariable=Tn, fg='black').pack(side=LEFT)
    cn = Entry(Mafenetre, textvariable=n, bg='bisque', fg='maroon')
    cn.focus_set()
    cn.pack(side=LEFT, padx=5, pady=5)

    Tc = StringVar()
    Tc.set("code :")
    Labelc = Label(Mafenetre, textvariable=Tc, fg='black').pack(side=LEFT)
    cmsg = Entry(Mafenetre, textvariable=code, bg='bisque', fg='maroon')
    cmsg.focus_set()
    cmsg.pack(side=LEFT, padx=5, pady=5)

    LabelResultat = Label(Mafenetre, fg='black', bg='yellow')
    boutonchiffrer = Button(Mafenetre, text='Déchiffrer', command=lambda: dechiffrer(LabelResultat, d, n, code))

    boutonchiffrer.pack(side=LEFT, padx=5, pady=5)

    BoutonQuitter = Button(Mafenetre, text='Quitter', command=Mafenetre.destroy)
    BoutonQuitter.pack(side=LEFT, padx=5, pady=5)







def RSAcrtDechiff():
    for ele in Mafenetre.winfo_children():
        ele.destroy()
    menu()

    Mafenetre.title("Déchiffrement RSA avec CRT")

    code = StringVar()
    d = IntVar()
    p = IntVar()
    q = IntVar()

    Td = StringVar()
    Td.set("d :")
    Labeld = Label(Mafenetre, textvariable=Td, fg='black').pack(side=LEFT)
    cd = Entry(Mafenetre, textvariable=d, bg='bisque', fg='maroon')
    cd.focus_set()
    cd.pack(side=LEFT, padx=5, pady=5)

    Tp = StringVar()
    Tp.set("p :")
    Labelp = Label(Mafenetre, textvariable=Tp, fg='black').pack(side=LEFT)
    cp = Entry(Mafenetre, textvariable=p, bg='bisque', fg='maroon')
    cp.focus_set()
    cp.pack(side=LEFT, padx=5, pady=5)

    Tq = StringVar()
    Tq.set("q :")
    Labelq = Label(Mafenetre, textvariable=Tq, fg='black').pack(side=LEFT)
    cq = Entry(Mafenetre, textvariable=q, bg='bisque', fg='maroon')
    cq.focus_set()
    cq.pack(side=LEFT, padx=5, pady=5)

    Tc = StringVar()
    Tc.set("code :")
    Labelc = Label(Mafenetre, textvariable=Tc, fg='black').pack(side=LEFT)
    cmsg = Entry(Mafenetre, textvariable=code, bg='bisque', fg='maroon')
    cmsg.focus_set()
    cmsg.pack(side=LEFT, padx=5, pady=5)

    LabelResultat = Label(Mafenetre, fg='black', bg='yellow')
    boutonchiffrer = Button(Mafenetre, text='Déchiffrer', command=lambda: dechiffrerCRT(LabelResultat, d, p, q, code))

    boutonchiffrer.pack(side=LEFT, padx=5, pady=5)

    BoutonQuitter = Button(Mafenetre, text='Quitter', command=Mafenetre.destroy)
    BoutonQuitter.pack(side=LEFT, padx=5, pady=5)








def RSAwiener():
    Mafenetre.title("Attaque de Wiener")

    for ele in Mafenetre.winfo_children():
        ele.destroy()
    menu()

    code = StringVar()
    e = IntVar()
    n = IntVar()

    Te = StringVar()
    Te.set("e :")
    Labelp = Label(Mafenetre, textvariable=Te, fg='black').pack(side=LEFT)
    ce = Entry(Mafenetre, textvariable=e, bg='bisque', fg='maroon')
    ce.focus_set()
    ce.pack(side=LEFT, padx=5, pady=5)

    Tn = StringVar()
    Tn.set("n :")
    Labelp = Label(Mafenetre, textvariable=Tn, fg='black').pack(side=LEFT)
    cn = Entry(Mafenetre, textvariable=n, bg='bisque', fg='maroon')
    cn.focus_set()
    cn.pack(side=LEFT, padx=5, pady=5)

    Tc = StringVar()
    Tc.set("code :")
    Labelp = Label(Mafenetre, textvariable=Tc, fg='black').pack(side=LEFT)
    cipher = Entry(Mafenetre, textvariable=code, bg='bisque', fg='maroon')
    cipher.focus_set()
    cipher.pack(side=LEFT, padx=5, pady=5)

    Labeld = Label(Mafenetre, fg='black', bg='yellow')
    LabelResultat = Label(Mafenetre, fg='black', bg='yellow')
    boutonchiffrer = Button(Mafenetre, text='Déchiffrer', command=lambda: wiener(LabelResultat, Labeld, e, n, code))

    boutonchiffrer.pack(side=LEFT, padx=5, pady=5)

    BoutonQuitter = Button(Mafenetre, text='Quitter', command=Mafenetre.destroy)
    BoutonQuitter.pack(side=LEFT, padx=5, pady=5)







def RSAHastad():
    Mafenetre.title("Attaque de Hastad")

    for ele in Mafenetre.winfo_children():
        ele.destroy()
    menu()

    e = IntVar()

    Te = StringVar()
    Te.set("e :")
    Labele = Label(Mafenetre, textvariable=Te, fg='black').place(x=5,y=10)
    ce = Entry(Mafenetre, textvariable=e, bg='bisque', fg='maroon')
    ce.focus_set()
    ce.place(x=25, y=10)
    x = ce.winfo_reqwidth()
    y = ce.winfo_reqheight()
    print(ce.winfo_x())

    bouttonSuite = Button(Mafenetre, text='Continuer!', command=lambda: RSAHastadSuite(Labele, Te, ce, bouttonSuite, e.get(), x, y))
    bouttonSuite.place(x=x+35,y=6)






def RSAHastadSuite(Labele, Te, ce, bouttonSuite, e, x, y):

    if e >= 1:
        Mafenetre.title("Attaque de Hastad")

        for ele in Mafenetre.winfo_children():
            if ele != Labele and ele != ce and ele != bouttonSuite:
                ele.destroy()
        menu()
        Labele = Label(Mafenetre, textvariable=Te, fg='black').place(x=5, y=10)

        listn = []
        listcode = []

        for i in range(0, e):
            y += 35
            n = IntVar()
            code = StringVar()

            Tn = StringVar()
            Tn.set("n" + str(i + 1) + " :")
            Labeln = Label(Mafenetre, textvariable=Tn, fg='black').place(x=5, y=y)
            cn = Entry(Mafenetre, textvariable=n, bg='bisque', fg='maroon')
            cn.focus_set()
            cn.place(x=30, y=y)

            Tc = StringVar()
            Tc.set("code" + str(i + 1) + " :")
            Labelc = Label(Mafenetre, textvariable=Tc, fg='black').place(x=x + 50, y=y)
            cipher = Entry(Mafenetre, textvariable=code, bg='bisque', fg='maroon')
            cipher.focus_set()
            cipher.place(x=x + 100, y=y)
            listn.append(n)
            listcode.append(code)

        y += 35
        LabelResultat = Label(Mafenetre, fg='black', bg='yellow')
        boutonchiffrer = Button(Mafenetre, text='Déchiffrer',
                                command=lambda: hastad(LabelResultat, y, e, listn, listcode))
        boutonchiffrer.place(x=30, y=y)

        BoutonQuitter = Button(Mafenetre, text='Quitter', command=Mafenetre.destroy)
        BoutonQuitter.place(x=boutonchiffrer.winfo_reqwidth() + 50, y=y)

    else:
        messagebox.showerror("Mauvais choix","e doit être strictement positif!")





def Apropos():
    messagebox.showinfo("A propos","Application de cryptage RSA et simulation d'attaque Wiener et d'attaque de Hastad.")




Mafenetre = Tk()
Mafenetre.title("RSA")
Mafenetre.geometry("700x120+10+10")

def menu():
    menubar = Menu(Mafenetre)

    menuGener = Menu(menubar, tearoff=0)
    menuGener.add_command(label="Générer les clés", command=RSAgenerate)
    menuGener.add_separator()
    menuGener.add_command(label="Quitter", command=Mafenetre.destroy)
    menubar.add_cascade(label='Générer...', menu=menuGener)

    menuChiff = Menu(menubar, tearoff=0)
    menuChiff.add_command(label="RSA Simple", command=RSAsahl)
    menuChiff.add_command(label="RSA Aleat", command=RSAaleat)
    menubar.add_cascade(label="Chiffrement", menu=menuChiff)

    menuDechiff = Menu(menubar, tearoff=0)
    menuDechiff.add_command(label="Déchiffrement RSA", command=RSAdechiff)
    menuDechiff.add_command(label="Déchiffrement avec CRT", command=RSAcrtDechiff)
    menubar.add_cascade(label="Déchiffrement", menu=menuDechiff)

    menuAttaque = Menu(menubar, tearoff=0)
    menuAttaque.add_command(label="Wiener", command=RSAwiener)
    menuAttaque.add_command(label="Hastad", command=RSAHastad)
    menubar.add_cascade(label="Attaque sur RSA", menu=menuAttaque)

    menuaide = Menu(menubar, tearoff=0)
    menuaide.add_command(label="A propos", command=Apropos)
    menubar.add_cascade(label="Aide", menu=menuaide)

    Mafenetre.config(menu=menubar)


menu()

gifdict={}

Mafenetre.mainloop()