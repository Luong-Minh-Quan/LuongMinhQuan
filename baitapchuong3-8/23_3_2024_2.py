def kiem_tra_doi_xung(danh_sach):
    for i in range(len(danh_sach) // 2):
        if danh_sach[i] != danh_sach[-i - 1]:
            return False
    return True

# Ví dụ
danh_sach_1 = [1, 2, 3, 2, 1]
danh_sach_2 = [1, 2, 3, 4, 5]

if kiem_tra_doi_xung(danh_sach_1):
    print("Danh sách 1 là đối xứng.")
else:
    print("Danh sách 1 không đối xứng.")

if kiem_tra_doi_xung(danh_sach_2):
    print("Danh sách 2 là đối xứng.")
else:
    print("Danh sách 2 không đối xứng.")