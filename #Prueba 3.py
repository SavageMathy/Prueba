#Prueba 3
import json
DiccionarioLibros = {}
Libros = []
Autores = []
Generos = ["acción","aventura","ciencia ficción","fantasía","ciencia","cocina"]
Precios = []
LibroVendido = []
Total = 0

def RegistroLibro():
        global DiccionarioLibros
        try:
            Titulo = input("Ingrese titulo del libro: ")
            Autor = input("Ingrese autor: ")
            print(Generos)
            Genero = input("Ingese genero del libro: ")
            if Genero not in Generos:
                print(Generos)
                Genero = input("Ingese un genero válido de los listdos\n")
            Precio = (input("Ingrese precio del libro: "))
            if Titulo == "" or Autor == "" or Genero == "" or Precio == "":
                print("Los campos no pueden estar vacíos")
                return
            else:
                DiccionarioLibros.append({
                    "Titulo": Titulo,
                    "Autor": Autor,
                    "Genero": Genero,
                    "Precio": Precio
                })
            return(DiccionarioLibros)
        except:
            print("Error de escritura")

def ListarTodos():
    for i in range(len(DiccionarioLibros)):
        try:
            print(f"{DiccionarioLibros}")
        except:
            print("Error en datos")

def RegistrarVenta():
    global contador
    global Generos
    try:
        contador = 0
        TituloVenta = input("Ingrese titulo del libro: ")
        PrecioVenta = int(input("Ingese precio unitario: "))
        CantidadVender = int(input("Ingrese cantidad a vender: "))
        for TituloVenta in Libros:
            if TituloVenta == Libros:
                contador += 1
        if CantidadVender < contador:
            print("La cantidad a vender supera el stock")
            return
        else:
            Total = PrecioVenta * CantidadVender
            print(f"El total de la venta es: {Total}")
            return(Total)
    except:
        print("Error en lectura de datos")
def ImprimirVentas(genero):
    TotalPlatino = Total
    print(f"Libros vendidos de {genero}: {contador}\nTotal generado: {TotalPlatino} ")

def GenerarTXT(genero):
    with open({genero}.txt,"w"):
        json.write(ImprimirVentas) #variable de la fn

while True:
    option = int(input(f"Menu\n(1)registrar libro\n(2)Litar todos los libros\n(3)Registrar Venta\n(4)Imprimir reporte de ventas\n(5)Generar TXT\n(6)Cerrar programa\nDigite su opción: "))
    try:
        if option == 1:
            print(RegistroLibro())
        elif option == 2:
            print(ListarTodos())
        elif option == 3:
            print(RegistrarVenta())
        elif option == 4:
            print(ImprimirVentas())
        elif option == 5:
            print(GenerarTXT())
        elif option == 6:
            break
        else:
            print("opción inválida")
    except:
        print("Error en los datos")
