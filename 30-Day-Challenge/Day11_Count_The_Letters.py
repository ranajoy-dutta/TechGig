def main():
    string = input()
    lower,upper = 0,0
    
    for i in range(len(string)):
        if string[i].isupper() :
            upper += 1
        elif string[i].islower() :
            lower += 1
    print(upper)
    print(lower, end="")
main()
