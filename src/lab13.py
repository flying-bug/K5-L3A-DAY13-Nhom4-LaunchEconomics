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


def pct(x):
    """Phần trăm có dấu: +5,6% · −2,8%."""
    return ('+' if x >= 0 else '−') + vnd(abs(x), 1) + '%'


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

    # ---------- B1 · Đổi từng yếu tố ----------
    print('\n=== B1 · Bảng độ nhạy: đổi từng yếu tố (toàn bộ 1.200 yêu cầu) ===')
    goc = mo_hinh(runs, reqs)['cps']
    kich_ban = {
        'Giá token gấp đôi':          dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':     dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi':      dict(he_so_xem_lai=2),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi':      dict(he_so_lam_lai=2),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%':   dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần':  dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần':         dict(max_lan_chay=1),
    }
    print(f"{'Gốc (A2)':28s} {vnd(goc):>7s} đ")
    do_nhay = {}
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        do_nhay[ten] = (cps / goc - 1) * 100
        print(f'{ten:28s} {vnd(cps):>7s} đ  {pct(do_nhay[ten]):>7s}  [simulated]')
    # Tự kiểm tra: "giảm một nửa" = ½ mức tăng của "gấp đôi" (mô hình tuyến tính)
    for cap in ['Giá token', 'Tỉ lệ xem lại', 'Số ca làm lại']:
        gd, gn = do_nhay[f'{cap} gấp đôi'], do_nhay[f'{cap} giảm một nửa']
        assert abs(gn + gd / 2) < 1e-6, f'{cap}: giảm một nửa phải bằng −½ gấp đôi'
    print('Tự kiểm tra tuyến tính (giảm một nửa = −½ gấp đôi): ĐẠT')

    # ---------- B2 · Đổi một cặp và xếp hạng ----------
    print('\n=== B2 · Đổi một cặp: giá token gấp đôi + xem lại gấp đôi ===')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    tong_rieng = do_nhay['Giá token gấp đôi'] + do_nhay['Tỉ lệ xem lại gấp đôi']
    print(f'cps = {vnd(cps_cap)} đ ({pct((cps_cap / goc - 1) * 100)}) · tổng hai tác động riêng'
          f' = {pct(tong_rieng)} → cộng tuyến tính [simulated]')
    # Xếp hạng theo biên độ (gấp đôi − giảm một nửa) của từng yếu tố
    bien_do = {
        'Số ca làm lại':   do_nhay['Số ca làm lại gấp đôi'] - do_nhay['Số ca làm lại giảm một nửa'],
        'Tỉ lệ xem lại':   do_nhay['Tỉ lệ xem lại gấp đôi'] - do_nhay['Tỉ lệ xem lại giảm một nửa'],
        'Lương nhân viên': do_nhay['Lương nhân viên tăng 25%'],
        'Giá token':       do_nhay['Giá token gấp đôi'] - do_nhay['Giá token giảm một nửa'],
        'Giới hạn chạy':   -do_nhay['Chỉ cho chạy 1 lần'],
    }
    print('Xếp hạng yếu tố (theo biên độ thay đổi cps):')
    for i, (ten, bd) in enumerate(sorted(bien_do.items(), key=lambda x: -x[1]), 1):
        print(f'  {i}. {ten:16s} biên độ {vnd(bd, 1)} điểm %')

    # ---------- B3 · Giới hạn chạy lại có thật sự rẻ hơn ----------
    print('\n=== B3 · Giới hạn số lần chạy: chi phí cả hệ thống ===')
    print(f"{'Giới hạn':9s} {'Tổng trợ lý':>13s} {'Không TC':>9s} {'Cả hệ thống':>13s} {'cps':>7s}")
    b3 = {}
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - kq['thanh_cong']
        he_thong = kq['tong'] + khong_tc * BASELINE  # nhân viên làm thay mỗi ca không thành công
        b3[k] = (he_thong, kq['cps'], khong_tc)
        print(f"{k} lần     {vnd(kq['tong']):>13s} {khong_tc:>9d} {vnd(he_thong):>13s} {vnd(kq['cps']):>7s}")
    k_re = min(b3, key=lambda k: b3[k][0])
    k_cps = min(b3, key=lambda k: b3[k][1])
    print(f'Rẻ nhất cho công ty: {k_re} lần ({vnd(b3[k_re][0])} đ) · cps thấp nhất: {k_cps} lần'
          f' ({vnd(b3[k_cps][1])} đ), đẩy thêm {b3[k_cps][2] - b3[k_re][2]} việc sang nhân viên [simulated]')

    # ---------- B4 · Nếu phải xem lại tất cả (noi_dia + hang_nang) ----------
    print('\n=== B4 · Xem lại 100% trong phạm vi noi_dia + hang_nang ===')
    PHUT_XEM_LAI_100 = 5   # phút xem lại mỗi yêu cầu có kết quả (giả định đề)
    PHUT_LAM_LAI_DE = 9    # phút làm lại mỗi ca (giả định đề)
    pv_runs = runs[runs.request_id.isin(pv.request_id)]
    so_co_ok = pv_runs.loc[pv_runs.status == 'ok', 'request_id'].nunique()
    so_lam_lai = int((pv.ket_qua == 'lam_lai').sum())
    token_tool_pv = (pv_runs.tokens_in / 1000 * GIA_VAO + pv_runs.tokens_out / 1000 * GIA_RA
                     + pv_runs.tool_calls * GIA_TOOL).sum()
    tc_pv = int((pv.ket_qua == 'thanh_cong').sum())

    def cps_b4(phut_xem, phut_lam):
        return (so_co_ok * phut_xem * LUONG_PHUT + so_lam_lai * phut_lam * LUONG_PHUT + token_tool_pv) / tc_pv

    tien_xem = so_co_ok * PHUT_XEM_LAI_100 * LUONG_PHUT
    tien_lam = so_lam_lai * PHUT_LAM_LAI_DE * LUONG_PHUT
    print(f'Yêu cầu có ≥1 lần chạy ok: {so_co_ok} × {PHUT_XEM_LAI_100} phút → {vnd(tien_xem)} đ')
    print(f'Ca lam_lai: {so_lam_lai} × {PHUT_LAM_LAI_DE} phút → {vnd(tien_lam)} đ')
    print(f'Token + tool mọi lần chạy của {len(pv)} yêu cầu: {vnd(token_tool_pv)} đ')
    c9 = cps_b4(PHUT_XEM_LAI_100, PHUT_LAM_LAI_DE)
    print(f'cps = {vnd(tien_xem + tien_lam + token_tool_pv)} / {tc_pv} = {vnd(c9)} đ'
          f' = {vnd(c9 / BASELINE, 2)}× của 12.000 đ [simulated]')
    # Độ nhạy theo phút làm lại thực tế trong dữ liệu
    phut_lam_tb = reqs.loc[reqs.ket_qua == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    c_tt = cps_b4(PHUT_XEM_LAI_100, phut_lam_tb)
    print(f'Nếu làm lại {vnd(phut_lam_tb, 1)} phút/ca (trung bình dữ liệu): cps = {vnd(c_tt)} đ'
          f' = {vnd(c_tt / BASELINE, 2)}× [simulated]')
    # Hoà vốn: số phút xem lại tối đa để cps ≤ 12.000 đ
    for phut_lam in [PHUT_LAM_LAI_DE, phut_lam_tb]:
        x = (BASELINE * tc_pv - so_lam_lai * phut_lam * LUONG_PHUT - token_tool_pv) / (so_co_ok * LUONG_PHUT)
        print(f'  Hoà vốn (làm lại {vnd(phut_lam, 1)} phút): mỗi lần xem lại ≤ {vnd(x, 1)} phút [simulated]')

    # ---------- D1 · Cỡ mẫu theo ba cách chia ----------
    print('\n=== D1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02) ===')
    from statistics import NormalDist
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower

    P1, MDE, ALPHA, POWER, ICC = 0.70, 0.05, 0.05, 0.80, 0.02

    def co_mau(p1, p2, alpha=ALPHA, power=POWER):
        """Cỡ mẫu mỗi nhóm khi chia theo yêu cầu (so sánh hai tỉ lệ, hai phía)."""
        za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
        pb = (p1 + p2) / 2
        return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                          + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)

    def he_so_thiet_ke(m, icc=ICC):
        return 1 + (m - 1) * icc

    def n_hieu_dung(c, m, icc=ICC):
        """Cỡ mẫu hiệu dụng của c cụm, mỗi cụm m yêu cầu; luôn < c / ICC."""
        return c * m / he_so_thiet_ke(m, icc)

    # a) Chia theo yêu cầu
    n_a = co_mau(P1, P1 + MDE)
    print(f'a) Theo yêu cầu: co_mau(0,70; 0,75) = {vnd(n_a)} yêu cầu mỗi nhóm')

    # b) Theo nhân viên, m = 75 yêu cầu mỗi người
    m_b = 75
    de_b = he_so_thiet_ke(m_b)
    n_b = math.ceil(n_a * de_b)
    nv_b = math.ceil(n_b / m_b)
    so_nv = 40  # quy mô công ty theo đề: khoảng 40 nhân viên CSKH (CSV chỉ có 20 người của 6 depot chạy thử)
    print(f'b) Theo nhân viên, m = {m_b}: DE = {vnd(de_b, 2)}; n = {vnd(n_a)} × {vnd(de_b, 2)} = {vnd(n_b)}'
          f' mỗi nhóm → {nv_b} người mỗi nhóm, tổng {2 * nv_b} > {so_nv} nhân viên: KHÔNG ĐỦ NGƯỜI')

    # c) 20 nhân viên mỗi nhóm: trần cỡ mẫu hiệu dụng c / ICC khi m → ∞
    tran_c = 20 / ICC
    print(f'c) 20 nhân viên mỗi nhóm: n hiệu dụng < 20 / {vnd(ICC, 2)} = {vnd(tran_c)}'
          f' {"<" if tran_c < n_a else "≥"} {vnd(n_a)}: {"KHÔNG ĐẠT" if tran_c < n_a else "ĐẠT"}')

    # d) 6 depot mỗi nhóm
    tran_d = 6 / ICC
    print(f'd) 6 depot mỗi nhóm: n hiệu dụng < 6 / {vnd(ICC, 2)} = {vnd(tran_d)} (và chỉ 6 cụm < 20): KHÔNG ĐẠT')

    # e) Mức chênh 6 điểm, 20 nhân viên mỗi nhóm: giải 20m / (1 + (m-1)·ICC) ≥ n_e
    n_e = co_mau(P1, P1 + 0.06)
    c_e = 20
    m_e = math.ceil(n_e * (1 - ICC) / (c_e - n_e * ICC))
    de_e = he_so_thiet_ke(m_e)
    print(f'e) Mức chênh 6 điểm: n = {vnd(n_e)} mỗi nhóm; 20m / (1 + (m − 1) × 0,02) ≥ {n_e}'
          f' → m ≥ {m_e} yêu cầu mỗi người (DE {vnd(de_e, 2)}, n hiệu dụng {vnd(n_hieu_dung(c_e, m_e), 0)})')
    # Thời gian gom đủ m_e yêu cầu mỗi người: 1.500 yc/ngày chia 40 người, chỉ phần trong phạm vi noi_dia + hang_nang
    yc_ngay_nv = 1500 / so_nv * len(pv) / len(reqs)
    print(f'   Tổng {vnd(2 * c_e * m_e)} yêu cầu; mỗi người ~{vnd(yc_ngay_nv, 1)} yc trong phạm vi/ngày'
          f' → cần ~{math.ceil(m_e / yc_ngay_nv)} ngày làm việc ở bước 0.50 [quy mô từ đề]')

    # Đánh đổi: thiết kế cho 6 điểm nhưng tác động thật chỉ 5 điểm thì power còn bao nhiêu?
    es5 = proportion_effectsize(P1 + MDE, P1)
    power_5 = NormalIndPower().power(effect_size=es5, nobs1=n_e, alpha=ALPHA, ratio=1.0)
    print(f'Đánh đổi: n = {n_e}/nhóm, nếu tác động thật chỉ 5 điểm thì power = {vnd(power_5, 2)} (< 0,80)')
    # Kiểm tra chéo công thức tay với statsmodels (arcsine, nên lệch nhẹ)
    n_sm = NormalIndPower().solve_power(effect_size=es5, alpha=ALPHA, power=POWER, ratio=1.0)
    print(f'Đối chiếu statsmodels (arcsine): {vnd(n_sm, 0)} mỗi nhóm cho 5 điểm (lệch {pct((n_sm / n_a - 1) * 100)})')

    # Dữ liệu thực tế về cụm trong mẫu 1.200 yêu cầu
    yc_moi_nv = reqs.groupby('staff_id').size()
    print(f'Mẫu CSV: {reqs.staff_id.nunique()} nhân viên, {reqs.depot.nunique()} depot; trung bình'
          f' {vnd(yc_moi_nv.mean(), 1)} yc/nhân viên (min {yc_moi_nv.min()}, max {yc_moi_nv.max()})')

    # ---------- D3 · Tỉ lệ mở lại hiện tại trước khi đặt luật an toàn ----------
    print('\n=== D3 · Tỉ lệ mo_lai_trong_7_ngay hiện tại ===')
    mo_lai = reqs.mo_lai_trong_7_ngay.astype(int)
    print(f'Toàn bộ: {vnd(mo_lai.mean() * 100, 2)}% ({mo_lai.sum()}/{len(reqs)})')
    mo_lai_pv = pv.mo_lai_trong_7_ngay.astype(int)
    print(f'Phạm vi noi_dia + hang_nang: {vnd(mo_lai_pv.mean() * 100, 2)}% ({mo_lai_pv.sum()}/{len(pv)})')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs.loai == loai].mo_lai_trong_7_ngay.astype(int)
        print(f'  {loai:10s} {vnd(r.mean() * 100, 2):>6s}% ({r.sum()}/{len(r)})')
    print('→ Ngưỡng tuyệt đối 3% sẽ dừng pilot ngay tuần đầu; dùng chênh so với đối chứng ≥ +2 điểm, trần tuyệt đối 6%')
    # Chỉ số chính hiện tại (không có đối chứng, chỉ để tham khảo)
    chinh = ((reqs.dong_trong_24h.astype(int) == 1) & (mo_lai == 0)).mean()
    chinh_pv = ((pv.dong_trong_24h.astype(int) == 1) & (mo_lai_pv == 0)).mean()
    print(f'Chỉ số chính trong đợt chạy thử: {vnd(chinh * 100, 2)}% toàn bộ · {vnd(chinh_pv * 100, 2)}% trong phạm vi'
          f' (chưa có đối chứng, không kết luận tác động)')
