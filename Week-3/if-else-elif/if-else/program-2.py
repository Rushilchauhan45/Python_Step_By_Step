# ATM Withdraw Amount Check 

balance = 3000

amt_withdraw = int(input("Enter the amount to withdraw: "))

if amt_withdraw <= balance:
    print("Please collect your cash.")
    balance -= amt_withdraw
    print("Your remaining balance is: ",balance)
else:
    print("Insufficient balance.")
