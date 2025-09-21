import pytest
from pathlib import Path

from avro_cli.services.avro_service import AvroService


def test_inspect_file():
    test_file = Path(__file__).parent.parent / "data" / "1.a.avro"
    if not test_file.exists():
        pytest.skip("Test file 1.a.avro not found")

    service = AvroService(str(test_file))
    result = service.inspect_file()

    assert "file" in result
    assert "schema" in result
    assert "metadata" in result
    assert "record_count" in result
    assert result["record_count"] == 1


def test_get_head_records():
    test_file = Path(__file__).parent.parent / "data" / "1.a.avro"
    if not test_file.exists():
        pytest.skip("Test file 1.a.avro not found")

    service = AvroService(str(test_file))
    result = service.get_head_records(5)

    assert "file" in result
    assert "records_shown" in result
    assert "records" in result
    assert len(result["records"]) == 1
    assert result["records_shown"] == 1


def test_get_head_records_with_limit():
    test_file = Path(__file__).parent.parent / "data" / "1.a.avro"
    if not test_file.exists():
        pytest.skip("Test file 1.a.avro not found")

    service = AvroService(str(test_file))
    result = service.get_head_records(1)

    assert result["records_shown"] == 1
    assert len(result["records"]) == 1


def test_invalid_file():
    with pytest.raises(FileNotFoundError):
        AvroService("nonexistent.avro")
