import dao.weather as dao
from models.weather import  WeatherModel



def detect_weather_change() ->list:
    dates = list(dao.get_rainy_days())
    # se salta el primer elemento ya que no se tiene informacion del dia anterior
    bad_weather_days = []
    for i in range(1,len(dates)):
        if dates[i].was_rainy != 1:
            # si no esta lloviendo, se continua con el siguiente dia
            continue
        rained = previous_day_was_raining(dates, i)
        if rained is False:   
            bad_weather_days.append(
                WeatherModel(
                    dates[i].date,
                    True
                ).__dict__
            )
    return bad_weather_days
            
def previous_day_was_raining(dates, i):
    # se verifica el anterior dia, para ver si llovio
    # si llovio se regresa true
    if dates[i-1].was_rainy == 0:
        return False
    return True