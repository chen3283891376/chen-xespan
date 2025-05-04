from typing import Dict

USER_AGENT: str = "1145141919810"
UNITS: Dict[str, int] = {
    "B": 1,
    "K": 1024,
    "M": 1024 ** 2,
    "G": 1024 ** 3
}

def size_to_bytes(size_str: str) -> int:
    """
    将文件大小字符串转换为字节数
    :param size_str: 文件大小字符串，例如 "5M"
    :return: 字节数
    """
    for unit, multiplier in UNITS.items():
        if unit in size_str:
            number = float(size_str.replace(unit, ""))
            return int(number * multiplier)
    return None
def get_size(size: int, r: int = 2) -> str:
    """将字节转换为可读的文件大小格式"""
    i = 0
    modes = ("B", "KB", "MB", "GB")
    while size >= 1024:
        i += 1
        size /= 1024
    return f"{round(size, r)}{modes[i]}"