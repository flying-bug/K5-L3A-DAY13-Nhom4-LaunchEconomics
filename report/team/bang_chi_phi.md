# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | 890 phút × 2.000 đ/phút | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | Token + tool + xem lại + làm lại | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | đếm từ dữ liệu |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (245.585 + 84.000) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp khoảng 16,3 lần hoá đơn chia số yêu cầu (simulated).
- Làm lại chiếm tỉ trọng lớn nhất: 2.264.000 ÷ 4.373.585 ≈ 51,8% (simulated).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ (simulated) | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ (simulated) | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ (simulated) | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ (simulated) | 0,85× |

- `quoc_te` có chi phí 22.515 đ/việc thành công, bằng 1,88× mức 12.000 đ (simulated). Tỉ lệ ok lần 2 là 11,4% và lần 3 là 2,2%; chạy lại có thêm ca thành công nhưng hiệu quả giảm mạnh.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ (simulated) | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ (simulated) | 0,48× |

- Ở cả hai mức khối lượng, chi phí mỗi việc vẫn thấp hơn 12.000 đ; khi khối lượng giảm một nửa, chi phí cố định mỗi việc tăng từ 1.185 lên 2.370 đ (simulated).

## B1 · Đổi từng yếu tố

Các chi phí và thay đổi trong B1–B4 có phần simulated; chi phí cả hệ thống ở B3 cộng 12.000 đ cho mỗi yêu cầu không thành công.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token và tỉ lệ xem lại cùng gấp đôi: 6.543 đ/việc, tăng 46,3% (simulated).
- Theo biên độ các kịch bản đã chọn: 1. Số ca làm lại (77,6 điểm %) · 2. Tỉ lệ xem lại (61,0 điểm %) · 3. Lương nhân viên (23,1 điểm %) (simulated).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn 2 lần rẻ nhất cho công ty: 6.901.220 đ; giới hạn 1 lần có chi phí/việc thành công thấp nhất: 4.111 đ, nhưng có thêm 85 yêu cầu không thành công so với 2 lần (simulated).

## B4 · Nếu phải xem lại tất cả

- Xem lại 100% trong phạm vi `noi_dia` + `hang_nang`: 11.743 đ/việc, bằng 0,98× 12.000 đ, giả định xem lại 5 phút và làm lại 9 phút/ca (simulated). Nếu làm lại trung bình 15,3 phút/ca: 12.415 đ, bằng 1,03× (simulated).
- Pilot cần đo thời gian xem lại và làm lại thực tế, đồng thời tìm cách giảm tỉ lệ xem lại an toàn: 100% xem lại khiến chi phí gần bằng hoặc vượt 12.000 đ (simulated).
