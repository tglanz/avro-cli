import json
from pathlib import Path
from typing import Dict, List, Any

from avro_cli.utils.avro_reader import AvroFileReader


class AvroService:
    def __init__(self, file_path: str):
        self.reader = AvroFileReader(file_path)
        self.file_path = Path(file_path)

    def inspect_file(self) -> Dict[str, Any]:
        return {
            "file": str(self.file_path.resolve()),
            "schema": self.reader.get_schema(),
            "metadata": self.reader.get_metadata(),
            "record_count": self.reader.count_records(),
        }

    def get_head_records(self, num_records: int = 5) -> Dict[str, Any]:
        records = list(self.reader.read_records(limit=num_records))
        return {
            "file": str(self.file_path.resolve()),
            "records_shown": len(records),
            "records": records,
        }
