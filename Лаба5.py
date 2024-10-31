# Входные данные: количество сувениров и безделушек
souvenirs = int(input("Введите количество сувениров: "))  # Сувенир весит 70 грамм
trinkets = int(input("Введите количество безделушек: "))  # Безделушка весит 140 грамм

# Вес сувениров и безделушек
weight_souvenir = 70
weight_trinket = 140

# Вычисляем общий вес посылки
total_weight = (souvenirs * weight_souvenir) + (trinkets * weight_trinket)

# Выводим результат
print("Итоговый вес посылки:", total_weight, "грамм")