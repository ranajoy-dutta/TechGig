def main():
    a,b = map(int,input().split())
    c,d = a,b
    a_sum,b_sum = 0,0
    while True:
        if a==0 and b==0:
            break
        if a > 0:
            a_sum = a_sum + (a%10)
            a = int(a/10)
        if b > 0:
            b_sum = b_sum + (b%10)
            b = int(b/10)
    if a_sum>b_sum:
        print(c)
    elif b_sum>a_sum:
        print(d)
    else:
        print("Equal")
    
main()

