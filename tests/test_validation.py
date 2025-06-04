import  pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


from data_loader import load_orders
from validation import validate_order_ids_unique, validate_ship_after_order, validate_no_nulls

@pytest.fixture
def orders_df():
    return load_orders()

def test_order_ids_unique(orders_df):
    assert validate_order_ids_unique(orders_df), "Duplicate Order IDs found."
    
    
def test_ship_after_order(orders_df):
    assert validate_ship_after_order(orders_df), "Some Ship Dates are before Order Dates" 
    
def test_no_nulls(orders_df):
    nulls_df = validate_no_nulls(orders_df)
    assert nulls_df.empty, "Nulls found in critical columns"
      
                
                


