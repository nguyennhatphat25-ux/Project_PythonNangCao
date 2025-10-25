from . import db

class ExpenseCategory(db.Model):
    __tablename__ = 'expense_categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    icon = db.Column(db.String(50))
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<Category {self.name}>"
