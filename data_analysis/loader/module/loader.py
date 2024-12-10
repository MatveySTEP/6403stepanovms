import logging
from datetime import datetime
import datetime as dt

from meteostat import Daily, Stations


class DataLoader:
    def __init__(self, coords: []):
        self.logger = logging.getLogger(f"data_loader")
        self.coords = coords

    def refresh(self):
        start = datetime(2015, 1, 10)
        end = datetime(2015, 1, 15)

        stations = Stations()
        stations = stations.nearby(self.coords[0], self.coords[1])
        # vancouver = stations.region('CA', 'ON')
        vancouver = stations.fetch(1)
        data = Daily(vancouver, start, end)
        try:
            self.data = data.fetch()
        except:
            self.logger.error("could not fetch data")
            return

        self.logger.debug(f"refreshed data from {start} to {end}")

    def set_coords(self, coords: []) -> None:
        self.logger.info("updated coordinates")
        self.coords = coords

    def get_data(self):
        return self.data