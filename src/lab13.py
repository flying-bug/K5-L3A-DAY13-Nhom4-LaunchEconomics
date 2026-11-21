"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    # Lần chạy thứ i xảy ra khi i-1 lần trước đều sai: E = sum_{i=1..k} (1-p)^(i-1) = (1-(1-p)^k)/p
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    # Thất bại chỉ khi cả k lần đều sai
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    # Tử số: mọi lần chạy (kể cả lần sai); mẫu số: chỉ việc thành công → k triệt tiêu, còn 1/p
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    # Chỉ giữ các lần chạy thuộc tập yêu cầu đang xét (để A3 chỉ cần lọc reqs)
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:  # dùng cho B1, B3
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    # Tử số: MỌI lần chạy, kể cả lần lỗi. Giá tính cho 1.000 token.
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai   # simulated
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai   # simulated
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai

    # Mẫu số: chỉ yêu cầu thành công
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong if thanh_cong else float('nan'),
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


def vnd(x, so_le=0):
    """Định dạng số kiểu Việt Nam: 4.472 · 0,22."""
    s = f'{x:,.{so_le}f}'
    return s.replace(',', '_').replace('.', ',').replace('_', '.')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    print(f'  so_lan_chay_ky_vong(0.8, 2)               = {vnd(so_lan_chay_ky_vong(0.8, 2), 2)}')
    print(f'  so_lan_chay_ky_vong(0.8)                  = {vnd(so_lan_chay_ky_vong(0.8), 2)}')
    print(f'  he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) = {vnd(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3), 2)}')

    # ---------- A2 ----------
    print('\n=== A2 · Mô hình chi phí từ trace (toàn bộ 1.200 yêu cầu) ===')
    ket_qua = mo_hinh(runs, reqs)
    nhan = dict(token='đo từ trace', tool='đo từ trace', chay_lai='đo từ trace',
                xem_lai='simulated', lam_lai='simulated', tong='có phần simulated',
                thanh_cong='', cps='simulated', hoa_don_moi_yc='đo từ trace')
    for ten, gia_tri in ket_qua.items():
        so_le = 1 if ten == 'hoa_don_moi_yc' else 0
        print(f'{ten:15s} {vnd(gia_tri, so_le):>14s}  {nhan[ten]}')
    print(f'Số lần gọi tool: {vnd(runs.tool_calls.sum())} · phút xem lại: {vnd(reqs.phut_xem_lai_simulated.sum())}'
          f' · phút làm lại: {vnd(reqs.phut_lam_lai_simulated.sum())} [simulated]')
    tong = ket_qua['tong']
    print(f"cps gấp {vnd(ket_qua['cps'] / ket_qua['hoa_don_moi_yc'], 1)} lần hoá đơn token+tool chia số yêu cầu")
    for ten in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f'  tỉ trọng {ten:8s} {vnd(ket_qua[ten] / tong * 100, 1)}%')
    print(f"  giờ nhân viên (xem lại + làm lại) = {vnd((ket_qua['xem_lai'] + ket_qua['lam_lai']) / tong * 100, 1)}% [simulated]")
    # So với nhân viên tự làm: các ca không thành công phải để nhân viên làm thay 12.000 đ/ca
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    he_thong_moi_yc = (tong + khong_tc * BASELINE) / len(reqs)
    print(f'Chi phí cả hệ thống / yêu cầu = ({vnd(tong)} + {khong_tc} × {vnd(BASELINE)}) / {len(reqs)}'
          f' = {vnd(he_thong_moi_yc)} đ = {vnd(he_thong_moi_yc / BASELINE, 2)}× của 12.000 đ [simulated]')

    # ---------- A3 ----------
    print('\n=== A3 · Tách theo loại yêu cầu ===')
    print(f"{'loai':10s} {'so_yc':>6s} {'ti_le_tc':>9s} {'lan/yc':>7s} {'cps [sim]':>10s} {'so 12k':>7s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs.loai == loai]
        kq = mo_hinh(runs, r)
        so_lan = runs[runs.request_id.isin(r.request_id)].shape[0] / len(r)
        print(f"{loai:10s} {len(r):>6d} {vnd(kq['thanh_cong'] / len(r) * 100, 1):>8s}% {vnd(so_lan, 2):>7s}"
              f" {vnd(kq['cps']):>10s} {vnd(kq['cps'] / BASELINE, 2):>6s}×")

    # Chạy lại có giúp không: tỉ lệ status == ok theo loại × lần thử
    print('\nTỉ lệ ok theo lần thử (%) — chạy lại có giúp không:')
    rl = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    rl['ok'] = (rl.status == 'ok').astype(int)
    bang = rl.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean') * 100
    so_run = rl.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='count')
    for loai in bang.index:
        o = '  '.join(f'lần {a}: {vnd(bang.loc[loai, a], 1):>5s}% (n={int(so_run.loc[loai, a])})'
                      for a in bang.columns if not pd.isna(bang.loc[loai, a]))
        print(f'  {loai:10s} {o}')

    # ---------- A4 ----------
    print('\n=== A4 · Chi phí cố định 40 triệu đ/tháng, phạm vi noi_dia + hang_nang ===')
    CO_DINH = 40_000_000
    YC_THANG = 1500 * 30  # 45.000 yêu cầu/tháng ở quy mô đầy đủ
    pv = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pv)
    print(f"Trong phạm vi: {len(pv)} yêu cầu, {kq_pv['thanh_cong']} thành công, tổng {vnd(kq_pv['tong'])} đ,"
          f" cps = {vnd(kq_pv['cps'])} đ [simulated]")
    for ten, yc_thang in [('45.000 yc/tháng', YC_THANG), ('Một nửa khối lượng', YC_THANG / 2)]:
        # Tỉ lệ việc thành công trong phạm vi tính trên toàn mẫu 1.200 yêu cầu
        tc_thang = yc_thang * kq_pv['thanh_cong'] / len(reqs)
        cd_moi_viec = CO_DINH / tc_thang
        tong_moi_viec = kq_pv['cps'] + cd_moi_viec
        print(f'  {ten:20s} việc TC/tháng {vnd(tc_thang):>7s} · cố định/việc {vnd(cd_moi_viec):>6s} đ'
              f' · cps + cố định {vnd(tong_moi_viec):>6s} đ = {vnd(tong_moi_viec / BASELINE, 2)}× [simulated]')

    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
