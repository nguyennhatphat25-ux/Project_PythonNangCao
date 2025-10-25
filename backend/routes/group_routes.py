from flask import Blueprint, jsonify
from models.group import Group

group_bp = Blueprint('group_bp', __name__)

@group_bp.route('/', methods=['GET'])
def get_all_groups():
    groups = Group.query.all()
    return jsonify([
        {"id": g.id, "name": g.name, "created_by": g.created_by}
        for g in groups
    ])
