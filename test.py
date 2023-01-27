numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_num = 11
i = 0

while i < len(numbers):
    if numbers[i] == search_num:
        print(search_num, " found at index ", i)
        break
    i += 1
else:
    print(search_num, " not found in the list.")
