
#Clase persona(objeto que el cliente quiere crear haciendo uso del DSL)
class Persona:
    def __init__(self, nombre, apellido, documento):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento

    def __repr__(self):
        return f"Persona({self.nombre} {self.apellido}, doc={self.documento})"

#diccionario que simula mi base de datos
BD = {}

#Parser para crear persona
def crear_persona(tokens):
    try:
        i_nombre = tokens.index("nombre") + 1
        i_apellido = tokens.index("apellido") + 1
        i_doc = tokens.index("documento") + 1

        nombre = tokens[i_nombre].capitalize()
        apellido = tokens[i_apellido].capitalize()
        documento = tokens[i_doc]

        BD[documento] = Persona(nombre, apellido, documento)
        return f"Persona creada: {BD[documento]}"

    except ValueError:
        return "Error en comando crear."
def modificar_persona(tokens):
    try:
        documento = tokens[2]
        atributo = tokens[3]
        valor = tokens[4].capitalize()

        if documento not in BD:
            return "Persona no encontrada."

        persona = BD[documento]
        setattr(persona, atributo, valor)

        return f"Persona modificada: {persona}"

    except:
        return "Error en comando modificar."
def eliminar_persona(tokens):
    documento = tokens[2]

    if documento in BD:
        del BD[documento]
        return f"Persona {documento} eliminada."
    return "Persona no encontrada."
def mostrar_persona(tokens):
    documento = tokens[2]

    if documento in BD:
        return BD[documento]
    return "Persona no encontrada."

#Motor que ejecuta las operaciones sobre persona
def ejecutar_comando(comando):
    #lexer, divide las instrucciones en tokens
    tokens = comando.lower().split()
    if tokens[0] == "crear":
        return crear_persona(tokens)
    elif tokens[0] == "modificar":
        return modificar_persona(tokens)
    elif tokens[0] == "eliminar":
        return eliminar_persona(tokens)
    elif tokens[0] == "mostrar":
        return mostrar_persona(tokens)
    else:
        return "Comando no reconocido."


aux=0
while aux!=1:
    instruccion = input("Ingrese la instrucción a realizar: ")
    print(ejecutar_comando(instruccion))
    aux=int(input("Desea finalizar la ejecucion del programa?\n 1:si\n 2:no\n "))
