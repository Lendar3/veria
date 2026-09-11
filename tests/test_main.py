from pathlib import Path

from veria.main import build_corpus


def test_build_corpus(tmp_path: Path) -> None:
    (tmp_path / "file1.txt").write_text("текст1 \nefe", encoding="utf-8")
    (tmp_path / "file2.txt").write_text("текст2 \nefe", encoding="utf-8")
    file_names = []
    p = Path(tmp_path)
    for file in p.glob("*.txt"):
        file_names += [Path(file)]
    file_names.sort()
    build_corpus(file_names, tmp_path)
    assert (tmp_path / "corpus.jsonl").exists()
