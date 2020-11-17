# 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input('Введите кол-во секунд:'))

minutes = seconds // 60
print(f"Это {minutes} минут")
hours = minutes // 60
print(f"Это {hours}  час(-a/-oв)")
time = seconds // 3600
print(f'Это: {hours}:{minutes}:{time}')
