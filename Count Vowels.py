def count_vowels(st):
    num = 0
    vowels = 'aeiou'
    for x in st:
        if x in vowels:
            num += 1
    print("Total number of vowels are ",num)

if __name__ == '__main__':
    x = input("Enter a String to count vowels: ")
    count_vowels(x)