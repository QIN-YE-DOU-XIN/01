with open("001.txt", "r+", encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)
    # 选择奇数行（索引从0开始，所以0, 2, 4...是奇数行）
    odd_lines = [lines[i] for i in range(len(lines)) if i % 2 == 0]
    print(odd_lines)

    """1123"""