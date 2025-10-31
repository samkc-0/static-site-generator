import pytest
import string
from copy_static import copy_static, empty_dir
from tempfile import NamedTemporaryFile, TemporaryDirectory
from pathlib import Path


@pytest.fixture(scope="module", name="static_dir")
def static_dir():
    with TemporaryDirectory() as static:
        yield Path(static)


@pytest.fixture(scope="module", name="public_dir")
def public_dir():
    with TemporaryDirectory() as public:
        yield Path(public)


def is_empty(dir: Path):
    return len(list(dir.iterdir())) == 0


def test_temporary_directores_exist(static_dir, public_dir):
    assert static_dir.exists()
    assert static_dir.is_dir()
    assert is_empty(static_dir)

    assert public_dir.exists()
    assert public_dir.is_dir()
    assert is_empty(public_dir)


def test_create_file(static_dir):
    file = static_dir / "test.txt"
    file.write_text("test")
    assert len(list(static_dir.iterdir())) == 1


def test_create_subdir(static_dir):
    subdir = static_dir / "subdir"
    subdir.mkdir()
    assert len(list(static_dir.iterdir())) == 2
    assert len([f for f in static_dir.iterdir() if f.is_dir()]) == 1
    assert len([f for f in static_dir.iterdir() if f.is_file()]) == 1


def test_create_file_in_subdir(static_dir):
    subdir = static_dir / "subdir"
    subdir.mkdir(exist_ok=True)
    file = subdir / "test.txt"
    file.write_text("test")
    assert file.exists()


def test_copy_static(static_dir, public_dir):
    file = static_dir / "test.txt"
    file.write_text("test")
    copy_static(static_dir, public_dir)
    assert (public_dir / "test.txt").exists()
    assert (public_dir / "subdir" / "test.txt").exists()


def test_empty_dir(public_dir):
    empty_dir(public_dir)
    assert is_empty(public_dir)
