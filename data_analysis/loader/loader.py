import pandas as pd
import logging
import logging.config
from pytrends.request import TrendReq

class WeatherLoader:
    def __init__(self, timeframe='today 12-m', config_path='configs/logging.conf'):
        """Инициализация параметров поиска."""
        self.timeframe = timeframe
        logging.config.fileConfig(config_path)
        self.logger = logging.getLogger("loader")

    def get_weather_data(self):
        """Получает данные о трендах для заданного ключевого слова."""
        try:
            self.pytrends.build_payload(self.kw_list, cat=0, timeframe=self.timeframe, geo='', gprop='')
            data = self.pytrends.interest_over_time()
            if data.empty:
                self.logger.warning("No trend data retrieved.")
                return None
            return data
        except Exception as e:
            self.logger.warning(f"An error occurred: {e}")
            return None

    def get_current_weather_data(self):
        """Получает текущие данные о трендах для заданного ключевого слова."""
        try:
            self.pytrends.build_payload(self.kw_list, cat=0, timeframe='now 1-H', geo='', gprop='')
            current_data = self.pytrends.interest_over_time()
            if current_data.empty:
                self.logger.warning("No current data retrieved for the given keyword.")
                return None
            return current_data
        except Exception as e:
            self.logger.warning(f"An error occurred while fetching current trend data: {e}")
            return None
