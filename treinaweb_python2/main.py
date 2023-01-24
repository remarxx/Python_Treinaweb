import carro
import moto

uno_vermelho = carro.Carro('vermelho', 'Flex', 1.0, 2)
uno_vermelho.ligar()

uno_vermelho.abastecer(50)
uno_vermelho.abastecer(10)
uno_vermelho.acelerar(110)
uno_vermelho.pintar('Laranja')
print(uno_vermelho.cor)


fazer = moto.Moto('Vermelha', 'Flex', 250, 2)
fazer.ligar()
fazer.abastecer(32)
fazer.abastecer(1)


