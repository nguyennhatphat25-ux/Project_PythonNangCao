from datetime import datetime
from . import db

class GroupMember(db.Model):
    __tablename__ = 'group_members'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    role = db.Column(db.Enum('admin', 'member', name='role_enum'), default='member')
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', back_populates='groups')
    group = db.relationship('Group', back_populates='members')

    def __repr__(self):
        return f"<GroupMember user={self.user_id} group={self.group_id}>"
