""" 
Test petl.
"""
from typing import Optional, List, Any

import petl as etl

def main():
  print("Starting...")
  table = csv_to_table("app/storage/test.csv")
  table = add_column(table, "new_col", (1, 2))
  print(table)
  table1 = list_to_table([["morning", "day", "evening"], [1, 2, 3], [4, 5, 6]])
  print(table1)
  print("Done.")


def csv_to_table(path):
  # Create a table from a CSV file.
  table = etl.fromcsv(path)
  return table


def list_to_table(list: List[List[Any]]) -> etl.Table:
  # Create a table from a 2D list.
  table = etl.wrap(list)
  return table



def add_column(table: etl.Table, col_name: str, col_data: Optional[tuple]):
  # Add a column to a table.
  table2 = etl.addfield(table, col_name, lambda row: row.name.lower())
  return table2



if __name__ == '__main__':
  main()  

