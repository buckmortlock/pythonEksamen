#Probability simulator

def data():
    def calc():
        sum = elv_a + elv_b + elv_c
        prob_a = elv_a/sum
        prob_b = elv_b/sum
        prob_c = elv_c/sum
        sum1 = elv_a_1+elv_a_2
        sum2 = elv_b_1+elv_b_2
        sum3 = elv_c_1+elv_c_2
        prob_a1 = elv_a_1/sum1
        prob_a2 = elv_a_2/sum1
        prob_b1 = elv_b_1/sum2
        prob_b2 = elv_b_2/sum2
        prob_c1 = elv_c_1/sum3
        prob_c2 = elv_c_2/sum3

        print(f"/{prob_a}probb = {prob_b}, probc = {prob_c}")
        print(f"proba1 = {prob_a1}, proba2 = {prob_a2}, probb1 = {prob_b1}")
        print(f"proba1 = {prob_b2}, proba2 = {prob_c1}, probb1 = {prob_c2}")

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

