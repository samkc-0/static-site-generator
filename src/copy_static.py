from pathlib import Path


def empty_dir(path: Path):
    if not path.exists():
        path.mkdir()
    for p in path.iterdir():
        if p.is_file():
            p.unlink()
        if p.is_dir():
            empty_dir(p)
            p.rmdir()
    return path


def copy_static(static: Path, public: Path):
    assert static.is_dir(), "src path must be a directory"
    assert public.is_dir(), "dst path hmust be a directory"
    for p in static.iterdir():
        if p.is_file():
            public.joinpath(p.name).write_bytes(p.read_bytes())
        if p.is_dir():
            dst = Path(public.joinpath(p.name))
            dst.mkdir(exist_ok=True)
            copy_static(p, dst)
