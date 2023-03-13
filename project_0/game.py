def game_core_v3(number) -> int:
  """Угадываем число с наименьшим количеством попыток, на каждой итерации делим диапазон значений на 2.

    Args:
        number (int, optional): Загаданное число.

    Returns:
        int: Число попыток
    """
  min = 0
  max = 100
  count = 0

  while True:
    predict = round((min+max)/2)
    count += 1
    if number == predict:
      break
    elif number > predict:
      min = predict
    elif number < predict:
      max = predict
  return print(f"Вы угадали число {number} за {count} попыток")

game_core_v3(12)