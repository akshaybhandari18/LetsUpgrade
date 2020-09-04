print("Armstrong no from 1042000 to 702648265 : ")
for num in range(1042000,702648265):
    no_of_digits = len(str(num))

    temp = num
    sum = 0

    while temp>0:

        d = temp%10
        sum += d**no_of_digits
        temp = temp//10

    if num == sum:
        print(num, end=" ")
