def valid_number():
 while True:
    try:
        x = int(input("Insert A Whole Number: "))
        return x
    except ValueError:
        print("Not a whole number, Try Again")
        

def even_odd_no_checker():
  
    number = valid_number()
    if number % 2 == 0:
        print(f"{number} is an even")
    else:
        print(f"{number} ia an odd")
                