

class Node:

    def __init__(self,val):
        self.val = val
        self.nxt = None
        return

class DoubleNode(Node):

    def __init__(self, val):

        return    


def listas():

   
    # Las listas son secuencias de objetos/valores separados por comas
    #  que quedan encasillados por brackets '[' ']'
    # Ej:
    asistencia = ["Juan" , "Jesus" , "Antonio" , "Luis"]
    print(f"Tomemos asistencia para la clase:\n{asistencia}\n")
    
    # Los objetos no necesariamente tienen que ser del mismo tipo.
    # Ej:
    valores_aleatorios = ["a", 10 , 0.75, False]
    print(f"Escupamos basura:\n{valores_aleatorios}\n")
    print()
    print(f"El tipo de 'asistencia' es {type(asistencia)} y el tipo de 'valores_aleatorios' es {type(valores_aleatorios)}'\n")
    
    #las listas pueden crecer o disminuir en tamano dinamicamente mientras se ejecuta el programa
    print(f"Tamano de asistencia: {len(asistencia)}\n")

    #ahora vamos anadir alguien que llego tarde
    tarde = "Andres"
    print(f"{tarde} llego tarde!")

    asistencia.append(tarde)

    # Tomemos asistencia otra vez
    print(f"Tomemos asistencia para la clase(gracias {tarde}!):\n{asistencia}\n")
    
    # verifiquemos de nuevo el tamano
    print(f"Tamano de asistencia: {len(asistencia)}\n")
    

    #Alguien se fue del salon
    #Para eliminar alguien de la lista usamos o eliminamos en base al indice que ocupan en la lista.
    # Nota: Los indices van en el rango: [0, len(lista)-1]
    #  Es decir, si el tamano de la lista es 5 el rango seria: [0,4]
    asistencia.remove('Jesus')

    print(f"Tomemos asistencia para la clase(adios Jesus!):\n{asistencia}\n")
    print(f"Tamano de asistencia: {len(asistencia)}\n")
    return

def sets():

    return

def tuples():
    # Las listas son secuencias de objetos/valores separados por comas
    #  que quedan encasillados por parentesis '(' ')'
    # Ej:
    asistencia = ("Juan" , "Jesus" , "Antonio" , "Luis")
    print(f"Tomemos asistencia para la clase:\n{asistencia}\n")
    
    # Los objetos no necesariamente tienen que ser del mismo tipo.
    # Ej:
    valores_aleatorios = ("a", 10 , 0.75, False)
    print(f"Escupamos basura:\n{valores_aleatorios}\n")
    print()
    print(f"El tipo de 'asistencia' es {type(asistencia)} y el tipo de 'valores_aleatorios' es {type(valores_aleatorios)}'\n")
    
    #las listas pueden crecer o disminuir en tamano dinamicamente mientras se ejecuta el programa
    print(f"Tamano de asistencia: {len(asistencia)}\n")

    #ahora vamos anadir alguien que llego tarde
    tarde = "Andres"
    print(f"{tarde} llego tarde!")

    asistencia.append(tarde)

    # Tomemos asistencia otra vez
    print(f"Tomemos asistencia para la clase(gracias {tarde}!):\n{asistencia}\n")
    
    # verifiquemos de nuevo el tamano
    print(f"Tamano de asistencia: {len(asistencia)}\n")
    

    #Alguien se fue del salon
    #Para eliminar alguien de la lista usamos o eliminamos en base al indice que ocupan en la lista.
    # Nota: Los indices van en el rango: [0, len(lista)-1]
    #  Es decir, si el tamano de la lista es 5 el rango seria: [0,4]
    asistencia.remove('Jesus')

    print(f"Tomemos asistencia para la clase(adios Jesus!):\n{asistencia}\n")
    print(f"Tamano de asistencia: {len(asistencia)}\n")
    return

def main():
    listas()
    return

if __name__ == "__main__":
    main()