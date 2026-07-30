import pyreadr
from pathlib import Path

data_path = Path("data/raw")

files = list(data_path.glob("*.RData"))

print(f"Found {len(files)} files")

for file in files:
    print("\n" + "=" * 80)
    print(f"FILE: {file.name}")

    result = pyreadr.read_r(file)

    print(f"Objects found: {list(result.keys())}")

    for obj_name, df in result.items():

        print(f"\nObject: {obj_name}")

        try:
            print(f"Rows: {df.shape[0]}")
            print(f"Columns: {df.shape[1]}")

            print("\nColumns:")
            print(list(df.columns))

            print("\nSample:")
            print(df.head(3))

        except Exception as e:
            print(f"Unable to inspect object: {e}")