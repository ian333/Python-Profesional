from time import sleep


def fibo_gen(limit:int)-> int:
    z, b = 0, 1
    while z <limit:
        yield z 
        z, b = b, z+b

if __name__ == "__main__":
    limit=int(input("""Ingrese el numero maximo hasta donde llegara la cuenta \n
Ejemplo si usted ingresa 10000 \n el generador llegara al numero de fibonacci menor mas cercano que es 6765
    """))
    fibonacci = fibo_gen(limit)
    for element in fibonacci:
        print(element)
        sleep(0.05)