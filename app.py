from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_praca.receber_avaliacao('Marcio', 5)
restaurante_praca.receber_avaliacao('Alex', 4)
restaurante_praca.receber_avaliacao('Marcia', 2)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()