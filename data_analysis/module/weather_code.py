import numpy as np
import pandas as pd

from data_analysis.module.check_data_types import type_check


class WeatherData:
    """
    Класс для работы с погодными данными.

    Атрибуты:
        data (pd.DataFrame): Данные о погоде.
    """

    @type_check((pd.DataFrame,))
    def __init__(self, data: pd.DataFrame) -> None:
        """
        Инициализирует объект WeatherData.

        Аргументы:
            data (pd.DataFrame): Данные о погоде.
        """
        self.data = data

    def get_data(self) -> pd.DataFrame:
        """
        Возвращает данные о погоде.

        Возвращает:
            pd.DataFrame: Данные о погоде.
        """
        return self.data

    # def find_maxima(self) -> pd.Series:
    #     """Находит локальные максимумы во временном ряду."""
    #    #  maxima = [np.nan]
    #    #  maxima.extend(
    #    #      [self.data[i] if (self.data[i - 1] < self.data[i] > self.data[i + 1]) else np.nan
    #    #       for i in range(1, len(self.data) - 1)]
    #    #  )
    #    #  maxima.append(np.nan)
    #    # # self.logger.info(f"Analysis found maxima")
    #    #  return maxima
    #     return pd.Series(self.get_data())
    def find_max(self, window: int) -> None:
        """
        Вычисляет максимальное значение температуры за заданное окно.

        Аргументы:
            window (int): Размер окна для поиска максимального значения.
        """
        max_column = f'max_{window}'
        self.data[max_column] = self.data['tavg'].rolling(window=window).max()

    def find_min(self, window: int) -> None:
        """
        Вычисляет максимальное значение температуры за заданное окно.

        Аргументы:
            window (int): Размер окна для поиска максимального значения.
        """
        max_column = f'min_{window}'
        self.data[max_column] = self.data['tavg'].rolling(window=window).min()
    @type_check((int,))
    def moving_average(self, window: int) -> None:
        """
        Вычисляет скользящее среднее значение температуры за заданное окно.

        Аргументы:
            window (int): Размер окна для скользящего среднего значения.
        """
        ma_column = f'moving_average_{window}'
        self.data[ma_column] = self.data['tavg'].rolling(window=window).mean()
    # def moving_average(self, window_size: int = 3) -> pd.Series:
    #     """Вычисляет скользящее среднее для временного ряда с заданным размером окна."""
    #     moving_average = [np.nan] * (window_size - 1)
    #     moving_average.extend(self.data.rolling(window=window_size).mean()[window_size - 1:])
    #     return pd.Series(moving_average)

    def calculate_difference(self, window: int = 3) -> None:
        """
        Вычисляет разницу между последовательными значениями скользящего среднего.

        Аргументы:
            window (int): Размер окна для скользящего среднего значения.
        """
        ma_column = f'moving_average_{window}'
        if ma_column not in self.data:
            self.moving_average(window)
        self.data['temperature_difference'] = self.data[ma_column].diff()

    @type_check((int, int,))
    def autocorrelation(self, lag: int, window: int) -> None:
        """
        Вычисляет автокорреляцию скользящего среднего с заданным лагом.

        Аргументы:
            lag (int): Лаг для автокорреляции.
            window (int): Размер окна для скользящего среднего значения.
        """
        ma_column = f'moving_average_{window}'
        if ma_column not in self.data:
            self.moving_average(window)
        autocorr_value = self.data[ma_column].autocorr(lag)
        self.data[f'autocorrelation_lag_{lag}'] = autocorr_value

    @type_check((int,))
    # def find_extrema(self, window: int = 3) -> pd.Series:
    #     """
    #     Находит экстремальные значения скользящего среднего.
    #
    #     Аргументы:
    #         window (int): Размер окна для скользящего среднего значения.
    #
    #     Возвращает:
    #         pd.Series: Экстремальные значения скользящего среднего.
    #     """
    #     ma_column = f'moving_average_{window}'
    #     if ma_column not in self.data:
    #         self.moving_average(window)
    #     extrema = self.data[ma_column][self.data[ma_column].diff().ne(0)]
    #     self.data['extrema'] = extrema
    #     return extrema


    def find_minima(self) -> pd.Series:
        """Находит локальные минимумы во временном ряду."""
        minima = [np.nan]
        minima.extend(
            [self.data[i] if (self.data[i - 1] > self.data[i] < self.data[i + 1]) else np.nan
             for i in range(1, len(self.data) - 1)]
        )
        minima.append(np.nan)
        self.logger.info(f"Analysis found minima")
        return minima


if __name__ == "__main__":
    pass
