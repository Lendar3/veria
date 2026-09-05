import json
from pathlib import Path


def jsonl_creation(filenames: list[str]) -> None:
    with open("./data/stage1/corpus.jsonl", "w", encoding="utf-8") as jsonl:
        for source in filenames:
            with open("./" + source, "r", encoding="utf-8") as f:
                raw_text = f.read()
            title, main_text = raw_text.split("\n", 1)
            main_text = main_text.strip()
            data = {
                "id": Path(source).stem,
                "title": title,
                "text": main_text,
                "source": source,
            }
            jsonl.write(json.dumps(data, ensure_ascii=False) + "\n")


def main() -> None:
    file_names = []
    p = Path("./data/stage1/")
    for file in p.glob("local-search-*.txt"):
        file_names += [str(file)]
    file_names.sort()
    jsonl_creation(file_names)


if __name__ == "__main__":
    main()
