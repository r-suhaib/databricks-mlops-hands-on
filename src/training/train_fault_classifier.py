from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier


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
        outputCol="features",
        handleInvalid="skip"
    )

    transformed_df = assembler.transform(df)

    transformed_df = transformed_df.select(
        "faultNumber",
        "features"
    )

    transformed_df = transformed_df.na.drop()

    return transformed_df


def train_model(df):

    rf = RandomForestClassifier(
        labelCol="faultNumber",
        featuresCol="features",
        numTrees=20,
        maxDepth=5,
        seed=42
    )

    model = rf.fit(df)

    return model