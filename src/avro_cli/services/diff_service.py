import json
import difflib
from typing import List

from avro_cli.utils.avro_reader import AvroFileReader


class DiffService:
    def __init__(self, file1_path: str, file2_path: str):
        self.reader1 = AvroFileReader(file1_path)
        self.reader2 = AvroFileReader(file2_path)
        self.file1_path = file1_path
        self.file2_path = file2_path

    def diff_schemas(self) -> List[str]:
        schema1 = self.reader1.get_schema()
        schema2 = self.reader2.get_schema()

        schema1_str = json.dumps(schema1, indent=2, sort_keys=True)
        schema2_str = json.dumps(schema2, indent=2, sort_keys=True)

        return list(
            difflib.unified_diff(
                schema1_str.splitlines(keepends=True),
                schema2_str.splitlines(keepends=True),
                fromfile=f"{self.file1_path} (schema)",
                tofile=f"{self.file2_path} (schema)",
                lineterm="",
            )
        )

    def diff_data(self) -> List[str]:
        records1 = list(self.reader1.read_records())
        records2 = list(self.reader2.read_records())

        data1_str = json.dumps(records1, indent=2, sort_keys=True)
        data2_str = json.dumps(records2, indent=2, sort_keys=True)

        return list(
            difflib.unified_diff(
                data1_str.splitlines(keepends=True),
                data2_str.splitlines(keepends=True),
                fromfile=f"{self.file1_path} (data)",
                tofile=f"{self.file2_path} (data)",
                lineterm="",
            )
        )
