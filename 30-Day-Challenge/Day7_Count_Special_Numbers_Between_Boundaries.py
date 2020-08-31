def main():
    start = int(input())
    stop = int(input())
    count = 0
    for i in range(start,stop):
        j=2
        flag = 0
        while j<i:
            if i%j == 0:
                flag = 1
                break
            else:
                flag=0
                j+=1
            
        if flag == 0 and i!=1:
            count += 1
    print(count, end="")
            
main()
