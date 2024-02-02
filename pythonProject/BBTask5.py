import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
from reportlab.pdfgen import canvas

def capture_screenshot(url):
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    screenshot_path = 'screenshot.png'
    driver.save_screenshot(screenshot_path)

    driver.quit()

    return screenshot_path

def create_pdf(image_path, pdf_path):
    img = Image.open(image_path)
    width, height = img.size

    pdf = canvas.Canvas(pdf_path, pagesize=(width, height))
    pdf.drawImage(image_path, 0, 0, width, height)
    pdf.save()

    print(f"PDF creation successful: {pdf_path}")

def main():
    webpage = 'https://google.com'
    screenshot_path = capture_screenshot(webpage)

    pdf_file = 'output.pdf'
    create_pdf(screenshot_path, pdf_file)

    # Optionally, remove the intermediate screenshot file
    os.remove(screenshot_path)

if __name__ == "__main__":
    main()
