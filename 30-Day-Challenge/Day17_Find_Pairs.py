def main():
    n = int(input())
    arr = list(map(int,input().split()))
    summ = int(input())
    flag=0
    for i in range(n-1):
        if summ == arr[i]+arr[i+1]:
            flag = 1
    if flag == 1:
        print('True')
    else:
        print('False')
        
main()

