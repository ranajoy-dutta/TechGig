def main():
    n = int(input())
    maxx = 0
    while n > 0 :
        rem = n%10
        if rem > maxx:
            maxx = rem
        n /= 10
    print(maxx)
    
main()

