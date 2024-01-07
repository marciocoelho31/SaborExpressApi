from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('Praça', 'Gourmet')

bebida_suco_caju = Bebida('Suco de Caju', 8.0, 'Grande')
prato_sanduiche = Prato('Sanduiche', 11.0, 'Sanduiche Natural')
sobremesa_sundae = Sobremesa('Sundae', 15.0, 'Sundae de Chocolate')

bebida_suco_caju.aplicar_desconto()
prato_sanduiche.aplicar_desconto()
sobremesa_sundae.aplicar_desconto()

restaurante_praca.adicionar_item_no_cardapio(bebida_suco_caju)
restaurante_praca.adicionar_item_no_cardapio(prato_sanduiche)
restaurante_praca.adicionar_item_no_cardapio(sobremesa_sundae)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()