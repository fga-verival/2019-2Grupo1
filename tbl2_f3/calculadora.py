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

    print("taxa dia:")

    redimento_bruto = (
        valor_inicial * (1 + (taxa_dia * n_dias))) - valor_inicial

    tipo_tributacao = get_taxa_tributacao(n_dias)

    imp_pago = redimento_bruto * tipo_tributacao

    redimento_liquido = (redimento_bruto - imp_pago) / valor_inicial

    return {
        "redimento_bruto": redimento_bruto,
        "imposto_de_renda": imp_pago,
        "redimento_liquido": redimento_liquido,
    }


if __name__ == "__main__":
    a = calcula_imposto(60, 1000, 0.085)

    print(a)
