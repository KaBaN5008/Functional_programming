import csv
from io import StringIO
from typing import Optional

DATA = """date,item,quantity,price
2026-09-01,Apple,10,2.5
2026-09-02,Banana,5,3
2026-09-03,Orange,8,4
"""

# Уровень 1
def parse_csv(data: str) -> list[dict]:
    return list(csv.DictReader(StringIO(data)))


# Уровень 2
def compute_revenue(rows: list[dict]) -> float:
    return sum(
        int(row["quantity"]) * float(row["price"])
        for row in rows
    )


# Уровень 3
def top_item(rows: list[dict]) -> Optional[dict]:
    if not rows:
        return None

    return max(
        rows,
        key=lambda row: int(row["quantity"]) * float(row["price"])
    )
