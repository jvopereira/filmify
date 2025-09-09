"""Logger configuration module with custom formatting and color support"""
import logging
import sys
from typing import Optional

class CustomFormatter(logging.Formatter):
    """Custom log formatter with colors for better readability."""

    # ANSI escape codes for colors
    COLORS = {
        "DEBUG": "\033[94m",   # Blue
        "INFO": "\033[92m",    # Green
        "WARNING": "\033[93m", # Yellow
        "ERROR": "\033[91m",   # Red
        "CRITICAL": "\033[95m" # Magenta
    }
    RESET = "\033[0m"

    def format(self, record: logging.LogRecord) -> str:
        """Format log message with colors and structured output.

        Args:
            record (logging.LogRecord): The log record instance.

        Returns:
            str: The formatted log message with color.
        """
        log_color = self.COLORS.get(record.levelname, self.RESET)
        asctime = self.formatTime(record, "%Y-%m-%d %H:%M:%S")
        message = record.getMessage()

        formatted_message = (
            f"{log_color}[{record.levelname}] {asctime} "
            f"{record.name}: {message}{self.RESET}"
        )
        return formatted_message


def get_logger(
    name: Optional[str] = None,
    level: int = logging.INFO
) -> logging.Logger:
    """Create and configure a logger instance.

    Args:
        name (Optional[str], optional): Name of the logger. Defaults to None (root logger).
        level (int, optional): Logging level. Defaults to logging.INFO.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger_instance = logging.getLogger(name)
    logger_instance.setLevel(level)

    # Prevent duplicated handlers
    if not logger_instance.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)

        formatter = CustomFormatter()
        handler.setFormatter(formatter)
        logger_instance.addHandler(handler)

    return logger_instance


# Default logger for global usage
logger = get_logger("filmify")
