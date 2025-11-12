#Este es un ejercicio de POO, voy a crear una bilbioteca 

class libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        return f"{self.titulo} de {self.autor}  (isbn: {self.isbn}) {'disponible' if self.disponible else 'No disponible'}"

    def usuario(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuarios = id_usuario
        self.libros_alquilados = []

    def alquilar_libro(self, libro):
        if libro.disponible:
            libro.disponible = False
            self.libros_alquilados.append(libro)
            print(f"{self.nombre} a alquilado el libro {self.titulo}")
        else:
            print(f" No se pude alguilar {libro.titulo} el libro no está disponible")
        
    def devolver_libro(self, libro):
        if libro in self.libros_alquilados:
            libro.disponible = True    
            self.libros_alquilados.remove(libro)
            print(f"{self.nombre} a devuelto el libro {libro.titulo}")
        else:
            print(f"{self.nombre} no tiene {libro.titulo} para devolver")

class biblioteca:
    def __init_(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)    

    def registrar_un_usuario(self, usuario):
        self.usuarios.append(libro)    
        
    def mostrar_libros_disponibles(self):
        print("libros disponibles en la biblioteca: ")
        for libro in self.libros:
            if libro.disponible:
                print(libro)


# Ejemplo de uso

if __name__ == "__main__":
 
    # Crear biblioteca
    biblioteca = biblioteca()

    # Agregar libros a la biblioteca
    libro1 = libro("Cien años de soledad", "Gabriel García Márquez", "1234567890")
    libro2 = libro("1984", "George Orwell", "0987654321")
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

# Registrar usuarios

    usuario1 = usuario("Alice", "U001")
    usuario2 = usuario("Bob", "U002")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)