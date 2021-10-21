import typing

def is_palindrome(string:str) -> bool:
    """
    Esta funcion es para verificar que un string es un palindromo 
    """
    string=string.replace(" ","").lower()

    return string == string[::-1]

def run():
    print(is_palindrome(1000))

if __name__ == "__main__":

    run()    
    
    