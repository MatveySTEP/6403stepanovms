import logging
from datetime import datetime
import datetime as dt

from meteostat import Daily

class DataLoader:
    def __init__(self, coords: []):
        self.logger = logging.getLogger(f"data_loader")
        self.coords = coords

    def refresh(self):
        end = datetime(2015, 1, 15)
        start = end - dt.timedelta(days=5)

        data = Daily(self.coords, start, end)
        try:
            self.data = data.fetch()
        except:
            self.logger.error("could not fetch data")
            return

        self.logger.info(f"refreshed data from {start} to {end}")

    def set_coords(self, coords: []) -> None:
        self.logger.info("updated coordinates")
        self.coords = coords

    def get_data(self):
        return self.data