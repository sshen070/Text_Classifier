import sys
from pathlib import Path
import fitz
# from line_classifier import parse_pdf


def main(arg_file1: str) -> None:

    main_dir = Path(__file__).parent.parent
    print(f"Source Directory: {main_dir} \n")

    input_path = main_dir / "files" / arg_file1

    print(f"Input Path: {input_path}")

    # # parse_pdf(input_path)

    doc = fitz.open(input_path)
    print(f"Pages: {doc.page_count}")



if __name__ == "__main__":
    main(sys.argv[1])



