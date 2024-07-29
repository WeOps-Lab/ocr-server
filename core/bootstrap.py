import uvicorn
from langserve import add_routes

from core.server_settings import server_settings
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from loguru import logger

from runnable.azure_ocr_runnable import AzureOcrRunnable
from runnable.paddle_ocr_runnable import PaddleOcrRunnable


class Bootstrap:
    def __init__(self):
        load_dotenv()
        self.app = FastAPI(title=server_settings.app_name)

    def setup_middlewares(self):
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
            expose_headers=["*"],
        )

    def setup_router(self):
        if server_settings.enable_azure_ocr:
            logger.info('启动Azure OCR服务')
            add_routes(self.app, AzureOcrRunnable().instance(), path='/azure_ocr')
        add_routes(self.app, PaddleOcrRunnable().instance(), path='/paddle_ocr')

    def start(self):
        self.setup_middlewares()
        self.setup_router()
        uvicorn.run(self.app, host=server_settings.app_host, port=server_settings.app_port)
