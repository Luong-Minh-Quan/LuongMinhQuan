    for i in range(len(danh_sach) // 2):
        if danh_sach[i] != danh_sach[-i - 1]:
            return False
    return True