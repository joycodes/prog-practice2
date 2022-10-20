# assumed user balance
user_balance = 1234.55

# assumed user password
user_password = "!2A34"

pin = input ("Enter Pin: ")
if pin !=user_password:
    print("Invalid Pin")
    sys.exit()
    #exit


print("Welcome to Trusted Bank ATM")
print("1. Withdraw")
print("2. Exit")

choice = int(input("Enter 1 or 2: "))

if choice == 1:
    amount = float(input("Enter the amount:"))
    print("amount")

 # TODO 1: Check if the amount is less than the user balance
    # If so, print "Take your money" and deduct the amount from the user's balance
    # Also print the new balance.
    # Otherwise, print "Insufficient funds"

    if amount <= 0:
        print("Invalid amount")
    
    elif amount <= user_balance:
        user_balance = user_balance - amount
        print("Take your money")
        print("Your new balance is: ", user_balance)
    
    else:
        print("Insufficient funds")

    # TODO 2: Check if the choice is 2
    # # If so, print "Thank you for using our ATM"
    # # Otherwise, print "Invalid choice"

elif choice ==2:
    print ("Thank you for using our ATM")

else:
    print("Invalid Choice!")



# TODO 3 (Bonus): Check if the user password is correct before implementing the withdraw logic


# TODO 4 (Bonus): Add a deposit option to the ATM
# a deposit should ask for the amount, add money to the user's balance and print the new balance
