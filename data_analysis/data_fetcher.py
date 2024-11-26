import meteostat
from datetime import datetime, timedelta
import pandas as pd


def fetch_meteo_data(location: str, start_date: datetime, end_date: datetime) -> pd.DataFrame:
    # Получаем данные за указанный период
    data = meteostat.Daily(start=start_date, end=end_date)

    # Получаем координаты города
    city = meteostat.Station(name=location)
    station_data = city.fetch()

    # Фильтруем данные по выбранному городскому пункту
    filtered_data = data.filter(station_data.index)

    return filtered_data


if __name__ == "__main__":
    start_date = datetime(2015, 1, 1)
    end_date = datetime(2018, 12, 31)

    # Получаем данные для Ванкувера за 2018 год
    data = fetch_meteo_data("Vancouver", start_date, end_date)

    print(f"Total days processed: {len(data)}")
    print("\nSample of first few entries:")
    print(data.head())
