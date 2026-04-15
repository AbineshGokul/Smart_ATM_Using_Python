import time

bank_name = "State Bank of India"

print("========================================")
print(" Welcome to", bank_name)
print(" SMART ATM")
print("========================================")

name = input("Enter your name: ")

pin = "03092007"
entered_pin = input("Enter ATM PIN: ")

if entered_pin != pin:
    print("❌ Incorrect PIN. Access Denied.")
    exit()

print("\nHello", name + ", Welcome to", bank_name, "ATM!")

balance = 5000
transactions = []


def receipt_pattern():
    print("\nReceipt Pattern")
    for i in range(1, 6):
        print("$" * i)


def reward_series(n):
    print("\nReward Points:")
    for i in range(1, n + 1):
        print(i * 10, end=" ")
    print()


def total_transactions(arr, n):
    if n == 0:
        return 0
    return 1 + total_transactions(arr, n - 1)


def menu():
    print("\n======================")
    print(bank_name, "ATM MENU")
    print("======================")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")
    print("======================")


while True:
    menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        balance += amount
        transactions.append(amount)
        print("\nDeposit successful!")
        receipt_pattern()
        reward_series(5)

    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))
        if amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            transactions.append(-amount)
            print("\nWithdrawal successful!")
            receipt_pattern()
            reward_series(5)

    elif choice == 4:
        print("\nTransaction History:")
        for t in transactions:
            print(t)
        total = total_transactions(transactions, len(transactions))
        print("Total Transactions:", total)

    elif choice == 5:
        print("\n========================================")
        print(" Thank you for using", bank_name, "ATM")
        print(" We appreciate your banking with us")
        print(" Have a great day,", name)
        print("========================================")
        break

    else:
        print("Invalid choice")
