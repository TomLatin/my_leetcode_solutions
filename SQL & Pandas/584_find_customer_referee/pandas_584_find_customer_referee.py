import pandas as pd


def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    customer_not_referee_by_2 = customer[(customer["referee_id"] != 2) | (customer["referee_id"].isnull())]
    return customer_not_referee_by_2[["name"]]
