from src.models.churn_model import load_data, train_model


def test_load_data():
    df = load_data("data/churn.csv")
    assert not df.empty
    assert "churn" in df.columns


def test_train_model():
    df = load_data("data/churn.csv")
    model = train_model(df)
    assert model is not None
