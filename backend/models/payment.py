from datetime import datetime
from . import db

class Payment(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    payer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    note = db.Column(db.Text)

    group = db.relationship('Group', back_populates='payments')
    payer = db.relationship('User', foreign_keys=[payer_id])
    receiver = db.relationship('User', foreign_keys=[receiver_id])

    def __repr__(self):
        return f"<Payment {self.payer_id} -> {self.receiver_id} : {self.amount}>"
