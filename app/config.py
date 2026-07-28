from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_name: str = "AI-Proficient URL Shortener"
    db_path: str = "shortener.db"
    short_code_length: int = 7
    create_limit_per_minute: int = 60


def load_settings() -> Settings:
    return Settings(
        app_name=os.getenv("SHORTENER_APP_NAME", "AI-Proficient URL Shortener"),
        db_path=os.getenv("SHORTENER_DB_PATH", "shortener.db"),
        short_code_length=int(os.getenv("SHORTENER_CODE_LENGTH", "7")),
        create_limit_per_minute=int(os.getenv("SHORTENER_CREATE_LIMIT", "60")),
    )
