import tkinter

ventana = tkinter.Tk()
ventana.title("Electricidad y circuitos")
ventana.iconbitmap("img/llave-inglesa.ico")
ventana.geometry('1000x500')
ventana.config(background='black',)


#CHECAR EL GRID
frame_visualizacion = tkinter.Frame(ventana)
frame_visualizacion.config(background='skyblue2',width=100,height=100)

frame_visualizacion.pack(side='top')

frame_datos = tkinter.Frame(ventana)
frame_datos.config(background='gray',width=100,height=500)

frame_datos.pack(side='right')

frame_consola = tkinter.Frame(ventana)
frame_consola.config(background='snow2',width=1000,height=50)

frame_consola.pack(side='bottom')

ventana.mainloop()