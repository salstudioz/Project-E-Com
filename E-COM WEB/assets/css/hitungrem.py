def rem_to_px(rem):
    return rem * 16  # 1 rem = 16 px

# Input dari pengguna
rem_value = float(input("Masukkan nilai rem: "))
px_value = rem_to_px(rem_value)

print(f"{rem_value} rem = {px_value} px")
