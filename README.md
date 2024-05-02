# Cơ sở dữ liệu tri thức

- Required:
    python version==3.7.2

# Tạo môi trường ảo
    python venv venv

# Kích hoạt môi trường ảo
    venv\Scripts\activate

# Step 1:
    cd ..venv
# Step 2:
    cd ..Scripts
# Step 3: có 2 cách
    activate
    or
    .\activate

# Chạy thư viện Chatterbot  
    python -m pip install chatterbot==1.0.4 pytz

# Training Data - Chạy file app.py
    python app.py

- File app.py 'trainer.train("chatterbot.corpus.vietnamese")' trong đó vietnamese là data tự tạo / chỉnh sửa hoặc sử dụng có sẵn trong library
