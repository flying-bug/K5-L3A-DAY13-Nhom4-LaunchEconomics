# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Đinh Thị Hường  · Người gắn nhãn 2: Hoàng Lâm Minh (lấy nguyên bộ nhãn đã push ở commit 7caf86c).


| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Ngầm | Không | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ trùng giữa hai bộ hiện có:** 19 / 20 = 95%, vượt ngưỡng 80%. 
## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 8 — đã thống nhất Hệ thống:** dẫn điều khoản không tồn tại là lỗi Hệ thống; chỉ ưu tiên Ngầm khi mô tả xác nhận sai sót không được người dùng và hệ thống nhận ra. Số tiền vẫn đúng không loại bỏ lỗi dẫn căn cứ sai. Nhóm đã xác nhận lựa chọn này sau đối chiếu; nhãn ban đầu của vai 4 vẫn giữ là Ngầm, nên tỉ lệ trùng ban đầu vẫn là 19/20 = 95%.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

Các event, ngưỡng và hành động dưới đây là đề xuất, chưa phải kết quả đo hoặc biện pháp đã triển khai. Mỗi event cần trace_id, request_id và thời điểm.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `refund_account_validation_failed` khi tài khoản không đạt quy tắc độ dài/định dạng của ngân hàng; kiểm tra trước mọi lệnh hoàn. | Kiểm tra định dạng theo ngân hàng, đánh dấu ô sai và cho sửa; chặn gửi lệnh khi chưa hợp lệ. | Trưởng nhóm sản phẩm CSKH |
| 7 | Hệ thống | Đối chiếu mọi event `refund_success_notified` với xác nhận ghi sổ cái thành công; có ít nhất 1 thông báo không có xác nhận thì cảnh báo ngay. | Chỉ thông báo thành công sau xác nhận giao dịch; khi thất bại chuyển trạng thái chờ xử lý và giao nhân viên tiếp nhận. | Trưởng nhóm kỹ thuật thanh toán |
| 16 | Ngữ cảnh | Event `notification_sent` ghi kênh và giờ địa phương; cảnh báo nếu gửi thông báo không khẩn cấp trong khung giờ yên lặng đề xuất 22:00–07:00. | Xếp lịch gửi sau 07:00, cho khách chọn giờ và kênh nhận; vẫn lưu trạng thái hoàn tiền để khách chủ động tra cứu. | Trưởng nhóm trải nghiệm khách hàng |
| 19 | Giới hạn hệ thống | Event `lookup_out_of_retention` khi ngày đơn vượt thời hạn dữ liệu 12 tháng; rà hằng ngày để bảo đảm mỗi ca có mã bàn giao nhân viên. | Nói rõ giới hạn truy cập, chuyển nhân viên kèm tóm tắt và mã đơn; không suy đoán trạng thái giao dịch. | Trưởng ca CSKH |
| 17 | Ngầm | Đối chiếu phiên bản bảng giá ở mọi phép tính với phiên bản hiệu lực theo ngày đơn; có ít nhất 1 ca lệch phiên bản thì cảnh báo và rà các đơn liên quan. | Làm mới cache khi bảng giá đổi, chặn tính bằng phiên bản hết hiệu lực; tính lại các đơn bị ảnh hưởng và xử lý chênh lệch. | Trưởng nhóm vận hành chính sách giá |
