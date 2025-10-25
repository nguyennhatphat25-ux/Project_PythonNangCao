# Sơ đồ mối quan hệ (ER) và nguyên nhân không thể INSERT vào settlements / payments / expense_shares

## Tóm tắt nguyên nhân thường gặp khi INSERT thất bại
- Lỗi FK (Error 1452): giá trị trong cột khoá ngoại (ví dụ created_by, group_id, payer_id, expense_id, user_id) không tồn tại trong bảng tham chiếu.  
- Ràng buộc NOT NULL: thiếu cột bắt buộc khi chèn.  
- Ràng buộc UNIQUE: chèn trùng giá trị trên cột unique (ví dụ email).  
- Tên bảng/cột sai hoặc thiếu backticks với tên trùng từ khoá (`groups`).  
- Kiểm tra thông tin lỗi chi tiết: `SHOW ENGINE INNODB STATUS\G` và `SHOW CREATE TABLE <table>;`.

## Kiểm tra nhanh khi gặp lỗi
1. Kiểm tra cấu trúc table:



# ER Diagram — Quan hệ giữa các thực thể

Dưới đây là sơ đồ ER (Mermaid). Mở file này trong VS Code với extension Mermaid Preview hoặc xem trên GitHub để hiển thị đồ họa.

```mermaid
erDiagram
    USERS {
        int id PK
        string name
        string email
    }

    GROUPS {
        int id PK
        string name
        text description
        int created_by FK -> USERS.id
    }

    EXPENSES {
        int id PK
        int group_id FK -> GROUPS.id
        int paid_by FK -> USERS.id
        decimal amount
    }

    EXPENSE_SHARES {
        int id PK
        int expense_id FK -> EXPENSES.id
        int user_id FK -> USERS.id
    }

    PAYMENTS {
        int id PK
        int group_id FK -> GROUPS.id
        int payer_id FK -> USERS.id
        int receiver_id FK -> USERS.id
        decimal amount
    }

    SETTLEMENTS {
        int id PK
        int group_id FK -> GROUPS.id
        int payer_id FK -> USERS.id
        int receiver_id FK -> USERS.id
        decimal amount
        string status
    }

    USERS ||--o{ GROUPS : "created_by"
    GROUPS ||--o{ EXPENSES : "group_id"
    EXPENSES ||--o{ EXPENSE_SHARES : "expense_id"
    USERS ||--o{ EXPENSE_SHARES : "user_id"
    GROUPS ||--o{ PAYMENTS : "group_id"
    USERS ||--o{ PAYMENTS : "payer / receiver"
    GROUPS ||--o{ SETTLEMENTS : "group_id"
    USERS ||--o{ SETTLEMENTS : "payer / receiver"
```

Giải thích ngắn:
- ||--o{ : quan hệ 1 (||) — N (o{).
- Mỗi bảng có các FK trỏ về bảng USERS hoặc GROUPS hoặc EXPENSES như trong sơ đồ.
- Đảm bảo chèn dữ liệu theo thứ tự hợp lệ (USERS → GROUPS → EXPENSES → EXPENSE_SHARES / PAYMENTS / SETTLEMENTS) để tránh lỗi FK.