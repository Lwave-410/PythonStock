'''def first_function(cost,price,profit):
    print("This is my first function")
    return (price-cost)*profit

x=first_function(10,20,30)
print(x)'''
def feb(n):
    if n==0 or n==1:
        return n
    else:
        return feb(n-1)+feb(n-2)
x=int(input("請輸入一個數字"))
print(feb(x))
