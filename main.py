"""Write the out-of-office entry line to /output/entry.txt."""

from pathlib import Path

ENTRY_TEXT = "I am out of office, collecting the weekends I generated for everyone else."

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Create the output directory if needed, then write the line exactly."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY_TEXT, encoding="utf-8")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
