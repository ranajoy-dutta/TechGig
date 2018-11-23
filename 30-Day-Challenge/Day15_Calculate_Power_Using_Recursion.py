def rec(num, expo, res=1):
	if expo <= 0:
		return res
	res *= num
	return rec(num, expo-1, res)

def main():
    num, expo = map(int,input().split())
    res = rec(num,expo)
    print(res)
main()
