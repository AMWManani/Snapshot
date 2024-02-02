import subprocess

def convert_to_pdf_linux(docx_path, pdf_path):
    try:
        # Use unoconv command-line tool to convert docx to pdf
        subprocess.run(['unoconv', '-f', 'pdf', docx_path])
        print(f"Conversion successful: {pdf_path}")
    except Exception as e:
        print(f"Conversion failed: {e}")

# Replace the convert_to_pdf function in your original code with the new one
convert_to_pdf = convert_to_pdf_linux
