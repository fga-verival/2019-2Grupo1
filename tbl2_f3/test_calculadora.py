import unittest
import math


def get_taxa_tributacao(n_dias):
    if n_dias <= 180:
        return 0.225
    elif n_dias > 180 and n_dias <= 360:
        return 0.2
    elif n_dias > 360 and n_dias <= 720:
        return 0.175
    else:
        return 0.15


def calcula_imposto(n_dias, valor_inicial, taxa_anual):

    taxa_dia = math.pow((taxa_anual + 1),  (1/365)) - 1

    redimento_bruto = (
        valor_inicial * (1 + (taxa_dia * n_dias))) - valor_inicial

    tipo_tributacao = get_taxa_tributacao(n_dias)

    imp_pago = redimento_bruto * tipo_tributacao

    redimento_liquido = (redimento_bruto - imp_pago) / valor_inicial

    return [round(redimento_bruto, 2), round(imp_pago, 2), round(redimento_liquido, 2)]


class TesteCalculaCDB(unittest.TestCase):

    def test_redimento_bruto(self):
        self.assertEqual(calcula_imposto(60, 1000, 0.085)[0], 13.41)

    def test_imp_pago(self):
        self.assertEqual(calcula_imposto(60, 1000, 0.085)[1], 3.02)

    def test_redimento_liquido(self):
        self.assertEqual(calcula_imposto(60, 1000, 0.085)[2], 0.01)


if __name__ == "__main__":
    unittest.main()
