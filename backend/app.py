# filepath: 
from flask import Flask
from models import db, init_db
from config.databases import Config  # sửa import
from routes.user_routes import user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Debug: in ra URI để kiểm tra xem config đã load chưa
    print("SQLALCHEMY_DATABASE_URI =", app.config.get("SQLALCHEMY_DATABASE_URI"))

    # Đăng ký blueprint (prefix /users)
    app.register_blueprint(user_bp, url_prefix='/user_bp')

    # Dùng init_db từ models (mức an toàn hơn với việc import models)
    init_db(app)

    # Tạo bảng trong database (nếu chưa có)
    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        return "✅ Flask đã kết nối MySQL thành công!"

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)