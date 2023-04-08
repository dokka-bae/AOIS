variables = []


def priority(OP_1, OP_2):
    """приоритеты: !, *, +,(,)"""
    ops = list("!,*,+,(,)")
    return ops.index(OP_2) <= ops.index(OP_1)


def get_postfix(expr):
    result = []
    stack = []
    for symbol in expr:
        if symbol.isalpha():
            if not symbol in variables:
                variables.append(symbol)
            result.append(symbol)
        elif symbol == "(":
            stack.append(symbol)
        elif symbol == ")":
            while stack[-1] != "(":
                result.append(stack.pop())
            stack.pop()
        elif symbol in set("+,*,!"):
            if len(stack):
                while len(stack) and (stack[-1] == "!" or priority(symbol, stack[-1])):
                    result.append(stack.pop())
            stack.append(symbol)
    while len(stack) != 0:
        result.append(stack.pop())
    return result


def execute_logical_statement(postfix_expr, var_dictionary):
    stack = []
    for symbol in postfix_expr:
        if symbol.isalpha():
            stack.append(bool(int(var_dictionary[symbol])))
        elif symbol in set("!,+,*"):
            if symbol == "!":
                stack.append(not bool(stack.pop()))
            elif symbol == "+":
                stack.append(bool(stack.pop()) | bool(stack.pop()))
            elif symbol == "*":
                stack.append(bool(stack.pop()) & bool(stack.pop()))
    return str(stack[0])


def get_truth_table(postfix_expr):
    result = []
    variables = []
    for i in postfix_expr:
        if i.isalpha():
            if not (i in variables):
                variables.append(i)
    for i in range(2 ** len(variables)):
        table = []
        temp_row = list(str(bin(i))[2:].zfill(len(variables)))
        var_dictionary = {x: y for x, y in zip(variables, temp_row)}
        temp_row.append(execute_logical_statement(postfix_expr, var_dictionary))
        var_dictionary.clear()
        table.append(temp_row)
        result.append(table)
    return result


def get_sknf(truth_table, variables):
    target_rows = []
    result = []
    for row in truth_table:
        if row[-1][-1] == "False":
            target_rows.append(row)
    for row in target_rows:
        result.append("(")
        for i in range(len(variables)):
            if row[0][i] == "1":
                result.append(f"!{variables[i]}")
            else:
                result.append(str(variables[i]))
            result.append("+")
        result.pop()
        result.append(")")
        result.append("*")
    return result[:-1]


def get_dex_form(truth_table):
    result_dex_sknf = "("
    result_dex_sdnf = "("
    for i in range(len(truth_table)):
        if truth_table[i][-1][-1] == "True":
            result_dex_sdnf += str(i) + ","
        else:
            result_dex_sknf += str(i) + ","
    result_dex_sdnf = result_dex_sdnf[:-1] + ")"
    result_dex_sknf = result_dex_sknf[:-1] + ")"
    return result_dex_sknf, result_dex_sdnf


def get_sdnf(truth_table, variables):
    target_rows = []
    result = []
    for row in truth_table:
        if row[-1][-1] == "True":
            target_rows.append(row)
    for row in target_rows:
        result.append("(")
        for i in range(len(variables)):
            if row[0][i] == "0":
                result.append(f"!{variables[i]}")
            else:
                result.append(str(variables[i]))
            result += "*"
        result.pop()
        result += ")+"
    return result[:-1]


def get_index_form(truth_table):
    bin_index = ""
    for row in truth_table:
        if row[0][-1] == "False":
            bin_index += "0"
        else:
            bin_index += "1"
    return int(bin_index, 2)
