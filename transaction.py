from datetime import datetime

class Transaction:
    def __init__(self, sender_id, receiver_id, amount):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.amount = amount
        self.timestamp = datetime.now()

    def to_dict(self):
        return{
            "sender": self.sender_id,
            "receiver": self.receiver_id,
            "amount": self.amount,
            "timestamp": self.timestamp.isoformat()
        }
