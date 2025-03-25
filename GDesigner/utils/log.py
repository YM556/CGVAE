# GDesigner/utils/log.py
import logging

logger = logging.getLogger("GDesigner")
logger.setLevel(logging.INFO)

# 添加控制台日志处理器
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(console_handler)
