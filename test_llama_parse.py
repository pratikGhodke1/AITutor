from llmsherpa.readers import LayoutPDFReader

llmsherpa_api_url = "http://localhost:5010/api/parseDocument?renderFormat=all"
pdf_url = "data/pdfs/iemh1a2.pdf"
pdf_reader = LayoutPDFReader(llmsherpa_api_url)
doc = pdf_reader.read_pdf(pdf_url)
print(doc.chunks())