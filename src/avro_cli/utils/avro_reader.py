import json
from pathlib import Path
from typing import Dict, List, Any, Iterator

import avro.datafile
import avro.io


class AvroFileReader:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        if not self.file_path.suffix.lower() == ".avro":
            raise ValueError(f"File must have .avro extension: {file_path}")

    def get_schema(self) -> Dict[str, Any]:
        with open(self.file_path, "rb") as f:
            reader = avro.datafile.DataFileReader(f, avro.io.DatumReader())
            schema = reader.meta.get("avro.schema").decode("utf-8")
            reader.close()
            return json.loads(schema)

    def get_metadata(self) -> Dict[str, Any]:
        with open(self.file_path, "rb") as f:
            reader = avro.datafile.DataFileReader(f, avro.io.DatumReader())

            metadata = {}
            for key, value in reader.meta.items():
                if isinstance(value, bytes):
                    if key == "avro.schema":
                        metadata[key] = json.loads(value.decode("utf-8"))
                    else:
                        metadata[key] = value.decode("utf-8")
                else:
                    metadata[key] = value

            reader.close()
            return metadata

    def read_records(self, limit: int = None) -> Iterator[Dict[str, Any]]:
        with open(self.file_path, "rb") as f:
            reader = avro.datafile.DataFileReader(f, avro.io.DatumReader())

            count = 0
            for record in reader:
                if limit is not None and count >= limit:
                    break
                yield record
                count += 1

            reader.close()

    def count_records(self) -> int:
        with open(self.file_path, "rb") as f:
            reader = avro.datafile.DataFileReader(f, avro.io.DatumReader())
            count = sum(1 for _ in reader)
            reader.close()
            return count
