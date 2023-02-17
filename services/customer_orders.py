import dao.customer_orders as dao
from models.customer_orders import CustomerOrdersModel
from datetime import datetime
# fechas determinantes de la temporada (season)
SPRING = {'date_1':'03/19', 'date_2':'06/19'}
SUMMER = {'date_1':'06/20', 'date_2':'09/21'}
FALL = {'date_1':'09/22', 'date_2':'12/20'}
WINTER = {'date_1':'12/21', 'date_2':'03/18'}

def get_season() -> list:
    customer_orders = dao.get_customer_orders()
    orders_season = []
    for order in customer_orders:
        order_date = order.ord_dt
        # se separa la fecha por / y se elimina el año ya que no es relavante
        order_date = order_date.split('/')
        order_date = "/".join(order_date[0:2])
        order_date = str_to_date(order_date)
        season = determinate_season(order_date)
        orders_season.append(
            CustomerOrdersModel(
                order.ord_id,
                season
            ).__dict__
        )
    return orders_season
    
def determinate_season(order_date:datetime) -> str:
    if str_to_date(SPRING['date_1']) <= order_date <= str_to_date(SPRING['date_2']):
        return "SPRING"
    if str_to_date(SUMMER['date_1']) <= order_date <= str_to_date(SUMMER['date_2']):
        return "SUMMER"
    if str_to_date(FALL['date_1']) <= order_date <= str_to_date(FALL['date_2']):
        return "FALL"
    # si no entra en ninguna de las anteriores, la estacion es WINTER   
    return "WINTER"
    

def str_to_date(date_str) -> datetime:
    return datetime.strptime(date_str, "%m/%d")