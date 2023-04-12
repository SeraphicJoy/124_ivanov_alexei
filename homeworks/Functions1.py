def sum_range(start, end):
    if start>end:
        a=end
        b=start
        start=a
        end=b
    sum=0
    for i in range(start,end+1):
        sum+=i
    return sum
start = int(input("Начальное значение: "))
end = int(input("Конечное значение: "))
print(sum_range(start, end))