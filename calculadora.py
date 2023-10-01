import time
class Calculadora:
    def __init__(self):
        print("Bem-vindo(a) à sua calculadora!")
        print("Atenção essa calculadora só realiza operações básicas!")
        time.sleep(1)
        print("Digite 1 para somar")
        print("Digite 2 para subtrair")
        print("Digite 3 para multiplicar")
        print("Digite 4 para dividir")
        print("Digite 5 para potenciar")
        print("Digite 6 para radiciar")
        print("Digite 7 para sair")
        self.escolha = input("Digite aqui a sua escolha: ")
        while self.escolha not in ['1', '2', '3', '4', '5', '6', '7']:
            self.escolha = input("Digite aqui sua escolha corretamente!:")
    def Soma(self):
        self.a = int(input("Digite um número: "))
        self.b = int(input("Digite outro número: "))
        simnum = input("Deseja somar mais um número? s/n: ")
        while simnum not in ['s', 'n']:
            simnum = input("Digite corretamente! Deseja somar mais um número? (s/n): ")
        while simnum == "s":
            maisnum = int(input("Digite um número: "))
            self.a += maisnum
            simnum = input("Deseja somar mais um número? s/n: ")
            while simnum not in ['s', 'n']:
                simnum = input("Digite corretamente! Deseja somar mais um número? (s/n): ")
        return self.a + self.b

    def Subtração(self):
        self.a = int(input("Digite um número: "))
        self.b = int(input("Digite outro número: "))
        simnum2 = input("Deseja subtrair mais um número? s/n: ")
        while simnum2 not in ['s', 'n']:
            simnum2 = input("Digite corretamente! Deseja subtrair mais um número? (s/n): ")
        while simnum2 == "s":
            menusnum = int(input("Digite um número: "))
            self.b += menusnum
            simnum2 = input("Deseja subtrair mais um número? s/n: ")
            while simnum2 not in ['s', 'n']:
                simnum2 = input("Digite corretamente! Deseja subtrair mais um número? (s/n): ")
        return self.a - self.b

    def Multiplicação(self):
        self.a = int(input("Digite um número: "))
        self.b = int(input("Digite outro número: "))
        simnum3 = input("Deseja multiplicar mais um número? s/n: ")
        while simnum3 not in ['s', 'n']:
            simnum3 = input("Digite corretamente! Deseja multiplicar mais um número? (s/n): ")
        while simnum3 == "s":
            multinum = int(input("Digite um número: "))
            self.b *= multinum
            simnum3 = input("Deseja multiplicar mais um número? s/n: ")
            while simnum3 not in ['s', 'n']:
                simnum3 = input("Digite corretamente! Deseja multiplicar mais um número? (s/n): ")
        return self.a * self.b

    def Divisão(self):
        self.a = float(input("Digite um número: "))
        self.b = float(input("Digite outro número: "))
        simnum4 = input("Deseja dividir por mais um número? s/n: ")
        while simnum4 not in ['s', 'n']:
            simnum4 = input("Digite corretamente! Deseja dividir por mais um número? (s/n): ")
        while simnum4 == "s":
            divinum = float(input("Digite um número: "))
            if divinum == 0:
                print("Não é possível dividir por zero.")
            else:
                self.a = self.a / self.b
                self.b = divinum
            simnum4 = input("Deseja dividir por mais um número? s/n: ")
            while simnum4 not in ['s', 'n']:
                simnum4 = input("Digite corretamente! Deseja dividir por mais um número? (s/n): ")
        return self.a / self.b

    def Potenciação(self):
        self.a = int(input("Digite a base: "))
        self.b = int(input("Digite o expoente: "))
        resultadopo = self.a ** self.b
        simnum5 = input("Deseja potenciar o expoente? (s/n): ")
        while simnum5 not in ['s', 'n']:
            simnum5 = input("Digite corretamente! Deseja potenciar o expoente? (s/n): ")
        while simnum5 == "s":
            novo_expoente1 = int(input("Digite mais um potenciador: "))
            resultadopo **= novo_expoente1
            simnum5 = input("Deseja potenciar o expoente novamente? (s/n): ")
            while simnum5 not in ['s', 'n']:
                simnum5 = input("Digite corretamente! Deseja potenciar o expoente? (s/n): ")
        print("O resultado da potenciação é:", resultadopo)

    def Radiciação(self):
        self.a = int(input("Digite a base: "))
        self.b = int(input("Digite o expoente, o índice da raiz: "))
        resultado_radiciacao = self.a ** (1 / self.b)
        simnum6 = input("Deseja radiciar esta radiciação? (s/n): ")
        while simnum6 not in ['s', 'n']:
            simnum6 = input("Digite corretamente! Deseja radiciar esta radiciação? (s/n): ")
        while simnum6 == "s":
            novo_expoente2 = int(input("Digite um novo expoente: "))
            resultado_radiciacao **= (1 / novo_expoente2)
            simnum6 = input("Deseja radiciar esta radiciação? (s/n): ")
            while simnum6 not in ['s', 'n']:
                simnum6 = input("Digite corretamente! Deseja radiciar esta radiciação? (s/n): ")
        print("O resultado da radiciação é:", resultado_radiciacao)

##################################################################################

c1 = Calculadora()
if c1.escolha == "1":
    resultado = c1.Soma()
    print("O resultado da soma é:", resultado)
    time.sleep(5)

if c1.escolha == "2":
    resultado2 = c1.Subtração()
    print("O resultado da subtração é:", resultado2)
    time.sleep(5)

if c1.escolha == "3":
    resultado3 = c1.Multiplicação()
    print("O resultado da multiplicação é:", resultado3)
    time.sleep(5)

if c1.escolha == "4":
    resultado4 = c1.Divisão()
    print("O resultado da divisão é:", resultado4)
    time.sleep(5)

if c1.escolha == "5":
    c1.Potenciação()

if c1.escolha == "6":
    c1.Radiciação()

if c1.escolha == "7":
    print("Tchauzinho!")
    time.sleep(5)


#não está pronta
#GreatestSteph



