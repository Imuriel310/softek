from datetime import date

class WeatherModel:

    def __init__(self,
                date = None,
                was_rainy = None):
        """Constructor"""
        self.date = date
        self.was_rainy = was_rainy

    unit_measure_id: str
    name: bool