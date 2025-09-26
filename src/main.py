import sys
from pathlib import Path
from line_classifier import parse_pdf


def main(arg_file1: str, page_number: int) -> None:

    main_dir = Path(__file__).parent.parent
    print(f"Source Directory: {main_dir} \n")

    input_path = main_dir / "files" / arg_file1

    # print(f"Input Path: {input_path}")

    parsed = parse_pdf(input_path, page_number)

    for item in parsed:
        print(item)


    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <pdf_file_name> <page_number>")
        sys.exit(1)

    main(sys.argv[1], int(sys.argv[2]))



