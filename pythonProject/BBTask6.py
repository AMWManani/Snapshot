import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def capture_screenshot(url):
    options = Options()
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    screenshot_path = 'screenshot.png'
    driver.save_screenshot(screenshot_path)

    print ("Capturing Screenshot...")

    driver.quit()

    return screenshot_path

def create_pdf(image_path, pdf_path):
    img = Image.open(image_path)
    width, height = A4

    pdf = canvas.Canvas(pdf_path, pagesize=A4)

    # Header
    pdf.setFont("Helvetica-Bold", 9)
    pdf.drawCentredString(width // 2, height - 20, "Webpage Screenshot Task")

    # Cover Page
    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawCentredString(width // 2, height // 2, "Google Webpage Screenshot")

    # Footer
    pdf.setFont("Helvetica-Bold", 9)
    pdf.drawCentredString(width // 2, 20, "Wesley 2024")

    pdf.showPage()

    # Header
    pdf.setFont("Helvetica-Bold", 9)
    pdf.drawCentredString(width // 2, height - 20, "Webpage Screenshot Task")

    # Screenshot Page
    pdf.drawImage(image_path, 0, 0, width, height, preserveAspectRatio=True)

    # Footer
    pdf.setFont("Helvetica-Bold", 9)
    pdf.drawCentredString(width // 2, 20, "Wesley 2024")

    pdf.save()

    print(f"PDF creation successful: {pdf_path}")

def main():
    webpage = input("Enter target url") 
    screenshot_path = capture_screenshot(webpage)

    pdf_file = 'output.pdf'
    create_pdf(screenshot_path, pdf_file)

    # Optionally, remove the intermediate screenshot file
    #os.remove(screenshot_path)

main()
