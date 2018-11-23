def mat_input():
    row, col = map(int,input().split())
    arr=[]
    for i in range(row):
        arr.append(list(map(int, input().split())))
    return arr

def main():
    arr1 = mat_input()
    arr2 = mat_input()
    arr3 = []
    for i in range(len(arr1)):
        new = []
        for j in range(len(arr1[0])):
            new.append(arr1[i][j]+arr2[i][j])
        arr3.append(new)
    for i in arr3:
        for j in i:
            print(j, end=" ")
        print()
main()

