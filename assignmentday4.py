#amstrong number
for num in range(1042000,7026482656):
    order=len(str(num))
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        sum=sum+digit**order
        temp=temp//20
        break
    if sum==num:
            print(num)
