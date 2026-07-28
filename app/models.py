from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, HttpUrl


class CreateLinkRequest(BaseModel):
    original_url: HttpUrl
    custom_alias: Optional[str] = Field(default=None, pattern=r"^[a-zA-Z0-9_-]{4,24}$")
    created_by: Optional[str] = Field(default=None, max_length=128)
    expires_in_minutes: Optional[int] = Field(default=None, ge=1, le=60 * 24 * 365)


class CreateLinkResponse(BaseModel):
    short_code: str
    short_url: str
    original_url: HttpUrl
    created_at: datetime
    expires_at: Optional[datetime] = None
    already_exists: bool


class LinkDetailsResponse(BaseModel):
    short_code: str
    original_url: HttpUrl
    created_by: Optional[str] = None
    created_at: datetime
    expires_at: Optional[datetime] = None
    is_active: bool


class LinkStatsResponse(BaseModel):
    short_code: str
    total_clicks: int
    unique_visitors: int
    top_referrers: list[str]


class DeactivateLinkResponse(BaseModel):
    short_code: str
    deactivated: bool


class HealthResponse(BaseModel):
    status: str
    db_ok: bool
    timestamp: datetime
