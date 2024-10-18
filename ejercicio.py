# Clase que representa a un paciente
class Paciente:
    def __init__(self, nombre, cedula, genero, servicio):
        # Atributos privados del paciente
        self.__nombre = nombre
        self.__cedula = cedula
        self.__genero = genero
        self.__servicio = servicio

    # Método para obtener la cédula del paciente
    def get_cedula(self):
        return self.__cedula

    # Método para obtener todos los datos del paciente como una cadena formateada
    def get_datos(self):
        return f"""
    Datos del paciente en la búsqueda:
    Nombre: {self.__nombre}
    Cédula: {self.__cedula}
    Género: {self.__genero}
    Servicio: {self.__servicio}
    """

    # Método especial para convertir el objeto a una cadena cuando se imprime
    def __str__(self):
        return f"Nombre: {self.__nombre}, Cédula: {self.__cedula}, Género: {self.__genero}, Servicio: {self.__servicio}"

# Clase que representa el sistema de gestión de pacientes
class Sistema:
    def __init__(self):
        # Lista privada para almacenar los objetos de tipo Paciente
        self.__lista_pacientes = []

    # Método para ingresar un nuevo paciente al sistema
    def ingresar_paciente(self, paciente):
        # Agregar el paciente a la lista
        self.__lista_pacientes.append(paciente)
        return True

    # Método para buscar un paciente por su cédula
    def get_datos_paciente(self, c):
        # Recorrer la lista de pacientes para encontrar el que tiene la cédula dada
        for p in self.__lista_pacientes:
            if c == p.get_cedula():
                return p  # Retorna el paciente si lo encuentra
        return None  # Retorna None si no se encuentra

    # Método para imprimir la cantidad de pacientes en el sistema
    def get_cantidad_pacientes(self):
        print("En el sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes")
    
    # Método para verificar si un paciente ya existe en el sistema por su cédula
    def verificar_existencia_paciente(self, ced):
        # Recorre la lista y compara la cédula
        for p in self.__lista_pacientes:
            if p.get_cedula() == ced:
                return True  # Retorna True si encuentra la cédula
        return False  # Retorna False si no la encuentra

# Función que genera un menú de servicios válidos a partir de una lista
def fill_menu_servicio(lista_servicios):
    menu = "Servicios disponibles:\n"
    # Enumerate agrega un contador que se incrementa con cada iteración
    for i, m in enumerate(lista_servicios):
        menu += f"{i}: {m} \n"  # Concatena cada servicio con su índice en el menú
    return menu  # Retorna el menú como una cadena

# Función para regresar al menú principal, esperando que el usuario presione "0"
def opcion_regresar_menu_principal():
    while True:
        o = input("Presione 0 (cero) para regresar al menú principal\n")
        if o == "0":
            break  # Sale del bucle si el usuario presiona "0"

# Función para validar si una cédula es numérica
def validar_cedula(ced):
    if ced.isdigit():  # Verifica si la cédula contiene solo dígitos
        return True
    print("Error: La cédula deben ser dígitos")  # Muestra un error si no es numérica
    return False

# Función principal que ejecuta el programa
def main():
    # Crea una instancia de la clase Sistema
    sis = Sistema()
    
    # Se crean algunos pacientes y se agregan al Sistema, en la lista de pacientes
    sis.ingresar_paciente(Paciente("Pedro Gómez", 123456, "Masculino", "Hospitalización"))
    sis.ingresar_paciente(Paciente("Laura Restrepo", 123457, "Femenino", "Hospitalización"))
    sis.ingresar_paciente(Paciente("Miguel Mejía", 123458, "Masculino", "Laboratorio"))
    
    flag = True  # Bandera para controlar el flujo del programa
    # Lista de servicios válidos
    servicios_validos = [
        "Ayudas diagnósticas", "Cuidados intensivos", "Urgencias", "Odontología",
        "Cirugía", "Hospitalización", "Laboratorio"
    ]
    
    # Menú principal del sistema
    menu_main = """
    Menú:
    ---------------
    
    1. Ingresar nuevo paciente
    2. Buscar y ver Paciente
    3. Ver número total de pacientes
    4: Salir
    
    Ingrese el número: """
    
    # Genera el menú de servicios válidos
    menu_servicios = fill_menu_servicio(servicios_validos)
    
    # Bucle principal del programa que muestra el menú
    while True:
        opcion = int(input(menu_main))  # Muestra el menú principal y lee la opción del usuario
        if opcion == 1:  # Opción para ingresar un nuevo paciente
            print("Formulario de Paciente Nuevo")
            while True:  # Bucle para validar la cédula ingresada
                cedula = input("Ingrese cédula: ")
                
                if validar_cedula(cedula):  # Si es válida, convierte a entero y verifica existencia
                    cedula = int(cedula)
                    if not sis.verificar_existencia_paciente(cedula):  # Verifica si el paciente no existe
                        break
                    else:
                        print("Ya existe el paciente.\n")
            
            nombre = input("Ingrese nombre: ")  # Pide el nombre del paciente
            
            while True:  # Bucle para validar el género ingresado
                genero = input("Ingrese género(M/F ó Masculino/Femenino): ").lower()
                if genero in ["m", "f", "masculino", "femenino"]:
                    if genero == "m" or genero == "masculino":
                        genero = "Masculino"
                    elif genero == "f" or genero == "femenino":
                        genero = "Femenino"
                    break
                else:
                    print("Error: Género no válido. Debe ser M, F, Masculino o Femenino.")
            
            while True:  # Bucle para seleccionar un servicio válido
                servicio = int(input(menu_servicios + "\nIngrese el número de Servicio: "))
                if 0 <= servicio <= 6:  # Asegura que el servicio esté en el rango correcto
                    servicio = servicios_validos[servicio]
                    break
                else:
                    print(f"Error: Servicio no válido. Ingrese número entre 0 y {len(servicios_validos)-1}")
            
            # Crea un nuevo paciente con los datos ingresados
            pac = Paciente(nombre, cedula, genero, servicio)
            if sis.ingresar_paciente(pac):  # Intenta agregar el paciente al sistema
                print("Paciente ingresado con éxito.\n")     
            else:
                print("No se pudo ingresar el paciente.\n")
        
        elif opcion == 2:  # Opción para buscar y ver los datos de un paciente por cédula
            c = input("Ingrese la cédula a buscar: ")
            if validar_cedula(c):  # Valida que la cédula sea numérica
                c = int(c)
                p = sis.get_datos_paciente(c)  # Busca el paciente por cédula
                if p:
                    print("Datos del paciente: ")
                    print(p.get_datos())  # Muestra los datos del paciente encontrado
                else:
                    print("Paciente no encontrado.\n")        
        
        elif opcion == 3:  # Opción para ver el número total de pacientes en el sistema
            sis.get_cantidad_pacientes()  # Llama al método para imprimir la cantidad de pacientes
            print()
        
        elif opcion == 4:  # Opción para salir del programa
            print("Saliendo del sistema.")
            break  # Sale del bucle principal
        
        else:
            print("Opción no válida. Intente de nuevo.\n")
            flag = False  # Indica que hubo un error en la opción
        
        if flag:  # Si no hubo errores, espera a que el usuario presione 0 para volver al menú principal
            opcion_regresar_menu_principal()

# Punto de entrada del programa
if __name__ == "__main__":
    main()

