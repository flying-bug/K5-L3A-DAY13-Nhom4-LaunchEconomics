# Team

## Thông tin nhóm

- Tên nhóm: Nhom4
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-Nhom4-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/flying-bug/K5-L3A-DAY13-Nhom4-LaunchEconomics, main, 

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Hoàng Lam Minh | 2A202603566 |  | https://github.com/laminh-h | Người gắn nhãn 2, kiêm giữ hồ sơ |
|   2 | Đỗ Duy Bộ | 2A202603591 | duybohshl@gmail.com | https://github.com/flying-bug | Nhóm trưởng, người viết code |
|   3 | Đinh Thị Hường | 2A202603569 |  | https://github.com/dihnhuonq130104 | Người gắn nhãn 1 |
|   4 | Nguyễn Minh Đạt | 2A202603582 | nguyenminhdat6401@gmail.com | https://github.com/nguyenminhdat6401 | Người kiểm số |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## NguyenMinhDat-2A202603582

### Phần việc phụ trách

- Người kiểm số: đối chiếu kết quả và điền bảng chi phí A1–B4.
- Đối chiếu cỡ mẫu D1, tỉ lệ mở lại D3 và rà lịch pilot ở CP4.

### Đóng góp cụ thể

- Đối chiếu kết quả từ `src/lab13.py` với bảng chi phí.
- Kiểm tra tiền xem lại: 890 × 2.000 = 1.780.000 đ (simulated).
- Kiểm tra chi phí cả hệ thống khi giới hạn 2 lần chạy: 4.093.220 + 234 × 12.000 = 6.901.220 đ (simulated).
- Đối chiếu cỡ mẫu hiệu dụng: 20 × 299 ÷ 6,96 ≈ 859,2 yêu cầu mỗi nhóm.
- Đối chiếu tỉ lệ mở lại: 51/1.200 = 4,25% toàn mẫu và 39/982 = 3,97% trong phạm vi pilot.
- Cùng trợ lý AI rà và bổ sung lịch dự kiến vào kế hoạch pilot; chạy chương trình và kiểm tra cú pháp YAML.
- Đọc hồ sơ launch của nhóm XYZ và tham gia đánh giá chéo Gate 2a.
- Tham gia câu hỏi về điều kiện giảm tỉ lệ xem lại, ghi câu trả lời của nhóm XYZ vào `report/team/phieu_cham.md`.

### Bằng chứng

- `report/team/bang_chi_phi.md` — commit `6ef2632`.
- `report/team/pilot_plan.yaml` — kết quả D1, D3 và lịch pilot.
- `report/team/2A202603582_NguyenMinhDat.md` — báo cáo cá nhân, commit `0617e27`.


## DoDuyBo-2A202603591

### Phần việc phụ trách

- Nhóm trưởng: chia vai, theo dõi tiến độ năm checkpoint, gộp nhánh và chốt bài nộp.
- Người viết code: viết và chạy `src/lab13.py` cho Nhiệm vụ A (CP1), B (CP2), D (CP4); viết `report/team/pilot_plan.yaml`.

### Đóng góp cụ thể

- CP1: viết ba hàm A1 (ba phép thử ĐẠT 1,20 · 1,25 · 1,25) và hàm `mo_hinh`; chi phí mỗi việc thành công 4.472 đ, gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (simulated); tách theo loại (A3) và cộng chi phí cố định 40 triệu đ/tháng (A4).
- CP2: bảng độ nhạy 9 kịch bản có `assert` tự kiểm tra tuyến tính; B3: giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ), giới hạn 1 lần cho chi phí mỗi việc thấp nhất (4.111 đ) nhưng đẩy thêm 85 việc sang nhân viên (simulated).
- CP4: tính D1 trong code (1.251 · 3.103 · 1.000 · 300 · m ≥ 299, DE 6,96), đối chiếu statsmodels; chọn chia theo nhân viên 20 + 20, MDE 6 điểm, ghi power 0,64 nếu tác động thật là 5 điểm; tính tỉ lệ mở lại hiện tại 4,25% trước khi đặt luật an toàn; viết ba luật dừng.
- Gộp nhánh: xử lý xung đột mục 5, 6 của `ho_so_launch_v0.md`; đồng bộ ngày quyết định 2027-01-08 trong `pilot_plan.yaml`; viết `report/team/group_report.md`.

### Bằng chứng

- Commit: `0761df0` (CP1), `bcacb19` (CP2), `77be503` (CP4), `2d332ab` (gộp CP4 với CP5).
- File: `src/lab13.py`, `report/team/pilot_plan.yaml`, `report/team/group_report.md`.
- Báo cáo cá nhân: `report/team/2A202603591_DoDuyBo.md`.

## HoangLamMinh-2A202603566

### Phần việc phụ trách

- Người gắn nhãn 2, kiêm giữ hồ sơ: điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

### Đóng góp cụ thể

- Dựng hồ sơ launch v0 đủ bảy mục, đối chiếu từng con số với output `src/lab13.py` (A2–B4, D1, E1) và các file `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`; ghi nhãn simulated; đề xuất Go có điều kiện với bốn điều kiện, mỗi điều kiện có người phụ trách và ngày kiểm tra.
- Gắn độc lập 20 ca lỗi (cột "Nhãn người 2"), trùng 19/20 = 95% với người gắn nhãn 1.
- Bổ sung E2 trong `chi_so.md`: ngưỡng tỉ lệ làm lại 7%/tuần và dòng rủi ro khối lượng thấp (+2.370 đ/việc ở nửa khối lượng, simulated) để hồ sơ mục 7 khớp bằng chứng.

### Bằng chứng

- File: `report/team/ho_so_launch_v0.md`, `report/team/bang_loi.md` (cột người 2), `report/team/chi_so.md` (E2).
- Commit: `7caf86c` (nhãn người 2, hồ sơ v0), `6d7a582` (E2, hồ sơ mục 5).
## DinhThiHuong-2A202603569

### Phần việc phụ trách

- Người gắn nhãn 1: phân loại 20 ca lỗi ở CP3 và theo dõi điều kiện hoàn thành checkpoint.

### Đóng góp cụ thể

- Viết nhãn và lý do phân loại 20 ca theo năm loại lỗi Google PAIR; rà và cập nhật bảng lỗi.
- Đối chiếu với bộ nhãn của Hoàng Lâm Minh: trùng 19/20 ca, đạt 95%.
- Cùng nhóm thống nhất ca 8 là Hệ thống; giữ nguyên hai nhãn ban đầu và ghi quy tắc phân biệt với lỗi Ngầm.
- Hoàn thiện bảng khắc phục cho 5 ca đại diện đủ năm loại, có cách phát hiện đo được và vai trò phụ trách.

### Bằng chứng

- File: `report/team/bang_loi.md`.
- Commit: `876cd32` — CP3: hoan thanh bang loi va doi chieu nhan.
- Báo cáo cá nhân: `report/team/2A202603569_DinhThiHuong.md`.
