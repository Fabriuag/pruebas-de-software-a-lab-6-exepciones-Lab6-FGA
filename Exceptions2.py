class MyException(Exception):
    pass

class ExceptionsDemo:
    
    def divide(self, a, b):
        try:
            result = a / b
            print("Division result:", result)
        except TypeError:
            print('ZeroDivisionerror Detected')
    
    def access_list(self, lst, index):
        try:
            print("Element:", lst[index])
        except Exception:
            print('IndexErrpr Detected')


    
    def access_dict(self, dic, key):
        print("Value:", dic[key])
    
    def read_file(self, filename):
        with open(filename, "r") as f:
            content = f.read()
            print(content)
    
    def access_attribute(self, obj):
        print(obj.tnonexistent_attribue)
    
    def check_positive(self, number):
        if number < 0:
            raise MyException("The number must be positive.")
        else:
            print("Valid number:", number)


class MyException(Exception):
    pass

if __name__ == "__main__":

    demo = ExceptionsDemo()

    demo.divide(10, 0)   
    demo.divide("10", 2)  

    demo.access_list([1,2,3], 5)   
    demo.access_list(1, 0)   

    demo.access_dict({"a": 1, "b": 2, "c": 3}, "d")  
    demo.access_dict("not_a_dict", "b")  

    demo.read_file("text_2.txt") 
    demo.read_file("text.txt") 

    demo.access_attribute(object())  

    try:
        demo.check_positive(-5)
    except MyException as e:
        print(" Custom error:", e)
