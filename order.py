"""Модуль обработки заказов — рефакторинг."""

def calculate_item_price(item):
    """Рассчитать стоимость одного товара с учётом скидки за объём."""
    price = item['price'] * item['quantity']
    if item['type'] == 'food' and item['quantity'] > 10:
        return price * 0.9
    if item['type'] == 'drink' and item['quantity'] > 5:
        return price * 0.95
    return price

def apply_promo(total, promo):
    """Применить промокод к сумме заказа."""
    discounts = {'SALE10': 0.9, 'SALE20': 0.8, 'SALE30': 0.7}
    return total * discounts.get(promo, 1.0)

def calculate_delivery(delivery_type):
    """Вернуть стоимость доставки."""
    costs = {'express': 300, 'standard': 150}
    return costs.get(delivery_type, 0)

def apply_total_discount(total):
    """Применить скидку за большую сумму заказа."""
    if total > 5000:
        return total - 500
    if total > 2000:
        return total - 200
    return total

def process_order(order):
    """Обработать заказ."""
    if order is None:
        return "Ошибка: заказ пустой"
    if 'items' not in order:
        return "Ошибка: нет товаров"
    
    total = sum(calculate_item_price(item) for item in order['items'])
    
    if 'promo' in order:
        total = apply_promo(total, order['promo'])
    if 'delivery' in order:
        total += calculate_delivery(order['delivery'])
    
    total = apply_total_discount(total)
    return round(total, 2)
