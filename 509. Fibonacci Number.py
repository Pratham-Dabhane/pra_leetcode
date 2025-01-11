# def fib(n):
#         a, b = 0,1
#         result = 0
#         for i in range (n):
#             a,b = b, result
#             result = a + b
#         return result




def fib(n):
    x=[0,1]
    num=0
    if n==1:
        return x[1]
    for i in range(1,n):
        num=x[0]+x[1]
        x[0]=x[1]
        x[1]=num
    return num
print(fib(10))