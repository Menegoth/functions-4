# 1
def max_num(a, b, c):
    return max([a, b, c])

print(max_num(1, 2, 3))

# 2
def mult_list(numbers):
    if len(numbers) == 0:
        return 0

    total = numbers[0]

    if len(numbers) > 1:
        for num in numbers:
            total *= num
        return total
    else:
        return total

print(mult_list([1, 2, 3]))
print(mult_list([]))
print(mult_list([3]))

# 3
def rev_string(str):
    return str[::-1]

print(rev_string("asd"))

# 4
def num_within(num, start, end):
    return num in range(start, end + 1)

print(num_within(3,2,4))     
print(num_within(3,1,3))     
print(num_within(10,2,5))

# 5
triangle = [[1], [1, 1]]
def pascal(n):
    if n < 1:
        print("Invalid number of rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]

            length = len(row_prev) + 1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length - 1:
                    row.append(triangle[row_number - 1][i - 1] + triangle[row_number - 1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

        for row in triangle:
            print(row)

pascal(2)
pascal(5)
    