def calcular_descuento(monto_total, porcentaje_descuento=12):
    """
    Calcula el monto del descuento basado en el monto total de la compra y el porcentaje de descuento.

    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (valor predeterminado es 10%).
    :return: Monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Llamadas a la función

# Primera llamada con el valor predeterminado para el porcentaje de descuento
monto_total_1 = 200.0
descuento_1 = calcular_descuento(monto_total_1)
monto_final_1 = monto_total_1 - descuento_1
print(
    f"Para un monto total de ${monto_total_1:.2f} con un descuento del 12%, el monto del descuento es ${descuento_1:.2f} y el monto final a pagar es ${monto_final_1:.2f}.")

# Segunda llamada especificando un porcentaje de descuento diferente
monto_total_2 = 150.0
porcentaje_descuento_2 = 20
descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
monto_final_2 = monto_total_2 - descuento_2
print(
    f"Para un monto total de ${monto_total_2:.2f} con un descuento del {porcentaje_descuento_2}%, el monto del descuento es ${descuento_2:.2f} y el monto final a pagar es ${monto_final_2:.2f}.")
