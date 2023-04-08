from kuain import laba_2
import kuain

sdnf_expr1 = "(!a*b*c*d)+(a*b*c*d)"
sdnf_expr2 = "(!a*!b*c*d)+(!a*b*c*d)+(a*!b*c*d)+(a*b*c*d)"
sdnf_expr3 = "(!a*!b*!c*d)+(!a*!b*c*d)+(!a*b*!c*d)+(!a*b*c*d)+(a*!b*!c*d)+(a*!b*c*d)+(a*b*!c*d)+(a*b*c*d)"


def minimal_form_sdnf(expr):
    truth_table = laba_2.get_truth_table(laba_2.get_postfix(expr))
    for i, row in enumerate(truth_table):
        print(row)
        if i == 9:
            break
    minimal = kuain.first_method(expr, False)
    print(minimal, "\n----------------------------")
    return minimal


mdnf_1 = minimal_form_sdnf(sdnf_expr1)
mdnf_2 = minimal_form_sdnf(sdnf_expr2)
mdnf_3 = minimal_form_sdnf(sdnf_expr3)

print("SDNF------------------", mdnf_1, mdnf_2, mdnf_3, sep="\n")
