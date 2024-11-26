import threading
import time
import logging
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List
import meteostat
import pandas as pd
from meteostat import Point

from data_analysis.data_fetcher import fetch_meteo_data


@dataclass
class Subscription:
    location: str
    callback: callable
    last_received_data: pd.DataFrame = None

class ChangeMonitor:
    def __init__(self):
        self.subscriptions = []
        self.running = False
        self.logger = self.configure_logging()

    def configure_logging(self):
        logging.config.fileConfig('configs/logging.conf')
        logger = logging.getLogger(__name__)
        return logger

    def start(self):
        if not self.running:
            self.running = True
            thread = threading.Thread(target=self.run)
            thread.start()

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            for subscription in self.subscriptions[:]:
                try:
                    new_data = fetch_meteo_data(subscription.location,
                                                datetime.now(),
                                                datetime.now() + timedelta(days=1))
                    if not new_data.empty and not new_data.equals(subscription.last_received_data):
                        subscription.callback(new_data)
                        subscription.last_received_data = new_data
                except Exception as e:
                    self.logger.warning(f"Error processing {subscription.location}: {str(e)}")
                time.sleep(60)  # Проверяем каждую минуту

    def subscribe(self, location: str, callback: callable):
        self.subscriptions.append(
            Subscription(location, callback)
        )

# Пример использования
def handle_meteo_data_change(new_data):
    print(f"New meteo data received for {new_data['location'].iloc[0]}:")
    print(new_data.head())

monitor = ChangeMonitor()
monitor.start()

monitor.subscribe("Vancouver", handle_meteo_data_change)

# Держим приложение в работе
while True:
    time.sleep(1)
