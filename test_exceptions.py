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
        demo.access_atribute(demofake)      

@pytest.mark.wip
def test_my_exception_error():
    demo = ExceptionsDemo()
    with pytest.raises(MyException):
        demo.check_positive(-3)      
