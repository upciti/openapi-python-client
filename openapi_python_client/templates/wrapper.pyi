from typing import Any, Dict, Optional, Union, cast
from .client import Client as InnerClient, AuthenticatedClient

from .models import (
    {% for import in imports | sort %}
    {{ import }},
    {% endfor %}
)

from .api import (
    {% for tag, collection in endpoint_collections.items() %}
    {{ tag | snakecase }},
    {% endfor %}
)

{% from "endpoint_macros.pyi" import arguments, client, kwargs %}

{% for tag, collection in endpoint_collections.items() %}

class {{ tag | pascalcase }}Api:

    def __init__(self, client: InnerClient):
        self._client = client

    {% for endpoint in collection.endpoints %}
    async def {{ endpoint.name | snakecase }}(self, {{ arguments(endpoint, False) }}):
        {% if endpoint.requires_security %}
        client = cast(AuthenticatedClient, self._client)
        {% else %}
        client = self._client
        {% endif %}
        return await {{ tag }}.{{ endpoint.name | snakecase }}.asyncio({{ kwargs(endpoint) }})

    {% endfor %}


class Sync{{ tag | pascalcase }}Api:

    def __init__(self, client: InnerClient):
        self._client = client

    {% for endpoint in collection.endpoints %}
    def {{ endpoint.name | snakecase }}(self, {{ arguments(endpoint, False) }}):
        {% if endpoint.requires_security %}
        client = cast(AuthenticatedClient, self._client)
        {% else %}
        client = self._client
        {% endif %}
        return {{ tag }}.{{ endpoint.name | snakecase }}.sync({{ kwargs(endpoint) }})

    {% endfor %}

{% endfor %}

{% for prefix in '', 'Sync' %}

class {{ prefix }}{{ client_name }}:
    def __init__(self, base_url: Optional[str] = None, timeout: float = 5.0, token: Optional[str] = None):
        if token is None:
            self.connection = InnerClient(
                base_url=base_url,
                timeout=timeout)
        else:
            self.connection = AuthenticatedClient(
                base_url=base_url,
                timeout=timeout,
                token=token)
        {% for tag, collection in endpoint_collections.items() %}
        self.{{ tag | snakecase }} = {{ prefix }}{{ tag | pascalcase }}Api(self.connection)
        {% endfor %}

{% endfor %}