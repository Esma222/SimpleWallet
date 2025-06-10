from wallet import Wallet
from transaction import Transaction
from ledger import Ledger

def main():
    ledger = Ledger()

    #Users
    alice = Wallet("Alice")
    bob = Wallet("Bob")

    #initial balance load
    alice.deposit(100)

    print(f"Alice balance: {alice.get_balance()}")
    print(f"Bob's balance: {bob.get_balance()}")
    
    #Alice sends 30 coins to Bob
    amount = 30
    try:
        alice.withdraw(amount)
        bob.deposit(amount)
        tx = Transaction("Alice", "Bob", amount)
        ledger.add_transaction(tx)
        print(f"transaction successful: Alice > Bob: {amount}")
    except ValueError as e:
        print("Transaction failed", e)

    print(f"Alice balance: {alice.get_balance()}")
    print(f"Bob's balance: {bob.get_balance()}")

    # Transaction history save to the file
    ledger.save_to_file()

if __name__ == "__main__":
    main()    