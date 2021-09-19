import numpy as np

def random_predict(number: int =1) -> int:
    """Угадываем число, используя алгорим бинарного поиска

    Args:
        number (int, optional): Загаданное число. 
        По умолчанию = 1.

    Returns:
        int: Число попыток
    """
    
    # Будем выбирать догадки в диапазоне между
    # left_rorder и right_border
    left_border = 0
    rigth_border = 100
    
    # счётчик попыток
    count = 0
    
    while True:
        count += 1
        
        # догадку берём как середину диапазона
        my_guess = left_border + int((rigth_border-left_border+1) / 2)
        
        # если угадали
        if my_guess == number:
            return count
        # если догадка меньше загаданного числа,
        # то сдвигаем левую границу диапазона
        elif my_guess < number:
            left_border = my_guess
        # если догадка больше загаданного числа,
        # то сдвигаем праую границу диапазона
        else:
            rigth_border = my_guess
   

def game_score(iterations: int=1000) -> float:
    """Подсчёт среднего числа попыток отгадываний,
        на iterations повторений

    Args:
        iterations (int, optional): Число повторений. Defaults to 1000.

    Returns:
        float: Среднее количество попыток при 1000 повторений
    """
    # фиксируем seed для воспроизводимости результата
    # при вызове функции возврата случайного числа

    np.random.seed(0)
    
    # Здесь будем сохранять количество попыток отгадываний
    result_list = []

    for i in range(iterations):
        # генерируем случайное число между 1 и 100
        number = np.random.randint(1,101)
        
        # запуск алгоритма угадывания
        result = random_predict(number)
        result_list.append(result)

    # считаем средее число попыток
    average_score = np.average(result_list)
    return average_score
    
if __name__ == "__main__":
    print(game_score(1000))