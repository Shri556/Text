#Enter a string and the program will reverse it and print it out.
from time import sleep
def reverse_string(st):
    extra = [str(x) for x in st]
    st1 = '' 
    for x in range(1,len(extra)):
        st1 = st1 + extra[-x]
        
    st1 = st1 + extra[0]
    print(st1)

if __name__ == '__main__':
    x = input("Enter a String: ")
    reverse_string(x)

