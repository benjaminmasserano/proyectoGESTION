import json
import os
import platform
from datetime import datetime

def limpiar_pantalla():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

class Persona:
    def __init__(self, id_persona, nombre, apellido, telefono, email):
        self.id_persona = id_persona
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

    def to_dict(self):
        return {
            "id_persona": self.id_persona,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "telefono": self.telefono,
            "email": self.email
        }

    @staticmethod
    def from_dict(data):
        return Persona(
            data["id_persona"],
            data["nombre"],
            data["apellido"],
            data["telefono"],
            data["email"]
        )

    def __str__(self):
        return f"ID: {self.id_persona}, Nombre: {self.nombre}, Apellido: {self.apellido}, Teléfono: {self.telefono}, Email: {self.email}"

class Proveedor:
    def __init__(self, id_proveedor, nombre, telefono, email, localidad):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.localidad = localidad

    def to_dict(self):
        return {
            "id_proveedor": self.id_proveedor,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "email": self.email,
            "localidad": self.localidad
        }

    @staticmethod
    def from_dict(data):
        return Proveedor(
            data["id_proveedor"],
            data["nombre"],
            data["telefono"],
            data["email"],
            data["localidad"]
        )

    def __str__(self):
        return f"ID: {self.id_proveedor}, Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}, Localidad: {self.localidad}"

class Mercaderia:
    def __init__(self, id_mercaderia, nombre, id_proveedor, detalle, fragmentacion):
        self.id_mercaderia = id_mercaderia
        self.nombre = nombre
        self.id_proveedor = id_proveedor
        self.detalle = detalle
        self.fragmentacion = fragmentacion

    def to_dict(self):
        return {
            "id_mercaderia": self.id_mercaderia,
            "nombre": self.nombre,
            "id_proveedor": self.id_proveedor,
            "detalle": self.detalle,
            "fragmentacion": self.fragmentacion
        }

    @staticmethod
    def from_dict(data):
        return Mercaderia(
            data["id_mercaderia"],
            data["nombre"],
            data["id_proveedor"],
            data["detalle"],
            data["fragmentacion"]
        )

    def __str__(self):
        return f"ID: {self.id_mercaderia}, Nombre: {self.nombre}, ID Proveedor: {self.id_proveedor}, Detalle: {self.detalle}, Fragmentación: {self.fragmentacion}"

class Almacen:
    def __init__(self, id_mercaderia, cantidad, fecha_entrada):
        self.id_mercaderia = id_mercaderia
        self.cantidad = cantidad
        self.fecha_entrada = fecha_entrada

    def to_dict(self):
        return {
            "id_mercaderia": self.id_mercaderia,
            "cantidad": self.cantidad,
            "fecha_entrada": self.fecha_entrada
        }

    @staticmethod
    def from_dict(data):
        return Almacen(
            data["id_mercaderia"],
            data["cantidad"],
            data["fecha_entrada"]
        )

    def __str__(self):
        return f"ID Mercadería: {self.id_mercaderia}, Cantidad: {self.cantidad}, Fecha de Entrada: {self.fecha_entrada}"

def cargar_datos(ruta_archivo):
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo:
            datos = json.load(archivo)
            personas = [Persona.from_dict(persona) for persona in datos.get("personas", [])]
            proveedores = [Proveedor.from_dict(proveedor) for proveedor in datos.get("proveedores", [])]
            mercaderias = [Mercaderia.from_dict(mercaderia) for mercaderia in datos.get("mercaderias", [])]
            almacenes = [Almacen.from_dict(almacen) for almacen in datos.get("almacenes", [])]
            return personas, proveedores, mercaderias, almacenes
    return [], [], [], []

def guardar_datos(personas, proveedores, mercaderias, almacenes, ruta_archivo):
    datos = {
        "personas": [persona.to_dict() for persona in personas],
        "proveedores": [proveedor.to_dict() for proveedor in proveedores],
        "mercaderias": [mercaderia.to_dict() for mercaderia in mercaderias],
        "almacenes": [almacen.to_dict() for almacen in almacenes]
    }
    with open(ruta_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    print("Datos guardados exitosamente.")

def imprimir_lista_personas(personas):
    if personas:
        print("\nLista de personas:")
        for persona in personas:
            print(persona)
    else:
        print("\nNo hay personas registradas.")

def imprimir_lista_proveedores(proveedores):
    if proveedores:
        print("\nLista de proveedores:")
        for proveedor in proveedores:
            print(proveedor)
    else:
        print("\nNo hay proveedores registrados.")

def imprimir_lista_mercaderias(mercaderias):
    if mercaderias:
        print("\nLista de mercaderías:")
        for mercaderia in mercaderias:
            print(mercaderia)
    else:
        print("\nNo hay mercaderías registradas.")

def imprimir_estado_almacen(almacenes, mercaderias):
    if almacenes:
        print("\nEstado del Almacén:")
        for almacen in almacenes:
            mercaderia = next((m for m in mercaderias if m.id_mercaderia == almacen.id_mercaderia), None)
            if mercaderia:
                print(f"ID Mercadería: {almacen.id_mercaderia}, Nombre: {mercaderia.nombre}, Cantidad: {almacen.cantidad}, Fecha de Entrada: {almacen.fecha_entrada}")
            else:
                print(f"ID Mercadería: {almacen.id_mercaderia} (No encontrada), Cantidad: {almacen.cantidad}, Fecha de Entrada: {almacen.fecha_entrada}")
    else:
        print("\nNo hay registros en el almacén.")
    input("Presiona Enter para continuar...")

def seleccionar_proveedor(proveedores, id_proveedor_counter, nombre_mercaderia):
    if not proveedores:
        print("No hay proveedores registrados. Primero debes agregar un proveedor.")
        return None
    
    while True:
        print("\nLista de proveedores:")
        for proveedor in proveedores:
            print(proveedor)
        
        id_proveedor = input("\nIntroduce el ID del proveedor (o escribe 'nuevo' para agregar uno nuevo): ").strip()
        
        if id_proveedor.lower() == 'nuevo':
            limpiar_pantalla()
            nombre = input("Nombre del proveedor: ").strip()
            telefono = input("Teléfono del proveedor: ").strip()
            email = input("Email del proveedor: ").strip()
            localidad = input("Localidad del proveedor: ").strip()
            
            nuevo_proveedor = Proveedor(
                id_proveedor_counter,
                nombre,
                telefono,
                email,
                localidad
            )
            proveedores.append(nuevo_proveedor)
            limpiar_pantalla()
            print(f"Mercadería en proceso:\nNombre: {nombre_mercaderia}\nProveedor añadido con ID: {id_proveedor_counter}")
            id_proveedor_counter += 1
            return nuevo_proveedor.id_proveedor
        else:
            try:
                id_proveedor = int(id_proveedor)
                proveedor = next((p for p in proveedores if p.id_proveedor == id_proveedor), None)
                if proveedor:
                    return proveedor.id_proveedor
                else:
                    print("ID de proveedor no encontrado. Intenta de nuevo.")
            except ValueError:
                print("ID de proveedor inválido. Debe ser un número entero.")

def agregar_mercaderia(mercaderias, proveedores, almacenes, id_mercaderia_counter, id_proveedor_counter):
    nombre = input("Nombre de la mercadería: ").strip()
    id_proveedor = seleccionar_proveedor(proveedores, id_proveedor_counter, nombre)
    detalle = input("Detalle de la mercadería: ").strip()
    fragmentacion = input("Fragmentacion:").strip()
    
    nueva_mercaderia = Mercaderia(id_mercaderia_counter, nombre, id_proveedor, detalle, fragmentacion)
    mercaderias.append(nueva_mercaderia)
    
    print(f"Mercadería '{nombre}' agregada con ID: {id_mercaderia_counter}")
    return id_mercaderia_counter + 1

def agregar_entrada_mercaderia(almacenes, mercaderias):
    print("Seleccione la mercadería a ingresar:")
    imprimir_lista_mercaderias(mercaderias)
    
    id_mercaderia = int(input("ID de la mercadería: ").strip())
    cantidad = int(input("Cantidad a agregar: ").strip())
    fecha_entrada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Buscar si ya existe el registro en el almacén
    almacen = next((a for a in almacenes if a.id_mercaderia == id_mercaderia), None)
    if almacen:
        almacen.cantidad += cantidad
        almacen.fecha_entrada = fecha_entrada
    else:
        nuevo_almacen = Almacen(id_mercaderia, cantidad, fecha_entrada)
        almacenes.append(nuevo_almacen)
    
    print("Entrada de mercadería registrada exitosamente.")

def agregar_salida_mercaderia(almacenes, mercaderias):
    # Imprimir estado del almacén antes de seleccionar la mercadería
    print("\nEstado actual del almacén:")
    imprimir_estado_almacen(almacenes, mercaderias)
    
    id_mercaderia = int(input("ID de la mercadería a retirar: ").strip())
    cantidad = int(input("Cantidad a retirar: ").strip())

    # Buscar si ya existe el registro en el almacén
    almacen = next((a for a in almacenes if a.id_mercaderia == id_mercaderia), None)
    if almacen:
        if almacen.cantidad >= cantidad:
            almacen.cantidad -= cantidad
            print("Salida de mercadería registrada exitosamente.")
        else:
            print("Cantidad insuficiente en el almacén.")
    else:
        print("Mercadería no encontrada en el almacén.")

def main():
    ruta_archivo = r'C:\Users\sysadmin\OneDrive\Escritorio\XUBA PRUEBA\base_datos.json'
    
    personas, proveedores, mercaderias, almacenes = cargar_datos(ruta_archivo)
    id_persona_counter = max([persona.id_persona for persona in personas], default=0) + 1
    id_proveedor_counter = max([proveedor.id_proveedor for proveedor in proveedores], default=0) + 1
    id_mercaderia_counter = max([mercaderia.id_mercaderia for mercaderia in mercaderias], default=0) + 1

    while True:
        limpiar_pantalla()
        print("Menú:")
        print("1. Agregar persona")
        print("2. Imprimir lista de personas")
        print("3. Agregar proveedor")
        print("4. Imprimir lista de proveedores")
        print("5. Agregar mercadería")
        print("6. Imprimir lista de mercaderías")
        print("7. Consultar estado del almacén")
        print("8. Agregar entrada de mercadería")
        print("9. Agregar salida de mercadería")
        print("10. Salir")
        
        opcion = input("Selecciona una opción (1/2/3/4/5/6/7/8/9/10): ").strip()
        
        if opcion == '1':
            limpiar_pantalla()
            nombre = input("Nombre: ").strip()
            apellido = input("Apellido: ").strip()
            telefono = input("Teléfono: ").strip()
            email = input("Email: ").strip()
            
            nueva_persona = Persona(id_persona_counter, nombre, apellido, telefono, email)
            personas.append(nueva_persona)
            
            id_persona_counter += 1
        elif opcion == '2':
            limpiar_pantalla()
            imprimir_lista_personas(personas)
            input("Presiona Enter para continuar...")
        elif opcion == '3':
            limpiar_pantalla()
            nombre = input("Nombre: ").strip()
            telefono = input("Teléfono: ").strip()
            email = input("Email: ").strip()
            localidad = input("Localidad: ").strip()
            
            nuevo_proveedor = Proveedor(id_proveedor_counter, nombre, telefono, email, localidad)
            proveedores.append(nuevo_proveedor)
            
            id_proveedor_counter += 1
        elif opcion == '4':
            limpiar_pantalla()
            imprimir_lista_proveedores(proveedores)
            input("Presiona Enter para continuar...")
        elif opcion == '5':
            limpiar_pantalla()
            id_mercaderia_counter = agregar_mercaderia(mercaderias, proveedores, almacenes, id_mercaderia_counter, id_proveedor_counter)
        elif opcion == '6':
            limpiar_pantalla()
            imprimir_lista_mercaderias(mercaderias)
            input("Presiona Enter para continuar...")
        elif opcion == '7':
            limpiar_pantalla()
            imprimir_estado_almacen(almacenes, mercaderias)
        elif opcion == '8':
            limpiar_pantalla()
            agregar_entrada_mercaderia(almacenes, mercaderias)
        elif opcion == '9':
            limpiar_pantalla()
            agregar_salida_mercaderia(almacenes, mercaderias)
        elif opcion == '10':
            guardar_datos(personas, proveedores, mercaderias, almacenes, ruta_archivo)
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 10.")

if __name__ == "__main__":
    main()

