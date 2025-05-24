# for i in range(6):
#     print(i)
#     if i==4:
#         break
# else:
#     print('sorry no i ') # yaha else nahi chalega kyuki break se bahar aa gaye.


# i = 0
# while i < 5:  # Loop will run as long as i is less than 5
#     print(i)
#     i += 1  # Increment i to eventually stop the loop


# i = 0
# while i < 5:
#     print(i)
#     if i == 3:  # Exit the loop when i equals 3
#         break
#     i += 1  # Increment i to eventually stop the loop
# else:
#     print("Loop completed")  # This will not execute because of the break


# while True:  # This condition is always True
#     print("This will run forever!")
#     break  # Use break to stop the loop


# try:
#     a = int(input('Enter a number: '))  # Attempt to convert input to an integer
#     print(f"Multiplication table of {a} is:")
#     for i in range(1, 11):
#         print(f"{a} X {i} = {a * i}")  # Generate the multiplication table
# except ValueError as e:
#     # Handle the case where the input is not a valid integer
#     print("Invalid input! Please enter a valid number.")
# except Exception as e:
#     # Handle any other unexpected exceptions
#     print(e)
# finally:
#     print("This will always execute, regardless of errors.")



# # Finally keyword
# try:
#     print('trying to divideby zero....')
#     result = 10 / 0
# except ZeroDivisionError:
#     print('caught a division by zero error !')
# finally:
#     print('finally block executed')

#except: Handles specific error that occur during the try block.
#finally: Always executes after the try block, regardless of whether an error occurred or not.



                                # Raising errors


a = int(input('Enter a number between 5 and 9: '))  # Assign the input value to 'a'
if a < 5 or a > 9:
        raise ValueError('Number is not in range')  # Raise an error if the condition is met

try:
    a = int(input('Enter a number between 5 and 9: '))  # Assign the input value to 'a'
    if a < 5 or a > 9:
        raise ValueError('Number is not in range')  # Raise an error if the condition is met
except ValueError as quit:
    print('Exiting the program:')
    print('exited the program')
else:
    print('Number is in range')
    