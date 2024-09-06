from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import re

def parse_date(date_str, today):
    try:
        date_obj = datetime.strptime(date_str, '%d de %b. de %Y')
        return date_obj
    except ValueError:
        pass
    
    time_patterns = {
        'dia': timedelta(days=1),
        'dias': timedelta(days=1),
        'semana': timedelta(weeks=1),
        'semanas': timedelta(weeks=1),
        'mês': relativedelta(months=1),
        'meses': relativedelta(months=1),
        'ano': relativedelta(years=1),
        'anos': relativedelta(years=1)
    }
    
    for key, delta in time_patterns.items():
        if key in date_str:
            number = int(re.search(r'\d+', date_str).group())
            return today - (delta * number)
    
    return None
