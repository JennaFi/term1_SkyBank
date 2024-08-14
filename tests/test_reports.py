from src.reports import spending_by_category


def test_spending_by_category(input_dataframe):
    assert spending_by_category(input_dataframe, "Аптеки", "31.12.2021") == []
