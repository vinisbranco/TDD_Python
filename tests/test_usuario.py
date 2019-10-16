from src.leilao.dominio import Usuario, Leilao, Lance
from src.leilao.excecoes import LanceInvalido
import pytest

@pytest.fixture
def vini():
    return Usuario('Vini', 100.0)

@pytest.fixture
def leilao():
    return Leilao("Xiomi")


def test_propor_lance_menor_valor_carteira(vini, leilao):

    vini.propoe_lance(leilao, 50.0)

    assert vini.carteira == 50.0

def test_propor_lance_igual_valor_carteira(vini, leilao):

    vini.propoe_lance(leilao, 100.0)

    assert vini.carteira == 0.0

def test_propor_lance_maior_valor_carteira(vini, leilao):

    with pytest.raises(LanceInvalido):

        vini.propoe_lance(leilao, 200.0)