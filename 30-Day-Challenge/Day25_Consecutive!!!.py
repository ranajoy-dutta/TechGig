def main():
    n = int(input())
    arr = list(map(int,input().split()))
    start = arr[0]
    for i in range(n):
        if start+i != arr[i]:
            print('False')
            return 0
    print('True')
    
    
main()



