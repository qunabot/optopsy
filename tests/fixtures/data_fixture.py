import pytest

@pytest.fixture
def full_data_set():
    curr_file = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(curr_file, "../test_data/data_full.csv")

    return pd.read_csv(
        filepath(), parse_dates=["expiration", "quote_date"], infer_datetime_format=True
    )