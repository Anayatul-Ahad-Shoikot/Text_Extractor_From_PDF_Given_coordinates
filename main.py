# !pip install pdf2image pytesseract pillow
# !apt-get install -y poppler-utils tesseract-ocr


import pdfplumber
import csv
import os

# Directory containing the uploaded PDF files
PDF_DIR = "/content/pdf_files"
OUTPUT_CSV = "/content/extracted_data.csv"

# Define the coordinates for the regions of interest
# (x1, y1, x2, y2) for order information
ORDER_COORDINATES = (65, 244, 105, 256)
TRACKING_COORDINATES = (356, 115, 472, 128)

def remove_specific_positions(extracted_tracking_number):
    position = [1, 2, 5, 10, 14, 18]
    positions = [pos - 1 for pos in position] # Convert to 0-based index
    result = ''.join([char for i, char in enumerate(extracted_tracking_number) if i not in positions]) # list comprehension to filter out characters
    return result

def extract_text_from_pdf(pdf_path, output_writer):
    print(f"Processing {pdf_path}...")
    pdf_name = pdf_path.split("/")[-1]
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            # Extract text from specific coordinates
            order_text = page.crop(ORDER_COORDINATES).extract_text()
            tracking_text = page.crop(TRACKING_COORDINATES).extract_text()
            # Clean up extracted text
            order_text = order_text.strip() if order_text else ""
            tracking_text = tracking_text.strip() if tracking_text else ""
            # Apply cleaning to the extracted tracking number
            cleaned_tracking_text = remove_specific_positions(tracking_text)
            # Save to CSV
            output_writer.writerow([f"{pdf_name}", order_text, cleaned_tracking_text])

# Main function to process all PDFs and save results to CSV
def main():
    with open(OUTPUT_CSV, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["PDF Files", "Order", "Tracking Number"])
        for filename in os.listdir(PDF_DIR):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(PDF_DIR, filename)
                extract_text_from_pdf(pdf_path, writer)
    print(f"Extraction complete. Data saved to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
