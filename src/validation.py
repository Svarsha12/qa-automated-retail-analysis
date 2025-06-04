# validation.py
CRITICAL_COLUMNS = ['Order ID', 'Order Date', 'Ship Date', 'Customer ID', 'Product ID', 'Sales']

def validate_no_nulls(df, columns=CRITICAL_COLUMNS):
    """
    Checks for null values in specified columns.
    Returns a DataFrame of rows with nulls.
    """
    null_rows = df[df[columns].isnull().any(axis=1)]
    return null_rows

def  validate_order_ids_unique(df):
    
    """
    checks that Order IDs are unique.
    
    Returns:
       bool: True if unique, False is duplicates found.
       
    
    """
    
    return df['Order ID'].is_unique


def validate_ship_after_order(df):
    
    """
    Ensures Ship Date is not before Order Date.
    
    Returns:
    bool: True if all Ship Dates are same or after Order Dates.
    
    """
    
    return(df['Ship Date'] >= df['Order Date']).all()

