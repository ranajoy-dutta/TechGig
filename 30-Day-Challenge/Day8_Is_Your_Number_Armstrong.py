def main():
    num = int(input())
    cpy = num
    arr=[]
    sum = 0
    while int(num) > 0:
        arr.append(int(num % 10))
        num/=10
    n = len(arr)
    
    for i in range(n):
        sum += arr[i]**n
        
    if sum == cpy:
        print('True', end="")
    else :
        print('False', end="")

main()
