"""
HAPT Secure Credentials Manager
-------------------------------

Handles broker credentials securely.
"""

import os
from dataclasses import dataclass


@dataclass(slots=True)
class Credentials:
    """
    Broker credentials.
    """

    username: str = ""
    password: str = ""
    api_key: str = ""
    api_secret: str = ""

    def is_complete(self) -> bool:
        """
        True when all credential fields
        have non-empty values.
        """
        return all(
            (
                self.username,
                self.password,
                self.api_key,
                self.api_secret,
            )
        )

    def redacted(self) -> str:
        """
        Safe representation for logs.
        """
        return (
            "Credentials("
            f"username={self.username!r}, "
            "password='***', "
            "api_key='***', "
            "api_secret='***'"
            ")"
        )


class CredentialsManager:
    """
    Loads credentials from the environment.
    """

    @staticmethod
    def from_environment(
        prefix: str = "HAPT",
    ) -> Credentials:
        """
        Load credentials using a prefix.

        Example:
        HAPT_USERNAME
        HAPT_PASSWORD
        HAPT_API_KEY
        HAPT_API_SECRET
        """

        return Credentials(
            username=os.getenv(f"{prefix}_USERNAME", ""),
            password=os.getenv(f"{prefix}_PASSWORD", ""),
            api_key=os.getenv(f"{prefix}_API_KEY", ""),
            api_secret=os.getenv(f"{prefix}_API_SECRET", ""),
        )
