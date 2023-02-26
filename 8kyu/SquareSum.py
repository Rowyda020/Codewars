#Square(n) Sum
def square_sum(numbers):
   num_squares=[]
   for i in numbers:
       i=i**2
       num_squares.append(i)
   return sum(num_squares)