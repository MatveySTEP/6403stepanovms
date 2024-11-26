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

    @type_check((int,))
    def moving_average(self, window: int) -> None:
        """
        Вычисляет скользящее среднее значение температуры за заданное окно.

        Аргументы:
            window (int): Размер окна для скользящего среднего значения.
        """
        ma_column = f'moving_average_{window}'
        self.data[ma_column] = self.data['tavg'].rolling(window=window).mean()

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

    @type_check((int,int,))
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
    def find_extrema(self, window: int = 3) -> pd.Series:
        """
        Находит экстремальные значения скользящего среднего.

        Аргументы:
            window (int): Размер окна для скользящего среднего значения.

        Возвращает:
            pd.Series: Экстремальные значения скользящего среднего.
        """
        ma_column = f'moving_average_{window}'
        if ma_column not in self.data:
            self.moving_average(window)
        extrema = self.data[ma_column][self.data[ma_column].diff().ne(0)]
        self.data['extrema'] = extrema
        return extrema


if __name__ == "__main__":
    pass
