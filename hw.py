start=int(input("please enter the first number of your range"))
end=int(input("please enter the last number of your range"))
   
squares=[n**2 for n in range(start, end + 1)]
even_squares=[s for s in squares if s % 2 == 0]
odd_squares=[s for s in squares if s % 2 != 0]
    
print(f"Even squares: {even_squares}")
print(f"Odd squares: {odd_squares}")

