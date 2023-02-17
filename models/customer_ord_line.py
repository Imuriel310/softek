from datetime import date

class CustomerOrdLineModel:

    def __init__(self,
                order_number=None,
                status = None):
        """Constructor"""
        self.order_number = order_number
        self.status = status
        

    order_number: int
    status: bool