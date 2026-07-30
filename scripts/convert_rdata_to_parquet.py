from pathlib import Path
import pyreadr

RAW_DIR = Path("data/raw")
PARQUET_DIR = Path("data/parquet")

PARQUET_DIR.mkdir(parents=True, exist_ok=True)

for file in RAW_DIR.glob("*.RData"):

    print(f"Processing {file.name}")

    result = pyreadr.read_r(file)

    for object_name, df in result.items():

        output_file = PARQUET_DIR / f"{object_name}.parquet"

        df.to_parquet(output_file, index=False)

        print(f"Saved -> {output_file}")