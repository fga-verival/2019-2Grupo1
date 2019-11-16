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

    redimento_liquido = ((redimento_bruto - imp_pago) / valor_inicial)*100

    return [round(redimento_bruto, 2), round(imp_pago, 2), round(redimento_liquido, 2)]


class TesteCalculaCDB(unittest.TestCase):

    def test_redimento_bruto(self):
        self.assertEqual(calcula_imposto(60, 1000, 0.085)[0], 13.41)
        self.assertEqual(calcula_imposto(120, 500, 0.08)[0], 12.65)
        self.assertEqual(calcula_imposto(240, 3000, 0.09)[0], 170.01)
        self.assertEqual(calcula_imposto(270, 2000, 0.085)[0], 120.71)
        self.assertEqual(calcula_imposto(390, 100, 0.075)[0], 7.73)

    def test_imp_pago(self):
        self.assertEqual(calcula_imposto(60, 1000, 0.085)[1], 3.02)
        self.assertEqual(calcula_imposto(120, 500, 0.08)[1], 2.85)
        self.assertEqual(calcula_imposto(240, 3000, 0.09)[1], 34.0)
        self.assertEqual(calcula_imposto(270, 2000, 0.085)[1], 24.14)
        self.assertEqual(calcula_imposto(390, 100, 0.075)[1], 1.35)

    def test_redimento_liquido(self):
        self.assertEqual(calcula_imposto(60, 1000, 0.085)[2], 1.04)
        self.assertEqual(calcula_imposto(120, 500, 0.08)[2], 1.96)
        self.assertEqual(calcula_imposto(240, 3000, 0.09)[2], 4.53)
        self.assertEqual(calcula_imposto(270, 2000, 0.085)[2], 4.83)
        self.assertEqual(calcula_imposto(390, 100, 0.075)[2], 6.38)


if __name__ == "__main__":
    unittest.main()
