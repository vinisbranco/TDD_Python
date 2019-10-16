from unittest import TestCase
from src.leilao.dominio import Usuario, Leilao, Lance
from src.leilao.excecoes import LanceInvalido

class TestLeilao(TestCase):

    def setUp(self):
        self.leo = Usuario("Leo", 500.0)
        self.vini = Usuario("Vini", 1500.0)
        self.joice = Usuario("Joice", 100.0)

        
        self.lance_vini = Lance(self.vini, 1300.0)
        self.lance_leo = Lance(self.leo, 300.0)
        self.lance_joice = Lance(self.joice, 30.0)

        self.leilao = Leilao("Iphone XS")


    def test_decrescente(self):

        with self.assertRaises(LanceInvalido):           
            self.leilao.propoe(self.lance_leo)
            self.leilao.propoe(self.lance_vini)
            self.leilao.propoe(self.lance_joice)

    def test_crescente(self):
            
            self.leilao.propoe(self.lance_joice)
            self.leilao.propoe(self.lance_leo)
            self.leilao.propoe(self.lance_vini)

            menor_valor_esperado = 30.0
            maior_valor_esperado = 1300.0

            self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
            self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_um_lance(self):
            
            self.leilao.propoe(self.lance_vini)

            menor_valor_esperado = 1300.0
            maior_valor_esperado = 1300.0

            self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
            self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
    
    def test_insere_lance_lista_vazia(self):
            
            self.leilao.propoe(self.lance_vini)

            self.assertEqual(1, len(self.leilao.lances))

    def test_insere_lance_usuario_diferente(self):
            
            self.leilao.propoe(self.lance_leo)
            self.leilao.propoe(self.lance_vini)

            self.assertEqual(2, len(self.leilao.lances))
            
    def test_insere_lance_usuario_igual(self):
            
        with self.assertRaises(LanceInvalido):    
            lance_vini1400 = Lance(self.vini, 1400.0)
            self.leilao.propoe(self.lance_vini)
            self.leilao.propoe(lance_vini1400)

            

    def test_lance_maior_anterior_positivo(self):
            
            self.leilao.propoe(self.lance_joice)
            self.leilao.propoe(self.lance_vini)            

            self.assertEqual(2, len(self.leilao.lances))

    def test_lance_maior_anterior_negativo(self):
            
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_vini) 
            self.leilao.propoe(self.lance_joice)
            