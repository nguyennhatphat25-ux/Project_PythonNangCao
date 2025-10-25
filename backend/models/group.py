from datetime import datetime
from . import db

class Group(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    members = db.relationship('GroupMember', back_populates='group', cascade='all, delete-orphan')
    expenses = db.relationship('Expense', back_populates='group', cascade='all, delete-orphan')
    payments = db.relationship('Payment', back_populates='group', cascade='all, delete-orphan')
    settlements = db.relationship('Settlement', back_populates='group', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Group {self.name}>"
