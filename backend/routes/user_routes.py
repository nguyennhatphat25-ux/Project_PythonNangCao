from flask import Blueprint, jsonify, request
from models.user import User
from models import db

user_bp = Blueprint('user_bp', __name__)

# 🟢 GET - Lấy toàn bộ users
@user_bp.route('/', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([
        {"id": u.id, "name": u.name, "email": u.email}
        for u in users
    ])


# 🟢 GET - Lấy user theo ID
@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email
    })


# 🟡 POST - Thêm user mới
@user_bp.route('/', methods=['POST'])
def add_user():
    data = request.get_json()

    if not data or 'name' not in data or 'email' not in data or 'password_hash' not in data:
        return jsonify({"message": "Missing fields: name, email, password_hash"}), 400

    # Kiểm tra trùng email
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"message": "Email already exists"}), 409

    new_user = User(
        name=data['name'],
        email=data['email'],
        password_hash=data['password_hash']
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully", "id": new_user.id}), 201


# 🟠 PUT - Cập nhật thông tin user
@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"message": "No data provided"}), 400

    if 'name' in data:
        user.name = data['name']
    if 'email' in data:
        user.email = data['email']
    if 'password_hash' in data:
        user.password_hash = data['password_hash']

    db.session.commit()
    return jsonify({"message": "User updated successfully"})


# 🔴 DELETE - Xóa user
@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"})

# 🔴 DELETE - Xóa user
@user_bp.route('/', methods=['DELETE'])
def delete_all_user():
    users = User.query.all()
    for user in users:
        db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "All users deleted successfully"})
