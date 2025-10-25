# Sơ đồ mối quan hệ (ER) và nguyên nhân không thể INSERT vào settlements / payments / expense_shares

## Tóm tắt nguyên nhân thường gặp khi INSERT thất bại
- Lỗi FK (Error 1452): giá trị trong cột khoá ngoại (ví dụ created_by, group_id, payer_id, expense_id, user_id) không tồn tại trong bảng tham chiếu.  
- Ràng buộc NOT NULL: thiếu cột bắt buộc khi chèn.  
- Ràng buộc UNIQUE: chèn trùng giá trị trên cột unique (ví dụ email).  
- Tên bảng/cột sai hoặc thiếu backticks với tên trùng từ khoá (`groups`).  
- Kiểm tra thông tin lỗi chi tiết: `SHOW ENGINE INNODB STATUS\G` và `SHOW CREATE TABLE <table>;`.

## Kiểm tra nhanh khi gặp lỗi
1. Kiểm tra cấu trúc table: