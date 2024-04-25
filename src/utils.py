from datetime import date,datetime, timedelta 
import pandas as pd
from holidays import SG, Singapore
from db_utils import execute_query

def sg_holidays():
  """
  This function creates and returns a holidays.Singapore instance containing 
  all Singaporean public holidays.

  Returns:
      holidays.Singapore: An instance containing Singaporean public holidays.
  """
  return Singapore()

def is_holiday(date, sg_holidays=None):
  """
  This function checks if a given date is a public holiday in Singapore.

  Args:
      date (datetime.date): The date to check.
      sg_holidays (holidays.Singapore, optional): An optional Singapore holidays instance. 
          If not provided, a new instance will be created.

  Returns:
      bool: True if the date is a public holiday, False otherwise.
  """
  if sg_holidays is None:
      sg_holidays = Singapore()  # Create Singapore holidays instance if not provided
  return date in sg_holidays

def get_holidays(year):
  """
  This function retrieves public holidays for a specific year in Singapore.

  Args:
      year (int): The year for which to retrieve holidays.

  Returns:
      holidays.HolidayBase: A dictionary-like object containing public holidays for the year.
  """
  return Singapore(years=[year])



def year_holidays(year):
  """
  This function takes a year as input and returns a DataFrame containing
  public holidays in Singapore for that year with index starting from 1 
  and 'Date' as a separate column.

  Args:
      year (int): The year for which to retrieve holidays.

  Returns:
      pandas.DataFrame: A DataFrame with columns 'Date' and 'Name' containing
                        public holiday information with index starting from 1.
  """
  data = {'Date': [],
          'Holiday': []}  # Create an empty dictionary to store data
  for date, name in sorted(SG(years=year).items()):
      data["Date"].append(date)
      data["Holiday"].append(name)

  # Create DataFrame from dictionary outside the loop
  df= pd.DataFrame(data)
  return df



def get_global_week():
  # Get sunday of the current week
  today = datetime.now()
  sunday = today - timedelta(days=today.weekday() + 1)
  sunday_formatted = sunday.strftime("%Y-%m-%d")
  return sunday_formatted


def wage_query():
  """
  Retrieves all data from the 'Wage' table.

  Returns:
      pandas.DataFrame: A DataFrame containing wage data. (Also prints the DataFrame)
  """
  query = "SELECT * FROM Wage"
  wage_query = execute_query(query)
  df_wage = pd.DataFrame(wage_query)
  return df_wage

def get_employee_data():
  """
  Retrieves all data from the 'Employees' table and renames the 'emp_id' column to 'id'.

  Returns:
      pandas.DataFrame: A DataFrame containing employee data 
  """
  query = "SELECT * FROM Employees"
  employee_query = execute_query(query)
  df = pd.DataFrame(employee_query)
  return df

def get_avail_data(global_week):
  """
  Retrieves availability data for the specified 'global_week' from the 'Availability' table.

  Args:
      global_week (str): The week as a string formatted as 'YYYY-MM-DD'.

  Returns:
      pandas.DataFrame: A DataFrame containing availability data for the given week
  """
  query = "SELECT * FROM Availability WHERE week = '%s' " % (global_week) 
  avail_query = execute_query(query)
  df_avail = pd.DataFrame(avail_query)
  return df_avail

def get_event_data():
  """
  Retrieves all data from the 'Events' table.

  Returns:
      pandas.DataFrame: A DataFrame containing event data. (Also prints the DataFrame)
  """
  query = "SELECT * FROM Events"
  event_query = execute_query(query)
  df_events = pd.DataFrame(event_query)
  return df_events



