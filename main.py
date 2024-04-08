# Algoritmo de Bisección
# [a,b] se escogen de la gráfica de la función
# error = tolera
import numpy as np
import tkinter
from tkinter import ttk
from fractions import Fraction
import matplotlib.pyplot as plt
import sympy as sp
window=tkinter.Tk()
window.geometry("1600x1000")
window.columnconfigure(0,weight=3)
window.columnconfigure(1,weight=12)
window.columnconfigure(2,weight=12)
window.columnconfigure(3,weight=12)
window.columnconfigure(4,weight=1)
table=ttk.Treeview(window,columns=("i","a","c","b","f(a)","f(c)","f(b)","tramo"),show="headings")
table.heading("i",text="i")
table.heading("a",text="a")
table.heading("b",text="b")
table.heading("c",text="c")
table.heading("f(a)",text="f(a)")
table.heading("f(c)",text="f(c)")
table.heading("f(b)",text="f(b)")
table.heading("tramo",text="tramo")

table.pack()
table.place(x=20,y=200,width=1500,height=500)
table.place_forget()
tabletwo=ttk.Treeview(window,columns=("i","xa","xb","xc","tramo"),show="headings")
tabletwo.heading("i",text="i")
tabletwo.heading("xa",text="xa")
tabletwo.heading("xb",text="xb")
tabletwo.heading("xc",text="xc")
tabletwo.heading("tramo",text="tramo")
tabletwo.pack()
tabletwo.place(x=20,y=200,width=1500,height=500)
tabletwo.place_forget()
tablethree=ttk.Treeview(window,columns=("i","xi","xnuevo","tramo"),show="headings")
tablethree.heading("i",text="i")
tablethree.heading("xi",text="xi")
tablethree.heading("xnuevo",text="xnuevo")
tablethree.heading("tramo",text="tramo")
tablethree.pack()
tablethree.place(x=20,y=200,width=1500,height=500)
tablethree.place_forget()
label=ttk.Label(window,text="Metodos numericos")
label2=ttk.Label(window,text="Ingrese la funcion: f(x)= ")

label3=ttk.Label(window,text="Ingrese el limite inferior: ")
label4=ttk.Label(window,text="Ingrese el limite superior: ")
showresulbiseccion=ttk.Label(window,text='')
showeerrofalseposition=ttk.Label(window,text='')

showeerrofalseposition.grid(column=0,row=0)
showeerrofalseposition.place(x=20,y=190)
    
showresulbiseccion.grid(column=0,row=0)
showresulbiseccion.place(x=20,y=170)
input=ttk.Entry(window)

input2=ttk.Entry(window)
input3=ttk.Entry(window)

label.grid(column=0,row=0)
label.place(x=30,y=5)
label2.grid(column=0,row=0)
label2.place(x=20,y=26)
label3.grid(column=0,row= 0)
label3.place(x=20,y=70)
label4.grid(column=0,row= 0)
label4.place(x=20,y=110)

input.grid(column=1,row=0)
input.place(x=20,y=50,width=150)
input2.grid(column=1,row=3)
input2.place(x=20,y=90,width=35)
input3.grid(column=1,row=6)
input3.place(x=20,y=130,width=35)


def notswoenot():
    calcularporbiseccion.place_forget()
    calcularporpositionfallida.place_forget()
    calcularporsecante.place_forget()
    label3.place_forget()
    label4.config(text="Ingrese x0: ")
    input2.place_forget()
    butonreback.place(x=230,y=300)
    nutoncalcular.grid(column=4,row=1 )
    nutoncalcular.place(x=230,y=330)
    

def reback():
    calcularporbiseccion.place(x=230,y=100)
    calcularporpositionfallida.place(x=230,y=50)
    calcularporsecante.place(x=230,y=250)
    label3.place(x=20,y=70)
    label4.config(text="Ingrese el limite superior: ")
    input2.place(x=20,y=90,width=35)
    input3.place(x=20,y=130,width=35)
    butonreback.place_forget()
    nutoncalcular.place_forget()
    showeerrofalseposition.config(text='')
    showresulbiseccion.config(text='')
    tablethree.place_forget()
    
    

def generate():
    fx = eval('lambda x: '+input.get())
    a = float(input2.get())
    b = float(input3.get())
    tolera = 0.001


    tabla = []
    tramo = b-a

    fa = fx(a)
    fb = fx(b)
    i = 1
    while (tramo>tolera):
        c = (a+b)/2
        fc = fx(c)
        tabla.append([i,a,c,b,fa,fc,fb,tramo])
        i = i + 1
                 
        cambia = np.sign(fa)*np.sign(fc)
        if (cambia<0):
            b = c
            fb = fc
        else:
            a=c
            fa = fc
        tramo = b-a

# szzaz
    c = (a+b)/2
    fc = fx(c)
    tabla.append([i,a,c,b,fa,fc,fb,tramo])
    tabla = np.array(tabla)

    raiz = c

# SALIDA
    np.set_printoptions(precision = 4)
    print('[ i, a, c, b, f(a), f(c), f(b), tramo]')
# print(tabla)

# Tabla con formato
    n=len(tabla)
    for i in range(0,n,1):
        unafila = tabla[i]
        formato = '{:.0f}'+' '+(len(unafila)-1)*'{:.3f} '
        unafila = formato.format(*unafila)
        print(unafila)
    
    print('raiz: ',raiz)
    showresulbiseccion.config(text='la raiz por el metodo de biseecion es de : '+str(raiz))
    showeerrofalseposition.config(text='')
    tabletwo.place_forget()
    mostrarTablas(tabla)
    graficarBisseccion(tabla)


def mostrarTablas(tabla):
    table.place(x=20,y=400,width=1399,height=500)
    table.delete(*table.get_children())
    n=len(tabla)
    for i in range(0,n,1):
        unafila = tabla[i]
        formato = '{:.0f}'+' '+(len(unafila)-1)*'{:.3f} '
        unafila = formato.format(*unafila)
        table.insert(parent="",index=i,values=(unafila))
        
        
       
        
       
   

def graficarBisseccion(tabla):
    xi = tabla[:,2]
    yi = tabla[:,5]
    orden = np.argsort(xi)
    xi = xi[orden]
    yi = yi[orden]

    plt.plot(xi,yi)
    plt.plot(xi,yi,'o')
    plt.axhline(0, color="black")

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Bisección en f(x)')
    plt.grid()
    plt.show()

def graficarsinpuntos():
    fx = eval('lambda x: '+input.get())
    x = np.linspace(-10,10,100)
    y = fx(x)
    plt.plot(x,y)
    plt.grid()
    plt.show()




def generateTableFalsePosition(tabla):
    table.place(x=20,y=400,width=1399,height=500)
    table.delete(*table.get_children())
    for i in range(0,len(tabla),1):
        table.insert(parent="",index=i,values=(i+1,tabla[i,0],tabla[i,1],tabla[i,2],tabla[i,3],tabla[i,4],tabla[i,5],tabla[i,6]))


def generatebydefaultpoint():


    fx =eval('lambda x: '+input.get())

    a = float(input2.get())
    b = float(input3.get())
    tolera = 0.0001

# PROCEDIMIENTO
    tabla = []
    tramo = abs(b-a)
    fa = fx(a)
    fb = fx(b)
    while not(tramo<=tolera):
        c = b - fb*(a-b)/(fa-fb)
        fc = fx(c)
        tabla.append([a,c,b,fa,fc,fb,tramo])
        cambio = np.sign(fa)*np.sign(fc)
        if cambio>0:
            tramo = abs(c-a)
            a = c
            fa = fc
        else:
            tramo = abs(b-c)
            b = c
            fb = fc
        
    tabla = np.array(tabla)
    ntabla = len(tabla)

# SALIDA
    np.set_printoptions(precision=4)
    for i in range(0,ntabla,1):
        print('iteración:  ',i)
        print('[a,c,b]:    ', tabla[i,0:3])
        print('[fa,fc,fb]: ', tabla[i,3:6])
        print('[tramo]:    ', tabla[i,6])

    print('raiz:  ',c)


    tabletwo.place_forget()
    showresulbiseccion.config(text='la raiz por el metodo de posicion falsa es de : '+str(c))
    showeerrofalseposition.config(text='error por el metodo de posicion falsa: '+str(tramo))
    generateTableFalsePosition(tabla)
    print('error: ',tramo)



def generatebynewthonRhapsond():
     x = sp.Symbol('x')
     y = input.get()
     fx=eval('lambda x: '+y)
     dfx=eval('lambda x: '+str(sp.diff(y,x)))
     x0 = float(input3.get())
     tolera = 0.001

    # PROCEDIMIENTO
     tabla = []
     tramo = abs(2*tolera)
     xi = x0
     tablethree.place(x=20,y=400,width=1399,height=500)
     tablethree.delete(*tablethree.get_children())
     while (tramo>=tolera):
        xnuevo = xi - fx(xi)/dfx(xi)
        tramo  = abs(xnuevo-xi)
        tabla.append([xi,xnuevo,tramo])
        tablethree.insert(parent="",index=len(tabla),values=(len(tabla),xi,xnuevo,tramo))
        

        xi = xnuevo

# convierte la lista a un arreglo.
     tabla = np.array(tabla)
     n = len(tabla)

# SALIDA
     print(['xi', 'xnuevo', 'tramo'])
     np.set_printoptions(precision = 4)
     print(tabla)
     print('raiz en: ', xi)
     showresulbiseccion.config(text='la raiz por el metodo de newthon Rhapson es de : '+str(xi))
     showeerrofalseposition.config(text='error por el metodo de newthon Rhapson: '+str(tramo))
     showeerrofalseposition.place(x=20,y=185)
     print('con error de: ',tramo)

     
def secante_tabla(fx,xa,tolera):
    dx = 4*tolera
    xb = xa + dx
    tramo = dx
    tabla = []
    while (tramo>=tolera):
        fa = fx(xa)
        fb = fx(xb)
        xc = xa - fa*(xb-xa)/(fb-fa)
        tramo = abs(xc-xa)
        
        tabla.append([xa,xb,xc,tramo])
        xb = xa
        xa = xc

    tabla = np.array(tabla)
    return(tabla)

# PROGRAMA ---------------------
# INGRESO
def generatebysecante():
    fx = eval('lambda x: '+input.get())

    a  = float(input2.get())
    b  = float(input3.get())
    xa = 1.5
    tolera = 0.001
    tramos = 100

# PROCEDIMIENTO
    tabla = secante_tabla(fx,xa,tolera)
    n = len(tabla)
    raiz = tabla[n-1,2]

# SALIDA
    np.set_printoptions(precision=4)
    print('[xa ,\t xb , \t xc , \t tramo]')
    table.place_forget()
    tabletwo.place(x=20,y=400,width=1399,height=500)
    tabletwo.delete(*tabletwo.get_children())
   
    for i in range(0,n,1):
        tabletwo.insert(parent="",index=i,values=(i+1,tabla[i,0],tabla[i,1],tabla[i,2],tabla[i,3]))
        print(tabla[i])
    print('raiz en: ', raiz)
    showresulbiseccion.config(text='la raiz por el metodo de secante es de : '+str(raiz))
    xi = np.linspace(a,b,tramos+1)
    fi = fx(xi)
    dx = (b-xa)/2
    pendiente = (fx(xa+dx)-fx(xa))/(xa+dx-xa)
    b0 = fx(xa) - pendiente*xa
    tangentei = pendiente*xi+b0

    fxa = fx(xa)
    xb = xa + dx
    fxb = fx(xb)

    plt.plot(xi,fi, label='f(x)')

    plt.plot(xi,tangentei, label='secante')
    plt.plot(xa,fx(xa),'go', label='xa')
    plt.plot(xa+dx,fx(xa+dx),'ro', label='xb')
    plt.plot((-b0/pendiente),0,'yo', label='xc')

    plt.plot([xa,xa],[0,fxa],'m')
    plt.plot([xb,xb],[0,fxb],'m')

    plt.axhline(0, color='k')
    plt.title('Método de la Secante')
    plt.legend()
    plt.grid()
    plt.show()




def plot_function( x_range=(-10, 10), num_points=1000):
    """
    Plots the graph of a given function.

    Args:
        f (callable): The function to be plotted.
        x_range (tuple, optional): Range of x values for plotting. Defaults to (-10, 10).
        num_points (int, optional): Number of points for the plot. Defaults to 1000.
    """
    f=eval('lambda x: '+input.get())
    x_values = np.linspace(x_range[0], x_range[1], num_points)
    y_values = f(x_values)

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label=f"{f.__name__}(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Graph of "+input.get())
    plt.grid(True)
    plt.legend()
    plt.show()

# Example usage:












calcular=ttk.Button(window,text="Graficar funcion",command=plot_function)
butonreback=ttk.Button(window,text="Regresar",command=reback)
butonreback.grid(column=4,row=1 )
butonreback.place(x=230,y=300)
nutoncalcular=ttk.Button(window,text="calcular",command=generatebynewthonRhapsond)
nutoncalcular.grid(column=4,row=1 )
nutoncalcular.place(x=230,y=330)
nutoncalcular.place_forget()

butonreback.place_forget()
calcularporbiseccion=ttk.Button(window,text="Calcular por biseccion",command=generate)
calcularporpositionfallida=ttk.Button(window,text="Calcular por metodo de posicion falsa",command=generatebydefaultpoint)
calcularporsecante=ttk.Button(window,text="Calcular por metodo de secante",command=generatebysecante)
calcularporsecante.grid(column=4,row=1 )
calcularporsecante.place(x=230,y=250)
calcularpornewton=ttk.Button(window,text="Calcular por metodo de newton Rhapson",command=notswoenot)
calcularpornewton.grid(column=4,row=1 )
calcularpornewton.place(x=230,y=200)
calcularporpositionfallida.grid(column=4,row=1 )
calcularporpositionfallida.place(x=230,y=50)
calcularporbiseccion.grid(column=4,row=1 )
calcularporbiseccion.place(x=230,y=100)
calcular.grid(column=4,row=1 )
calcular.place(x=230,y=150)
window.mainloop()   




