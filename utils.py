"""Вспомогательные утилиты."""

def is_palindrome(text):
    """Проверить, является ли строка палиндромом."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def count_words(text):
    """Подсчитать количество слов в строке."""
    if not text.strip():
        return 0
    return len(text.split())

def celsius_to_fahrenheit(celsius):
    """Перевести градусы Цельсия в Фаренгейт."""
    return celsius * 9 / 5 + 32
