import pyautogui
from PIL import Image
from PIL import ImageDraw, ImageFont
import os

# Capture a screenshot
def capture_screenshot(filename, region=None):
    if region:
        screenshot = pyautogui.screenshot(region=region)
    else:
        screenshot = pyautogui.screenshot()

    screenshot.save(filename)

# Add annotations to a screenshot
def annotate_screenshot(filename, text, x, y):
    image = Image.open(filename)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 24)
    draw.text((x, y), text, fill="red", font=font)
    image.save(filename)

# Crop a screenshot
def crop_screenshot(filename, x1, y1, x2, y2):
    image = Image.open(filename)
    cropped = image.crop((x1, y1, x2, y2))
    cropped.save(filename)

# Resize a screenshot
def resize_screenshot(filename, width, height):
    image = Image.open(filename)
    resized = image.resize((width, height))
    resized.save(filename)

# Share the screenshot on social media
def share_on_social_media(filename):
    # Implement the social media sharing logic here

if __name__ == "__main__":
    save_location = "screenshots/"
    os.makedirs(save_location, exist_ok=True)

    # Capture a screenshot of the entire screen
    capture_screenshot(os.path.join(save_location, "full_screen.png"))

    # Annotate, crop, and resize the screenshot
    annotate_screenshot(os.path.join(save_location, "full_screen.png"), "Annotated Text", 50, 50)
    crop_screenshot(os.path.join(save_location, "full_screen.png"), 100, 100, 300, 300)
    resize_screenshot(os.path.join(save_location, "full_screen.png"), 800, 600)

    # Share the screenshot on social media
    share_on_social_media(os.path.join(save_location, "full_screen.png"))
