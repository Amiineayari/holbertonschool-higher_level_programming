#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # The first element of each row is always 1
        if i > 0:
            for j in range(1, i):
                # Calculate the value based on the values from the previous row
                value = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(value)
            row.append(1)  # The last element of each row is always 1
        triangle.append(row)

    return triangle

# Test the pascal_triangle function
if __name__ == "__main__":
    result = pascal_triangle(5)
    for row in result:
        print(row)
