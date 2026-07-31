def get_latest_delta_version(
    spark,
    table_name
):

    history_df = spark.sql(
        f"DESCRIBE HISTORY {table_name}"
    )

    latest_version = (
        history_df
        .select("version")
        .first()[0]
    )

    return latest_version