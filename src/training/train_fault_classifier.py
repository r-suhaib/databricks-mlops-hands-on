from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression

# preparing training data
def prepare_training_data(df):

    feature_columns = [
        "xmeas_1",
        "xmeas_2",
        "xmeas_3",
        "xmeas_1_delta1",
        "xmeas_2_delta1",
        "xmeas_3_delta1"
    ]

    assembler = VectorAssembler(
        inputCols=feature_columns,
        outputCol="features"
    )

    return assembler.transform(df)

# applying a baseline dummy logistic regression model; no sophisicated modelling for this mlops implementation
def train_model(df):

    lr = LogisticRegression(
        labelCol="faultNumber",
        featuresCol="features",
        maxIter=5
    )

    model = lr.fit(df)

    return model