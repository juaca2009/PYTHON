import tkinter

#ventanas
ventana = tkinter.Tk()
ventana.geometry("589x580")
ventana.title("road fighter")
ventana.resizable(0,0)
canvas = tkinter.Canvas(ventana,width =1000,height=1000,bg="black")

#nombre
nombre_jugador = canvas.create_text(490,50,text=".",font=("avantgarde",30),fill="white")

# puntos
p_puntos = canvas.create_text(490,400,text=".",font=("avantgarde",30),fill="white")
puntos = canvas.create_text(490,450,text=".",font=("avantgarde",30),fill="white")
p = 0

#tipo de nivel o mapa
tipo = 1

#carga mapa (nivel 1)
imapa = tkinter.PhotoImage(file="mapa.gif")
imapa_2 = tkinter.PhotoImage(file="mapa_2.gif")
imapa_3 = tkinter.PhotoImage(file="mapa_3.gif")
imapa_4 = tkinter.PhotoImage(file="mapa_4.gif")
imapa_5 = tkinter.PhotoImage(file="mapa_5.gif")
imapa_6 = tkinter.PhotoImage(file="mapa_6.gif")
imapa_7 = tkinter.PhotoImage(file="mapa_7.gif")
imapa_8 = tkinter.PhotoImage(file="mapa_8.gif")
imapa_9 = tkinter.PhotoImage(file="mapa_9.gif")
imapa_10 = tkinter.PhotoImage(file="mapa_10.gif")
imapa_11 = tkinter.PhotoImage(file="mapa_11.gif")


#carga mapa (nivel 2)
i2mapa = tkinter.PhotoImage(file="2mapa.gif")
i2mapa_2 = tkinter.PhotoImage(file="2mapa_2.gif")
i2mapa_3 = tkinter.PhotoImage(file="2mapa_3.gif")
i2mapa_4 = tkinter.PhotoImage(file="2mapa_4.gif")
i2mapa_5 = tkinter.PhotoImage(file="2mapa_5.gif")
i2mapa_6 = tkinter.PhotoImage(file="2mapa_6.gif")
i2mapa_7 = tkinter.PhotoImage(file="2mapa_7.gif")
i2mapa_8 = tkinter.PhotoImage(file="2mapa_8.gif")
i2mapa_9 = tkinter.PhotoImage(file="2mapa_9.gif")
i2mapa_10 = tkinter.PhotoImage(file="2mapa_10.gif")
i2mapa_11 = tkinter.PhotoImage(file="2mapa_11.gif")

#carga mapa (nivel 3)
i3mapa = tkinter.PhotoImage(file="3mapa.gif")
i3mapa_2 = tkinter.PhotoImage(file="3mapa_2.gif")
i3mapa_3 = tkinter.PhotoImage(file="3mapa_3.gif")
i3mapa_4 = tkinter.PhotoImage(file="3mapa_4.gif")
i3mapa_5 = tkinter.PhotoImage(file="3mapa_5.gif")
i3mapa_6 = tkinter.PhotoImage(file="3mapa_6.gif")
i3mapa_7 = tkinter.PhotoImage(file="3mapa_7.gif")
i3mapa_8 = tkinter.PhotoImage(file="3mapa_8.gif")
i3mapa_9 = tkinter.PhotoImage(file="3mapa_9.gif")
i3mapa_10 = tkinter.PhotoImage(file="3mapa_10.gif")
i3mapa_11 = tkinter.PhotoImage(file="3mapa_11.gif")

#carga mapa (nivel 4)
i4mapa = tkinter.PhotoImage(file="4mapa.gif")
i4mapa_2 = tkinter.PhotoImage(file="4mapa_2.gif")
i4mapa_3 = tkinter.PhotoImage(file="4mapa_3.gif")
i4mapa_4 = tkinter.PhotoImage(file="4mapa_4.gif")
i4mapa_5 = tkinter.PhotoImage(file="4mapa_5.gif")
i4mapa_6 = tkinter.PhotoImage(file="4mapa_6.gif")
i4mapa_7 = tkinter.PhotoImage(file="4mapa_7.gif")
i4mapa_8 = tkinter.PhotoImage(file="4mapa_8.gif")
i4mapa_9 = tkinter.PhotoImage(file="4mapa_9.gif")
i4mapa_10 = tkinter.PhotoImage(file="4mapa_10.gif")
i4mapa_11 = tkinter.PhotoImage(file="4mapa_11.gif")

#carga mapa (nivel 5)
i5mapa = tkinter.PhotoImage(file="5mapa.gif")
i5mapa_2 = tkinter.PhotoImage(file="5mapa_2.gif")
i5mapa_3 = tkinter.PhotoImage(file="5mapa_3.gif")
i5mapa_4 = tkinter.PhotoImage(file="5mapa_4.gif")
i5mapa_5 = tkinter.PhotoImage(file="5mapa_5.gif")
i5mapa_6 = tkinter.PhotoImage(file="5mapa_6.gif")
i5mapa_7 = tkinter.PhotoImage(file="5mapa_7.gif")
i5mapa_8 = tkinter.PhotoImage(file="5mapa_8.gif")
i5mapa_9 = tkinter.PhotoImage(file="5mapa_9.gif")
i5mapa_10 = tkinter.PhotoImage(file="5mapa_10.gif")
i5mapa_11 = tkinter.PhotoImage(file="5mapa_11.gif")


# carga carro
icarro = tkinter.PhotoImage(file="auto.gif")



#carga enemigos(AMARILLOS)
ienemigo = tkinter.PhotoImage(file="enemigo_1.gif")
ienemigo_2 = tkinter.PhotoImage(file="enemigo_2.gif")
ienemigo_3 = tkinter.PhotoImage(file="enemigo_3.gif")
ienemigo_4 = tkinter.PhotoImage(file="enemigo_4.gif")
ienemigo_5 = tkinter.PhotoImage(file="enemigo_5.gif")
ienemigo_6 = tkinter.PhotoImage(file="enemigo_6.gif")
ienemigo_7 = tkinter.PhotoImage(file="enemigo_7.gif")
ienemigo_8 = tkinter.PhotoImage(file="enemigo_8.gif")
ienemigo_9 = tkinter.PhotoImage(file="enemigo_9.gif")
ienemigo_10 = tkinter.PhotoImage(file="enemigo_10.gif")
ienemigo_11 = tkinter.PhotoImage(file="enemigo_11.gif")
ienemigo_12 = tkinter.PhotoImage(file="enemigo_12.gif")
ienemigo_13 = tkinter.PhotoImage(file="enemigo_13.gif")
ienemigo_14 = tkinter.PhotoImage(file="enemigo_14.gif")
ienemigo_15 = tkinter.PhotoImage(file="enemigo_15.gif")


#carga enemigos(AZULES)
iazul = tkinter.PhotoImage(file="enemigo2.gif")
iazul_2 = tkinter.PhotoImage(file="enemigo2_2.gif")
iazul_3 = tkinter.PhotoImage(file="enemigo2_3.gif")


#carga runner
irunner =  tkinter.PhotoImage(file="runner.gif")

#carga de vidas
ivida = tkinter.PhotoImage(file="vida.gif")
ivida_2 = tkinter.PhotoImage(file="vida_2.gif")
ivida_3 = tkinter.PhotoImage(file="vida_3.gif")
p_ivida = tkinter.PhotoImage(file="palabra_vida.gif")



# cargar todo

def mapas():
    global mapa, mapa_2,  mapa_3,  mapa_4,  mapa_5,  mapa_6,  mapa_7,  mapa_8,  mapa_9,  mapa_10,  mapa_11, canvas, tipo, bmapa, bmapa_2, bmapa_3, bmapa_4, bmapa_5, bmapa_6, bmapa_7, bmapa_8, bmapa_9, bmapa_10, bmapa_11, cmapa, cmapa_2, cmapa_3, cmapa_4, cmapa_5, cmapa_6, cmapa_7, cmapa_8, cmapa_9, cmapa_10, cmapa_11, dmapa, dmapa_2, dmapa_3, dmapa_4, dmapa_5, dmapa_6, dmapa_7, dmapa_8, dmapa_9, dmapa_10, dmapa_11, emapa, emapa_2, emapa_3, emapa_4, emapa_5, emapa_6, emapa_7, emapa_8, emapa_9, emapa_10, emapa_11
    if tipo == 1:
        mapa= canvas.create_image(195,290,image=imapa)
        mapa_2= canvas.create_image(195,-290,image=imapa_2)
        mapa_3= canvas.create_image(195,-870, image= imapa_3)
        mapa_4= canvas.create_image(195,-1450,image=imapa_4)
        mapa_5= canvas.create_image(195,-2030,image=imapa_5)
        mapa_6= canvas.create_image(195,-2610,image=imapa_6)
        mapa_7= canvas.create_image(195,-3190,image=imapa_7)
        mapa_8= canvas.create_image(195,-3770,image=imapa_8)
        mapa_9= canvas.create_image(195,-4350,image=imapa_9)
        mapa_10= canvas.create_image(195,-4930,image=imapa_10)
        mapa_11= canvas.create_image(195,-5510,image=imapa_11)
        mover_mapa_1()
        mover_mapa_2()
        mover_mapa_3()
        mover_mapa_4()
        mover_mapa_5()
        mover_mapa_6()
        mover_mapa_7()
        mover_mapa_8()
        mover_mapa_9()
        mover_mapa_10()
        mover_mapa_11()
    if tipo == 2:
         bmapa= canvas.create_image(195,290,image=i2mapa)
         bmapa_2= canvas.create_image(195,-290,image=i2mapa_2)
         bmapa_3= canvas.create_image(195,-870, image= i2mapa_3)
         bmapa_4= canvas.create_image(195,-1450,image=i2mapa_4)
         bmapa_5= canvas.create_image(195,-2030,image=i2mapa_5)
         bmapa_6= canvas.create_image(195,-2610,image=i2mapa_6)
         bmapa_7= canvas.create_image(195,-3190,image=i2mapa_7)
         bmapa_8= canvas.create_image(195,-3770,image=i2mapa_8)
         bmapa_9= canvas.create_image(195,-4350,image=i2mapa_9)
         bmapa_10= canvas.create_image(195,-4930,image=i2mapa_10)
         bmapa_11= canvas.create_image(195,-5510,image=i2mapa_11)
         mover_bmapa_1()
         mover_bmapa_2()
         mover_bmapa_3()
         mover_bmapa_4()
         mover_bmapa_5()
         mover_bmapa_6()
         mover_bmapa_7()
         mover_bmapa_8()
         mover_bmapa_9()
         mover_bmapa_10()
         mover_bmapa_11()

    if tipo == 3:
        cmapa = canvas.create_image(195,290,image=i3mapa)
        cmapa_2 = canvas.create_image(195,-290,image=i3mapa_2)
        cmapa_3 = canvas.create_image(195,-870, image= i3mapa_3)
        cmapa_4 = canvas.create_image(195,-1450,image=i3mapa_4)
        cmapa_5 = canvas.create_image(195,-2030,image=i3mapa_5)
        cmapa_6 = canvas.create_image(195,-2610,image=i3mapa_6)
        cmapa_7 = canvas.create_image(195,-3190,image=i3mapa_7)
        cmapa_8 = canvas.create_image(195,-3770,image=i3mapa_8)
        cmapa_9 = canvas.create_image(195,-4350,image=i3mapa_9)
        cmapa_10 = canvas.create_image(195,-4930,image=i3mapa_10)
        cmapa_11 = canvas.create_image(195,-5510,image=i3mapa_11)
        mover_cmapa_1()
        mover_cmapa_2()
        mover_cmapa_3()
        mover_cmapa_4()
        mover_cmapa_5()
        mover_cmapa_6()
        mover_cmapa_7()
        mover_cmapa_8()
        mover_cmapa_9()
        mover_cmapa_10()
        mover_cmapa_11()

    if tipo == 4:
        dmapa = canvas.create_image(195,290,image=i4mapa)
        dmapa_2 = canvas.create_image(195,-290,image=i4mapa_2)
        dmapa_3 = canvas.create_image(195,-870, image= i4mapa_3)
        dmapa_4 = canvas.create_image(195,-1450,image=i4mapa_4)
        dmapa_5 = canvas.create_image(195,-2030,image=i4mapa_5)
        dmapa_6 = canvas.create_image(195,-2610,image=i4mapa_6)
        dmapa_7 = canvas.create_image(195,-3190,image=i4mapa_7)
        dmapa_8 = canvas.create_image(195,-3770,image=i4mapa_8)
        dmapa_9 = canvas.create_image(195,-4350,image=i4mapa_9)
        dmapa_10 = canvas.create_image(195,-4930,image=i4mapa_10)
        dmapa_11 = canvas.create_image(195,-5510,image=i4mapa_11)
        mover_dmapa_1()
        mover_dmapa_2()
        mover_dmapa_3()
        mover_dmapa_4()
        mover_dmapa_5()
        mover_dmapa_6()
        mover_dmapa_7()
        mover_dmapa_8()
        mover_dmapa_9()
        mover_dmapa_10()
        mover_dmapa_11()

    if tipo == 5:
         emapa = canvas.create_image(195,290,image=i5mapa)
         emapa_2 = canvas.create_image(195,-290,image=i5mapa_2)
         emapa_3 = canvas.create_image(195,-870, image= i5mapa_3)
         emapa_4 = canvas.create_image(195,-1450,image=i5mapa_4)
         emapa_5 = canvas.create_image(195,-2030,image=i5mapa_5)
         emapa_6 = canvas.create_image(195,-2610,image=i5mapa_6)
         emapa_7 = canvas.create_image(195,-3190,image=i5mapa_7)
         emapa_8 = canvas.create_image(195,-3770,image=i5mapa_8)
         emapa_9 = canvas.create_image(195,-4350,image=i5mapa_9)
         emapa_10 = canvas.create_image(195,-4930,image=i5mapa_10)
         emapa_11 = canvas.create_image(195,-5510,image=i5mapa_11)
         mover_emapa_1()
         mover_emapa_2()
         mover_emapa_3()
         mover_emapa_4()
         mover_emapa_5()
         mover_emapa_6()
         mover_emapa_7()
         mover_emapa_8()
         mover_emapa_9()
         mover_emapa_10()
         mover_emapa_11()
         
          
          
        



def carro():
    global carro, canvas
    carro = canvas.create_image(250,450,image=icarro)

def amarillos():
    global enemigo, enemigo_2, enemigo_3, enemigo_4, enemigo_5, enemigo_6, enemigo_7, enemigo_8, enemigo_9, enemigo_10, enemigo_11, enemigo_12, enemigo_13, enemigo_14, enemigo_15, canvas
    enemigo = canvas.create_image(235,-70,image=ienemigo)
    enemigo_2 =  canvas.create_image(150,-200,image=ienemigo_2)
    enemigo_3 =  canvas.create_image(235,-330,image=ienemigo_3)
    enemigo_4 =  canvas.create_image(235,-900,image=ienemigo_4)
    enemigo_5 =  canvas.create_image(150,-990,image=ienemigo_5)
    enemigo_6 =  canvas.create_image(235,-1150,image=ienemigo_6)
    enemigo_7 =  canvas.create_image(235,-1650,image=ienemigo_7)
    enemigo_8 =  canvas.create_image(150,-1830,image=ienemigo_8)
    enemigo_9 =  canvas.create_image(235,-1990,image=ienemigo_9)
    enemigo_10 =  canvas.create_image(235,-3000,image=ienemigo_10)
    enemigo_11 =  canvas.create_image(150,-3120,image=ienemigo_11)
    enemigo_12 =  canvas.create_image(235,-3290,image=ienemigo_12)
    enemigo_13 =  canvas.create_image(235,-4300,image=ienemigo_13)
    enemigo_14 =  canvas.create_image(150,-4500,image=ienemigo_14)
    enemigo_15 =  canvas.create_image(235,-4700,image=ienemigo_15)
    mover_enemigo()
    mover_enemigo_2()
    mover_enemigo_3()
    mover_enemigo_4()
    mover_enemigo_5()
    mover_enemigo_6()
    mover_enemigo_7()
    mover_enemigo_8()
    mover_enemigo_9()
    mover_enemigo_10()
    mover_enemigo_11()
    mover_enemigo_12()
    mover_enemigo_13()
    mover_enemigo_14()
    mover_enemigo_15()

def azules():
    global azul, azul_2, azul_3, canvas
    azul =  canvas.create_image(255,-620,image=iazul)
    azul_2 =  canvas.create_image(150,-1500,image=iazul)
    azul_3 =  canvas.create_image(255,-3900,image=iazul)
    mover_azul()
    mover_azul_2()
    mover_azul_3()

def runners():
    global runner, canvas
    runner =  canvas.create_image(255,-3300,image=irunner)
    mover_runner()


def hud():
    global vida, vida_2, vida_3, p_vida, canvas
    vida = canvas.create_image(430,250,image=ivida)
    vida_2 = canvas.create_image(480,250,image=ivida_2)
    vida_3 = canvas.create_image(530,250,image=ivida_3)
    p_vida = canvas.create_image(490,200,image=p_ivida)    

#contador de vidas
cont_vidas = 3
carrom = False
fin = False


#movimiento mapa (nivel 1)
def mover_mapa_1():
    """
    funcion que permite mover el mapa
    """
    global canvas, mapa

    if canvas.coords(mapa)[1] < 870:
        canvas.move(mapa,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_mapa_1)
    elif canvas.coords(mapa)[1] >= 870:
        canvas.delete(mapa)
        

def mover_mapa_2():
    """
    funcion que permite mover el mapa
    """
    global canvas, mapa_2

    if canvas.coords(mapa_2)[1] < 870:
        canvas.move(mapa_2,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_mapa_2)
    elif canvas.coords(mapa_2)[1] >= 870:
        canvas.delete(mapa_2)



def mover_mapa_3():
    """
    funcion que permite mover el mapa
    """
    global canvas, mapa_3

    if canvas.coords(mapa_3)[1] < 870:
        canvas.move(mapa_3,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_mapa_3)
    elif canvas.coords(mapa_3)[1] >= 870:
        canvas.delete(mapa_3)


def mover_mapa_4():
    """
    funcion que permite mover el mapa
    """
    global canvas, mapa_4

    if canvas.coords(mapa_4)[1] < 870:
        canvas.move(mapa_4,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_mapa_4)
    elif canvas.coords(mapa_4)[1] >= 870:
        canvas.delete(mapa_4)


def mover_mapa_5():
    """
    funcion que permite mover el mapa
    """
    global canvas, mapa_5

    if canvas.coords(mapa_5)[1] < 870:
        canvas.move(mapa_5,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_mapa_5)
    elif canvas.coords(mapa_5)[1] >= 870:
        canvas.delete(mapa_5)


def mover_mapa_6():
    """
    funcion que permite mover el mapa
    """
    global canvas, mapa_6

    if canvas.coords(mapa_6)[1] < 870:
        canvas.move(mapa_6,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_mapa_6)
    elif canvas.coords(mapa_6)[1] >= 870:
        canvas.delete(mapa_6)


def mover_mapa_7():
    """
    funcion que permite mover el mapa
    """
    global canvas, mapa_7

    if canvas.coords(mapa_7)[1] < 870:
        canvas.move(mapa_7,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_mapa_7)
    elif canvas.coords(mapa_7)[1] >= 870:
        canvas.delete(mapa_7)


def mover_mapa_8():
    """
    funcion que permite mover el mapa
    """
    global canvas, mapa_8

    if canvas.coords(mapa_8)[1] < 870:
        canvas.move(mapa_8,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_mapa_8)
    elif canvas.coords(mapa_8)[1] >= 870:
        canvas.delete(mapa_8)


def mover_mapa_9():
    """
    funcion que permite mover el mapa
    """
    global canvas, mapa_9

    if canvas.coords(mapa_9)[1] < 870:
        canvas.move(mapa_9,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_mapa_9)
    elif canvas.coords(mapa_9)[1] >= 870:
        canvas.delete(mapa_9)


def mover_mapa_10():
    """
    funcion que permite mover el mapa
    funcion que detiene el mapa 
    """
    global canvas, mapa_10, mapa_11

    if canvas.coords(mapa_10)[1] == 450:
        canvas.move(mapa_10,0,0)
        ganar()
        

    elif canvas.coords(mapa_10)[1] < 870:
        canvas.move(mapa_10,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_mapa_10)
    elif canvas.coords(mapa_10)[1] >= 870:
        canvas.delete(mapa_10)
        
    

def mover_mapa_11():
    """
    funcion que permite mover el mapa
    funcion que detiene el mapa
    """
    global canvas, mapa_11, mapa_10
    
    if canvas.coords(mapa_10)[1] == 450:
        canvas.move(mapa_11,0,10)
        canvas.move(mapa_11,0,0)
        ganar()
        
    

    elif canvas.coords(mapa_11)[1] < 870:
        canvas.move(mapa_11,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_mapa_11)
    elif canvas.coords(mapa_11)[1] >= 870:
        canvas.delete(mapa_11)
        

#movimiento mapa (nivel 2)

def mover_bmapa_1():
    """
    funcion que permite mover el mapa
    """
    global canvas, bmapa

    if canvas.coords(bmapa)[1] < 870:
        canvas.move(bmapa,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_bmapa_1)
    elif canvas.coords(bmapa)[1] >= 870:
        canvas.delete(bmapa)

def mover_bmapa_2():
    """
    funcion que permite mover el mapa
    """
    global canvas, bmapa_2

    if canvas.coords(bmapa_2)[1] < 870:
        canvas.move(bmapa_2,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_bmapa_2)
    elif canvas.coords(bmapa_2)[1] >= 870:
        canvas.delete(bmapa_2)

def mover_bmapa_3():
    """
    funcion que permite mover el mapa
    """
    global canvas, bmapa_3

    if canvas.coords(bmapa_3)[1] < 870:
        canvas.move(bmapa_3,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_bmapa_3)
    elif canvas.coords(bmapa_3)[1] >= 870:
        canvas.delete(bmapa_3)

def mover_bmapa_4():
    """
    funcion que permite mover el mapa
    """
    global canvas, bmapa_4

    if canvas.coords(bmapa_4)[1] < 870:
        canvas.move(bmapa_4,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_bmapa_4)
    elif canvas.coords(bmapa_4)[1] >= 870:
        canvas.delete(bmapa_4)

def mover_bmapa_5():
    """
    funcion que permite mover el mapa
    """
    global canvas, bmapa_5

    if canvas.coords(bmapa_5)[1] < 870:
        canvas.move(bmapa_5,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_bmapa_5)
    elif canvas.coords(bmapa_5)[1] >= 870:
        canvas.delete(bmapa_5)

def mover_bmapa_6():
    """
    funcion que permite mover el mapa
    """
    global canvas, bmapa_6

    if canvas.coords(bmapa_6)[1] < 870:
        canvas.move(bmapa_6,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_bmapa_6)
    elif canvas.coords(bmapa_6)[1] >= 870:
        canvas.delete(bmapa_6)

def mover_bmapa_7():
    """
    funcion que permite mover el mapa
    """
    global canvas, bmapa_7

    if canvas.coords(bmapa_7)[1] < 870:
        canvas.move(bmapa_7,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_bmapa_7)
    elif canvas.coords(bmapa_7)[1] >= 870:
        canvas.delete(bmapa_7)

def mover_bmapa_8():
    """
    funcion que permite mover el mapa
    """
    global canvas, bmapa_8

    if canvas.coords(bmapa_8)[1] < 870:
        canvas.move(bmapa_8,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_bmapa_8)
    elif canvas.coords(bmapa_8)[1] >= 870:
        canvas.delete(bmapa_8)

def mover_bmapa_9():
    """
    funcion que permite mover el mapa
    """
    global canvas, bmapa_2

    if canvas.coords(bmapa_9)[1] < 870:
        canvas.move(bmapa_9,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_bmapa_9)
    elif canvas.coords(bmapa_9)[1] >= 870:
        canvas.delete(bmapa_9)


def mover_bmapa_10():
    """
    funcion que permite mover el mapa
    funcion que detiene el mapa 
    """
    global canvas, bmapa_10, bmapa_11

    if canvas.coords(bmapa_10)[1] == 450:
        canvas.move(bmapa_10,0,0)
        ganar()
        

    elif canvas.coords(bmapa_10)[1] < 870:
        canvas.move(bmapa_10,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_bmapa_10)
    elif canvas.coords(bmapa_10)[1] >= 870:
        canvas.delete(bmapa_10)




def mover_bmapa_11():
    """
    funcion que permite mover el mapa
    funcion que detiene el mapa
    """
    global canvas, bmapa_11, bmapa_10
    
    if canvas.coords(bmapa_10)[1] == 450:
        canvas.move(bmapa_11,0,10)
        canvas.move(bmapa_11,0,0)
        ganar()
        
    

    elif canvas.coords(bmapa_11)[1] < 870:
        canvas.move(bmapa_11,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_bmapa_11)
    elif canvas.coords(bmapa_11)[1] >= 870:
        canvas.delete(bmapa_11)





#movimiento mapa (nivel 3)

def mover_cmapa_1():
    """
    funcion que permite mover el mapa
    """
    global canvas, cmapa

    if canvas.coords(cmapa)[1] < 870:
        canvas.move(cmapa,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_cmapa_1)
    elif canvas.coords(cmapa)[1] >= 870:
        canvas.delete(cmapa)

def mover_cmapa_2():
    """
    funcion que permite mover el mapa
    """
    global canvas, cmapa_2

    if canvas.coords(cmapa_2)[1] < 870:
        canvas.move(cmapa_2,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_cmapa_2)
    elif canvas.coords(cmapa_2)[1] >= 870:
        canvas.delete(cmapa_2)

def mover_cmapa_3():
    """
    funcion que permite mover el mapa
    """
    global canvas, cmapa_3

    if canvas.coords(cmapa_3)[1] < 870:
        canvas.move(cmapa_3,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_cmapa_3)
    elif canvas.coords(cmapa_3)[1] >= 870:
        canvas.delete(cmapa_3)

def mover_cmapa_4():
    """
    funcion que permite mover el mapa
    """
    global canvas, cmapa_4

    if canvas.coords(cmapa_4)[1] < 870:
        canvas.move(cmapa_4,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_cmapa_4)
    elif canvas.coords(cmapa_4)[1] >= 870:
        canvas.delete(cmapa_4)

def mover_cmapa_5():
    """
    funcion que permite mover el mapa
    """
    global canvas, cmapa_5

    if canvas.coords(cmapa_5)[1] < 870:
        canvas.move(cmapa_5,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_cmapa_5)
    elif canvas.coords(cmapa_5)[1] >= 870:
        canvas.delete(cmapa_5)

def mover_cmapa_6():
    """
    funcion que permite mover el mapa
    """
    global canvas, cmapa_6

    if canvas.coords(cmapa_6)[1] < 870:
        canvas.move(cmapa_6,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_cmapa_6)
    elif canvas.coords(cmapa_6)[1] >= 870:
        canvas.delete(cmapa_6)


def mover_cmapa_7():
    """
    funcion que permite mover el mapa
    """
    global canvas, cmapa_7

    if canvas.coords(cmapa_7)[1] < 870:
        canvas.move(cmapa_7,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_cmapa_7)
    elif canvas.coords(cmapa_7)[1] >= 870:
        canvas.delete(cmapa_7)

def mover_cmapa_8():
    """
    funcion que permite mover el mapa
    """
    global canvas, cmapa_8

    if canvas.coords(cmapa_8)[1] < 870:
        canvas.move(cmapa_8,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_cmapa_8)
    elif canvas.coords(cmapa_8)[1] >= 870:
        canvas.delete(cmapa_8)

def mover_cmapa_9():
    """
    funcion que permite mover el mapa
    """
    global canvas, cmapa_9

    if canvas.coords(cmapa_9)[1] < 870:
        canvas.move(cmapa_9,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_cmapa_9)
    elif canvas.coords(cmapa_9)[1] >= 870:
        canvas.delete(cmapa_9)

def mover_cmapa_10():
    """
    funcion que permite mover el mapa
    funcion que detiene el mapa 
    """
    global canvas, cmapa_10, cmapa_11

    if canvas.coords(cmapa_10)[1] == 450:
        canvas.move(cmapa_10,0,0)
        ganar()
        

    elif canvas.coords(cmapa_10)[1] < 870:
        canvas.move(cmapa_10,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_cmapa_10)
    elif canvas.coords(cmapa_10)[1] >= 870:
        canvas.delete(cmapa_10)

def mover_cmapa_11():
    """
    funcion que permite mover el mapa
    funcion que detiene el mapa
    """
    global canvas, cmapa_11, cmapa_10
    
    if canvas.coords(cmapa_10)[1] == 450:
        canvas.move(cmapa_11,0,10)
        canvas.move(cmapa_11,0,0)
        ganar()
        
    

    elif canvas.coords(cmapa_11)[1] < 870:
        canvas.move(cmapa_11,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_cmapa_11)
    elif canvas.coords(cmapa_11)[1] >= 870:
        canvas.delete(cmapa_11)


#movimiento mapa (nivel 4)

def mover_dmapa_1():
    """
    funcion que permite mover el mapa
    """
    global canvas, dmapa

    if canvas.coords(dmapa)[1] < 870:
        canvas.move(dmapa,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_dmapa_1)
    elif canvas.coords(dmapa)[1] >= 870:
        canvas.delete(dmapa)

def mover_dmapa_2():
    """
    funcion que permite mover el mapa
    """
    global canvas, dmapa_2

    if canvas.coords(dmapa_2)[1] < 870:
        canvas.move(dmapa_2,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_dmapa_2)
    elif canvas.coords(dmapa_2)[1] >= 870:
        canvas.delete(dmapa_2)


def mover_dmapa_3():
    """
    funcion que permite mover el mapa
    """
    global canvas, dmapa_3

    if canvas.coords(dmapa_3)[1] < 870:
        canvas.move(dmapa_3,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_dmapa_3)
    elif canvas.coords(dmapa_3)[1] >= 870:
        canvas.delete(dmapa_3)

def mover_dmapa_4():
    """
    funcion que permite mover el mapa
    """
    global canvas, dmapa_4

    if canvas.coords(dmapa_4)[1] < 870:
        canvas.move(dmapa_4,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_dmapa_4)
    elif canvas.coords(dmapa_4)[1] >= 870:
        canvas.delete(dmapa_4)


def mover_dmapa_5():
    """
    funcion que permite mover el mapa
    """
    global canvas, dmapa_5

    if canvas.coords(dmapa_5)[1] < 870:
        canvas.move(dmapa_5,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_dmapa_5)
    elif canvas.coords(dmapa_5)[1] >= 870:
        canvas.delete(dmapa_5)


def mover_dmapa_6():
    """
    funcion que permite mover el mapa
    """
    global canvas, dmapa_6

    if canvas.coords(dmapa_6)[1] < 870:
        canvas.move(dmapa_6,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_dmapa_6)
    elif canvas.coords(dmapa_6)[1] >= 870:
        canvas.delete(dmapa_6)


def mover_dmapa_7():
    """
    funcion que permite mover el mapa
    """
    global canvas, dmapa_7

    if canvas.coords(dmapa_7)[1] < 870:
        canvas.move(dmapa_7,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_dmapa_7)
    elif canvas.coords(dmapa_7)[1] >= 870:
        canvas.delete(dmapa_7)

def mover_dmapa_8():
    """
    funcion que permite mover el mapa
    """
    global canvas, dmapa_8

    if canvas.coords(dmapa_8)[1] < 870:
        canvas.move(dmapa_8,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_dmapa_8)
    elif canvas.coords(dmapa_8)[1] >= 870:
        canvas.delete(dmapa_8)


def mover_dmapa_9():
    """
    funcion que permite mover el mapa
    """
    global canvas, dmapa_9

    if canvas.coords(dmapa_9)[1] < 870:
        canvas.move(dmapa_9,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_dmapa_9)
    elif canvas.coords(dmapa_9)[1] >= 870:
        canvas.delete(dmapa_9)

def mover_dmapa_10():
    """
    funcion que permite mover el mapa
    funcion que detiene el mapa 
    """
    global canvas, dmapa_10, dmapa_11

    if canvas.coords(dmapa_10)[1] == 450:
        canvas.move(dmapa_10,0,0)
        ganar()
        

    elif canvas.coords(dmapa_10)[1] < 870:
        canvas.move(dmapa_10,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_dmapa_10)
    elif canvas.coords(dmapa_10)[1] >= 870:
        canvas.delete(dmapa_10)

def mover_dmapa_11():
    """
    funcion que permite mover el mapa
    funcion que detiene el mapa
    """
    global canvas, dmapa_11, dmapa_10
    
    if canvas.coords(dmapa_10)[1] == 450:
        canvas.move(dmapa_11,0,10)
        canvas.move(dmapa_11,0,0)
        ganar()
        
    

    elif canvas.coords(dmapa_11)[1] < 870:
        canvas.move(dmapa_11,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_dmapa_11)
    elif canvas.coords(dmapa_11)[1] >= 870:
        canvas.delete(dmapa_11)


#movimiento mapa (nivel 5)

def mover_emapa_1():
    """
    funcion que permite mover el mapa
    """
    global canvas, emapa

    if canvas.coords(emapa)[1] < 870:
        canvas.move(emapa,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_emapa_1)
    elif canvas.coords(emapa)[1] >= 870:
        canvas.delete(emapa)

def mover_emapa_2():
    """
    funcion que permite mover el mapa
    """
    global canvas, emapa_2

    if canvas.coords(emapa_2)[1] < 870:
        canvas.move(emapa_2,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_emapa_2)
    elif canvas.coords(emapa_2)[1] >= 870:
        canvas.delete(emapa_2)

def mover_emapa_3():
    """
    funcion que permite mover el mapa
    """
    global canvas, emapa_3

    if canvas.coords(emapa_3)[1] < 870:
        canvas.move(emapa_3,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_emapa_3)
    elif canvas.coords(emapa_3)[1] >= 870:
        canvas.delete(emapa_3)


def mover_emapa_4():
    """
    funcion que permite mover el mapa
    """
    global canvas, emapa_4

    if canvas.coords(emapa_4)[1] < 870:
        canvas.move(emapa_4,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_emapa_4)
    elif canvas.coords(emapa_4)[1] >= 870:
        canvas.delete(emapa_4)


def mover_emapa_5():
    """
    funcion que permite mover el mapa
    """
    global canvas, emapa_5

    if canvas.coords(emapa_5)[1] < 870:
        canvas.move(emapa_5,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_emapa_5)
    elif canvas.coords(emapa_5)[1] >= 870:
        canvas.delete(emapa_5)

def mover_emapa_6():
    """
    funcion que permite mover el mapa
    """
    global canvas, emapa_6

    if canvas.coords(emapa_6)[1] < 870:
        canvas.move(emapa_6,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_emapa_6)
    elif canvas.coords(emapa_6)[1] >= 870:
        canvas.delete(emapa_6)


def mover_emapa_7():
    """
    funcion que permite mover el mapa
    """
    global canvas, emapa_7

    if canvas.coords(emapa_7)[1] < 870:
        canvas.move(emapa_7,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_emapa_7)
    elif canvas.coords(emapa_7)[1] >= 870:
        canvas.delete(emapa_7)


def mover_emapa_8():
    """
    funcion que permite mover el mapa
    """
    global canvas, emapa_8

    if canvas.coords(emapa_8)[1] < 870:
        canvas.move(emapa_8,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_emapa_8)
    elif canvas.coords(emapa_8)[1] >= 870:
        canvas.delete(emapa_8)



def mover_emapa_9():
    """
    funcion que permite mover el mapa
    """
    global canvas, emapa_9

    if canvas.coords(emapa_9)[1] < 870:
        canvas.move(emapa_9,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_emapa_9)
    elif canvas.coords(emapa_9)[1] >= 870:
        canvas.delete(emapa_9)



def mover_emapa_10():
    """
    funcion que permite mover el mapa
    funcion que detiene el mapa 
    """
    global canvas, emapa_10, emapa_11

    if canvas.coords(emapa_10)[1] == 450:
        canvas.move(emapa_10,0,0)
        ganar()
        

    elif canvas.coords(emapa_10)[1] < 870:
        canvas.move(emapa_10,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_emapa_10)
    elif canvas.coords(emapa_10)[1] >= 870:
        canvas.delete(emapa_10)




def mover_emapa_11():
    """
    funcion que permite mover el mapa
    funcion que detiene el mapa
    """
    global canvas, emapa_11, emapa_10
    
    if canvas.coords(emapa_10)[1] == 450:
        canvas.move(emapa_11,0,10)
        canvas.move(emapa_11,0,0)
        ganar()
        
    

    elif canvas.coords(emapa_11)[1] < 870:
        canvas.move(emapa_11,0,10)
        #print(canvas.coords(mapa)[1])
        ventana.after(100,mover_emapa_11)
    elif canvas.coords(emapa_11)[1] >= 870:
        canvas.delete(emapa_11)
       






















        




#movimiento jugador

presionar = [0,0]

def mover(event):
    """
    funcion que recive como entrada las entradas del teclado y permite mover al jugador
    """
    global canvas, carro, presionar, carrom, enemigo, enemigo_2, enemigo_3 
    tecla = repr(event.char)
    
    
    


        
            
    if canvas.coords(carro)[0]-25 >= 100 and carrom == False: 
        if tecla == "'a'":
            presionar[0] = True
            canvas.move(carro,-10,0)

    if canvas.coords(carro)[0]+25 <= 290 and carrom == False :
        if tecla == "'d'":
            presionar[1] = True
            canvas.move(carro,10,0)

def no_mover(event):
    
    global canvas, carro, presionar
    tecla = repr(event.char)
    if tecla == "'a'":
        presionar[0] = False
    if tecla == "'d'":
        presionar[1] = False

for char in ["a", "d"]:
    canvas.bind ("<KeyPress-%s>" % char,mover)
    canvas.bind ("<KeyRelease-%s>" % char, no_mover)



# movimiento enemigo (AMARILLOS)

def mover_enemigo():
    """
    funcion que permite que el enemigo se mueva a traves del mapa
    """
    global enemigo, canvas, x, enemigo, carro, carrom, puntos, p 

    if (canvas.coords(carro)[0]-5 <= canvas.coords(enemigo)[0]+25    and canvas.coords(carro)[0]+5 >= canvas.coords(enemigo)[0]-25)  and (canvas.coords(carro)[1]-25 <= canvas.coords(enemigo)[1]+27 and canvas.coords(carro)[1]+25 >= canvas.coords(enemigo)[1]-27) and carrom == False : 
        carrom = True
        canvas.delete(enemigo)
        p = p -50
        canvas.itemconfig(puntos,text= p)
        chocar()
    else:
        
        #if canvas.coords(mapa_10)[1] == 450:
             #canvas.move(enemigo,0,0)
        if canvas.coords(enemigo)[1] < 600:
            canvas.move(enemigo,0,10)
            ventana.after(100,mover_enemigo)
        elif canvas.coords(enemigo)[1] >= 600:
            canvas.delete(enemigo)
            p = p +100
            canvas.itemconfig(puntos,text= p)
        
        
       
        
def mover_enemigo_2():
    """
    funcion que permite que el enemigo se mueva a traves del mapa
    """
    global enemigo_2, canvas, x2, enemigo_2, carro, carrom, y2, p, puntos

    if (canvas.coords(carro)[0]-5 <= canvas.coords(enemigo_2)[0]+25    and canvas.coords(carro)[0]+5 >= canvas.coords(enemigo_2)[0]-25)  and (canvas.coords(carro)[1]-25 <= canvas.coords(enemigo_2)[1]+27 and canvas.coords(carro)[1]+25 >= canvas.coords(enemigo_2)[1]-27) and carrom == False : 
        carrom = True
        canvas.delete(enemigo_2)
        p = p -50
        canvas.itemconfig(puntos,text= p)
        chocar()
        

    else:
        #if canvas.coords(mapa_10)[1] == 450:
             #canvas.move(enemigo_2,0,0)
        if canvas.coords(enemigo_2)[1] < 610:
            canvas.move(enemigo_2,0,10)
            ventana.after(100,mover_enemigo_2)
        elif canvas.coords(enemigo_2)[1] >= 610:
            canvas.delete(enemigo_2)
            p = p +100
            canvas.itemconfig(puntos,text= p)
            

def mover_enemigo_3():
    """
    funcion que permite que el enemigo se mueva a traves del mapa
    """
    global enemigo_3, canvas, x3, enemigo_3, carro, carrom, y3, puntos, p

    if (canvas.coords(carro)[0]-5 <= canvas.coords(enemigo_3)[0]+25    and canvas.coords(carro)[0]+5 >= canvas.coords(enemigo_3)[0]-25)  and (canvas.coords(carro)[1]-25 <= canvas.coords(enemigo_3)[1]+27 and canvas.coords(carro)[1]+25 >= canvas.coords(enemigo_3)[1]-27) and carrom == False: 
        carrom = True
        canvas.delete(enemigo_3)
        p = p -50
        canvas.itemconfig(puntos,text= p)
        chocar()
    else:

        #if canvas.coords(mapa_10)[1] == 450:
             #canvas.move(enemigo_3,0,0)

        if canvas.coords(enemigo_3)[1] < 610:
            canvas.move(enemigo_3,0,10)
            ventana.after(100,mover_enemigo_3)
        elif canvas.coords(enemigo_3)[1] >= 610:
            canvas.delete(enemigo_3)
            p = p +100
            canvas.itemconfig(puntos,text= p)


          
def mover_enemigo_4():
    """
    funcion que permite que el enemigo se mueva a traves del mapa
    """
    global enemigo_4, canvas, x3, enemigo_4, carro, carrom, y3, puntos, p

    if (canvas.coords(carro)[0]-5 <= canvas.coords(enemigo_4)[0]+25    and canvas.coords(carro)[0]+5 >= canvas.coords(enemigo_4)[0]-25)  and (canvas.coords(carro)[1]-25 <= canvas.coords(enemigo_4)[1]+27 and canvas.coords(carro)[1]+25 >= canvas.coords(enemigo_4)[1]-27) and carrom == False: 
        carrom = True
        canvas.delete(enemigo_4)
        p = p -50
        canvas.itemconfig(puntos,text= p)
        chocar()
    else:

        #if canvas.coords(mapa_10)[1] == 450:
             #canvas.move(enemigo_4,0,0)

        if canvas.coords(enemigo_4)[1] < 610:
            canvas.move(enemigo_4,0,10)
            ventana.after(100,mover_enemigo_4)
        elif canvas.coords(enemigo_4)[1] >= 610:
            canvas.delete(enemigo_4)
            p = p +100
            canvas.itemconfig(puntos,text= p)

def mover_enemigo_5():
    """
    funcion que permite que el enemigo se mueva a traves del mapa
    """
    global enemigo_5, canvas, x3, enemigo_5, carro, carrom, y3, puntos, p

    if (canvas.coords(carro)[0]-5 <= canvas.coords(enemigo_5)[0]+25    and canvas.coords(carro)[0]+5 >= canvas.coords(enemigo_5)[0]-25)  and (canvas.coords(carro)[1]-25 <= canvas.coords(enemigo_5)[1]+27 and canvas.coords(carro)[1]+25 >= canvas.coords(enemigo_5)[1]-27) and carrom == False: 
        carrom = True
        canvas.delete(enemigo_5)
        p = p -50
        canvas.itemconfig(puntos,text= p)
        chocar()
    else:

        #if canvas.coords(mapa_10)[1] == 450:
             #canvas.move(enemigo_5,0,0)

        if canvas.coords(enemigo_5)[1] < 610:
            canvas.move(enemigo_5,0,10)
            ventana.after(100,mover_enemigo_5)
        elif canvas.coords(enemigo_5)[1] >= 610:
            canvas.delete(enemigo_5)
            p = p +100
            canvas.itemconfig(puntos,text= p)


def mover_enemigo_6():
    """
    funcion que permite que el enemigo se mueva a traves del mapa
    """
    global enemigo_6, canvas, x3, enemigo_6, carro, carrom, y3, puntos, p

    if (canvas.coords(carro)[0]-5 <= canvas.coords(enemigo_6)[0]+25    and canvas.coords(carro)[0]+5 >= canvas.coords(enemigo_6)[0]-25)  and (canvas.coords(carro)[1]-25 <= canvas.coords(enemigo_6)[1]+27 and canvas.coords(carro)[1]+25 >= canvas.coords(enemigo_6)[1]-27) and carrom == False: 
        carrom = True
        canvas.delete(enemigo_6)
        p = p -50
        canvas.itemconfig(puntos,text= p)
        chocar()
    else:

        #if canvas.coords(mapa_10)[1] == 450:
             #canvas.move(enemigo_6,0,0)

        if canvas.coords(enemigo_6)[1] < 610:
            canvas.move(enemigo_6,0,10)
            ventana.after(100,mover_enemigo_6)
        elif canvas.coords(enemigo_6)[1] >= 610:
            canvas.delete(enemigo_6)
            p = p +100
            canvas.itemconfig(puntos,text= p)

def mover_enemigo_7():
    """
    funcion que permite que el enemigo se mueva a traves del mapa
    """
    global enemigo_7, canvas, x3, enemigo_7, carro, carrom, y3, puntos, p

    if (canvas.coords(carro)[0]-5 <= canvas.coords(enemigo_7)[0]+25    and canvas.coords(carro)[0]+5 >= canvas.coords(enemigo_7)[0]-25)  and (canvas.coords(carro)[1]-25 <= canvas.coords(enemigo_7)[1]+27 and canvas.coords(carro)[1]+25 >= canvas.coords(enemigo_7)[1]-27) and carrom == False: 
        carrom = True
        canvas.delete(enemigo_7)
        p = p -50
        canvas.itemconfig(puntos,text= p)
        chocar()
    else:

        #if canvas.coords(mapa_10)[1] == 450:
             #canvas.move(enemigo_7,0,0)

        if canvas.coords(enemigo_7)[1] < 610:
            canvas.move(enemigo_7,0,10)
            ventana.after(100,mover_enemigo_7)
        elif canvas.coords(enemigo_7)[1] >= 610:
            canvas.delete(enemigo_7)
            p = p +100
            canvas.itemconfig(puntos,text= p)

def mover_enemigo_8():
    """
    funcion que permite que el enemigo se mueva a traves del mapa
    """
    global enemigo_8, canvas, x3, enemigo_8, carro, carrom, y3, puntos, p

    if (canvas.coords(carro)[0]-5 <= canvas.coords(enemigo_8)[0]+25    and canvas.coords(carro)[0]+5 >= canvas.coords(enemigo_8)[0]-25)  and (canvas.coords(carro)[1]-25 <= canvas.coords(enemigo_8)[1]+27 and canvas.coords(carro)[1]+25 >= canvas.coords(enemigo_8)[1]-27) and carrom == False: 
        carrom = True
        canvas.delete(enemigo_8)
        p = p -50
        canvas.itemconfig(puntos,text= p)
        chocar()
    else:

        #if canvas.coords(mapa_10)[1] == 450:
             #canvas.move(enemigo_8,0,0)

        if canvas.coords(enemigo_8)[1] < 610:
            canvas.move(enemigo_8,0,10)
            ventana.after(100,mover_enemigo_8)
        elif canvas.coords(enemigo_8)[1] >= 610:
            canvas.delete(enemigo_8)
            p = p +100
            canvas.itemconfig(puntos,text= p)

def mover_enemigo_9():
    """
    funcion que permite que el enemigo se mueva a traves del mapa
    """
    global enemigo_9, canvas, x3, enemigo_9, carro, carrom, y3, puntos, p

    if (canvas.coords(carro)[0]-5 <= canvas.coords(enemigo_9)[0]+25    and canvas.coords(carro)[0]+5 >= canvas.coords(enemigo_9)[0]-25)  and (canvas.coords(carro)[1]-25 <= canvas.coords(enemigo_9)[1]+27 and canvas.coords(carro)[1]+25 >= canvas.coords(enemigo_9)[1]-27) and carrom == False: 
        carrom = True
        canvas.delete(enemigo_9)
        p = p -50
        canvas.itemconfig(puntos,text= p)
        chocar()
    else:

        #if canvas.coords(mapa_10)[1] == 450:
             #canvas.move(enemigo_9,0,0)

        if canvas.coords(enemigo_9)[1] < 610:
            canvas.move(enemigo_9,0,10)
            ventana.after(100,mover_enemigo_9)
        elif canvas.coords(enemigo_9)[1] >= 610:
            canvas.delete(enemigo_9)
            p = p +100
            canvas.itemconfig(puntos,text= p)

def mover_enemigo_10():
    """
    funcion que permite que el enemigo se mueva a traves del mapa
    """
    global enemigo_10, canvas, x3, enemigo_10, carro, carrom, y3, puntos, p

    if (canvas.coords(carro)[0]-5 <= canvas.coords(enemigo_10)[0]+25    and canvas.coords(carro)[0]+5 >= canvas.coords(enemigo_10)[0]-25)  and (canvas.coords(carro)[1]-25 <= canvas.coords(enemigo_10)[1]+27 and canvas.coords(carro)[1]+25 >= canvas.coords(enemigo_10)[1]-27) and carrom == False: 
        carrom = True
        canvas.delete(enemigo_10)
        p = p -50
        canvas.itemconfig(puntos,text= p)
        chocar()
    else:

        #if canvas.coords(mapa_10)[1] == 450:
             #canvas.move(enemigo_10,0,0)

        if canvas.coords(enemigo_10)[1] < 610:
            canvas.move(enemigo_10,0,10)
            ventana.after(100,mover_enemigo_10)
        elif canvas.coords(enemigo_10)[1] >= 610:
            canvas.delete(enemigo_10)
            p = p +100
            canvas.itemconfig(puntos,text= p)

def mover_enemigo_11():
    """
    funcion que permite que el enemigo se mueva a traves del mapa
    """
    global enemigo_11, canvas, x3, enemigo_11, carro, carrom, y3, puntos, p

    if (canvas.coords(carro)[0]-5 <= canvas.coords(enemigo_11)[0]+25    and canvas.coords(carro)[0]+5 >= canvas.coords(enemigo_11)[0]-25)  and (canvas.coords(carro)[1]-25 <= canvas.coords(enemigo_11)[1]+27 and canvas.coords(carro)[1]+25 >= canvas.coords(enemigo_11)[1]-27) and carrom == False: 
        carrom = True
        canvas.delete(enemigo_11)
        p = p -50
        canvas.itemconfig(puntos,text= p)
        chocar()
    else:

        #if canvas.coords(mapa_10)[1] == 450:
             #canvas.move(enemigo_11,0,0)

        if canvas.coords(enemigo_11)[1] < 610:
            canvas.move(enemigo_11,0,10)
            ventana.after(100,mover_enemigo_11)
        elif canvas.coords(enemigo_11)[1] >= 610:
            canvas.delete(enemigo_11)
            p = p +100
            canvas.itemconfig(puntos,text= p)


def mover_enemigo_12():
    """
    funcion que permite que el enemigo se mueva a traves del mapa
    """
    global enemigo_12, canvas, x3, enemigo_12, carro, carrom, y3, puntos, p

    if (canvas.coords(carro)[0]-5 <= canvas.coords(enemigo_12)[0]+25    and canvas.coords(carro)[0]+5 >= canvas.coords(enemigo_12)[0]-25)  and (canvas.coords(carro)[1]-25 <= canvas.coords(enemigo_12)[1]+27 and canvas.coords(carro)[1]+25 >= canvas.coords(enemigo_12)[1]-27) and carrom == False: 
        carrom = True
        canvas.delete(enemigo_12)
        p = p -50
        canvas.itemconfig(puntos,text= p)
        chocar()
    else:

        #if canvas.coords(mapa_10)[1] == 450:
             #canvas.move(enemigo_12,0,0)

        if canvas.coords(enemigo_12)[1] < 610:
            canvas.move(enemigo_12,0,10)
            ventana.after(100,mover_enemigo_12)
        elif canvas.coords(enemigo_12)[1] >= 610:
            canvas.delete(enemigo_12)
            p = p +100
            canvas.itemconfig(puntos,text= p)


def mover_enemigo_13():
    """
    funcion que permite que el enemigo se mueva a traves del mapa
    """
    global enemigo_13, canvas, x3, enemigo_13, carro, carrom, y3, puntos, p

    if (canvas.coords(carro)[0]-5 <= canvas.coords(enemigo_13)[0]+25    and canvas.coords(carro)[0]+5 >= canvas.coords(enemigo_13)[0]-25)  and (canvas.coords(carro)[1]-25 <= canvas.coords(enemigo_13)[1]+27 and canvas.coords(carro)[1]+25 >= canvas.coords(enemigo_13)[1]-27) and carrom == False: 
        carrom = True
        canvas.delete(enemigo_13)
        p = p -50
        canvas.itemconfig(puntos,text= p)
        chocar()
    else:

        #if canvas.coords(mapa_10)[1] == 450:
             #canvas.move(enemigo_13,0,0)

        if canvas.coords(enemigo_13)[1] < 610:
            canvas.move(enemigo_13,0,10)
            ventana.after(100,mover_enemigo_13)
        elif canvas.coords(enemigo_13)[1] >= 610:
            canvas.delete(enemigo_13)
            p = p +100
            canvas.itemconfig(puntos,text= p)


def mover_enemigo_14():
    """
    funcion que permite que el enemigo se mueva a traves del mapa
    """
    global enemigo_14, canvas, x3, enemigo_14, carro, carrom, y3, puntos, p

    if (canvas.coords(carro)[0]-5 <= canvas.coords(enemigo_14)[0]+25    and canvas.coords(carro)[0]+5 >= canvas.coords(enemigo_14)[0]-25)  and (canvas.coords(carro)[1]-25 <= canvas.coords(enemigo_14)[1]+27 and canvas.coords(carro)[1]+25 >= canvas.coords(enemigo_14)[1]-27) and carrom == False: 
        carrom = True
        canvas.delete(enemigo_14)
        p = p -50
        canvas.itemconfig(puntos,text= p)
        chocar()
    else:

        #if canvas.coords(mapa_10)[1] == 450:
            # canvas.move(enemigo_14,0,0)

        if canvas.coords(enemigo_14)[1] < 610:
            canvas.move(enemigo_14,0,10)
            ventana.after(100,mover_enemigo_14)
        elif canvas.coords(enemigo_14)[1] >= 610:
            canvas.delete(enemigo_14)
            p = p +100
            canvas.itemconfig(puntos,text= p)


def mover_enemigo_15():
    """
    funcion que permite que el enemigo se mueva a traves del mapa
    """
    global enemigo_15, canvas, x3, enemigo_15, carro, carrom, y3, puntos, p

    if (canvas.coords(carro)[0]-5 <= canvas.coords(enemigo_15)[0]+25    and canvas.coords(carro)[0]+5 >= canvas.coords(enemigo_15)[0]-25)  and (canvas.coords(carro)[1]-25 <= canvas.coords(enemigo_15)[1]+27 and canvas.coords(carro)[1]+25 >= canvas.coords(enemigo_15)[1]-27) and carrom == False: 
        carrom = True
        canvas.delete(enemigo_15)
        p = p -50
        canvas.itemconfig(puntos,text= p)
        chocar()
    else:

        #if canvas.coords(mapa_10)[1] == 450:
             #canvas.move(enemigo_15,0,0)

        if canvas.coords(enemigo_15)[1] < 610:
            canvas.move(enemigo_15,0,10)
            ventana.after(100,mover_enemigo_15)
        elif canvas.coords(enemigo_15)[1] >= 610:
            canvas.delete(enemigo_15)
            p = p +100
            canvas.itemconfig(puntos,text= p)


#movimiento enemigos (AZULES)

def mover_azul():
    """
    funcion que permite que el enemigo se mueva a traves del mapa
    """
    global azul, canvas,carro, carrom, puntos, p

    if (canvas.coords(carro)[0]-5 <= canvas.coords(azul)[0]+25    and canvas.coords(carro)[0]+5 >= canvas.coords(azul)[0]-25)  and (canvas.coords(carro)[1]-25 <= canvas.coords(azul)[1]+27 and canvas.coords(carro)[1]+25 >= canvas.coords(azul)[1]-27) and carrom == False: 
        carrom = True
        canvas.delete(azul)
        p = p -50
        canvas.itemconfig(puntos,text= p)
        chocar()
    else:

        #if canvas.coords(mapa_10)[1] == 450:
             #canvas.move(azul,0,0)

        if canvas.coords(azul)[1] < 610:
            
            if canvas.coords(azul)[0] >= 120 and canvas.coords(azul)[0] >= 190:
                #print("1")
                canvas.move(azul,-50,60)
                ventana.after(600,mover_azul)
            elif canvas.coords(azul)[0] <= 270 and  canvas.coords(azul)[0] <= 270:
                #print("2")
                #print(canvas.coords(carro)[0]-25)
                canvas.move(azul,70,60)
                ventana.after(600,mover_azul)
            #ventana.after(100,mover_azul)
        elif canvas.coords(azul)[1] >= 610:
            canvas.delete(azul)
            p = p +100
            canvas.itemconfig(puntos,text= p)

def mover_azul_2():
    """
    funcion que permite que el enemigo se mueva a traves del mapa
    """
    global azul_2, canvas,carro, carrom, puntos, p

    if (canvas.coords(carro)[0]-5 <= canvas.coords(azul_2)[0]+25    and canvas.coords(carro)[0]+5 >= canvas.coords(azul_2)[0]-25)  and (canvas.coords(carro)[1]-25 <= canvas.coords(azul_2)[1]+27 and canvas.coords(carro)[1]+25 >= canvas.coords(azul_2)[1]-27) and carrom == False: 
        carrom = True
        canvas.delete(azul_2)
        p = p -50
        canvas.itemconfig(puntos,text= p)
        chocar()
    else:

        #if canvas.coords(mapa_10)[1] == 450:
             #canvas.move(azul_2,0,0)

        if canvas.coords(azul_2)[1] < 610:
            
            if canvas.coords(azul_2)[0] >= 120 and canvas.coords(azul_2)[0] >= 190:
                #print("1")
                canvas.move(azul_2,-50,60)
                ventana.after(600,mover_azul_2)
            elif canvas.coords(azul_2)[0] <= 270 and  canvas.coords(azul_2)[0] <= 270:
                #print("2")
                #print(canvas.coords(carro)[0]-25)
                canvas.move(azul_2,70,60)
                ventana.after(600,mover_azul_2)
            #ventana.after(100,mover_azul)
        elif canvas.coords(azul_2)[1] >= 610:
            canvas.delete(azul_2)
            p = p +100
            canvas.itemconfig(puntos,text= p)
    
def mover_azul_3():
    """
    funcion que permite que el enemigo se mueva a traves del mapa
    """
    global azul_3, canvas,carro, carrom, puntos, p

    if (canvas.coords(carro)[0]-5 <= canvas.coords(azul_3)[0]+25    and canvas.coords(carro)[0]+5 >= canvas.coords(azul_3)[0]-25)  and (canvas.coords(carro)[1]-25 <= canvas.coords(azul_3)[1]+27 and canvas.coords(carro)[1]+25 >= canvas.coords(azul_3)[1]-27) and carrom == False: 
        carrom = True
        canvas.delete(azul_3)
        p = p -50
        canvas.itemconfig(puntos,text= p)
        chocar()
    else:

        #if canvas.coords(mapa_10)[1] == 450:
             #canvas.move(azul,0,0)

        if canvas.coords(azul_3)[1] < 610:
            
            if canvas.coords(azul_3)[0] >= 120 and canvas.coords(azul_3)[0] >= 190:
                #print("1")
                canvas.move(azul_3,-50,60)
                ventana.after(600,mover_azul_3)
            elif canvas.coords(azul_3)[0] <= 270 and  canvas.coords(azul_3)[0] <= 270:
                #print("2")
                #print(canvas.coords(carro)[0]-25)
                canvas.move(azul_3,70,60)
                ventana.after(600,mover_azul_3)
            #ventana.after(100,mover_azul)
        elif canvas.coords(azul_3)[1] >= 610:
            canvas.delete(azul_3)
            p = p +100
            canvas.itemconfig(puntos,text= p)



#movimiento runner

def mover_runner():
    """
    """
    global runner, canvas,carro, carrom, puntos, p
    
    if (canvas.coords(carro)[0]-5 <= canvas.coords(runner)[0]+25    and canvas.coords(carro)[0]+5 >= canvas.coords(runner)[0]-25)  and (canvas.coords(carro)[1]-25 <= canvas.coords(runner)[1]+27 and canvas.coords(carro)[1]+25 >= canvas.coords(runner)[1]-27) and carrom == False: 
        carrom = True
        canvas.delete(runner)
        p = p -50
        canvas.itemconfig(puntos,text= p)
        chocar()

    else:
        if canvas.coords(runner)[1] < 610:
            if canvas.coords(runner)[0] == canvas.coords(carro)[0]:
                canvas.move(runner,0,60)
                ventana.after(500,mover_runner)
            elif canvas.coords(runner)[0] > canvas.coords(carro)[0]:
                canvas.move(runner,-20,60)
                ventana.after(500,mover_runner)
            elif canvas.coords(runner)[0]< canvas.coords(carro)[0]:
                canvas.move(runner,20,60)
                ventana.after(500,mover_runner)

        elif canvas.coords(runner)[1] >= 610:
            canvas.delete(runner)
            p = p +100
            canvas.itemconfig(puntos,text= p)


                
        









def ganar():
    """
    """
    global canvas
    canvas.delete('all')
    canvas.create_text(300,250,text="ganaste!",font=("avantgarde",50),fill="white")
    print("ganaste")
    ventana.after(2000,cerrar)






def cerrar():
    """
    funcion que cierra el juego
    """
    ventana.destroy()




def resucitar():
    """
    funcion que vuelve a colocar el carro en su lugar original y de ser el caso cierra el juego
    y muestra la pantalla de perdiste
    """
    global canvas, carro, enemigo, enemigo_2, enemigo_3, cont_vidas, carrom, fin
    if fin == True:
        canvas.delete('all')
        canvas.create_text(300,250,text="Has Perdido",font=("avantgarde",50),fill="white")
        print("perdiste")
        ventana.after(2000,cerrar)
    else:
        
        carro = canvas.create_image(200,450,image=icarro)
        carrom = False
   
    
             




def chocar():
    """
    funcion que despues de chocar con un enemigo desaparece el carro y quita una vida
    """
    global canvas, carro, enemigo, enemigo_2, enemigo_3, cont_vidas, carrom, vida, vida_2, vida_3, cont_vidas, fin


    if carrom == True:
        if canvas.coords(carro)[1]< 610:
            canvas.move(carro,0,30)
            ventana.after(10,chocar)
        else:
            if cont_vidas == 3:
                canvas.delete(vida_3)
            elif cont_vidas == 2:
                canvas.delete(vida_2)
            elif cont_vidas == 1:
                canvas.delete(vida)
            elif cont_vidas == 0:
                canvas.delete(enemigo)
                canvas.delete(enemigo_2)
                canvas.delete(enemigo_3)
                canvas.delete(carro)
                
                fin = True
            cont_vidas = cont_vidas -1
            canvas.delete(carro)
            resucitar()
    
    
        
        

    
    
# menu

# carga imagenes del menu 
iniveles = tkinter.PhotoImage(file="niveles.gif")
niveles= canvas.create_image(290,290,image=iniveles)
imano_2 = tkinter.PhotoImage(file="mano_2.gif")
mano_2= canvas.create_image(150,170,image=imano_2)
inombre = tkinter.PhotoImage(file="nombre.gif")
nombre= canvas.create_image(290,290,image=inombre)
imenu = tkinter.PhotoImage(file="menu.gif")
menu= canvas.create_image(290,290,image=imenu)
imano = tkinter.PhotoImage(file="mano.gif")
mano= canvas.create_image(150,300,image=imano)
man = True
man_2 = True
menub = True
nombreb = True
dif = False

# funciones de movimineto selector
def mover_mano_u(event):
    global mano, canvas, man
    #print(canvas.coords(mano)[1])
    if man == True:
        if canvas.coords(mano)[1] >= 400:
            canvas.move(mano,0,-100)
        if canvas.coords(mano)[1] == 261.8:
            canvas.move(mano,0,-100)
    if man == False and man_2 == True:
        if canvas.coords(mano_2)[1] > 170:
            canvas.move(mano_2,0,-62)

def mover_mano_d(event):
    global mano, canvas, man
    #print(canvas.coords(mano)[1])
    if man == True:
        if canvas.coords(mano)[1] < 500:
            canvas.move(mano,0,100)
        if canvas.coords(mano)[1] == 261.8:
            canvas.move(mano,0,100)
    if man == False and man_2 == True:
        #print(canvas.coords(mano_2)[1])
        if canvas.coords(mano_2)[1]<388:
            canvas.move(mano_2,0,62)

#funcion que permite realizar las diferentes opciones 
def opciones(event):
    global menu, dif, niveles, nombre, mano, nombre_jugador, man, menub, nombreb, nombre1, man_2, tipo, inombre, p_puntos, puntos, p
    tecla = repr(event.char)

    if (menub == True) and (dif == False )and (tecla == "'o'" and canvas.coords(mano)[1] == 300 and man==True and nombreb == True):
        print("1")
        canvas.delete(menu)
        canvas.delete(mano)
        canvas.delete(niveles)
        canvas.delete(mano_2)
        inombre = tkinter.PhotoImage(file="nombre.gif")
        nombre= canvas.create_image(290,290,image=inombre)
        man = False
        man_2 = False
        menub = False
        nombre1=tkinter.Entry(canvas,bd=5)
        nombre1.place(x=190,y=350)
        nombreb = False
    elif nombreb == False:
        n=nombre1.get()
        canvas.itemconfig(nombre_jugador,text=str(n))
        canvas.itemconfig(p_puntos,text="puntos")
        canvas.itemconfig(puntos,text= p)
        nombre1.destroy()
        canvas.focus_set()
        canvas.delete(nombre)
        llamar_todo()

    if( menub == True ) and (dif == False)  and (tecla == "'o'" and canvas.coords(mano)[1] == 500 and man ==  True) and (nombreb == True):
        cerrar()

    if (menub == True) and (tecla=="'o'" and man == True and canvas.coords(mano)[1]== 400) and (nombreb == True) and (dif == False):
        #print("2")
        man = False
        dif = True
        canvas.delete(nombre)
        canvas.delete(menu)
        canvas.delete(mano)

    elif (menub == True) and (dif == True) and ((tecla == "'o'" and man == False) and (canvas.coords(mano_2)[1]== 170) and (man_2== True)) and (nombreb == True):
        man_2 = False
        dif = False
        man = True
        canvas.delete(niveles)
        canvas.delete(mano_2)
        menu= canvas.create_image(290,290,image=imenu)
        mano= canvas.create_image(150,300,image=imano)
        print("1")
        tipo = 1
    
    elif (menub == True) and dif == True and ((tecla == "'o'" and man == False) and (canvas.coords(mano_2)[1]== 232) and (man_2== True)) and (nombreb == True): 
        man_2 = False
        dif = False
        man = True
        canvas.delete(niveles)
        canvas.delete(mano_2)
        menu= canvas.create_image(290,290,image=imenu)
        mano= canvas.create_image(150,300,image=imano)
        print("2")
        tipo = 2


    elif (menub == True) and dif == True and ((tecla == "'o'" and man == False) and (canvas.coords(mano_2)[1]== 294) and (man_2== True)) and (nombreb == True): 
        man_2 = False
        dif = False
        man = True
        canvas.delete(niveles)
        canvas.delete(mano_2)
        menu= canvas.create_image(290,290,image=imenu)
        mano= canvas.create_image(150,300,image=imano)
        print("3")
        tipo = 3

    elif (menub == True) and dif == True and ((tecla == "'o'" and man == False) and (canvas.coords(mano_2)[1]== 356) and (man_2== True)) and (nombreb == True): 
        man_2 = False
        dif = False
        man = True
        canvas.delete(niveles)
        canvas.delete(mano_2)
        menu= canvas.create_image(290,290,image=imenu)
        mano= canvas.create_image(150,300,image=imano)
        print("4")
        tipo = 4

    elif (menub == True) and dif == True and ((tecla == "'o'" and man == False) and (canvas.coords(mano_2)[1]== 418) and (man_2== True)) and (nombreb == True): 
        man_2 = False
        dif = False
        man = True
        canvas.delete(niveles)
        canvas.delete(mano_2)
        menu= canvas.create_image(290,290,image=imenu)
        mano= canvas.create_image(150,300,image=imano)
        print("5")
        tipo = 5
        



def llamar_todo():
    mapas()
    carro()
    amarillos()
    azules()
    runners()
    hud()
    
        
    

ventana.bind('<Up>',mover_mano_u)
ventana.bind('<Down>',mover_mano_d)
ventana.bind('<o>',opciones)














canvas.focus_set()
canvas.pack()
ventana.mainloop()
