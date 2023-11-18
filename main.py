# Write a function 'sum_of_even_numbers' , which recieved in arr integer, and return summ all even numbers
def sum_of_even_numbers(arr):
    even_numbers = [num for num in arr if num % 2 == 0]

     #return summ all even numbers
    return sum(even_numbers)




numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_even_numbers(numbers)
print(result)


