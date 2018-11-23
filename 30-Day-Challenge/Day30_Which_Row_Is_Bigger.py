def main():
    row, col = map(int,input().split())
    mat = []
    max=0
    for i in range(row):
        arr = list(map(int,input().split()))
        if sum(arr)>max:
            max = sum(arr)
            rowid = i+1
    print("Row",rowid)
    
main()

