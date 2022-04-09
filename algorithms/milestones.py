# 改善前
def calc_achieve(sales, milestones):
    result = []

    for elm_mil in milestones:    
        temp_sum = 0
        for idx_sal, elm_sal in enumerate(sales):
            if temp_sum >= elm_mil:
                result.append(idx_sal)
                break
            temp_sum += elm_sal

    if sum(sales) < milestones[-1]:
        result.append(-1)

    return result


# 改善後
def calc_achieve_imp(sales, milestones):
    result = []

    for elm_mil in milestones:    
        temp_sum = 0
        for idx_sal, elm_sal in enumerate(sales):
            temp_sum += elm_sal
            if temp_sum >= elm_mil:
                result.append(idx_sal + 1)
                break

    if sum(sales) < milestones[-1]:
        result.append(-1)

    return result