import fitz 
from PIL import Image 
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

pdf_path = "invoice.pdf"

#open the document 
pdf_document = fitz.open(pdf_path)

if len(pdf_document) != 1 : 
    print("The pdf has more than one page. Please use the correct file")
    pdf_document.close()
    exit()


page = pdf_document.load_page(0)
pix = page.get_pixmap()

image_path = "invoice_image.png"
pix.save(image_path)
print(f"Saved PDF page as image :{image_path}")


#perform ocr on the image 
img = Image.open(image_path)
extracted_text = pytesseract.image_to_string(img, lang='eng')


#output the text 
print("Extracted Test :")
print(extracted_text)

pdf_document.close()