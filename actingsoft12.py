from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
import pathlib

root = Tk()
root.title("Entrada de Datos")
root.geometry('700x700+300+200')
root.resizable(False, False)
root.configure(bg="#326273")

lista_pacientes = []
lista_imc = []


class Paciente:
    def __init__(self, codigo, nombre, ap, am, edad, genero):
        self.codigo = codigo
        self.nombre = nombre
        self.ap = ap
        self.am = am
        self.edad = edad
        self.genero = genero

def enviar():
    codigo = codValor.get()
    nombre = nomValor.get()
    ap = apValor.get()
    am = amValor.get()
    edad = edadValor.get()
    genero = gen_combobox.get()

    paciente = Paciente(codigo, nombre, ap, am, edad, genero)

  
    lista_pacientes.append(paciente)
    print(paciente)

pesoValor = tk.Entry(root, width=5, bd=2, font=20)
pesoValor.place(x=260, y=270)
alturaValor = tk.Entry(root, width=5, bd=2, font=20)
alturaValor.place(x=500, y=270)   
    

def limpiar():
    nomValor.delete(0, 'end')
    codValor.delete(0, 'end')
    edadValor.delete(0, 'end')
    apValor.delete(0, 'end')
    amValor.delete(0, 'end')
    pesoValor.delete(0, 'end')
    alturaValor.delete(0, 'end')

def buscar():
    ventana_emergente = tk.Toplevel(root)
    ventana_emergente.geometry('700x700+300+200')
    ventana_emergente.resizable(False,False)
    ventana_emergente.configure(bg="#326273")
    ventana_emergente.title("Sección Buscar")
    
    try:
        codigo = int(codValor.get())  # Convertimos el valor recogido a entero
    except ValueError:
        messagebox.showerror('Error', 'El ID ingresado no es válido.')
        return

    paciente_encontrado = None

    # Buscamos al paciente en la lista de pacientes
    for paciente in lista_pacientes:
        if paciente.codigo == codigo:  # Asegúrate de que el ID del paciente también sea entero
            paciente_encontrado = paciente
            break

    # Mostramos los datos del paciente si lo encontramos
    if paciente_encontrado:
        info = f'''
        ID: {paciente_encontrado.codigo}
        Nombre: {paciente_encontrado.nombre}
        Apellido Paterno: {paciente_encontrado.ap}
        Apellido Materno: {paciente_encontrado.am}
        Edad: {paciente_encontrado.edad}
        Género: {paciente_encontrado.genero}
        '''
        messagebox.showinfo('Información del paciente', info)
    else:
        messagebox.showerror('Error', 'Paciente con ese ID no encontrado')
    
    Label(ventana_emergente, text='ID', font=23, bg="#326273", fg="#fff").place(x=50, y=50)
    Label(ventana_emergente, text='Nombre', font=23, bg="#326273", fg="#fff").place(x=50, y=100)
    Label(ventana_emergente, text='Apellido paterno', font=23, bg="#326273", fg="#fff").place(x=40, y=150)
    Label(ventana_emergente, text='Apellido materno', font=23, bg="#326273", fg="#fff").place(x=40, y=200)
    Label(ventana_emergente, text='Edad', font=23, bg="#326273", fg="#fff").place(x=360, y=100)
    Label(ventana_emergente, text='Género', font=23, bg="#326273", fg="#fff").place(x=360, y=200)

    Label(ventana_emergente, text='Peso en kg', font=23, bg="#326273", fg="#fff").place(x=140, y=270)
    Label(ventana_emergente, text='Altura en cm', font=23, bg="#326273", fg="#fff").place(x=360, y=270)

# entrada de datos

#cajas
    nomValor = tk.Entry(ventana_emergente, width=12, bd=2, font=20)
    nomValor.place(x=200, y=50)
    apValor = tk.Entry(ventana_emergente, width=12, bd=2, font=20)
    apValor.place(x=200, y=150)
    amValor = tk.Entry(ventana_emergente, width=12, bd=2, font=20)
    amValor.place(x=200, y=200)
    codValor = tk.Entry(ventana_emergente, width=10, bd=2, font=20)
    codValor.place(x=200, y=100)
    edadValor = tk.Entry(ventana_emergente, width=5, bd=2, font=20)
    edadValor.place(x=440, y=100)

# combobox género
    gen_combobox = Combobox(ventana_emergente, values=['Masculino', 'Femenino'], font='arial 14', state='r', width=12)
    gen_combobox.place(x=440, y=200)
    gen_combobox.set('Masculino')


Label(root, text="Por favor llena este formulario: ", font="arial 13", bg="#326273", fg="#fff").place(x=20, y=20)

# etiquetado
Label(root, text='ID', font=23, bg="#326273", fg="#fff").place(x=50, y=50)
Label(root, text='Nombre', font=23, bg="#326273", fg="#fff").place(x=50, y=100)
Label(root, text='Apellido paterno', font=23, bg="#326273", fg="#fff").place(x=40, y=150)
Label(root, text='Apellido materno', font=23, bg="#326273", fg="#fff").place(x=40, y=200)
Label(root, text='Edad', font=23, bg="#326273", fg="#fff").place(x=360, y=100)
Label(root, text='Género', font=23, bg="#326273", fg="#fff").place(x=360, y=200)

Label(root, text='Peso en kg', font=23, bg="#326273", fg="#fff").place(x=140, y=270)
Label(root, text='Altura en cm', font=23, bg="#326273", fg="#fff").place(x=360, y=270)

# entrada de datos

#cajas
nomValor = tk.Entry(root, width=12, bd=2, font=20)
nomValor.place(x=200, y=50)
apValor = tk.Entry(root, width=12, bd=2, font=20)
apValor.place(x=200, y=150)
amValor = tk.Entry(root, width=12, bd=2, font=20)
amValor.place(x=200, y=200)
codValor = tk.Entry(root, width=10, bd=2, font=20)
codValor.place(x=200, y=100)
edadValor = tk.Entry(root, width=5, bd=2, font=20)
edadValor.place(x=440, y=100)

# combobox género
gen_combobox = Combobox(root, values=['Masculino', 'Femenino'], font='arial 14', state='r', width=12)
gen_combobox.place(x=440, y=200)
gen_combobox.set('Masculino')



Button(root, text="Guardar", bg="#326273", fg="white", width=15, height=2, command=enviar).place(x=100, y=350)
Button(root, text="Limpiar", bg="#326273", fg="white", width=15, height=2, command=limpiar).place(x=390, y=350)
Button(root, text="Salir", bg="#326273", fg="white", width=15, height=2, command=lambda: root.destroy()).place(x=540, y=350)
Button(root, text="Buscar", bg="#326273", fg="white", width=15, height=2, command=buscar).place(x=100, y=420)

root.mainloop()
