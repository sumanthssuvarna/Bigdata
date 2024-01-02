def a(lst):
    b = []
    for item in lst:
        if isinstance(item, list):
            b.extend(a(item))
        else:
            b.append(item)
    return b

# Example usage:
input_list = [1, 1, [2, 7, [6, 8, [7, [9]]]]]
output_list = a(input_list)

print(output_list)
