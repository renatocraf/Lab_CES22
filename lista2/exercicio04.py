def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # CXalc the absolute x distance
    return dx == dy          # They clash if dx == dy

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False


def main(tamanho):
    import random
    rng = random.Random()   # Instantiate a generator

    bd = list(range(tamanho))     # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 1:
       rng.shuffle(bd)
       tries += 1
       if not has_clashes(bd):
           print("Found solution {0} in {1} tries.".format(bd, tries))
           tries = 0
           num_found += 1

print("Soluções para tamanho 4:")
main(4)
print("Soluções para tamanho 12:")
main(12)
print("Soluções para tamanho 16:")
main(16)


def maiortabuleiro(limite):
    import random
    import time
    rng = random.Random()   # Instantiate a generator
    tamanho = 12
    achou = True

    while tamanho<= limite and achou:
        bd = list(range(tamanho))     # Generate the initial permutation
        num_found = 0
        tries = 0
        tempoini = time.time()
        tempofim = time.time()
        #minuto = tempofim-tempoini
        while num_found < 1 and (tempofim-tempoini)<60:
            tempofim = time.time()
            rng.shuffle(bd)
            tries += 1
            if not has_clashes(bd):
                print("Tamanho do Tabuleiro:{0}\nSolução: {1} em {2} tentativas e {3} segundos".format(tamanho,bd, tries,round(tempofim-tempoini)))
                tries = 0
                num_found += 1
        if num_found <1:
            achou = False
        else:
            tamanho+=1
            num_found = 0
            tries = 0

    if achou == True:
        print("Aumente o limite, o tempo ainda nao foi excedido")
        tamanho -=1
    print("O tamanho foi:")
    print(tamanho)
    return tamanho

print("Procurando tabuleiro em menos de 1 minuto:")
maiortabuleiro(20)

# No geral para o meu computador a resposta foi 16