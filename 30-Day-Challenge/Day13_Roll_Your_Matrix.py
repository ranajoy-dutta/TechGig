def main():
    row, col = map(int,input().split())
    arr=[]
    for i in range(row):
        arr.append(list(map(int, input().split())))
    newarr = []
    
    for i in range(col):
        new = []
        for j in range(row):
            new.append(arr[j][i])
        newarr.append(new)
    
    for i in newarr:
        for j in i:
            print(j, end=" ")
        print()
main()

