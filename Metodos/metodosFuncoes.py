class metodosFuncoes:

    @staticmethod
    def meio(a, b):
        m = (b + a) / 2
        return m

    @staticmethod
    def bissectionFunction(funcao, inicio, fim, erro, num_iteracoes):
        iteracoes = []
        if num_iteracoes == 0:
            return

        if abs(funcao(inicio)) <= erro:
            iteracoes.append((inicio, fim, inicio, funcao(inicio), erro))
            return iteracoes, inicio, fim

        if abs(funcao(fim)) <= erro:
            iteracoes.append((inicio, fim, fim, funcao(fim), erro))
            return iteracoes, inicio, fim

        i = 0
        while True:
            m = metodosFuncoes.meio(inicio, fim)

            iteracoes.append((inicio, fim, m, funcao(m), erro))

            i += 1
            if abs(funcao(m)) <= erro:
                return iteracoes, inicio, fim

            if funcao(inicio) * funcao(m) < 0:
                fim = m
            else:
                inicio = m

            if (i >= num_iteracoes): return iteracoes, inicio, fim

    @staticmethod
    def meioFp(funcao, a, b):

        m = (funcao(b)*a - funcao(a)*b)/(funcao(b) - funcao(a))

        return m

    @staticmethod
    def fpFunction(funcao, inicio, fim, erro, num_iteracoes):
        iteracoes = []
        if num_iteracoes == 0:
            return iteracoes, inicio, fim

        i=0
        while True:
            m = metodosFuncoes.meioFp(funcao, inicio, fim)
            i+=1

            iteracoes.append((inicio, fim, m, funcao(m), erro))

            if abs(funcao(m)) <= erro:
                return iteracoes, inicio, fim

            if funcao(inicio) * funcao(m) < 0:
                fim = m
            else:
                inicio = m

            if (i >= num_iteracoes): return iteracoes, inicio, fim

    @staticmethod
    def newtonFunction(funcao, deriv, inicio, fim, erro, num_iteracoes):
        iteracoes = []
        xn = inicio
        if (num_iteracoes == 0): return iteracoes
        for n in range(num_iteracoes):
            fxn = funcao(xn)
            dfxn = deriv(xn)

            iteracoes.append((xn, fxn, erro))

            if abs(fxn) < erro:
                return iteracoes
            if dfxn == 0:
                return iteracoes
            xn = xn - fxn / dfxn

            if (n+1 >= num_iteracoes): return iteracoes

    @staticmethod
    def secant_method(funcao, inicio, fim, erro, num_iteracoes):
        iteracoes = []
        if (num_iteracoes == 0): return iteracoes, inicio, fim
        for i in range(num_iteracoes):
            f_x0 = funcao(inicio)
            f_x1 = funcao(fim)

            if f_x1 - f_x0 == 0:
                return iteracoes, inicio, fim

            x2 = fim - f_x1 * (fim - inicio) / (f_x1 - f_x0)

            iteracoes.append((inicio, fim, f_x0, f_x1, x2, funcao(x2)))

            if abs(x2 - fim) < erro:
                return iteracoes, inicio, fim

            inicio = fim
            fim = x2

            if (i+1 >= num_iteracoes): return iteracoes, inicio, fim