def check_palindrome(string):
    string = string.lower().replace(' ','')
    string1 = string[::-1]
    if string == string1:
        print("This is a palindrome")

    else:
        print("Not a palindrome")

if __name__ == '__main__':
    x= input("Enter a string: ")
    check_palindrome(x)