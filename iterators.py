from time import sleep

class FiboIter():
    """
    This class is to create an iter for Fibonacci Series
    """
    def __init__(self,max_number:int):
        self.max_number= max_number

    def __iter__(self):
        """
        docstring
        """
        self.n1=0
        self.n2=1
        self.counter=0
        return self 
        
    def __next__(self):
        aux=0
        
        if self.counter==0:
            self.counter+=1
            return self.n1
        elif self.counter==1:
            self.counter+=1
            return self.n2
        else :
            aux=self.n1+self.n2
            self.n1,self.n2=self.n2,aux
            if aux >= self.max_number:  raise StopIteration
            return aux


if __name__ == "__main__":
    fibonacci = FiboIter(900)

    for element in fibonacci:
        print(element)
        sleep(1)
    
