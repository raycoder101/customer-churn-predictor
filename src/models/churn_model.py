import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def train_model(df: pd.DataFrame):
    X = df.drop(columns=["customer_id", "churn"])
    y = df["churn"]

    categorical = ["contract"]
    numeric = ["age", "monthly_charges"]

    preprocessor = ColumnTransformer(
        [
            ("cat", OneHotEncoder(), categorical),
        ],
        remainder="passthrough",
    )

    model = Pipeline([("pre", preprocessor), ("clf", LogisticRegression())])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print(f"Accuracy: {score:.2f}")
    return model
