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
|   2 | Đỗ Duy Bộ | 2A202603591 | https://github.com/flying-bug |        |         |
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
- Kiểm tra chi phí cả hệ thống khi giới hạn 2 lần chạy:
  4.093.220 + 234 × 12.000 = 6.901.220 đ (simulated).
- Cùng trợ lý AI hoàn thiện `report/team/bang_chi_phi.md`.
- Đối chiếu cỡ mẫu hiệu dụng: 20 × 299 ÷ 6,96 ≈ 859,2 yêu cầu mỗi nhóm.
- Đối chiếu tỉ lệ mở lại: 51/1.200 = 4,25% toàn mẫu và 39/982 = 3,97% trong phạm vi pilot.
- Cùng trợ lý AI rà và bổ sung lịch dự kiến vào kế hoạch pilot; chạy chương trình và kiểm tra cú pháp YAML.

### Bằng chứng

- `report/team/bang_chi_phi.md` — commit `6ef2632`.
- `report/team/pilot_plan.yaml` — kết quả D1, D3 và lịch pilot.
- `report/team/2A202603582_NguyenMinhDat.md` — báo cáo cá nhân, commit `0617e27`.


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
