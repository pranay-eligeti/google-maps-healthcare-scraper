"""CSV export utilities."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

OUTPUT_COLUMNS = ["name", "address", "phone", "email", "specialty", "state", "source_url"]


def export_csv(records: list[dict[str, str]], output_path: str | Path) -> Path:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(records, columns=OUTPUT_COLUMNS).to_csv(path, index=False)
    return path
