"""Модуль обработки заказов."""

def process_order(order):
    """Обработать заказ — сложная функция."""
    if order is None:
        return "Ошибка: заказ пустой"
    if 'items' not in order:
        return "Ошибка: нет товаров"

    total = 0
    for item in order['items']:
        if item['type'] == 'food':
            if item['quantity'] > 10:
                total += item['price'] * item['quantity'] * 0.9
            else:
                total += item['price'] * item['quantity']
        elif item['type'] == 'drink':
            if item['quantity'] > 5:
                total += item['price'] * item['quantity'] * 0.95
            else:
                total += item['price'] * item['quantity']
        else:
            total += item['price'] * item['quantity']

    if 'promo' in order:
        if order['promo'] == 'SALE10':
            total *= 0.9
        elif order['promo'] == 'SALE20':
            total *= 0.8
        elif order['promo'] == 'SALE30':
            total *= 0.7

    if 'delivery' in order:
        if order['delivery'] == 'express':
            total += 300
        elif order['delivery'] == 'standard':
            total += 150
        else:
            total += 0

    if total > 5000:
        total -= 500
    elif total > 2000:
        total -= 200

    return round(total, 2)
