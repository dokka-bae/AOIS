from kuain import laba_2
import kuain

sdnf_expr1 = "(!a*!b*c)+(!a*b*!c)+(a*!b*!c)+(a*b*c)"
sdnf_expr2 = "(!a*!b*c)+(!a*b*!c)+(!a*b*c)+(a*b*c)"

sknf_expr_1 = (
    "(a+b+c+d)*(a+b+c+!d)*(a+b+!c+d)*(a+b+!c+!d)*(a+!b+c+d)*(a+!b+c+!d)*(a+!b+!c+d)"
)
sknf_expr_2 = "(a+b+c+d)*(a+b+c+!d)*(a+b+!c+d)*(a+!b+!c+!d)*(!a+b+c+d)*(!a+b+c+!d)"
sknf_expr_3 = "(a+b+c+d)*(a+b+!c+!d)*(a+!b+c+d)*(a+!b+!c+!d)*(!a+b+c+d)"
sknf_expr_4 = "(a+b+c+!d)*(a+b+!c+!d)*(a+!b+c+!d)*(a+!b+!c+!d)*(!a+b+c+!d)"


def minimal_form_sknf(expr):
    truth_table = laba_2.get_truth_table(laba_2.get_postfix(expr))
    for i, row in enumerate(truth_table):
        print(row)
        if i == 9:
            break
    minimal = kuain.first_method(expr, True)
    print(minimal, "\n----------------------------")
    return minimal


def minimal_form_sdnf(expr):
    truth_table = laba_2.get_truth_table(laba_2.get_postfix(expr))
    for i, row in enumerate(truth_table):
        print(row)
        if i == 9:
            break
    minimal = kuain.first_method(expr, False)
    print(minimal, "\n----------------------------")
    return minimal


mknf_1 = minimal_form_sknf(sknf_expr_1)
mknf_2 = minimal_form_sknf(sknf_expr_2)
mknf_3 = minimal_form_sknf(sknf_expr_3)
mknf_4 = minimal_form_sknf(sknf_expr_4)

mdnf_1 = minimal_form_sdnf(sdnf_expr1)
mdnf_2 = minimal_form_sdnf(sdnf_expr2)

print("SKNF------------------", mknf_1, mknf_2, mknf_3, mknf_4, sep="\n")
print("SDNF------------------", mdnf_1, mdnf_2, sep="\n")
