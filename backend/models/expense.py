from datetime import datetime
from . import db

class Expense(db.Model):
    __tablename__ = 'expenses'

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    paid_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('expense_categories.id'))
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    split_type = db.Column(db.Enum('equal', 'unequal', 'percentage', name='split_type_enum'), default='equal')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    group = db.relationship('Group', back_populates='expenses')
    payer = db.relationship('User', back_populates='expenses')
    category = db.relationship('ExpenseCategory')
    shares = db.relationship('ExpenseShare', back_populates='expense', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Expense {self.description} - {self.amount}>"
