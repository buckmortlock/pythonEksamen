#Probability simulator

def data():
    def calc():
        sum_a = elv_a + elv_b + elv_c
        prob_a = elv_a/sum_a
        prob_b = elv_b/sum_a
        prob_c = elv_c/sum_a

        print(f"proba = {prob_a}, probb = {prob_b}, probc = {prob_c}")

    print('Dette er en simulering som viser veivalg.')
    str_1 = str("Elven deler seg i tre. Hvor bred er elv")
    elv_a = int(input(f"{str_1} A?"))
    elv_b = int(input(f"{str_1} B?"))
    elv_c = int(input(f"{str_1} C?"))
    print('Elv[A] deler seg i to. Hvor bred er elvene?')
    elv_a_1 = int(input(f"{str_1} A1?"))
    elv_a_2 = int(input(f"{str_1} A2"))
    print('Elv[B] deler seg i to. Hvor bred er elvene?')
    elv_b_1 = int(input(f"{str_1} B1"))
    elv_b_2 = int(input(f"{str_1} B2"))
    print('Elv[C] deler seg i to. Hvor bred er elvene?')
    elv_c_1 = int(input(f"{str_1} C1?"))
    elv_c_2 = int(input(f"{str_1} C2?"))

    calc()

    return elv_a, elv_b, elv_c, elv_a_1, elv_a_2, elv_b_1, elv_b_2, elv_c_1, elv_c_2




def main():
    elv_a, elv_b, elv_c, elv_a_1, elv_a_2, elv_b_1, elv_b_2, elv_c_1, elv_c_2 = data()
    print(f"Elv 1A:{elv_a} meter bred - Elv 1B:{elv_b} meter bred - Elv 1C:{elv_c} meter bred")

main()

