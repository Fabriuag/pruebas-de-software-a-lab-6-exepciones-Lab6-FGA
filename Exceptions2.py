class MyException(Exception):
    """Excepción personalizada para reglas propias del programa."""
    pass


class ExceptionsDemo:

    def divide(self, a, b):
        try:
            result = a / b
            print("Division result:", result)
        except ZeroDivisionError:
            print("ZeroDivisionError detectado: no se puede dividir entre cero.")
        except TypeError:
            print("TypeError detectado: los operandos deben ser numéricos.")

    def access_list(self, lst, index):
        try:
            print("Element:", lst[index])
        except IndexError:
            print("IndexError detectado: el índice", index, "está fuera de rango.")
        except TypeError:
            print("TypeError detectado: el objeto no es una lista indexable.")

    def access_dict(self, dic, key):
        try:
            print("Value:", dic[key])
        except KeyError:
            print("KeyError detectado: la clave", repr(key), "no existe.")
        except TypeError:
            print("TypeError detectado: el objeto no es un diccionario.")

    def read_file(self, filename):
        try:
            with open(filename, "r") as f:
                content = f.read()
                print(content)
        except FileNotFoundError:
            print("FileNotFoundError detectado: no existe el archivo", filename)
        except IOError:
            print("IOError detectado: error de lectura en", filename)

    def access_attribute(self, obj):
        try:
            print(obj.tnonexistent_attribue)
        except AttributeError:
            print("AttributeError detectado: el objeto no tiene ese atributo.")

    def check_positive(self, number):
        try:
            if number < 0:
                raise MyException("The number must be positive.")
            print("Valid number:", number)
        except MyException as e:
            print("MyException detectada:", e)


if __name__ == "__main__":

    demo = ExceptionsDemo()

    demo.divide(10, 0)
    demo.divide("10", 2)

    demo.access_list([1, 2, 3], 5)
    demo.access_list(1, 0)

    demo.access_dict({"a": 1, "b": 2, "c": 3}, "d")
    demo.access_dict("not_a_dict", "b")

    demo.read_file("text_2.txt")
    demo.read_file("text.txt")

    demo.access_attribute(object())

    demo.check_positive(-5)

    print("Fin del programa: el flujo del main continuó hasta el final.")