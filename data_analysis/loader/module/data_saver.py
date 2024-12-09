import logging

import pandas as pd


def save_to_excel(data: pd.DataFrame, filename: str):
    """
        Сохраняет данные в формате Excel.

        Аргументы:
        data (pd.DataFrame): Данные для сохранения.
        filename (str): Имя файла для сохранения.

        Возвращает:
        None
        """
    logger = logging.getLogger(f"analysis")
    if data is not None:
        data.to_excel(filename, index=False)
        print(f"Данные успешно сохранены в {filename}")
        logger.debug(" данных для сохранения.")
    else:
        logger.warning("Нет данных для сохранения.")
        print("Нет данных для сохранения.")
