def main():
    num = int(input())
    count = 0
    while int(num)>0:
        count += 1
        num/=10
    print(count, end="")
main()
