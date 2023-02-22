def sum_with_range(min, max):
    print(min, max)
    sum = 0
    for i in range(min,max):
        sum += i
    return sum

result = sum_with_range(1,10) # 1 10
print(result) # 45
result = sum_with_range(result,result + 10) # 45 55
print(result) # 495