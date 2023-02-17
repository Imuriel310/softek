

class CustomerOrdersModel:

    def __init__(self,
                ord_id = None,
                season = None,
        ):
        """Constructor"""
        self.ord_id = ord_id
        self.season = season
        

    ord_id: str
    season: str