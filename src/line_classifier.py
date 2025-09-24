# # import fitz

# # def parse_pdf(pdf_path: str) -> list[dict]:
# #     results = []
# #     doc = fitz.open(pdf_path)

# #     for page_num, page in enumerate(doc, start=1):
# #         text = page.get_text("text")
# #         lines = text.splitlines()
# #         for line in lines:
# #             if line.strip():
# #                 results.append({
# #                     "page": page_num,
# #                     "text": line.strip(),
# #                 })
# #     return results


