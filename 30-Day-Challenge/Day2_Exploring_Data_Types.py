def main():
    a=input()
    if a.isalpha():
        print("This input is of type string.", end="")
    elif a.isnumeric():
        print("This input is of type Integer.", end="")
    elif a.rfind('.')!=-1:
        try:
            a=float(a)
            print('This input is of type Float.', end="")
        except:
            print("This input is of type string.", end="")
    elif a[0]=='-':
        print("This input is of type Integer.", end="")
    else:
        print('This is something else.', end="")
main()
