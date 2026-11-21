# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | Số yêu cầu có `dong_trong_24h = 1` và `mo_lai_trong_7_ngay = 0` / tổng số yêu cầu | 994/1.200 = 82,83% |
| Dùng | Tỉ lệ bỏ qua gợi ý | Số quyết định `sua` hoặc `bo` / số yêu cầu được xem lại | 48/177 = 27,12% |
| An toàn | Tỉ lệ mở lại trong 7 ngày | Số yêu cầu có `mo_lai_trong_7_ngay = 1` / tổng số yêu cầu | 51/1.200 = 4,25% |
| Dùng | Tỉ lệ yêu cầu được mở bằng trợ lý | Số yêu cầu của nhóm can thiệp được mở bằng trợ lý / tổng yêu cầu của nhóm can thiệp | Không cần tính |
| An toàn | Tỉ lệ hoàn sai tiền qua kiểm tra mẫu | Số đơn hoàn sai tiền được phát hiện / tổng số đơn được kiểm tra | Không cần tính |

Chỉ số đóng trong 24 giờ và không mở lại trong đợt chạy thử là 82,83%. Đợt chạy thử không có nhóm đối chứng nên chưa kết luận được trợ lý làm tăng chỉ số.

## Danh sách event

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, loại yêu cầu, nhóm can thiệp/đối chứng, `trace_id` | Khi gửi yêu cầu |
| `agent_run_completed` | Agent | `request_id`, lần chạy, token, trạng thái, `trace_id` | Sau mỗi lần chạy |
| `agent_opened` | Giao diện nhân viên | `request_id`, `staff_id`, `trace_id` | Khi mở yêu cầu bằng trợ lý |
| `agent_suggestion_shown` | Giao diện nhân viên | `request_id`, `staff_id`, `trace_id` | Khi hiện gợi ý |
| `staff_review_decision` | Giao diện nhân viên | `request_id`, giữ/sửa/bỏ, `trace_id` | Khi nhân viên quyết định |
| `ticket_closed` | Hệ thống ticket | `request_id`, thời điểm đóng, `trace_id` | Khi đóng yêu cầu |
| `ticket_reopened` | Hệ thống ticket | `request_id`, thời điểm mở lại, lý do, `trace_id` | Khi mở lại yêu cầu |
| `audit_sample_checked` | Nhân viên kiểm tra | `request_id`, số tiền đúng, số tiền đã hoàn, `trace_id` | Khi kiểm tra mẫu |

**Kiểm tra chéo:**

- Đóng trong 24 giờ và không mở lại trong 7 ngày:
  `refund_request_created`, `ticket_closed`, `ticket_reopened`.
  Theo dõi đủ 7 ngày để xác định yêu cầu không có event mở lại.
- Bỏ qua gợi ý: `agent_suggestion_shown`, `staff_review_decision`.
- Mở lại trong 7 ngày: `refund_request_created`, `ticket_reopened`.
- Yêu cầu được mở bằng trợ lý: `refund_request_created`, `agent_opened`.
- Hoàn sai tiền qua kiểm tra mẫu: `audit_sample_checked`.

## E2 · Rủi ro kinh tế

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí lên 6.787 đ/việc, tăng 51,8% (simulated) | Tỉ lệ và thời gian làm lại tăng theo tuần | Rà các trace làm lại và xem xét thu hẹp phạm vi pilot | PM trợ lý hoàn phí |
| Phải xem lại 100% | Chi phí 11.743 đ/việc, bằng 0,98× mức 12.000 đ (simulated) | Tỉ lệ và thời gian xem lại duy trì cao | Đánh giá điều kiện giảm xem lại theo bậc, đồng thời theo dõi an toàn | Trưởng nhóm CSKH |
