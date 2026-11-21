# Báo cáo cá nhân — Đinh Thị Hường — 2A202603569

## 1. Thông tin thành viên

- Họ tên: Đinh Thị Hường.
- MSSV: 2A202603569.
- Email:
- GitHub: https://github.com/dihnhuonq130104.
- Nhóm: Nhom4 — Lớp L3A.
- Vai trong nhóm: Người gắn nhãn 1.

## 2. Phần việc phụ trách

Tôi phụ trách phân loại 20 ca lỗi của trợ lý hoàn phí LogiX-VN theo năm loại của Google PAIR, phối hợp với người gắn nhãn 2 để đối chiếu và hoàn thiện bảng khắc phục. Tôi cũng theo dõi điều kiện hoàn thành checkpoint để nhận diện các phần hồ sơ còn thiếu.

## 3. Đóng góp cụ thể

- Hoàn thiện cột nhãn người 1 cho 20 ca trong `bang_loi.md`
- Đối chiếu với bộ nhãn của Hoàng Lâm Minh đã push ở commit `7caf86c`: hai bộ trùng 19/20 ca, tương ứng 95%, vượt ngưỡng 80% của lab.
- Thảo luận ca 8 với nhóm và thống nhất nhãn Hệ thống: trợ lý viện dẫn điều khoản không tồn tại dù số tiền hoàn vẫn đúng. Giữ nguyên nhãn Ngầm ban đầu của người gắn nhãn 2 để bảo toàn kết quả đối chiếu.
- Hoàn thiện bảng khắc phục cho các ca 1, 7, 16, 19 và 17, lần lượt đại diện cho Do người dùng, Hệ thống, Ngữ cảnh, Giới hạn hệ thống và Ngầm. Mỗi dòng có cách phát hiện, hành động và một vai trò phụ trách.
- Chạy lại `src/lab13.py` và rà output với bảng chi phí: ba phép thử A1 và kiểm tra tính tuyến tính ở B1 đều ĐẠT.
- Commit phần CP3 trong `876cd32`.

Các event, ngưỡng phát hiện và cách khắc phục trong bảng là đề xuất thiết kế, chưa phải biện pháp đã triển khai hoặc kết quả đo thực tế.

## 4. Bằng chứng

- Repo nhóm: https://github.com/flying-bug/K5-L3A-DAY13-Nhom4-LaunchEconomics.
- File chính: `report/team/bang_loi.md`.
- Commit CP3: `876cd32` — CP3: hoan thanh bang loi va doi chieu nhan.
- Kết quả đối chiếu: 19/20 = 95%; ca không trùng ban đầu là ca 8, nhãn cuối thống nhất là Hệ thống.
- Bảng khắc phục có 5 dòng, đủ năm loại lỗi và vai trò phụ trách.

## 5. Công cụ AI đã dùng

Tôi dùng Codex đề xuất nhãn và lý do cho 20 ca.

## 6. Tự đánh giá

Tôi đã hoàn thành phần bảng lỗi CP3 với kết quả đối chiếu 95% và bảng khắc phục đủ năm loại. Điểm cần chú ý là phân biệt hành vi hệ thống làm sai với sai sót không được nhận ra, cũng như tách nguyên nhân gốc khỏi chỗ cần cải thiện giao diện.