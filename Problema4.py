class Autor:
    def __init__(self, nombre_completo, nacionalidad):
        self.nombre_completo = nombre_completo
        self.nacionalidad = nacionalidad

class Editorial:
    def __init__(self, nombre, ciudad, estado, pais, website):
        self.nombre = nombre
        self.ciudad = ciudad
        self.estado = estado
        self.pais = pais
        self.website = website

class Libro:
    def __init__(self, titulo, autores, editorial, fecha_publicacion, descripcion):
        self.titulo = titulo
        self.autores = autores  # Lista de objetos Autor
        self.editorial = editorial  # Objeto Editorial
        self.fecha_publicacion = fecha_publicacion  # mes/año
        self.descripcion = descripcion
        self.nivel_avance = 0  # Porcentaje de avance de lectura
        self.anotaciones = []  # Lista de anotaciones

    def leer(self, porcentaje):
        self.nivel_avance += porcentaje
        if self.nivel_avance > 100:
            self.nivel_avance = 100

    def agregar_anotacion(self, texto):
        anotacion = Anotacion(texto)
        self.anotaciones.append(anotacion)

    def ver_anotaciones(self):
        return [anotacion.texto for anotacion in self.anotaciones]

class Anotacion:
    def __init__(self, texto):
        self.texto = texto

class Usuario:
    def __init__(self, identificacion, nombre_completo, tipo):
        self.identificacion = identificacion
        self.nombre_completo = nombre_completo
        self.tipo = tipo  # Profesor o Estudiante
        self.libro_actual = None
        self.lista_libros = []  # Lista de objetos ListaLibros

    def acceder_libro(self, libro):
        if self.libro_actual is None:
            self.libro_actual = libro
        else:
            print(f"El usuario ya tiene un libro en uso: {self.libro_actual.titulo}")

    def cerrar_libro(self):
        self.libro_actual = None

    def crear_lista_libros(self, tema):
        lista_libros = ListaLibros(tema)
        self.lista_libros.append(lista_libros)
        return lista_libros

    def hacer_anotacion(self, texto):
        if self.libro_actual:
            self.libro_actual.agregar_anotacion(texto)
        else:
            print("No hay libro abierto para hacer una anotación.")

    def ver_anotaciones(self):
        if self.libro_actual:
            return self.libro_actual.ver_anotaciones()
        else:
            print("No hay libro abierto para ver anotaciones.")

class ListaLibros:
    def __init__(self, tema):
        self.tema = tema
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def ver_libros(self):
        return [libro.titulo for libro in self.libros]

# Ingreso de datos
autor1 = Autor("Gabriel García Márquez", "Colombiana")
autor2 = Autor("J.K. Rowling", "Británica")
autor3 = Autor("Isaac Asimov", "Rusa-Estadounidense")

editorial1 = Editorial("Editorial Sudamericana", "Buenos Aires", "BA", "Argentina", "www.sudamericana.com")
editorial2 = Editorial("Bloomsbury", "Londres", "Inglaterra", "Reino Unido", "www.bloomsbury.com")

libro1 = Libro("Cien años de soledad", [autor1], editorial1, "06/1967", "Una novela sobre la familia Buendía.")
libro2 = Libro("Harry Potter y la Piedra Filosofal", [autor2], editorial2, "06/1997", "El primer libro de la saga de Harry Potter.")
libro3 = Libro("Fundación", [autor3], editorial2, "05/1951", "Una saga sobre el futuro de la civilización galáctica.")
libro4 = Libro("El amor en los tiempos del cólera", [autor1], editorial1, "09/1985", "Una historia de amor en tiempos difíciles.")
libro5 = Libro("Harry Potter y la Cámara Secreta", [autor2], editorial2, "07/1998", "El segundo libro de la saga de Harry Potter.")

usuario1 = Usuario("12345", "Juan Pérez", "Estudiante")
usuario2 = Usuario("67890", "María Gómez", "Profesor")

# Accediendo a libros
usuario1.acceder_libro(libro1)
usuario2.acceder_libro(libro2)

# Listas de libros según tema
lista_fantasia = usuario1.crear_lista_libros("Fantasía")
lista_ciencia_ficcion = usuario2.crear_lista_libros("Ciencia Ficción")

# Se agregan libros a las listas
lista_fantasia.agregar_libro(libro2)
lista_fantasia.agregar_libro(libro5)
lista_ciencia_ficcion.agregar_libro(libro3)

# Se hace una anotación
usuario1.hacer_anotacion("Este pasaje es muy importante.")

# Se cierra el libro
usuario1.cerrar_libro()

print("Anotaciones de Usuario1 en el libro:")
print(usuario1.ver_anotaciones())

print("\nLista de libros de fantasía de Usuario1:")
print(lista_fantasia.ver_libros())

print("\nLista de libros de ciencia ficción de Usuario2:")
print(lista_ciencia_ficcion.ver_libros())
