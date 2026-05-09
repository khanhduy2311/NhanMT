# 🧮 Matrix Chain Multiplication - Tối Ưu Hóa Nhân Ma Trận Dây Chuyền

Một ứng dụng web chuyên nghiệp, trực quan giúp giải quyết bài toán **Nhân ma trận dây chuyền (Matrix Chain Multiplication)**. Ứng dụng cung cấp giao diện hiện đại, dễ sử dụng cùng các công cụ mạnh mẽ để so sánh hiệu suất và quan sát từng bước thực thi của các thuật toán khác nhau.

---

## 🌟 Các Tính Năng Nổi Bật

### 1. 🛠 Giao Diện Nhập Liệu Thông Minh & Tự Động Xác Thực
- **Khởi tạo động:** Cho phép tùy chỉnh số lượng ma trận (N) từ 2 đến 10.
- **Tự động liên kết kích thước:** Kích thước (số cột) của ma trận trước tự động đồng bộ với kích thước (số hàng) của ma trận sau, đảm bảo tính hợp lệ của phép nhân.
- **Báo lỗi trực tiếp (Real-time Validation):** Cảnh báo ngay lập tức bằng giao diện trực quan nếu chuỗi ma trận có kích thước không khớp nhau (ví dụ: cột A không bằng hàng B).
- **Nút "Ngẫu nhiên":** Tự động điền dữ liệu ma trận với các giá trị ngẫu nhiên chỉ bằng 1 cú click, tiết kiệm thời gian test.

### 2. 🧠 Hỗ Trợ Đa Thuật Toán
Ứng dụng cho phép bạn chọn và đánh giá 3 phương pháp phổ biến nhất để giải quyết bài toán, giúp người dùng so sánh trực tiếp tốc độ thực thi:
- 🚀 **Chia để trị (Divide & Conquer):** Đệ quy Top-Down thuần túy `O(2ⁿ)`.
- 📊 **Quy hoạch động (Bottom-Up DP):** Xây dựng bảng phương án tối ưu `O(n³)`.
- 💡 **Top-Down + Memoization:** Đệ quy có nhớ (lưu trữ kết quả bài toán con) `O(n³)`.

### 3. 📖 Cẩm Nang Thuật Toán (Algorithm Modal)
- Nút "Xem thuật toán" mở ra một cửa sổ pop-up chuyên nghiệp.
- Cung cấp **Mã giả (Pseudo-code)**, mô tả nguyên lý hoạt động, cùng với đánh giá độ phức tạp về Không gian/Thời gian (Space/Time Complexity) trực quan cho từng phương pháp tương ứng.

### 4. 📈 Báo Cáo Kết Quả Chi Tiết & Chuyên Nghiệp
Sau khi hệ thống xử lý, một báo cáo kết quả toàn diện sẽ được hiển thị:
- **Thời gian thực thi:** Đo lường chính xác thời gian chạy thuật toán (ms) để đo lường hiệu năng.
- **Số phép nhân vô hướng:** Trả về số phép nhân tối ưu nhất (ít nhất) có thể đạt được.
- **Cách đặt dấu ngoặc:** Hiển thị công thức chuỗi nhân ma trận với cách đặt ngoặc theo chuẩn toán học.
- **Bảng tính toán (M-Table):** Hiển thị trực quan bảng sinh từ quy hoạch động `M[i,j]` cho phép dễ dàng track số liệu.
- **Ma trận kết quả:** Hiển thị ma trận cuối cùng thu được sau khi thực hiện tích của toàn bộ chuỗi.

### 5. 🔍 Theo Dõi Từng Bước (Step-by-step Logs)
- Ứng dụng ghi log chi tiết **từng bước tính toán**, chỉ ra các giá trị `k` được thử, khi nào có cache-hit (sử dụng Memoization), và thao tác lưu mảng.
- **Trải nghiệm UI tối ưu:** Khung hiển thị log được thiết kế dạng **Accordion** (Thu gọn/Mở rộng), tự động hiển thị trước một lượng log vừa đủ và ẩn bớt các bước còn lại giúp giao diện không bị tràn khi giải các bài toán lớn.

---

## 🚀 Hướng Dẫn Cài Đặt & Sử Dụng

1. **Clone repository này về máy** hoặc tải mã nguồn dưới dạng ZIP.
2. Không cần cài đặt `npm` hay chạy server ảo. Bạn chỉ cần **mở file `index.html`** bằng trình duyệt web của bạn (Chrome, Edge, Firefox, Safari).
3. Tại giao diện chính:
   - Thay đổi số lượng ma trận N theo ý muốn.
   - Nhập vào giá trị hàng/cột (nhớ tuân thủ nguyên tắc cột của trước = hàng của sau).
   - Điền giá trị ma trận thủ công hoặc bấm **Ngẫu nhiên**.
   - Tick chọn loại thuật toán mà bạn muốn áp dụng.
4. Nhấn **"Tính toán"** để xem phép màu xảy ra ở kết quả bên dưới!

