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

class Paciente:
    def __init__(self, codigo, nombre, ap, am, edad, genero, peso, altura):
        self.codigo = codigo
        self.nombre = nombre
        self.ap = ap
        self.am = am
        self.edad = edad
        self.genero = genero
        self.peso = float(peso)
        self.altura = float(altura) / 100  
        
    def calcular_imc(self):
        if self.altura > 0:
            return self.peso / (self.altura ** 2)
        else:
            return 0

def enviar():
    codigo = codValor.get()
    nombre = nomValor.get()
    ap = apValor.get()
    am = amValor.get()
    edad = edadValor.get()
    genero = gen_combobox.get()
    peso = pesoValor.get()
    altura = alturaValor.get()

    paciente = Paciente(codigo, nombre, ap, am, edad, genero, peso, altura)

  
    lista_pacientes.append(paciente)
    print(paciente)
    

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
    
    paciente_actual = None 
    
    def realizar_busqueda():
        nonlocal paciente_actual
        id_a_buscar = iDbuscar.get()
        for paciente in lista_pacientes:
            if paciente.codigo == id_a_buscar:
                paciente_actual = paciente
                nomValor.delete(0, 'end')
                nomValor.insert(0, paciente.nombre)
                apValor.delete(0, 'end')
                apValor.insert(0, paciente.ap)
                amValor.delete(0, 'end')
                amValor.insert(0, paciente.am)
                edadValor.delete(0, 'end')
                edadValor.insert(0, paciente.edad)
                pesoValor.delete(0, 'end')
                pesoValor.insert(0, paciente.peso)
                alturaValor.delete(0, 'end')
                alturaValor.insert(0, paciente.altura)
                imc = paciente_actual.calcular_imc()
                imcLabel.config(text=f"IMC: {imc:.2f}")
                gen_combobox.set(paciente.genero)
                return
        messagebox.showinfo("Búsqueda", "No se encontró paciente con ese ID")

    def modificar_paciente():
        nonlocal paciente_actual
        if paciente_actual:
            paciente_actual.nombre = nomValor.get()
            paciente_actual.ap = apValor.get()
            paciente_actual.am = amValor.get()
            paciente_actual.edad = edadValor.get()
            paciente_actual.genero = gen_combobox.get()
            paciente_actual.peso = pesoValor.get()
            paciente_actual.altura = alturaValor.get()
            messagebox.showinfo("Modificación", "Datos del paciente actualizados")
        else:
            messagebox.showwarning("Atención", "Primero busca y selecciona un paciente")
        
    Label(ventana_emergente, text="Por favor ingresa el ID del paciente a buscar: ", font="arial 13", bg="#326273", fg="#fff").place(x=20, y=20)
    
    Label(ventana_emergente, text='Nombre', font=23, bg="#326273", fg="#fff").place(x=50, y=100)
    Label(ventana_emergente, text='Apellido paterno', font=23, bg="#326273", fg="#fff").place(x=40, y=150)
    Label(ventana_emergente, text='Apellido materno', font=23, bg="#326273", fg="#fff").place(x=40, y=200)
    Label(ventana_emergente, text='Edad', font=23, bg="#326273", fg="#fff").place(x=360, y=100)
    Label(ventana_emergente, text='Género', font=23, bg="#326273", fg="#fff").place(x=360, y=200)

    Label(ventana_emergente, text='Peso en kg', font=23, bg="#326273", fg="#fff").place(x=140, y=270)
    Label(ventana_emergente, text='Altura en cm', font=23, bg="#326273", fg="#fff").place(x=360, y=270)
    imcLabel = Label(ventana_emergente, text='IMC: -', font=23, bg="#326273", fg="#fff")
    imcLabel.place(x=290, y=300)


# entrada de datos

#cajas
    iDbuscar = tk.Entry(ventana_emergente, width=12, bd=2, font=20)
    iDbuscar.place(x=400, y=20)
    nomValor = tk.Entry(ventana_emergente, width=12, bd=2, font=20)
    nomValor.place(x=200, y=100)
    apValor = tk.Entry(ventana_emergente, width=12, bd=2, font=20)
    apValor.place(x=200, y=150)
    amValor = tk.Entry(ventana_emergente, width=12, bd=2, font=20)
    amValor.place(x=200, y=200)
    edadValor = tk.Entry(ventana_emergente, width=5, bd=2, font=20)
    edadValor.place(x=440, y=100)
    pesoValor = tk.Entry(ventana_emergente, width=5, bd=2, font=20)
    pesoValor.place(x=260, y=270)
    alturaValor = tk.Entry(ventana_emergente, width=5, bd=2, font=20)
    alturaValor.place(x=500, y=270)

# combobox género
    gen_combobox = Combobox(ventana_emergente, values=['Masculino', 'Femenino'], font='arial 14', state='r', width=12)
    gen_combobox.place(x=440, y=200)
    
    Button(ventana_emergente, text="Buscar", bg="#326273", fg="white", width=15, height=2, command=realizar_busqueda).place(x=550, y=20)
    Button(ventana_emergente, text="Guardar", bg="#326273", fg="white", width=15, height=2, command=modificar_paciente).place(x=200, y=350)
    Button(ventana_emergente, text="Salir", bg="#326273", fg="white", width=15, height=2, command=lambda: ventana_emergente.destroy()).place(x=540, y=350)
    


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
codValor = tk.Entry(root, width=12, bd=2, font=20)
codValor.place(x=200, y=50)
nomValor = tk.Entry(root, width=10, bd=2, font=20)
nomValor.place(x=200, y=100)
apValor = tk.Entry(root, width=12, bd=2, font=20)
apValor.place(x=200, y=150)
amValor = tk.Entry(root, width=12, bd=2, font=20)
amValor.place(x=200, y=200)
edadValor = tk.Entry(root, width=5, bd=2, font=20)
edadValor.place(x=440, y=100)
pesoValor = tk.Entry(root, width=5, bd=2, font=20)
pesoValor.place(x=260, y=270)
alturaValor = tk.Entry(root, width=5, bd=2, font=20)
alturaValor.place(x=500, y=270)

# combobox género
gen_combobox = Combobox(root, values=['Masculino', 'Femenino'], font='arial 14', state='r', width=12)
gen_combobox.place(x=440, y=200)



Button(root, text="Guardar", bg="#326273", fg="white", width=15, height=2, command=enviar).place(x=100, y=350)
Button(root, text="Limpiar", bg="#326273", fg="white", width=15, height=2, command=limpiar).place(x=390, y=350)
Button(root, text="Salir", bg="#326273", fg="white", width=15, height=2, command=lambda: root.destroy()).place(x=540, y=350)
Button(root, text="Buscar", bg="#326273", fg="white", width=15, height=2, command=buscar).place(x=250, y=350)

root.mainloop()
