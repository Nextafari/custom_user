def counter(amount):
    if amount in range(100000, 999999):
        print("Ultimate Plan")
    elif amount in range(10000, 99999):
        print("Platinum Plan")
    elif amount in range(1000, 9999):
        print("Gold Plan")
    elif amount in range(100, 999):
        print("Basic Plan")
    else:
        print("Maximum amount exceeded")


# counter(10009)

def wallet(deposit, withdraw):
    initial_balance = 0
    if deposit:
        initial_balance = deposit + initial_balance
        print(initial_balance)
    if withdraw:
        initial_balance = initial_balance
        current_balance = initial_balance - withdraw
        print(current_balance)
    
wallet(1000, 300)
