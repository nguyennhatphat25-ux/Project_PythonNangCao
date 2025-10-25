from datetime import datetime
from . import db

class Settlement(db.Model):
    __tablename__ = 'settlements'

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    payer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.Enum('pending', 'done', name='settlement_status_enum'), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    group = db.relationship('Group', back_populates='settlements')
    payer = db.relationship('User', foreign_keys=[payer_id])
    receiver = db.relationship('User', foreign_keys=[receiver_id])

    def __repr__(self):
        return f"<Settlement {self.payer_id} -> {self.receiver_id} : {self.amount}>"
