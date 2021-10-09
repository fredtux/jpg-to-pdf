# jpg-to-pdf
Get all photos in a folder and create a PDF document with them

## Install requirements
```bash
pip install -r requirements.txt
```
## Usage (Python)
### For help
```bash
python3 jpg-to-pdf.py -h
```
### Getting files from directory and compressing
```bash
python3 jpg-to-pdf.py -i inputDirectory -o out.pdf -c
```
### Getting files from zip archive and compressing
```bash
python3 jpg-to-pdf.py -i archive.zip -z -o out.pdf -c
```
## Compressing PDFs
This script uses PDFTron. Get a key from here [https://www.pdftron.com/pws/get-key](https://www.pdftron.com/pws/get-key)

## Usage (Bash)
Make sure the **jpg-to-pdf.py** file is in the PATH. Then add the bash script to the PATH.
Make sure the bash script is executable with
```bash
chmod +x jpg-to-pdf
```
### Getting files from directory and compressing
### For help
```bash
jpg-to-pdf -h
```
### Getting files from directory and compressing
```bash
jpg-to-pdf -i inputDirectory -o out.pdf -c
```
### Getting files from zip archive and compressing
```bash
jpg-to-pdf -i archive.zip -z -o out.pdf -c
```
