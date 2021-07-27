import pytesseract
from PIL import Image


def getText(path):
    text = pytesseract.image_to_string(
        Image.open(path),
        config="-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz"
    )

    return text


if __name__ == "__main__":
    path = "1627320525.png"
    print('Resolving Captcha')
    captcha_text = getText(path)
    print('Extracted Text', captcha_text)
