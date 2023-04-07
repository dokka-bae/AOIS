import kuain
from kuain import laba_2

"""Method Kuain-MacKlaski"""


def second_method(expr, is_sknf):
    if len(expr) == 2:
        return
    truth_table = laba_2.get_truth_table(laba_2.get_postfix(expr))
    target_rows = []
    target_result = "True"
    if is_sknf:
        target_result = "False"
    for i in truth_table:
        if i[-1][-1] == target_result:
            target_rows.append(i)
    group_table = get_group_table(target_rows)
    star_group_table = get_star_group_table(group_table)
    second_star_group_table = get_star_second_group_table(star_group_table)
    final_table = []
    temp_table = []
    for i in range(len(group_table)):
        for j in range(len(group_table[i])):
            temp_table.append(group_table[i][j])
    group_table = temp_table
    temp_table = []
    for i in range(len(second_star_group_table)):
        temp_table.append(second_star_group_table[i])
    second_star_group_table = temp_table
    get_final_table(final_table, group_table, second_star_group_table)
    result = get_minimazed_function(final_table, second_star_group_table, is_sknf)
    return result


def get_group_table(table):
    result = []
    for i in range(len(table[0][0])):
        result.append([])
    for row in table:
        result[row[0].count("1")].append(row[0][:-1])
    return result


def get_star_group_table(table):
    result = []
    for i in range(len(table) - 1):
        result.append([])
    while [] in table:
        table.remove([])
    for i in range(len(table) - 1):
        for j in range(len(table[i])):
            for z in range(len(table[i + 1])):
                star_index = 0
                count_not_equal = 0
                for k in range(len(table[i][j])):
                    if table[i][j][k] != table[i + 1][z][k]:
                        star_index = k
                        count_not_equal += 1
                if count_not_equal == 1:
                    row_copy = table[i][j].copy()
                    row_copy[star_index] = "*"
                    result[star_index].append(row_copy)
    return result


def get_star_second_group_table(table):
    result = []
    for i in range(len(table)):
        if len(table[i]) == 1:
            result.append(table[i][0])
            continue
        for j in range(len(table[i]) - 1):
            for k in range(len(table[i][j])):
                if table[i][j][k] != table[i][j + 1][k]:
                    temp = table[i][j]
                    temp[k] = "*"
                    if temp not in result:
                        result.append(temp)
    return result


def get_final_table(final_table, group_table, second_star_group_table):
    for i in range(len(second_star_group_table)):
        final_table.append([])
        for j in range(len(group_table)):
            final_table[i].append("0")
    for i in range(len(second_star_group_table)):
        for k in range(len(group_table)):
            is_similiar = True
            for z in range(len(group_table[k])):
                if second_star_group_table[i][z] == "*":
                    continue
                if group_table[k][z] != second_star_group_table[i][z]:
                    is_similiar = False
            if is_similiar == True:
                final_table[i][k] = "1"


def get_minimazed_function(final_table, second_star_group_table, is_sknf):
    result = []
    negative_sknf = ""
    negative_sdnf = "!"
    sign = "+"
    if is_sknf:
        negative_sknf = "!"
        negative_sdnf = ""
        sign = "*"
    for i in range(len(final_table[0])):
        count = 0
        target_index = 0
        for j in range(len(final_table)):
            if final_table[j][i] == "1":
                count += 1
                target_index = j
        if count == 1:
            if second_star_group_table[target_index] not in result:
                result.append(second_star_group_table[target_index])
    result_string = build_min_form(result, negative_sdnf, negative_sknf, sign)
    return result_string[:-1]


def build_min_form(result, negative_sdnf, negative_sknf, sign):
    for i in range(len(result)):
        for j in range(len(result[i])):
            if result[i][j] == "0":
                result[i][j] = negative_sdnf + laba_2.variables[j]
            elif result[i][j] == "1":
                result[i][j] = negative_sknf + laba_2.variables[j]
    result_string = ""

    for i in range(len(result)):
        result_string += "".join(result[i]) + "/"
        result_string = result_string.replace("*", "")
    result_string = result_string.replace("/", sign)
    return result_string


"""Karnaugh map"""


def third_method(expr, is_sknf):
    truth_table = laba_2.get_truth_table(laba_2.get_postfix(expr))
    for i in range(len(truth_table)):
        truth_table[i] = truth_table[i][-1]
    temp_truth_table = []
    temp_truth_table.append(truth_table[0:4])
    temp_truth_table.append(truth_table[4:])
    target_symbol = "False"
    if not is_sknf:
        target_symbol = "True"
    result = get_karnaugh_map(temp_truth_table, target_symbol, is_sknf)
    return result


def get_karnaugh_map(truth_table, target_symbol, is_sknf):
    ch_1 = "*"
    ch_2 = "+"
    if is_sknf:
        ch_1, ch_2 = ch_2, ch_1
    karnaugh_map = [[" "] * 4, [" "] * 4]
    karnaugh_map_used_elements = [["0"] * 4, ["0"] * 4]
    build_karnaugh_map(truth_table, karnaugh_map, target_symbol)
    octos = get_octos(karnaugh_map, target_symbol)
    quadros = get_quadros(karnaugh_map, karnaugh_map_used_elements, target_symbol)
    pairs = get_pairs(karnaugh_map, karnaugh_map_used_elements, target_symbol)
    result = ""
    if octos:
        return ""
    if len(quadros):
        result = get_minimal_form(quadros, is_sknf)
    if len(pairs):
        result += get_minimal_form(pairs, is_sknf)
    return make_normal_view(result, is_sknf)


def build_karnaugh_map(truth_table, karnaugh_map, target_symbol):
    for i in range(2):
        for j in range(4):
            if truth_table[i - 1][j][-1] == target_symbol:
                karnaugh_map[i][j] = target_symbol
        karnaugh_map[i][-1], karnaugh_map[i][-2] = (
            karnaugh_map[i][-2],
            karnaugh_map[i][-1],
        )


def get_minimal_form(coordinats, is_sknf):
    result = ""
    char_negative = "!"
    char_positive = ""
    if not is_sknf:
        char_negative, char_positive = char_positive, char_negative
    variables_coordinats = [[0], [-2, -1], [-3, -2]]
    variables = laba_2.variables
    result = build_minimal_form(
        coordinats, variables_coordinats, char_negative, char_positive, variables
    )
    return result


def build_minimal_form(
    coordinats, variables_coordinats, char_negative, char_positive, variables
):
    result = ""
    for i in range(len(coordinats)):
        count_variables = [0, 0, 0]
        for j in range(len(coordinats[i])):
            if coordinats[i][j][0] in variables_coordinats[0]:
                count_variables[0] += 1
            else:
                count_variables[0] -= 1
            if coordinats[i][j][1] in variables_coordinats[1]:
                count_variables[1] += 1
            else:
                count_variables[1] -= 1
            if coordinats[i][j][1] in variables_coordinats[2]:
                count_variables[2] += 1
            else:
                count_variables[2] -= 1
        result += "("
        for k in range(3):
            if count_variables[k] > 0:
                result += char_negative + variables[k]
            elif count_variables[k] < 0:
                result += char_positive + variables[k]
        result += ")"
    return result


def get_octos(karnaugh_map, target_symbol):
    if karnaugh_map[0][0] == target_symbol:
        if len(set(karnaugh_map[0])) == 1:
            if len(set(karnaugh_map[1])) == 1:
                return 1
    return 0


def get_quadros(karnaugh_map, karnaugh_map_used_elements, target_symbol):
    coordinats = []
    for j in range(4):
        j *= -1
        if karnaugh_map[0][j] == target_symbol and karnaugh_map[1][j] == target_symbol:
            if (
                karnaugh_map[0][j - 1] == target_symbol
                and karnaugh_map[1][j - 1] == target_symbol
            ):
                if (
                    karnaugh_map_used_elements[0][j - 1] == "0"
                    and karnaugh_map_used_elements[1][j - 1] == "0"
                ):
                    temp = []
                    temp.append([0, j - 1])
                    temp.append([1, j - 1])
                    temp.append([0, j])
                    temp.append([1, j])
                    coordinats.append(temp.copy())
                    karnaugh_map_used_elements[0][j - 1] = "1"
                    karnaugh_map_used_elements[1][j - 1] = "1"
                    karnaugh_map_used_elements[0][j] = "1"
                    karnaugh_map_used_elements[1][j] = "1"
    for i in range(2):
        if len(set(karnaugh_map[i])) == 1:
            if karnaugh_map[i][0] == target_symbol:
                if len(set(karnaugh_map_used_elements[i])) == 2:
                    karnaugh_map_used_elements[i][1] = "1"
                    temp = [[i, 0], [i, 1], [i, 2], [i, 3]]
                    coordinats.append(temp)
    return coordinats


def get_pairs(karnaugh_map, karnaugh_map_used_elements, target_symbol):
    pairs_coordinats = []
    get_vertical_vert_pair(
        karnaugh_map, karnaugh_map_used_elements, target_symbol, pairs_coordinats
    )
    get_horizontal_hor_pair(
        karnaugh_map, karnaugh_map_used_elements, target_symbol, pairs_coordinats
    )
    get_horizontal_vert_pair(
        karnaugh_map, karnaugh_map_used_elements, target_symbol, pairs_coordinats
    )
    return pairs_coordinats


def get_horizontal_hor_pair(
    karnaugh_map, karnaugh_map_used_elements, target_symbol, pairs_coordinats
):
    for j in range(4):
        j *= -1
        for i in range(2):
            if (
                karnaugh_map[i][j] == target_symbol
                and karnaugh_map[i][j - 1] == target_symbol
            ):
                if (
                    karnaugh_map_used_elements[i][j] == "0"
                    and karnaugh_map_used_elements[i][j - 1] == "0"
                ):
                    temp = []
                    temp.append([i, j])
                    temp.append([i, j - 1])
                    pairs_coordinats.append(temp.copy())
                    karnaugh_map_used_elements[i][j] = "1"
                    karnaugh_map_used_elements[i][j - 1] = "1"
    get_horizontal_hor_or_pair(
        karnaugh_map, karnaugh_map_used_elements, target_symbol, pairs_coordinats
    )


def get_horizontal_hor_or_pair(
    karnaugh_map, karnaugh_map_used_elements, target_symbol, pairs_coordinats
):
    for j in range(4):
        j *= -1
        for i in range(2):
            if (
                karnaugh_map[i][j] == target_symbol
                and karnaugh_map[i][j - 1] == target_symbol
            ):
                if (
                    karnaugh_map_used_elements[i][j] == "0"
                    or karnaugh_map_used_elements[i][j - 1] == "0"
                ):
                    temp = []
                    temp.append([i, j])
                    temp.append([i, j - 1])
                    pairs_coordinats.append(temp.copy())
                    karnaugh_map_used_elements[i][j] = "1"
                    karnaugh_map_used_elements[i][j - 1] = "1"


def get_vertical_vert_pair(
    karnaugh_map, karnaugh_map_used_elements, target_symbol, pairs_coordinats
):
    for j in range(4):
        j *= -1
        if (
            karnaugh_map[0][j] == target_symbol
            and karnaugh_map[1][j] == target_symbol
            and "0"
            in (karnaugh_map_used_elements[0][j], karnaugh_map_used_elements[1][j])
        ):
            pairs_coordinats.append([[0, j], [1, j]])
            karnaugh_map_used_elements[0][j] = "1"
            karnaugh_map_used_elements[1][j] = "1"
        if (
            karnaugh_map[0][j] == target_symbol
            and karnaugh_map[1][j] == target_symbol
            and "0"
            in (karnaugh_map_used_elements[0][j], karnaugh_map_used_elements[1][j])
        ):
            pairs_coordinats.append([[0, j], [1, j]])
            karnaugh_map_used_elements[0][j] = "1"
            karnaugh_map_used_elements[1][j] = "1"


def get_horizontal_vert_pair(
    karnaugh_map, karnaugh_map_used_elements, target_symbol, pairs_coordinats
):
    for j in range(4):
        j *= -1
        for i, row in enumerate(karnaugh_map):
            if (
                row[j] == target_symbol
                and row[j - 1] == target_symbol
                and "0"
                in (
                    karnaugh_map_used_elements[i][j],
                    karnaugh_map_used_elements[i][j - 1],
                )
            ):
                pairs_coordinats.append([[i, j], [i, j - 1]])
                karnaugh_map_used_elements[i][j] = "1"
                karnaugh_map_used_elements[i][j - 1] = "1"


def make_normal_view(result, is_sknf):
    if is_sknf:
        result = result.replace(")(", ")*(")
    else:
        result = result.replace(")(", ")+(")
    return result


sknf_expr = kuain.sknf_expr
sdnf_expr = kuain.sdnf_expr

print("Second Method SKNF: ", second_method(sknf_expr, True))
print("Second Method SDNF: ", second_method(sdnf_expr, False))

print("Third Method SKNF: ", third_method(sknf_expr, True))
print("Third Method SDNF: ", third_method(sdnf_expr, False))
