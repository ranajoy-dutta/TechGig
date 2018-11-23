def main():
    num = int(input())
    fact=1
    while num>0:
        fact = num*fact
        num-=1
    print(fact)
main()