from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import các models
from .user import User
from .group import Group
from .group_member import GroupMember
from .expense_category import ExpenseCategory
from .expense import Expense
from .expense_share import ExpenseShare
from .payment import Payment
from .settlement import Settlement
