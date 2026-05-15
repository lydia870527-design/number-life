def reduce_number(n):

    if n == 0:
        return 5

    while n > 9:

        n = sum(int(i) for i in str(n))

        if n == 0:
            return 5

    return n


def special_add(a, b):

    total = a + b

    if total == 0:
        return 5

    return reduce_number(total)


def father_gene(month, day):

    m = reduce_number(month)
    d = reduce_number(day)

    c = special_add(d, m)

    return f"{d}{m}{c}", d, m, c


def mother_gene(year):

    first = int(str(year)[:2])
    second = int(str(year)[2:])

    a = reduce_number(first)
    b = reduce_number(second)

    c = special_add(a, b)

    return f"{a}{b}{c}", a, b, c


def generate_chain(a, b):

    c = special_add(a, b)

    return f"{a}{b}{c}", c


def hidden_number(main):

    nums = [int(x) for x in str(main)]

    a = special_add(nums[0], nums[0])
    b = special_add(nums[1], nums[1])
    c = special_add(nums[2], nums[2])

    return f"{a}{b}{c}"


# ===== 五行對應 =====

number_element_map = {

    1: "金",
    6: "金",

    2: "水",
    7: "水",

    3: "火",
    8: "火",

    4: "木",
    9: "木",

    5: "土"
}


# ===== 五行相生排序 =====

cycle_order = {

    "金": ["金", "水", "木", "火", "土"],
    "水": ["水", "木", "火", "土", "金"],
    "木": ["木", "火", "土", "金", "水"],
    "火": ["火", "土", "金", "水", "木"],
    "土": ["土", "金", "水", "木", "火"]
}


def calculate(birthday):

    year, month, day = birthday.split("/")

    year = int(year)
    month = int(month)
    day = int(day)

    # ===== 父基因 =====

    father, fd, fm, fc = father_gene(month, day)

    # ===== 母基因 =====

    mother, ma, mb, mc = mother_gene(year)

    # ===== 主性格 =====

    main_personality, main_c = generate_chain(fc, mc)

    # ===== 過程 =====

    process1, p1c = generate_chain(fc, main_c)
    process2, p2c = generate_chain(mc, main_c)

    # ===== 子女下屬 =====

    children, child_c = generate_chain(p2c, p1c)

    # ===== 事業 =====

    career1, career1_c = generate_chain(fd, fc)
    career2, career2_c = generate_chain(fm, fc)

    # ===== 當下朋友 =====

    friends, friends_c = generate_chain(career1_c, career2_c)

    # ===== 婚姻 =====

    marriage1, marriage1_c = generate_chain(ma, mc)
    marriage2, marriage2_c = generate_chain(mb, mc)

    # ===== 未來 =====

    future, future_c = generate_chain(marriage1_c, marriage2_c)

    # ===== 隱藏號 =====

    hidden = hidden_number(main_personality)

    # ===== 缺失數字 =====

    core_numbers = []

    core_numbers.extend([int(x) for x in father])
    core_numbers.extend([int(x) for x in mother])

    core_numbers.append(main_c)

    missing_numbers = []

    for i in range(1, 10):

        if i not in core_numbers:
            missing_numbers.append(i)

    # ===== 五行統計核心16碼 =====

    all_numbers = []

    # 父基因 3碼
    all_numbers.extend([int(x) for x in father])

    # 母基因 3碼
    all_numbers.extend([int(x) for x in mother])

    # 主性格生成數
    all_numbers.append(main_c)

    # 子女下屬生成數
    all_numbers.append(child_c)

    # 過程1生成數
    all_numbers.append(p1c)

    # 過程2生成數
    all_numbers.append(p2c)

    # 當下朋友 3碼
    all_numbers.extend([int(x) for x in friends])

    # 未來財富 3碼
    all_numbers.extend([int(x) for x in future])

    # ===== 五行統計 =====

    element_count = {

        "金": 0,
        "水": 0,
        "木": 0,
        "火": 0,
        "土": 0
    }

    for num in all_numbers:

        element = number_element_map[num]

        element_count[element] += 1

    # ===== 主五行 =====

    main_element = number_element_map[main_c]

    # ===== 五行排序 =====

    order = cycle_order[main_element]

    # ===== 五行結果 =====

    five_result = {

        "自己": f"{order[0]}：{element_count[order[0]]}",
        "子女錢財": f"{order[1]}：{element_count[order[1]]}",
        "事業伴侶": f"{order[2]}：{element_count[order[2]]}",
        "官鬼疾病": f"{order[3]}：{element_count[order[3]]}",
        "父母貴人": f"{order[4]}：{element_count[order[4]]}"
    }

    return {

        "幾號人": main_c,

        "父基因": father,
        "母基因": mother,
        "主性格": main_personality,

        "過程1": process1,
        "過程2": process2,

        "子女下屬": children,

        "事業過程1": career1,
        "事業過程2": career2,

        "當下朋友": friends,

        "婚姻過程1": marriage1,
        "婚姻過程2": marriage2,

        "未來財富/健康/子媳": future,

        "隱藏號": hidden,

        "缺失數字": missing_numbers,

        "自身五行": five_result
    }