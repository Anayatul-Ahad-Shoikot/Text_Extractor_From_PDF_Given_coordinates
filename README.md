# PDF Data Extraction Tool

This Python script extracts specific text data from PDF files using pre-defined coordinates and saves the results in a CSV file. The script is particularly useful for processing batches of PDF files and extracting structured data like order and tracking information.

## Features
- Extracts text data from specific regions in PDFs based on coordinates.
- Cleans and formats the extracted data (e.g., removing characters at specific positions).
- Processes multiple PDF files in a directory.
- Saves extracted data to a CSV file for easy analysis.

## Prerequisites

Ensure you have the following installed:
- Python 3.6+
- `pdfplumber` library

Install the required library using pip:
```bash
pip install pdfplumber
```

## Directory Structure

```
project-directory/
|-- pdf_files/         # Directory containing your PDF files
|-- extracted_data.csv # Output file for the extracted data
|-- main.py          # The main Python script
```

## Configuration

- **PDF_DIR**: Directory containing the PDF files to process. Update this variable in the script if needed.
- **OUTPUT_CSV**: Path to the output CSV file where extracted data will be saved.
- **ORDER_COORDINATES** and **TRACKING_COORDINATES**: Define the coordinates (in the format `(x1, y1, x2, y2)`) for the regions of interest in the PDFs. Adjust these values as per your PDF's layout.

## Usage

1. Place your PDF files in the `pdf_files/` directory.
2. Run the script:

   ```bash
   python script.py
   ```

3. After processing, the extracted data will be saved in `extracted_data.csv`.

## Code Breakdown

### Functions

- **`remove_specific_positions(extracted_tracking_number)`**:
  As for this case extracted tracking numbers contains some extra miss detected letters/numbers in same places for each numbers. To cleans the tracking number by removing characters at specified positions.

- **`extract_text_from_pdf(pdf_path, output_writer)`**:
  Extracts order and tracking information from each PDF file and writes it to the CSV.

- **`main()`**:
  Iterates through all PDF files in the specified directory and processes them using `extract_text_from_pdf`.

## Example Output

The resulting CSV file will have the following structure:

| Page Name   | Order Info | Tracking Info |
|-------------|------------|---------------|
| file1       | 123456     | ABCDEFG       |
| file2       | 789012     | HIJKLMN       |

## Notes
- Ensure the PDF files are formatted consistently to avoid extraction errors.
- Modify the coordinate values in the script if the structure of your PDF files changes.


## Contributions

Contributions, suggestions, and improvements are welcome! Feel free to submit a pull request or raise an issue on GitHub.

## Author

**Anayatul Ahad Shoikot**

For questions or feedback, please contact: [aashoikot002@gmail.com](mailto:aashoikot002@gmail.com).
