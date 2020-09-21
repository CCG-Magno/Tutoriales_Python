
def caracteres():
    #Los caracteres son conocidos como strings en Python,
    # En otros lenguajes se conocen como 'char' singular.
    # Los strings son una subclase dentro de las Listas en Python y
    #  difieren en codificacion entre Python 2 y Python 3.
    nombre = "Magno"

    # Los caracteres pueden guardar cualquier tipo de otra variable,
    # pero internamente se reconoceran como "String" no como el typo de la otra variable.
    # Si quisieras obtener el tipo original tendrias que llamar la funcion de ese tipo.
    # Ej: a = "5" -> int(a) devolveria el valor de 5 en tipo entero.(no se escribe la flecha, es solo para dejarles saber que harian para sacar el valor correcto)
    edad = "500"
    altura = "777.7"
    print("Valores de characteres:")
    print(f"El valor {nombre} guardado en la variable 'a' de tipo{type(nombre)}")
    print(f"El valor {altura} guardado en la variable 'a' de tipo{type(altura)}")
    print(f"El valor {edad} guardado en la variable 'a' de tipo{type(edad)}\n\n")
    return

def booleanos():
    a = True
    b = False
    print("Valores de numeros booleanos:")
    print(f"El valor {a} guardado en la variable 'a' de tipo{type(a)}")
    print(f"El valor {b} guardado en la variable 'a' de tipo{type(b)}\n\n")
    return

def flotantes():
    # Esto es un numero tipo precision flotante, no es lo mismo que un numero decimal.
    # Aunque si se tiende a utilizar con el proposito de representar decimales.
    a = 0.25
    print("Valores de numeros flotantes:")
    print(f"El numero {a} guardado en la variable 'a' de tipo{type(a)}\n\n")

    # ej de porque no se deberia tomar como un numero decimal.
    # b = 
    c = 0.333
    b=1/3
    print(f"El numero {b} guardado en la variable 'b' de tipo{type(b)}")
    print(f"El numero {c} guardado en la variable 'c' de tipo{type(c)}\n\n")
    try:
        assert  b == c
    except Exception as e:
        print(f"Hubo un error de asercion cuando se verifica si b es igual a c!\n[!]Error:{e}\n\n")
    return

def enteros():
    # Esto es un entero
    a = 10
    print("Valores de numeros enteros:")
    print(f"El numero {a} guardado en la variable 'a' de tipo{type(a)}\n\n")
    return


def variables():
    enteros()
    flotantes()
    booleanos()
    caracteres()

    return



if __name__ == "__main__":
    variables()