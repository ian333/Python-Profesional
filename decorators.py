from datetime import datetime

def execution_time(func):
    def wrapper(*args,**kwargs):
        """
        This function print the execution time for a script
        """
        initial_time= datetime.now()
        func(*args,**kwargs)
        final_time=datetime.now()
        time_elapsed= final_time-initial_time
        print(f"Pasaron {time_elapsed.total_seconds()} segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range(10000000):
        pass

@execution_time
def suma(a:int , b :int ) ->int :
    """
    This function add 2 numbers
    """
    return a+b

@execution_time
def saludo(nombre="Cesar"):
    """
    This function print a salute
    """
    print(f"Hola {nombre}")
    
    

if __name__ == "__main__":
    random_func()
    suma(5,5)
    saludo("Sebastian")



    