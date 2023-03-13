import numpy as np

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
  # print(f"Вы угадали число {number} за {count} попыток") 
  return count

def score_game_core_v3(game_core_v3) -> int:
    """За какое количество попыток в среднем из 10000 подходов угадывает наш алгоритм
    Args:
        game_core_v3 ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000)) # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score


# RUN
if __name__ == '__main__':
   score_game_core_v3(game_core_v3)