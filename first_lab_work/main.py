import math
import argparse
import numpy as np
from parser import read_config
def calculate_y(a, b, c, x):
    return 2*x + (a * math.sin((b*x+c))**2) / (3+x)

def main():
    parser = argparse.ArgumentParser(description="Calculate function values")
    parser.add_argument('--config', default='config.yaml', help="Config file path")
    parser.add_argument('--start', type=float, default=None, help="Start value")
    parser.add_argument('--step', type=float, default=None, help="Step size")
    parser.add_argument('--end', type=float, default=None, help="End value")

    args = parser.parse_args()

    # Чтение конфигурации из файла
    config = read_config(args.config)

    # Получаем значения из конфига или аргументов командной строки
    start = args.start or config['n0']
    step = args.step or config['h']
    end = args.end or config['nk']

    # Проверка корректности диапазона
    if start >= end:
        raise ValueError("Начальное значение должно быть меньше конечного")

    # Вычисление значений функции
    x_values = np.arange(start, end + step, step)
    y_values = [calculate_y(config['a'], config['b'], config['c'], x) for x in x_values]

    # Запись результатов в файл
    with open('results.txt', 'w') as f:
        for x, y in zip(x_values, y_values):
            f.write(f"{x:.6f} {y:.6f}\n")

if __name__ == "__main__":
    main()