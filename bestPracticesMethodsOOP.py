class Alumno:
    '''Crea la funcion constructor con atributos vacios'''
    def __init__(self, nombre, apellido_paterno, apellido_materno, no_control, semestre):
        self.__nombre = nombre
        self.__apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno
        self.__no_control = no_control
        self.__semestre = semestre

    # Métodos para establecer los valores
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    # Métodos para obtener los valores
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre

    def get_nombre_completo(self):
        return f"{self.__nombre} {self.__apellido_paterno} {self.__apellido_materno}"

# Ejemplo de uso
# Crea instancia de alumno
# Una instancia es la creacion de un objeto a partir de una clase
alumno1 = Alumno("Milan", "Hernandez", "Hernandez", "123456", 3)

print(f"Nombre: {alumno1.get_nombre()} {alumno1.get_apellido_paterno()} {alumno1.get_apellido_materno()}")
print(f"No. Control: {alumno1.get_no_control()}")
print(f"Semestre: {alumno1.get_semestre()}")
print("Nombre Completo:", alumno1.get_nombre_completo())


# Solo el nombre
registro_alumnos={}
registro_alumnos[0]=alumno1
print(f"Nombre: {registro_alumnos[0].get_nombre()}")


# Bucle para capturar 3 nombres
# Inicializamos un diccionario vacío para almacenar los nombres
nombres_dict = {}

# Bucle para capturar 3 nombres
for i in range(3):
    nombre = input(f"Ingrese el nombre {i + 1}: ")
    apellido_paterno= input(f"Apellido Paterno {i + 1}: ")
    apellido_materno = input(f"Apellido Materno {i + 1}: ")
    no_control = input(f"Numero de control {i + 1}: ")

    nombres_dict[i + 1] = nombre  # Almacenamos el nombre con una clave numérica

# Mostrar los nombres almacenados
print("\nNombres almacenados:")
for clave, valor in nombres_dict.items():
    print(f"{clave}: {valor}")


# Inicializamos un diccionario vacío
alumnos_dict = {}

#Bucle para crear hasta 50 alumnos
for i in range(1, 51):
   nombre = input(f"Ingrese el nombre del alumno {i}: ")
   apellido_paterno = input(f"Ingrese el apellido paterno del alumno {i}: ")
   apellido_materno = input(f"Ingrese el apellido materno del alumno {i}: ")
   no_control = input(f"Ingrese el número de control del alumno {i}: ")
   semestre = int(input(f"Ingrese el semestre del alumno {i}: "))

# Creamos un objeto Alumno y lo almacenamos en el diccionario
   alumno = Alumno(nombre, apellido_paterno, apellido_materno, no_control, semestre)
   alumnos_dict[i] = alumno

# Mostrar los alumnos almacenados
print("\nAlumnos almacenados:")
for clave, alumno in alumnos_dict.items():
    print(f"{clave}: {alumno.get_nombre()} {alumno.get_apellido_paterno()} {alumno.get_apellido_materno()} - No. Control: {alumno.get_no_control()} - Semestre: {alumno.get_semestre()}")