import re
from typing import Any, Optional

import pydantic
from pydantic.types import SecretStr


class UserOut(pydantic.BaseModel):
    username: str
    avatar: Optional[str]

    @pydantic.validator("avatar")
    def avatar_must_be_url(cls, v):
        if not v:
            return v
        # Define a regular expression pattern to match URLs
        url_pattern = r'^https?://(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}(?:/[^/]*)*(?:\.(?:jpg|jpeg|png|gif))$'
        if "s3.amazonaws.com" not in v and not re.match(url_pattern, v):
            raise ValueError(f"Avatar must be a url. Received: {v}")
        return v

    @pydantic.validator("username")
    def username_must_be_valid(cls, v):
        if not re.match(r"^[a-zA-Z0-9_]{3,20}$", v):
            raise ValueError(
                "Username must be between 3 and 20 characters and only contain alphanumeric characters and underscores"
            )
        return v


class UserIn(pydantic.BaseModel):
    username: str
    password: SecretStr


class UserUpdate(pydantic.BaseModel):
    username: Optional[str]
    password: Optional[SecretStr]
    avatar: Optional[str]

