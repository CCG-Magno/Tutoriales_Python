# En este modulo se les estara describiendo como crear condiciones,
# para que se utilizan y algunos ejemplos.
# 

def control_de_flujo():
    # el sintaxis a seguir es:
    # if (condicion/equivalencia aqui o un valor booleano):
    # seguido por un nivel de indentacion
    
    # ej:
    # if 4 > 3:# Ojo, los parentesis son opcionales!
    #     pass #hacemos algo si la condicion es certera/veridica
    
    # Nota: 'pass' es una palabra clave en Python que cuando se interpreta no ejecuta una insrtruccion.
    # Es como cuando nosotros leemos una oracion y vemos el punto final.

    # A esta condicion le podemos a~adir una clausula 'else' que se ejecuta cuando la condicion predilecta no se alcanza
    # el sintaxis a seguir es:
    # else: # o alternativamente, else if(condicion aqui):
    # tambien seguido por otro nivel de indentacion.

    # Ahora un ejemplo completo que si ejecuta

    # Toda equivalencia o desigualdad es una condicion
    if 4  < 5:# se reduce a una condicion certera por lo cual se ejecuta lo que esta en su nivel de indentacion.
        print("4 es menor a 5!")
    
    if True:
        print("True siempre se ejecuta!")

    if False:
        # este nunca se ejecuta
        pass
    else:
        print("Una condicion 'if' falsa siempre ejecutara la clausula 'else'.")

    # Alternativamente

    if None:
        pass
    else:
        print("Cualquier condicion 'None' se trata como falso!")
    
    if not None:
        print("La negacion de 'None' es 'True'!")

    if None or True:
        print("Cualquier condicion con clausula 'or' con una parte que sea veridica, siempre se ejecutara!")

    if True and False:
        pass
    else:
        print("Cualquier condicion con clausula 'and' con una parte que sea falsa, nunca se ejecutara!")


    return

def main():
    control_de_flujo()
    return


if __name__ == "__main__":
    main() 