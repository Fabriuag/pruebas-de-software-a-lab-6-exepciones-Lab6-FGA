import pytest
from Exceptions import ExceptionsDemo, MyException
 
@pytest.mark.q
def test_divide_zero():
    demo = ExceptionsDemo()
    with pytest.raises(ZeroDivisionError):
        demo.divide(10,0)
 
@pytest.mark.y
def test_TypeError():
    demo = ExceptionsDemo()
    with pytest.raises(TypeError):
        demo.divide('Tamaulipas',5)
 
@pytest.mark.w
def test_index_error():
    demo = ExceptionsDemo()
    with pytest.raises(IndexError):
        demo.access_list([3,5,4],7)
 
@pytest.mark.e
def test_key_error():
    demo = ExceptionsDemo()
    with pytest.raises(KeyError):
        demo.access_dict({'Manzana': 'Dulce','Limon':'Agrio'},'Tomate')
 
@pytest.mark.r
def test_FileNotFoundError():
    demo = ExceptionsDemo()
    with pytest.raises(FileNotFoundError):
        demo.read_file('frutas.txt')
 
@pytest.mark.t
def test_attribute_error():
    demo = ExceptionsDemo()
    demofake = ExceptionsDemo()
    with pytest.raises(AttributeError):
        demo.access_attribute(demofake)
 
@pytest.mark.wip
def test_my_exception_error():
    demo = ExceptionsDemo()
    with pytest.raises(MyException):
        demo.check_positive(-3)
 
 
# ============================================================
#  PRUEBAS ADICIONALES - Preparación para el examen práctico
# ============================================================
 
# --- Fixture: objeto reutilizable para las pruebas nuevas ---
@pytest.fixture
def demo():
    return ExceptionsDemo()
 
 
# 1) FIXTURE + CAPSYS: camino feliz de check_positive
@pytest.mark.fixture
def test_check_positive_valido(demo, capsys):
    demo.check_positive(8)
    salida = capsys.readouterr()
    assert salida.out == "Valid number: 8\n"
 
 
# 2) CAPSYS: leer un archivo existente e imprimir su contenido
@pytest.mark.capsys
def test_read_file_contenido(demo, capsys):
    demo.read_file("text.txt")
    salida = capsys.readouterr()
    assert "Hola Mundo" in salida.out
 
 
# 3) PARAMETRIZE: varias divisiones válidas en una sola prueba
@pytest.mark.param
@pytest.mark.parametrize("a, b, esperado", [
    (10, 2, 5.0),
    (9, 3, 3.0),
    (-8, 4, -2.0),
    (7, 2, 3.5),
])
def test_divide_parametrizado(demo, capsys, a, b, esperado):
    demo.divide(a, b)
    salida = capsys.readouterr()
    assert salida.out == f"Division result: {esperado}\n"
 
 
# 4) MONKEYPATCH.SETATTR: simular que open() falla por permisos
@pytest.mark.setattr
def test_read_file_permission_error(demo, monkeypatch):
    def open_falso(*args, **kwargs):
        raise PermissionError("Acceso denegado")
 
    monkeypatch.setattr("builtins.open", open_falso)
 
    with pytest.raises(PermissionError, match="Acceso denegado"):
        demo.read_file("text.txt")
 
 
# 5) MONKEYPATCH.DELATTR: el atributo existe y luego se elimina
class ObjetoConAtributo:
    tnonexistent_attribue = "Estoy aquí"
 
@pytest.mark.delattr
def test_access_attribute_delattr(demo, monkeypatch, capsys):
    obj = ObjetoConAtributo()
 
    # Con el atributo presente, se imprime sin error
    demo.access_attribute(obj)
    assert capsys.readouterr().out == "Estoy aquí\n"
 
    # Se elimina el atributo de la clase y ahora debe fallar
    monkeypatch.delattr(ObjetoConAtributo, "tnonexistent_attribue")
    with pytest.raises(AttributeError):
        demo.access_attribute(obj)
 