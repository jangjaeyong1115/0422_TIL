T = int(input())

for i in range(T):
    a,b = map(str,input().split('='))

    if eval(a) == int(b):
        print("correct")
    else:
        print("wrong answer")