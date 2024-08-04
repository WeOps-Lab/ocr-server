import base64

from loguru import logger

from runnable.azure_ocr_runnable import AzureOcrRunnable
from user_types.azure_ocr_request import AzureOcrRequest
from user_types.paddle_ocr_request import PaddleOcrRequest


def test_azure_ocr_execute():
    runnable = AzureOcrRunnable()
    # read image file to base64
    with open('tests/asserts/table.png', 'rb') as f:
        img = f.read()
    base64_image = base64.b64encode(img).decode('utf-8')

    req = AzureOcrRequest(
        file=base64_image
    )
    result = runnable.execute(req)
    logger.info(result)
