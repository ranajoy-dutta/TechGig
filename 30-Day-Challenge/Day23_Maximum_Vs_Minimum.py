def main():
    n = int(input())
    arr = list(map(int,input().split()))
    minn = arr[0]
    maxx = arr[0]
    for i in arr:
        if i > maxx:
            maxx = i
        elif i < minn:
            minn = i
    print(minn*maxx)
main()

