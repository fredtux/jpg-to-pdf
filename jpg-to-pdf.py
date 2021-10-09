from argparse import ArgumentParser
from os import walk, path
from fpdf import FPDF
from PIL import Image
from PDFNetPython3 import PDFDoc, Optimizer, SDFDoc, PDFNet
from zipfile import ZipFile


def get_files_list(dir):
    files = []

    # Get files
    for (root, dirs, filenames) in walk(dir):
        files.extend(filenames)
        break

    # Only JPG, JPEG and PNG
    files = [file for file in files if file.lower().endswith(('.jpg', '.png', '.jpeg'))]

    # Sort in alphabetical order
    files.sort()

    return files

def get_pdf(input_directory):
    # Initialize the PDF object
    pdf = FPDF(unit="pt", format="A4", orientation="P")
    pdf.compress = True

    # Iterate through images and add them as PDF pages
    for file in files:
        # Rotate image to be able to be put in portrait mode
        image_path = path.join(input_directory, file)
        image = Image.open(image_path)
        width, height = image.size

        if width > height:
            new_image = image.transpose(Image.ROTATE_270)
            new_image.save(image_path)

        pdf.add_page()
        pdf.set_margins(10, 20)

        max_width = 580
        max_height = 800

        scale = min(max_width / width, max_height / height)

        pdf.image(image_path, 10, 10, width * scale, height * scale)

    return pdf

def compress(input_file):
    # Get PDFTron key from https://www.pdftron.com/pws/get-key
    PDFNet.Initialize("Insert your PDFTron key here")
    doc = PDFDoc(input_file)
    doc.InitSecurityHandler()
    Optimizer.Optimize(doc)
    doc.Save(args.output, SDFDoc.e_linearized)
    doc.Close()


if __name__ == "__main__":
    # Parse arguments
    parser = ArgumentParser(description="Convert photos from a directory into a pdf")
    parser.add_argument("-i", "--input", help="Input directory/zip file (for zip archives use -z parameter)", )
    parser.add_argument("-o", "--output", help="Output file")
    parser.add_argument("-c", "--compress",
                        help="Compress final PDF using PDFTron (needs a licence key from https://www.pdftron.com/pws/get-key)",
                        action="store_true")
    parser.add_argument("-z", "--zip",
                        help="Specifies if the input is a zip archive and unarchives it in the current directory",
                        action="store_true")

    args = parser.parse_args()

    # If there is a zip archive as input, then unarchive it and update path
    if args.zip:
        with ZipFile(args.input, "r") as zip:
            input_directory = args.input[:-4]
            zip.extractall(input_directory)
            print(f"Extracted files to {input_directory}")

    else:
        input_directory = args.input

    # Get files
    files = get_files_list(input_directory)

    # Get PDF and output it
    pdf = get_pdf(input_directory)
    pdf.output(args.output, "F")

    if args.compress:
        # Compress output
        compress(args.output)
