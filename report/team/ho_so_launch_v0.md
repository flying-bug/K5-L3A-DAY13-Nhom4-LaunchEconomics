# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Nhom4 · Lớp: L3A

Phạm vi đề xuất pilot: **chỉ `noi_dia` + `hang_nang`** (982/1.200 yêu cầu của mẫu). Mọi số tính bằng `src/lab13.py` trên dữ liệu giả lập; số có `[simulated]` dựa trên cột `_simulated`.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** [simulated] trên 1.200 yêu cầu, gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ). Trong phạm vi pilot: 3.414 đ, cộng cố định 40 triệu/tháng thành **4.599 đ** ở 45.000 yc/tháng, **5.784 đ** nếu khối lượng còn một nửa [simulated]. Giờ nhân viên chiếm 92,5% tổng chi phí | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại ×2: **+51,8%** (6.787 đ) · 2. Tỉ lệ xem lại ×2: **+40,7%** (6.292 đ) · 3. Lương +25%: **+23,1%** (5.506 đ). Giá token ×2 chỉ +5,6% [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Theo loại: noi_dia **0,22×**, hang_nang **0,69×**, doi_tac 0,85×, quoc_te **1,88×** (thành công 27,3%, chạy lại không giúp) của 12.000 đ. Cả hệ thống, đã cộng 222 ca nhân viên làm thay: 5.865 đ/yêu cầu = **0,49×**. **Bất lợi:** nếu xem lại 100%, chi phí là 11.743 đ = **0,98×** (12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu) [simulated] | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử là: chính **82,83%** (994/1.200) đóng trong 24 giờ và không mở lại 7 ngày · dùng: bỏ qua gợi ý **27,12%** (48/177) · an toàn: mở lại 7 ngày **4,25%** (51/1.200; 3,97% trong phạm vi). Chưa có đối chứng nên không kết luận được tác động | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận gắn nhãn: **19/20 = 95%** (lệch ca 8, thống nhất Hệ thống). Lỗi hệ thống 5/20 ca (2, 7, 8, 15, 20), nghiêm trọng nhất: báo "đã hoàn" khi sổ cái lỗi (ca 7), hoàn trùng (ca 20). Bảng khắc phục 5 ca đủ năm loại, mỗi dòng có event, ngưỡng và một vai trò phụ trách (`bang_loi.md`) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo **nhân viên**, 20 + 20, ngẫu nhiên phân tầng theo depot. Chia theo yêu cầu cần 1.251/nhóm nhưng tràn tác động; theo depot tối đa 300 hiệu dụng. 20 người/nhóm tối đa 1.000 < 1.251 nên chọn MDE **6 điểm**: 859/nhóm, m ≥ 299 yc/người, DE 6,96. **Bất lợi:** nếu tác động thật là 5 điểm thì power chỉ **0,64**. Ba luật dừng (an toàn, chi phí, mức dùng) trong `pilot_plan.yaml` | Chưa | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại ×2: +51,8% lên 6.787 đ; theo dõi tỉ lệ làm lại theo tuần, ngưỡng 7% (đợt chạy thử 4,9% trong phạm vi). Xem lại 100% kéo dài: 0,98× (1,03×). Khối lượng thấp: cố định +2.370 đ/việc ở nửa khối lượng [simulated] (`chi_so.md`) | Giả lập | PM trợ lý hoàn phí |

<!-- Người giữ hồ sơ: đổi mục 5 sang "Xong, có bằng chứng" khi bang_loi.md đã có hai bộ nhãn, tỉ lệ đồng thuận và bảng khắc phục; đổi mục 6 khi pilot_plan.yaml đọc được bằng yaml.safe_load và không còn dấu ?. Đối chiếu lại mọi số với output lab13.py của nhóm. -->

**Đề xuất: Go có điều kiện**, chỉ cho pilot `noi_dia` + `hang_nang`, chia theo nhân viên 20 + 20. Loại `quoc_te` (1,88×) và `doi_tac` (0,85×, điều khoản riêng) khỏi pilot. Điều kiện:

- Sửa khoá chống trùng khi ghi hoàn và chỉ báo "đã hoàn" khi sổ cái trả ok (lỗi hệ thống, ca 7 và 20); đối soát sổ cái mỗi giờ, ngưỡng 0 ca. Phụ trách: Kỹ sư trưởng agent. Kiểm tra: 2026-11-30, trước ngày bắt đầu.
- Ký chấp nhận mức chênh 6 điểm (power 0,64 nếu tác động thật chỉ 5 điểm) và chốt trước chỉ số chính, ngưỡng, luật dừng, ngày quyết định 2027-01-05. Phụ trách: Giám đốc vận hành. Kiểm tra: 2026-11-30.
- Bật đủ event có `trace_id`; thay phút xem lại và làm lại simulated bằng phút đo thật từ `staff_review_decision`, `staff_rework_completed`. Phụ trách: PM trợ lý hoàn phí. Kiểm tra: 2026-12-08, hết tuần 1.
- Giảm xem lại theo bậc (xem lại 100% thì 0,98×, không tiết kiệm), chỉ giảm khi tỉ lệ sửa + bỏ < 15%; mục tiêu mỗi lần xem lại ≤ 5,1 phút. Phụ trách: Trưởng nhóm CSKH. Kiểm tra: 2026-12-15, cuối bước rollout 0.25.
