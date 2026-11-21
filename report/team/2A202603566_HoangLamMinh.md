# Báo cáo cá nhân — HoangLamMinh-2A202603566

## 1. Thông tin thành viên

- Họ tên: Hoàng Lam Minh
- MSSV: 2A202603566
- Email:
- GitHub: [laminh-h](https://github.com/laminh-h)
- Vai trong nhóm: người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Giữ hồ sơ: điền `report/team/ho_so_launch_v0.md` từ đầu buổi, cập nhật sau mỗi checkpoint, chuẩn bị hồ sơ đủ bảy mục trước 17:00 để gửi nhóm hội đồng.
- Người gắn nhãn 2: gắn độc lập 20 ca lỗi ở CP3, so nhãn với người gắn nhãn 1.

## 3. Đóng góp cụ thể

- **Hồ sơ launch v0:** bảy mục, mỗi mục có con số chính, trạng thái (Xong, có bằng chứng · Giả lập) và một vai trò phụ trách. Phạm vi pilot thu hẹp về `noi_dia` + `hang_nang` có lý do bằng số (0,22× và 0,69×; loại `quoc_te` 1,88× và `doi_tac` 0,85×, simulated). Đề xuất **Go có điều kiện** với bốn điều kiện, mỗi điều kiện có người phụ trách và ngày kiểm tra.
- **Nêu rõ con số bất lợi** trong hồ sơ: xem lại 100% làm chi phí lên 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút, simulated); MDE 6 điểm thì power chỉ 0,64 nếu tác động thật là 5 điểm.
- **Đối chiếu số:** chạy `src/lab13.py` của nhóm sau CP1–CP2, so từng số trong hồ sơ với output; sửa B4 từ 12.414 đ thành 12.415 đ cho khớp code nhóm. Kiểm tra `pilot_plan.yaml` đọc được bằng `yaml.safe_load` và không còn dấu `?` trước khi chuyển mục 6 sang Xong.
- **Gắn nhãn 20 ca** (cột "Nhãn người 2" trong `bang_loi.md`): trùng 19/20 = 95% với người gắn nhãn 1; ca lệch duy nhất là ca 8 (mình gắn Ngầm, nhóm thống nhất Hệ thống).
- **Rủi ro kinh tế (E2):** thêm ngưỡng tỉ lệ làm lại > 7%/tuần (đợt chạy thử 48/982 = 4,9%) và dòng rủi ro khối lượng thấp (+1.185 đ/việc ở 45.000 yc/tháng, +2.370 đ/việc ở nửa khối lượng, simulated) để mục 7 của hồ sơ khớp với `chi_so.md`.

## 4. Bằng chứng

- `report/team/ho_so_launch_v0.md`
- `report/team/bang_loi.md`: cột "Nhãn người 2"
- `report/team/chi_so.md`: mục E2
- Commit `7caf86c`: nhãn người 2 và hồ sơ launch v0
- Commit `6d7a582`: E2 trong chi_so.md, hồ sơ mục 5

## 5. Công cụ AI đã dùng

- **Claude Code** (trợ lý lập trình trong VS Code):
  - đọc repo và tóm tắt yêu cầu của vai 4;
  - soạn bản nháp hồ sơ launch v0 và dòng rủi ro E2;
  - viết script nháp tính lại các số A2–B4, D1, E1 từ hai file CSV để đối chiếu;
  - điền nhãn mình đưa vào bảng;
  - commit và push.
- **Cách tự kiểm tra:**
  - so từng số trong hồ sơ với output `python -X utf8 lab13.py` của nhóm và với bảng số đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch không quá 2%);
  - chạy lệnh grep tìm từ bị cấm theo quy tắc 5 của lab trong `report/team` (không in gì);
  - kiểm tra `pilot_plan.yaml` bằng `yaml.safe_load`;
  - rà lại mỗi mục hồ sơ có người phụ trách là một vai trò, không ghi "cả đội".

## 6. Tự đánh giá

- **Làm tốt:** hồ sơ đủ bảy mục từ sớm, số khớp code nhóm, các con số simulated đều có nhãn, nêu thẳng con số bất lợi để hội đồng chấm C6, C7.
- **Cần cải thiện:** ca 8 gắn nhãn chưa đúng. Mình coi "tiền vẫn đúng" là lỗi không lộ ra, trong khi trích dẫn sai đã nhìn thấy được, nên phải là Hệ thống.
