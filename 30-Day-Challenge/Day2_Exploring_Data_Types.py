def main():
    a=input()
    if a.isalpha():
        print("This input is of type string.")
    elif a.isnumeric():
        print("This input is of type Integer.")
    elif a.rfind('.')!=-1:
        try:
            a=float(a)
            print('This input is of type Float.')
        except:
            print("This input is of type string.")
    elif a[0]=='-':
        print("This input is of type Integer.")
    else:
        print('This is something else.')
main()

