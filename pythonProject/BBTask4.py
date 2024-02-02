import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pdfkit

def capture_screenshot(url):
    # Set up Chrome options
    options = Options()
    options.add_argument("--window-size=1920,1080")
    # Initialize Chrome WebDriver with options
    driver = webdriver.Chrome(options=options)

    # Navigate to the specified URL
    driver.get(url)

    # Capture a screenshot
    screenshot_path = 'screenshot.png'
    driver.save_screenshot(screenshot_path)

    # Close the browser
    driver.quit()

    return screenshot_path

def create_pdf(html_content, pdf_path):
    try:
        # Use pdfkit to convert HTML to PDF
        pdfkit.from_file(html_content, pdf_path)
        print(f"PDF creation successful: {pdf_path}")
    except Exception as e:
        print(f"PDF creation failed: {e}")

def create_html(html_path, image_path):
    # Create a simple HTML file with an <img> tag to include the screenshot
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Webpage Screenshot</title>
    </head>
    <body>
        <h1>Google Webpage Screenshot</h1>
        <img src="{image_path}" alt="Webpage Screenshot">
    </body>
    </html>
    """

    with open(html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

webpage = 'https://google.com'
html_file = 'screenshot.html'
pdf_file = 'output.pdf'

screenshot_path = capture_screenshot(webpage)
create_html(html_file, screenshot_path)
create_pdf(html_file, pdf_file)

# Optionally, remove the intermediate HTML file
os.remove(html_file)
