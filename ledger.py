import json

class Ledger:
    def __init__(self):
        self.transaction = []

    def add_transaction(self, transaction):
        self.transaction.append(transaction)
    
    def save_to_file(self, filename="ledger.json"):
        with open(filename, "w") as f:
            json.dump([t.to_dict() for t in self.transaction], f, indent=4)

    def load_from_file(self, filename="ledger.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            pass

    