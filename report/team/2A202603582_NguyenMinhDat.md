# Báo cáo cá nhân — Nguyễn Minh Đạt — 2A202603582

## 1. Thông tin thành viên

- Họ tên: Nguyễn Minh Đạt
- MSSV: 2A202603582
- Email: nguyenminhdat6401@gmail.com
- Vai trong nhóm: Người kiểm số

## 2. Phần việc phụ trách

Kiểm tra kết quả tính chi phí, điền bảng chi phí A1–B4 và đối chiếu cỡ mẫu, tỉ lệ mở lại ở CP4.

## 3. Đóng góp cụ thể

- Đối chiếu kết quả A1–A4 và B1–B4 từ chương trình với bảng chi phí.
- Kiểm tra phép tính tiền xem lại và chi phí cả hệ thống.
- Đối chiếu kết quả cỡ mẫu D1 và tỉ lệ mở lại D3 với `pilot_plan.yaml`.
- Rà lịch pilot, bổ sung lịch dự kiến và điều kiện thu đủ mẫu, theo dõi đủ 7 ngày.
- Chạy lại chương trình và kiểm tra file YAML đọc được.
- Đọc hồ sơ launch của nhóm XYZ, tham gia đánh giá chéo Gate 2a và ghi kết quả vào `report/team/phieu_cham.md`.
- Tham gia đặt câu hỏi phản biện về điều kiện giảm tỉ lệ xem lại và ghi lại câu trả lời của nhóm XYZ.

## 4. Bằng chứng

- File `report/team/bang_chi_phi.md`: bảng chi phí A1–A4 và B1–B4; commit `6ef2632`.
- A2: 890 phút × 2.000 đ/phút = 1.780.000 đ (simulated).
- B1–B2: giá token và tiền xem lại cùng gấp đôi thì chi phí là 6.543 đ/việc, tăng 46,3% (simulated).
- B3: 4.093.220 + 234 × 12.000 = 6.901.220 đ (simulated).
- B4: xem lại 100% có chi phí 11.743 đ/việc, bằng 0,98 lần mức 12.000 đ (simulated).
- D1: với 20 nhân viên/nhóm và 299 yêu cầu/người, cỡ mẫu hiệu dụng là 20 × 299 ÷ 6,96 ≈ 859,2 mỗi nhóm.
- D3: tỉ lệ mở lại là 51/1.200 = 4,25% toàn mẫu và 39/982 = 3,97% trong phạm vi pilot.
- File `report/team/pilot_plan.yaml` đã được kiểm tra đọc bằng `yaml.safe_load`.

## 5. Công cụ AI đã dùng

Tôi dùng Codex để giải thích yêu cầu, chạy code, kiểm tra số, kiểm tra lại pilot. Tôi tự chạy chương trình, đối chiếu kết quả với hướng dẫn và kiểm tra lại các phép tính ở mục 4.

## 6. Tự đánh giá

Tôi hiểu cách tính chi phí mỗi việc thành công và vì sao cần cộng chi phí nhân viên làm thay khi so sánh các giới hạn chạy lại. Tôi cũng hiểu sự khác nhau giữa số yêu cầu cần thu và cỡ mẫu hiệu dụng khi chia theo nhân viên. Tôi cần tiếp tục chuẩn bị giải thích các kết quả và đánh đổi của kế hoạch pilot với nhóm.
