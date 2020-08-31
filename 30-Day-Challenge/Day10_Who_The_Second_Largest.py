def main():
    input()
    arr = list(map(int, input().split()))
    arr.remove(max(arr))
    print(max(arr), end="")
    
main()
