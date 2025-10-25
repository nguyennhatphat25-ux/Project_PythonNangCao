from flask import Blueprint, jsonify, request
from models.group import Group
from models import db

group_bp = Blueprint('group_bp', __name__)

# 🟢 GET - Lấy toàn bộ nhóm
@group_bp.route('/', methods=['GET'])
def get_all_groups():
    groups = Group.query.all()
    return jsonify([
        {
            "id": g.id,
            "name": g.name,
            "description": g.description,
            "created_by": g.created_by,
            "created_at": g.created_at.isoformat() if g.created_at else None,
            "updated_at": g.updated_at.isoformat() if g.updated_at else None
        }
        for g in groups
    ])


# 🟢 GET - Lấy nhóm theo ID
@group_bp.route('/<int:group_id>', methods=['GET'])
def get_group(group_id):
    group = Group.query.get(group_id)
    if not group:
        return jsonify({"message": "Group not found"}), 404

    return jsonify({
        "id": group.id,
        "name": group.name,
        "description": group.description,
        "created_by": group.created_by,
        "created_at": group.created_at.isoformat() if group.created_at else None,
        "updated_at": group.updated_at.isoformat() if group.updated_at else None
    })


# 🟡 POST - Tạo nhóm mới
@group_bp.route('/', methods=['POST'])
def create_group():
    data = request.get_json()

    if not data or 'name' not in data or 'created_by' not in data:
        return jsonify({"message": "Missing required fields: name, created_by"}), 400

    new_group = Group(
        name=data['name'],
        description=data.get('description'),
        created_by=data['created_by']
    )

    db.session.add(new_group)
    db.session.commit()

    return jsonify({
        "message": "Group created successfully",
        "id": new_group.id
    }), 201


# 🟠 PUT - Cập nhật nhóm
@group_bp.route('/<int:group_id>', methods=['PUT'])
def update_group(group_id):
    group = Group.query.get(group_id)
    if not group:
        return jsonify({"message": "Group not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"message": "No data provided"}), 400

    if 'name' in data:
        group.name = data['name']
    if 'description' in data:
        group.description = data['description']

    db.session.commit()
    return jsonify({"message": "Group updated successfully"})


# 🔴 DELETE - Xóa nhóm
@group_bp.route('/<int:group_id>', methods=['DELETE'])
def delete_group(group_id):
    group = Group.query.get(group_id)
    if not group:
        return jsonify({"message": "Group not found"}), 404

    db.session.delete(group)
    db.session.commit()
    return jsonify({"message": "Group deleted successfully"})
