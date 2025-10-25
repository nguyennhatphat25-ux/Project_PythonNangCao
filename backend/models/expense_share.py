from . import db

class ExpenseShare(db.Model):
    __tablename__ = 'expense_shares'

    id = db.Column(db.Integer, primary_key=True)
    expense_id = db.Column(db.Integer, db.ForeignKey('expenses.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    share_amount = db.Column(db.Float, nullable=False)
    paid = db.Column(db.Boolean, default=False)

    expense = db.relationship('Expense', back_populates='shares')
    user = db.relationship('User')

    def __repr__(self):
        return f"<ExpenseShare user={self.user_id} amount={self.share_amount}>"
