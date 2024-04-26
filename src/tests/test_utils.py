import pytest
import pandas as pd
from datetime import date
from holidays import Singapore
from utils import is_holiday, get_holidays, year_holidays, get_global_week, wage_query, get_employee_data, get_avail_data, get_event_data
from unittest.mock import patch




def test_is_holiday():
    # Simulate a Singapore public holiday
    known_holiday = date(2024, 8, 9)  # National Day

    # Test with pre-created Singapore holidays instance
    assert is_holiday(known_holiday)

    # Test with creating holidays instance during the call
    assert not is_holiday(date(2024, 4, 18))  # Not a holiday

def test_get_global_week():
    global_week = get_global_week()
    assert isinstance(global_week, str)
    # You might want to add a format check (YYYY-MM-DD) based on your implementation


def test_wage_query():
    df_wage = wage_query()
    assert isinstance(df_wage, pd.DataFrame)
    # You might want to add assertions on specific columns or data types based on your schema


def test_get_employee_data():
    df = get_employee_data()
    assert isinstance(df, pd.DataFrame)
    assert 'emp_id' in df.columns  # Check renamed column
    # You might want to add assertions on other columns or data types based on your schema


def test_get_avail_data():
    global_week = "2024-04-18"  # Use the mocked latest week
    df_avail = get_avail_data(global_week)
    assert isinstance(df_avail, pd.DataFrame)
    # You might want to add assertions on specific columns or data types based on your schema


def test_get_event_data():
    df_events = get_event_data()
    assert isinstance(df_events, pd.DataFrame)
    # You might want to add assertions on specific columns or data types based on your schema
