import os
from typing import Dict, Optional

import attr


@attr.s(auto_attribs=True)
class Client:
    """ A class for keeping track of data related to the API """

    base_url: Optional[str] = attr.ib(None, kw_only=True)
    cookies: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    headers: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    timeout: float = attr.ib(5.0, kw_only=True)

    def __attrs_post_init__(self) -> None:
        env_base_url = os.environ.get("MY_TEST_API_BASE_URL")
        self.base_url = self.base_url or env_base_url
        if self.base_url is None:
            raise ValueError(
                f'"base_url" has to be set either from the '
                f'environment variable "{env_base_url}", or '
                f'passed with the "base_url" argument'
            )

    def get_headers(self) -> Dict[str, str]:
        """ Get headers to be used in all endpoints """
        return {**self.headers}

    def with_headers(self, headers: Dict[str, str]) -> "Client":
        """ Get a new client matching this one with additional headers """
        return attr.evolve(self, headers={**self.headers, **headers})

    def get_cookies(self) -> Dict[str, str]:
        return {**self.cookies}

    def with_cookies(self, cookies: Dict[str, str]) -> "Client":
        """ Get a new client matching this one with additional cookies """
        return attr.evolve(self, cookies={**self.cookies, **cookies})

    def get_timeout(self) -> float:
        return self.timeout

    def with_timeout(self, timeout: float) -> "Client":
        """ Get a new client matching this one with a new timeout (in seconds) """
        return attr.evolve(self, timeout=timeout)


@attr.s(auto_attribs=True)
class AuthenticatedClient(Client):
    """ A Client which has been authenticated for use on secured endpoints """

    token: str

    def get_headers(self) -> Dict[str, str]:
        """ Get headers to be used in authenticated endpoints """
        return {"Authorization": f"Bearer {self.token}", **self.headers}
