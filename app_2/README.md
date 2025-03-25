# Ứng dụng Truy vấn Dữ liệu với Ngôn ngữ Tự nhiên

Đây là một ứng dụng sử dụng Streamlit kết hợp với LangChain để cho phép người dùng truy vấn cơ sở dữ liệu bằng ngôn ngữ tự nhiên. Ứng dụng chuyển đổi câu hỏi của người dùng thành các truy vấn SQL và hiển thị kết quả tương ứng.

## Tính năng chính

- **Chuyển đổi ngôn ngữ tự nhiên sang SQL:**
  - Sử dụng mô hình ngôn ngữ để chuyển đổi câu hỏi của người dùng thành truy vấn SQL.
  - Hỗ trợ các truy vấn phức tạp với nhiều điều kiện và phép toán.

- **Thực thi truy vấn và hiển thị kết quả:**
  - Kết nối với cơ sở dữ liệu và thực thi truy vấn SQL được tạo ra.
  - Hiển thị kết quả truy vấn một cách trực quan trên giao diện Streamlit.

- **Tùy chỉnh và mở rộng:**
  - Dễ dàng tùy chỉnh và mở rộng để phù hợp với các cơ sở dữ liệu và yêu cầu cụ thể.

## Cài đặt

1. **Cloning repository:**

   ```bash
   git clone https://github.com/pntrungbk15/All_Demo.git
   cd All_Demo/app_2
   ```

2. **Tạo và kích hoạt môi trường ảo:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Trên macOS/Linux
   venv\Scripts\activate     # Trên Windows
   ```

3. **Cài đặt các thư viện cần thiết:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Cấu hình biến môi trường:**

   Tạo tệp `.env` trong thư mục `app_2` và thêm các thông tin cấu hình cần thiết, ví dụ:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   DATABASE_URL=your_database_url
   ```

## Sử dụng

1. **Chạy ứng dụng Streamlit:**

   ```bash
   streamlit run main.py
   ```

2. **Tương tác với ứng dụng:**
   - Nhập câu hỏi bằng ngôn ngữ tự nhiên vào ô nhập liệu.
   - Ứng dụng sẽ hiển thị truy vấn SQL tương ứng và kết quả truy vấn từ cơ sở dữ liệu.

## Cấu trúc thư mục

- `main.py`: Tệp chính chạy ứng dụng Streamlit, xử lý giao diện người dùng và tương tác.
- `langchain_help.py`: Chứa các hàm hỗ trợ liên quan đến LangChain, bao gồm tạo truy vấn SQL từ ngôn ngữ tự nhiên và thực thi truy vấn.
- `few_shots.py`: Cung cấp các ví dụ mẫu (few-shot examples) để cải thiện độ chính xác của mô hình khi chuyển đổi ngôn ngữ tự nhiên sang SQL.

## Hình ảnh khi chạy UI
![](assets/image.jpg)
