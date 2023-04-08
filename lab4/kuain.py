import laba_2

"""Method Kuain"""


def first_method(expr, is_sknf):
    elements = []
    expr = expr.replace("(", "")
    expr = expr.replace(")", "")
    ch_1 = "*"
    ch_2 = "+"
    if is_sknf:
        ch_1, ch_2 = ch_2, ch_1
    elements = expr.split(ch_2)
    if len(elements) in (0, 1):
        return elements
    for i in range(len(elements)):
        elements[i] = elements[i].split(ch_1)
    result, temp = get_cluid_form(elements)
    extra = temp.copy()
    while len(result) != 0:
        result, temp = get_cluid_form(result)
        if len(temp) != 0:
            extra += temp
    for i in range(len(extra)):
        extra[i] = "".join(extra[i])
    return delete_excess_implicants(set(extra), is_sknf)


def get_cluid_form(implicants):
    result = []
    extra = []
    not_used = [0 for i in range(len(implicants))]
    for i in range(len(implicants)):
        for j in range(i + 1, len(implicants)):
            count = 0
            not_find_element = []
            for k in range(len(implicants[i])):
                if implicants[i][k] in implicants[j]:
                    count += 1
                elif (implicants[i][k] == "!" + implicants[j][k]) or (
                    implicants[j][k] == "!" + implicants[i][k]
                ):
                    not_find_element.append(implicants[i][k])
            if count == len(implicants[0]) - 1 and not_find_element != "":
                for element in not_find_element:
                    not_used[i] = 1
                    not_used[j] = 1
                    temp = implicants[i].copy()
                    temp.remove(element)
                    result.append(temp)
    for i in range(len(not_used)):
        if not_used[i] == 0:
            extra.append(implicants[i])
    return result, extra


def get_normal_form(expr, is_sknf):
    ch_1 = "*"
    ch_2 = "+"
    if is_sknf:
        ch_1, ch_2 = ch_2, ch_1
    expr = list(expr)
    for i in range(len(expr)):
        expr[i] = list(expr[i])
    for i in range(len(expr)):
        j = 0
        while j < len(expr[i]) - 1:
            if expr[i][j].isalpha() and expr[i][j + 1].isalpha():
                expr[i].insert(j + 1, ch_1)
            elif expr[i][j + 1] == "!" and expr[i][j].isalpha():
                expr[i].insert(j + 1, ch_1)
            j += 1
    for i in range(len(expr)):
        expr[i] = "".join(expr[i])
    result = "(" + f"){ch_2}(".join(expr) + ")"
    return result


def delete_excess_implicants(expr, is_sknf):
    ch_1 = "+"
    ch_2 = "*"
    if is_sknf:
        ch_1, ch_2 = ch_2, ch_1
    str_expr = get_normal_form(expr, is_sknf)
    expr_list = str_expr.split(ch_1)
    excesses = [0 for i in range(len(expr_list))]
    if len(expr_list) == 1:
        return "".join(expr_list)
    for i in range(len(expr_list)):
        temp = expr_list.pop(i)
        current_truth_table = laba_2.get_truth_table(laba_2.get_postfix(temp))
        target = get_target_rows(current_truth_table, is_sknf)
        var_vocublary = get_var_vocublary(temp, target)
        equals = execute(expr_list, var_vocublary, ch_1, is_sknf)
        excesses[i] = 1
        expr_list.insert(i, temp)
    result = []
    for i, excesse in enumerate(excesses):
        if excesse == 1:
            result.append(expr_list[i])
    return ch_1.join(result)


def execute(expr, var_vocublary, ch, is_sknf):
    vars = get_vars("".join(expr))
    additional_vars = []
    for var in vars:
        if var not in var_vocublary:
            var_vocublary[var] = "0"
            additional_vars.append(var)
    if len(additional_vars) > 1:
        return False
    first_result = laba_2.execute_logical_statement(
        laba_2.get_postfix(ch.join(expr)), var_vocublary
    )
    for var in additional_vars:
        var_vocublary[var] = "1"
    second_result = laba_2.execute_logical_statement(
        laba_2.get_postfix(ch.join(expr)), var_vocublary
    )
    target = bool(is_sknf)
    if first_result or second_result == target:
        return True
    return False


def get_var_vocublary(expr, table):
    var_vocublary = {}
    vars = get_vars(expr)
    for i, var in enumerate(vars):
        var_vocublary[var] = table[i]
    return var_vocublary


def get_normal_truth_table(truth_table):
    for i in range(len(truth_table)):
        truth_table[i] = truth_table[i][-1]
    return truth_table


def get_target_rows(table, is_sknf):
    target = "True"
    if is_sknf:
        target = "False"
    result = []
    for i in range(len(table)):
        if table[i][-1][-1] == target:
            result.append(table[i])
    return result[0][0]


def get_vars(expr):
    variables = []
    for i in expr:
        if i.isalpha():
            if not (i in variables):
                variables.append(i)
    return sorted(variables)


"""
expr = "(a+b+c+d)*(!a+b+c+d)*(!a+!b+c+d)"

truth_table = laba_2.get_truth_table(laba_2.get_postfix(expr))
sknf_expr = "".join(laba_2.get_sknf(truth_table, laba_2.variables))
sdnf_expr = "".join(laba_2.get_sdnf(truth_table, laba_2.variables))
truth_table = get_normal_truth_table(truth_table)

print("First Method SKNF: ", first_method(sknf_expr, True))
print("First Method SDNF: ", first_method(sdnf_expr, False))"""
