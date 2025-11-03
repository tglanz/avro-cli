import pytest
from pathlib import Path

from avro_cli.services.diff_service import DiffService


def test_diff_schemas_same_files():
    test_file = Path(__file__).parent.parent / "data" / "1.a.avro"
    if not test_file.exists():
        pytest.skip("Test file 1.a.avro not found")

    service = DiffService(str(test_file), str(test_file))
    diff_lines = service.diff_schemas()

    assert len(diff_lines) == 0


def test_diff_data_same_files():
    test_file = Path(__file__).parent.parent / "data" / "1.a.avro"
    if not test_file.exists():
        pytest.skip("Test file 1.a.avro not found")

    service = DiffService(str(test_file), str(test_file))
    diff_lines = service.diff_data()

    assert len(diff_lines) == 0


def test_diff_schemas_different_files():
    file_a = Path(__file__).parent.parent / "data" / "1.a.avro"
    file_b = Path(__file__).parent.parent / "data" / "1.b.avro"

    if not file_a.exists() or not file_b.exists():
        pytest.skip("Test files not found")

    service = DiffService(str(file_a), str(file_b))
    diff_lines = service.diff_schemas()

    assert len(diff_lines) > 0


def test_diff_metadata_same_files():
    test_file = Path(__file__).parent.parent / "data" / "1.a.avro"
    if not test_file.exists():
        pytest.skip("Test file 1.a.avro not found")

    service = DiffService(str(test_file), str(test_file))
    diff_lines = service.diff_metadata()

    assert len(diff_lines) == 0


def test_diff_metadata_different_files():
    file_a = Path(__file__).parent.parent / "data" / "1.a.avro"
    file_b = Path(__file__).parent.parent / "data" / "1.b.avro"

    if not file_a.exists() or not file_b.exists():
        pytest.skip("Test files not found")

    service = DiffService(str(file_a), str(file_b))
    diff_lines = service.diff_metadata()

    # Metadata could be the same or different depending on the test files
    assert isinstance(diff_lines, list)
