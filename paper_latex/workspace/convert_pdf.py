import fitz  # pymupdf
import os

pdf_path = "/ai-inventor/aii_data/runs/run_6gT5lHFn8559/4_gen_paper_repo/_4_assemble_paper/paper/workspace/paper.pdf"
out_dir = "/ai-inventor/aii_data/runs/run_6gT5lHFn8559/4_gen_paper_repo/_4_assemble_paper/paper/workspace/pages"
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf_path)
print(f"Total pages: {len(doc)}")
for i, page in enumerate(doc):
    mat = fitz.Matrix(150/72, 150/72)  # 150 DPI
    pix = page.get_pixmap(matrix=mat)
    out_path = f"{out_dir}/page_{i+1:02d}.png"
    pix.save(out_path)
    print(f"Saved: {out_path}")
doc.close()
print("Done.")
