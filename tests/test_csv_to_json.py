import json
import tempfile
import unittest
from pathlib import Path

from proyecto.csv_to_json import csv_to_json


class CsvToJsonTests(unittest.TestCase):
    def test_csv_to_json_converts_rows_to_json(self):
        csv_content = "name,age,city\nAna,28,Bogota\nLuis,32,Madrid\n"

        with tempfile.TemporaryDirectory() as tmp_dir:
            csv_path = Path(tmp_dir) / "people.csv"
            json_path = Path(tmp_dir) / "people.json"

            csv_path.write_text(csv_content, encoding="utf-8")

            result = csv_to_json(str(csv_path), str(json_path))

            self.assertEqual(result, [
                {"name": "Ana", "age": "28", "city": "Bogota"},
                {"name": "Luis", "age": "32", "city": "Madrid"},
            ])

            saved = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(saved, result)


if __name__ == "__main__":
    unittest.main()
