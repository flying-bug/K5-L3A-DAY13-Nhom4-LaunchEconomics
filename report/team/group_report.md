# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Nhom4
- Lớp: L3A
- Thành viên: xem `TEAM.md` (nhóm trưởng: Đỗ Duy Bộ)

## 2. Mục tiêu và cách tiếp cận

Định giá trợ lý hoàn phí LogiX-VN và lập kế hoạch pilot để hội đồng Gate 2a ra quyết định. Nhóm đi theo thứ tự: chi phí thật cho mỗi việc thành công (A) → yếu tố làm chi phí biến động mạnh nhất (B) → lỗi và cách khắc phục (C) → pilot tách được tác động (D) → chỉ số, rủi ro và hồ sơ một trang (E). Mọi số tính bằng `src/lab13.py` trên dữ liệu giả lập; số dựa trên cột `_simulated` ghi nhãn simulated.

## 3. Giải pháp

| Nhiệm vụ | Cách làm | File |
| --- | --- | --- |
| A · Chi phí mỗi việc thành công | Tử số cộng mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm `thanh_cong`; ba phép thử đáp án biết trước ĐẠT trước khi tính trên dữ liệu; tách theo loại, cộng cố định 40 triệu đ/tháng | `src/lab13.py`, `bang_chi_phi.md` |
| B · Độ nhạy | Gọi lại `mo_hinh` cho 9 kịch bản, kiểm tra tuyến tính bằng `assert`; so giới hạn 1–3 lần chạy theo chi phí cả hệ thống | `bang_chi_phi.md` |
| C · Bảng lỗi | Hai người gắn nhãn độc lập 20 ca theo năm loại Google PAIR, so nhãn, ghi quy tắc cho ca lệch; bảng khắc phục 5 ca đủ năm loại | `bang_loi.md` |
| D · Pilot plan | Tính đủ năm câu cỡ mẫu rồi mới chọn cách chia; tính tỉ lệ mở lại hiện tại trước khi đặt ngưỡng an toàn | `pilot_plan.yaml` |
| E · Chỉ số, rủi ro, hồ sơ | Ba chỉ số tính thử, 8 event có `trace_id`, ba dòng rủi ro lấy số từ bảng độ nhạy; hồ sơ một trang bảy mục | `chi_so.md`, `ho_so_launch_v0.md` |

## 4. Kết quả

- Chi phí mỗi việc thành công **4.472 đ** (simulated), gấp **16,3 lần** hoá đơn token + tool chia số yêu cầu; giờ nhân viên chiếm 92,5% tổng chi phí. Trong phạm vi pilot `noi_dia` + `hang_nang`: 3.414 đ, cộng cố định thành **4.599 đ** ở 45.000 yc/tháng (simulated).
- So với 12.000 đ khi nhân viên tự làm: `noi_dia` 0,22×, `hang_nang` 0,69×, `doi_tac` 0,85×, `quoc_te` **1,88×** (thành công 27,3%, chạy lại không giúp) (simulated).
- Ba yếu tố nhạy nhất: số ca làm lại ×2 **+51,8%**, tỉ lệ xem lại ×2 **+40,7%**, lương +25% **+23,1%**; giá token ×2 chỉ +5,6% (simulated).
- Bảng lỗi: đồng thuận **19/20 = 95%**; 5/20 ca là lỗi hệ thống, nặng nhất là báo "đã hoàn" khi sổ cái lỗi (ca 7) và hoàn trùng (ca 20).
- Pilot: chia theo nhân viên 20 + 20, ngẫu nhiên phân tầng theo depot. Với 40 nhân viên không cách chia theo cụm nào đủ mẫu cho 5 điểm, nên chọn MDE **6 điểm** (859/nhóm, m ≥ 299 yc/người, DE 6,96). Ba luật dừng: an toàn, chi phí, mức dùng; ngày quyết định 2027-01-08.
- Chỉ số trong đợt chạy thử là: chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25%. Chưa có đối chứng nên không kết luận được tác động.
- **Con số bất lợi:** xem lại 100% đưa chi phí lên 11.743 đ = 0,98× (1,03× nếu làm lại 15,3 phút như dữ liệu); nếu tác động thật chỉ 5 điểm thì power còn **0,64**.
- **Đề xuất cuối: Go có điều kiện**, chỉ pilot `noi_dia` + `hang_nang`, loại `quoc_te` và `doi_tac`; bốn điều kiện có người phụ trách và ngày kiểm tra (xem `ho_so_launch_v0.md`).
- Duyệt chéo: Nhóm 4 chấm Nhóm XYZ trong `phieu_cham.md` (30/30, Go có điều kiện).
- **Kết quả hội đồng (Nhóm XYZ chấm Nhóm 4): 30/30, Go có điều kiện.** Lý do hội đồng nêu: gắn đủ nhãn simulated; thu hẹp phạm vi về `noi_dia` + `hang_nang` (0,38× gồm chi phí cố định); pilot chia theo nhân viên 20 + 20 tách được tác động (MDE 6 điểm, n = 859/nhóm); nêu thẳng con số bất lợi (0,98×–1,03× nếu xem lại 100%, power 0,64 ở mức 5 điểm) kèm 4 điều kiện có vai trò phụ trách và hạn kiểm tra.
- Câu hỏi phản biện: *ngưỡng dừng an toàn là bao nhiêu và vì sao không làm pilot dừng oan ngay tuần đầu khi tỉ lệ mở lại hiện tại đã là 4,25% (3,97% trong phạm vi)?* Trả lời của nhóm: luật an toàn không dùng ngưỡng tuyệt đối thấp (3% sẽ dừng ngay tuần đầu) mà so với nhóm đối chứng chạy cùng thời gian: dừng khi mở lại 7 ngày của nhóm trợ lý cao hơn đối chứng **≥ 2 điểm** hoặc vượt **trần tuyệt đối 6%** (cao hơn nền 3,97% khoảng 2 điểm), kéo dài **3 ngày liên tiếp**; riêng hoàn trùng dừng ngay từ ca đầu tiên. So với đối chứng loại được biến động chung theo mùa, yêu cầu ba ngày liên tiếp tránh dừng vì nhiễu của một ngày (`pilot_plan.yaml`, luật dừng 1).

## 5. Khó khăn và cách xử lý

- Không cách chia theo cụm nào đủ mẫu cho mức chênh 5 điểm: nhóm không chọn chia theo yêu cầu (đủ 1.251 nhưng tràn tác động) mà nâng MDE lên 6 điểm và ghi rõ power 0,64 thay vì giấu.
- Ngưỡng an toàn tuyệt đối 3% sẽ dừng pilot ngay tuần đầu vì tỉ lệ mở lại hiện tại đã là 4,25%: chuyển sang so với nhóm đối chứng (+2 điểm) kèm trần 6%.
- Hai người gắn nhãn lệch ở ca 8: thống nhất nhãn Hệ thống và ghi quy tắc phân biệt với lỗi Ngầm.
- Nhiều người push song song nên có xung đột ở `ho_so_launch_v0.md` và ngày quyết định lệch giữa các file: nhóm trưởng gộp tay, đối chiếu lại số và đồng bộ ngày 2027-01-08.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Mọi chi phí dựa trên phút xem lại và làm lại giả lập; tuần 1 của pilot phải thay bằng phút đo thật từ `staff_review_decision` và event làm lại.
- ICC 0,02 và baseline 0,70 là giả định đề; cần ước lượng lại từ dữ liệu tuần đầu và tính lại cỡ mẫu nếu ICC cao hơn.
- Power 0,64 cho tác động 5 điểm: nếu kết quả không có ý nghĩa thống kê, chưa được kết luận là trợ lý không có tác động.
- Lỗi hệ thống (ca 7, 20) phải sửa và đối soát sổ cái trước ngày bắt đầu 2026-12-02.

## 8. Tài liệu tham khảo

- `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` · `docs/du_lieu_va_cong_thuc.md` · `docs/Ngay13_Slide_Launch_Economics.pdf`.
- Google PAIR, *People + AI Guidebook*, chương Errors + Graceful Failure (năm loại lỗi).
- statsmodels: `NormalIndPower`, `proportion_effectsize` (đối chiếu cỡ mẫu và power).
