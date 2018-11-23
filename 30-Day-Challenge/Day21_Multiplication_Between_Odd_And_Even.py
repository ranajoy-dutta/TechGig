def main():
    n = int(input())
    arr = list(map(int,input().split()))
    odd = 0
    even = 0
    for i in range(n):
        if arr[i]%2 == 0:
            even += arr[i]
        else:
            odd += arr[i]
    print(even*odd)
main()

