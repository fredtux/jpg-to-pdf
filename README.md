# jpg-to-pdf
Get all photos in a folder and create a PDF document with them

## Usage
### For help
```bash
python3 jpg-to-pdf -h
```
### Getting files from directory and compressing
```bash
python3 jpg-to-pdf -i inputDirectory -o out.pdf -c
```
### Getting files from zip archive and compressing
```bash
python3 jpg-to-pdf -i archive.zip -z -o out.pdf -c
```
## Compressing PDFs
This script uses PDFTron. Get a key from here [https://www.pdftron.com/pws/get-key](https://www.pdftron.com/pws/get-key)
