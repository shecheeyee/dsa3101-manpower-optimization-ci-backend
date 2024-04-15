from datetime import date
import pandas as pd
from holidays import SG, Singapore

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

