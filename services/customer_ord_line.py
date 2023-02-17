import dao.customer_ord_line as dao  # imports the data access object for products
from models.customer_ord_line import CustomerOrdLineModel  # imports the model for products

def get_customer_ord_lines() -> list:
    order_numbers = dao.get_order_numbers()
    orders_status_response = []
    for order in order_numbers:
        orders_status = dao.get_order_by_order_number(order.order_number)
        final_status = calculate_order_final_status(orders_status)
        orders_status_response.append(
            CustomerOrdLineModel(
                order.order_number,
                final_status
            ).__dict__
        )
    return orders_status_response
    
def calculate_order_final_status(orders_status:list) -> list:
    # se quitan todas las ordenes canceladas debido a que no tienen prioridad
    # order_status = [ 
    #     ( order for order in orders_status if order.status != 'CANCELLED'), 
    #     None
    # ]
    order_status = filter(lambda order: order.status != 'CANCELLED', orders_status)
    order_status = list(order_status) if order_status else []
    # si el filtro queda vacio, quiere decir que todas las ordenes estan canceladas
    # por lo tanto su estatus es cancelado
    if not order_status:
        return "CANCELLED"
    has_pending = next(
        (order for order in order_status if order.status=='PENDING'), 
        None
    )
    if has_pending:
        return "PENDING"
    
    return "SHIPPED"
