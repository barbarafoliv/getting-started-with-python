# Mathematical Function Calculation

import math
if __name__=='__main__':
    X=float(input("Insert value of X: "))
    Y=float(input("Insert value of Y: "))
    F=(Y+math.sqrt(abs(2*X+10)))/(2*X)
    print(f"F({X:1.0f},{Y:1.0f}) ={F:6.3f}")

# 6 em {F:6.3f} especifica a largura mínima da saída formatada. Garante que F seja exibido com pelo menos 6 caracteres.
# .3f em {F:6.3f} indica que o valor de F deve ser formatado como um número de ponto flutuante com 3 casas decimais.
