import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


print("=" * 50)
print("STOCKOUT MODEL TRAINING")
print("=" * 50)

df = pd.read_csv(
    "data/processed/ml_training_dataset.csv"
)

print("\nDATASET SHAPE")
print(df.shape)

print("\nTARGET DISTRIBUTION")
print(
    df["stockout_target"].value_counts()
)


# ==================================
# FEATURE SELECTION
# ==================================

X = df[
    [
        "weekly_consumption_velocity",
        "days_of_supply",
        "annual_consumption_value",
        "current_stock"
    ]
]

y = df["stockout_target"]

print("\nFEATURE MATRIX SHAPE")
print(X.shape)

print("\nTARGET SHAPE")
print(y.shape)




# ==================================
# TRAIN TEST SPLIT
# ==================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTRAIN TEST SPLIT")
print("-" * 50)

print("X_train :", X_train.shape)
print("X_test  :", X_test.shape)

print("y_train :", y_train.shape)
print("y_test  :", y_test.shape)



# ==================================
# LOGISTIC REGRESSION MODEL
# ==================================

model = LogisticRegression(
    class_weight="balanced",
    random_state=42,
    max_iter=1000
)

model.fit(
    X_train,
    y_train
)

print("\nMODEL TRAINED SUCCESSFULLY")



# ==================================
# PREDICTIONS
# ==================================

y_pred = model.predict(X_test)

print("\nPREDICTIONS GENERATED")



# ==================================
# EVALUATION
# ==================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nMODEL ACCURACY")
print("-" * 50)

print(f"Accuracy : {accuracy:.4f}")

print("\nCLASSIFICATION REPORT")
print("-" * 50)

print(
    classification_report(
        y_test,
        y_pred
    )
)



from sklearn.metrics import confusion_matrix

cm = confusion_matrix(
    y_test,
    y_pred
)

print("\nCONFUSION MATRIX")
print("-" * 50)

print(cm)



import joblib

joblib.dump(
    model,
    "ml/stockout_model.pkl"
)

print("\nMODEL SAVED SUCCESSFULLY")