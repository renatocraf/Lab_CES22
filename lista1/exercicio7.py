def sum_of_squares(xs):
    sum = 0
    for i in range(len(xs)):
        sum = sum+ xs[i]*xs[i]

    return sum

# definindo a função teste
def test(bool):
    if bool:
        print("Teste OK")
    else:
        print("Teste falhou")

#testes
test(sum_of_squares([2, 3, 4])==29)
test(sum_of_squares([])==0)
test(sum_of_squares([2, -3, 4])==29)
