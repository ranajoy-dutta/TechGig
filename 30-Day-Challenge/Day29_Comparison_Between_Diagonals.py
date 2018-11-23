def main():
    row, col = map(int,input().split())
    mat = []
    for i in range(row):
        mat.append(list(map(int,input().split())))
    d1,d2,forward,backward = 0,0,0,col-1
    for i in range(row):
        d1 += mat[i][forward]
        forward += 1
        d2 += mat[i][backward]
        backward -= 1
    if d1>d2:
        print('Diagonal 1')
    elif d2>d1:
        print('Diagonal 2')
    else:
        print('Equal')
main()

