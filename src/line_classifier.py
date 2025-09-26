import fitz

def parse_pdf(pdf_path: str, page_number: int) -> list[dict]:

    results = []
    doc = fitz.open(pdf_path)

    if (page_number < 1 or page_number > doc.page_count):
        print(f"Invalid page number: {page_number}. Document has {doc.page_count} pages.")
        return results

    # Holds the page object itself --> location
    page = doc.load_page(page_number - 1)

    # Extract text from the page --> raw text (str) --> lines (list)
    text: str = page.get_text("text")
    lines: list[str] = text.splitlines()
        

    for line_number, line in enumerate(lines, start=0):
        if line.strip():
            results.append({
                "Line": line_number,
                "Text": line
            })

    return results
