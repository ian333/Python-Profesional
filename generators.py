import time

def fibo_gen(limit:int) -> int:
    n1=0
    n2=1
    counter=0
    while True:
        if counter == 0:
            counter+=1
            yield n1
        elif counter == 1:
            counter+=1
            yield n2
        else:
            aux=n1+n2
            n1,n2=n2,aux
            if aux > limit: break
            yield aux
if __name__ == "__main__":
    limit=int(input("Ingrese el numero maximo de la susecion: "))
    fibonacci=fibo_gen(limit)
    

    for element in fibonacci:
        print(element)
        time.sleep(0.1)

                        