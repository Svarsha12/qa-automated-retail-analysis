import pandas as pd

def load_orders(path='data/retail_order.csv'):
    """
    Loads the retail order data
    
    parameters:
    path(str): Path to the CSV file.
    
    Returns:
    
    pd.Dataframe: The loaded DataFrame with parsed dates
    
    """
    
    return pd.read_csv(path, parse_dates=['Order Date', 'Ship Date'])


def load_calendar(path='data/calendar_table.csv'):
    """
    Loads the calendar/dates data
    
    parameters:
    path(str): Path to the calendar CSV file.
    
    Returns:
    
    pd.Dataframe: The loaded calendar DataFrame 
    
    """
    
    return pd.read_csv(path, parse_dates=['Date'])

    
