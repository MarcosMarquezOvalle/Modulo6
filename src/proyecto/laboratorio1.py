from __future__ import annotations

import csv
import json
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def csv_to_json(csv_path: str = "file.csv", json_path: str = "file.json"):
    """Read a CSV file, convert each row to a dict, and save it as JSON."""
    csv_file = Path(csv_path)
    json_file = Path(json_path)

    logger.debug("Trying to read CSV file: %s", csv_file)

    if not csv_file.exists():
        logger.error("CSV file not found: %s", csv_file)
        raise FileNotFoundError(f"CSV file not found: {csv_file}")

    with csv_file.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if not rows:
        logger.warning("CSV file is empty: %s", csv_file)
        return []

    logger.info("Loaded %d rows from %s", len(rows), csv_file)
    logger.debug("Sample row: %s", rows[0])

    json_file.parent.mkdir(parents=True, exist_ok=True)
    with json_file.open("w", encoding="utf-8") as file:
        json.dump(rows, file, ensure_ascii=False, indent=2)

    logger.info("JSON file created successfully: %s", json_file)
    logger.warning("This is a warning example for logging level demonstration.")
    logger.error("This is an error example for logging level demonstration.")
    logger.critical("This is a critical example for logging level demonstration.")

    return rows


def main():
    csv_path: str = "file.csv"
    json_path: str = "file.json"

    logger.info("Starting CSV-to-JSON conversion")
    csv_to_json(csv_path, json_path)
    logger.info("Process finished successfully")


if __name__ == "__main__":
    main()
