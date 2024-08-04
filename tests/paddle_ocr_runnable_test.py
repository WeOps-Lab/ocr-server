import base64

from runnable.paddle_ocr_runnable import PaddleOcrRunnable
from user_types.paddle_ocr_request import PaddleOcrRequest
from loguru import logger


def test_paddle_ocr_execute():
    runnable = PaddleOcrRunnable()
    # read image file to base64
    with open('tests/asserts/table.png', 'rb') as f:
        img = f.read()
    base64_image = base64.b64encode(img).decode('utf-8')

    req = PaddleOcrRequest(
        file=base64_image
    )
    result = runnable.execute(req)
    logger.info(result)
