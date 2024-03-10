

import app.main as main

class TestMain:
  def test_csv_to_table(self):
    table = main.csv_to_table("app/storage/test.csv")
    assert len(table) == 4
    assert table[0] == ("name", "age", "height")
    assert table[1] == ("John", "23", "1.80")
    assert table[2] == ("Jane", "25", "1.70")
    assert table[3] == ("Sue", "21", "1.65")


  def test_list_to_table(self):
    table = main.list_to_table([["morning", "day", "evening"], [1, 2, 3], [4, 5, 6]])
    assert len(table) == 3
    assert table[0] == ["morning", "day", "evening"]
    assert table[1] == [1, 2, 3]
    assert table[2] == [4, 5, 6]