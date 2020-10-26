import datetime
from typing import List, Optional, Union

from dateutil.parser import isoparse

from .api import tests
from .client import AuthenticatedClient
from .client import Client as InnerClient
from .models import (
    AModel,
    AnEnum,
    AnIntEnum,
    BodyUploadFileTestsUploadPost,
    HTTPValidationError,
    ModelWithUnionProperty,
    TestInlineObjectsJsonBody,
    TestInlineObjectsResponse_200,
)
from .types import UNSET, File, Response, Unset


class TestsApi:
    def __init__(self, client: InnerClient):
        self._client = client

    async def get_user_list(
        self,
        *,
        an_enum_value: List[AnEnum],
        some_date: Union[datetime.date, datetime.datetime],
    ) -> Optional[Union[List[AModel], HTTPValidationError]]:
        client = self._client
        return await tests.get_user_list.asyncio(
            client=client,
            an_enum_value=an_enum_value,
            some_date=some_date,
        )

    async def get_user_list_detailed(
        self,
        *,
        an_enum_value: List[AnEnum],
        some_date: Union[datetime.date, datetime.datetime],
    ) -> Response[Union[List[AModel], HTTPValidationError]]:
        client = self._client
        return await tests.get_user_list.asyncio_detailed(
            client=client,
            an_enum_value=an_enum_value,
            some_date=some_date,
        )

    async def get_basic_list_of_strings(
        self,
    ) -> Optional[List[str]]:
        client = self._client
        return await tests.get_basic_list_of_strings.asyncio(
            client=client,
        )

    async def get_basic_list_of_strings_detailed(
        self,
    ) -> Response[List[str]]:
        client = self._client
        return await tests.get_basic_list_of_strings.asyncio_detailed(
            client=client,
        )

    async def get_basic_list_of_integers(
        self,
    ) -> Optional[List[int]]:
        client = self._client
        return await tests.get_basic_list_of_integers.asyncio(
            client=client,
        )

    async def get_basic_list_of_integers_detailed(
        self,
    ) -> Response[List[int]]:
        client = self._client
        return await tests.get_basic_list_of_integers.asyncio_detailed(
            client=client,
        )

    async def get_basic_list_of_floats(
        self,
    ) -> Optional[List[float]]:
        client = self._client
        return await tests.get_basic_list_of_floats.asyncio(
            client=client,
        )

    async def get_basic_list_of_floats_detailed(
        self,
    ) -> Response[List[float]]:
        client = self._client
        return await tests.get_basic_list_of_floats.asyncio_detailed(
            client=client,
        )

    async def get_basic_list_of_booleans(
        self,
    ) -> Optional[List[bool]]:
        client = self._client
        return await tests.get_basic_list_of_booleans.asyncio(
            client=client,
        )

    async def get_basic_list_of_booleans_detailed(
        self,
    ) -> Response[List[bool]]:
        client = self._client
        return await tests.get_basic_list_of_booleans.asyncio_detailed(
            client=client,
        )

    async def upload_file_tests_upload_post(
        self,
        *,
        multipart_data: BodyUploadFileTestsUploadPost,
        keep_alive: Union[Unset, bool] = UNSET,
    ) -> Optional[Union[None, HTTPValidationError]]:
        client = self._client
        return await tests.upload_file_tests_upload_post.asyncio(
            client=client,
            multipart_data=multipart_data,
            keep_alive=keep_alive,
        )

    async def upload_file_tests_upload_post_detailed(
        self,
        *,
        multipart_data: BodyUploadFileTestsUploadPost,
        keep_alive: Union[Unset, bool] = UNSET,
    ) -> Response[Union[None, HTTPValidationError]]:
        client = self._client
        return await tests.upload_file_tests_upload_post.asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
            keep_alive=keep_alive,
        )

    async def json_body_tests_json_body_post(
        self,
        *,
        json_body: AModel,
    ) -> Optional[Union[None, HTTPValidationError]]:
        client = self._client
        return await tests.json_body_tests_json_body_post.asyncio(
            client=client,
            json_body=json_body,
        )

    async def json_body_tests_json_body_post_detailed(
        self,
        *,
        json_body: AModel,
    ) -> Response[Union[None, HTTPValidationError]]:
        client = self._client
        return await tests.json_body_tests_json_body_post.asyncio_detailed(
            client=client,
            json_body=json_body,
        )

    async def defaults_tests_defaults_post(
        self,
        *,
        string_prop: Union[Unset, str] = "the default string",
        datetime_prop: Union[Unset, datetime.datetime] = isoparse("1010-10-10T00:00:00"),
        date_prop: Union[Unset, datetime.date] = isoparse("1010-10-10").date(),
        float_prop: Union[Unset, float] = 3.14,
        int_prop: Union[Unset, int] = 7,
        boolean_prop: Union[Unset, bool] = False,
        list_prop: Union[Unset, List[AnEnum]] = UNSET,
        union_prop: Union[Unset, float, str] = "not a float",
        union_prop_with_ref: Union[Unset, float, AnEnum] = 0.6,
        enum_prop: Union[Unset, AnEnum] = UNSET,
        model_prop: Union[ModelWithUnionProperty, Unset] = UNSET,
        required_model_prop: ModelWithUnionProperty,
    ) -> Optional[Union[None, HTTPValidationError]]:
        client = self._client
        return await tests.defaults_tests_defaults_post.asyncio(
            client=client,
            string_prop=string_prop,
            datetime_prop=datetime_prop,
            date_prop=date_prop,
            float_prop=float_prop,
            int_prop=int_prop,
            boolean_prop=boolean_prop,
            list_prop=list_prop,
            union_prop=union_prop,
            union_prop_with_ref=union_prop_with_ref,
            enum_prop=enum_prop,
            model_prop=model_prop,
            required_model_prop=required_model_prop,
        )

    async def defaults_tests_defaults_post_detailed(
        self,
        *,
        string_prop: Union[Unset, str] = "the default string",
        datetime_prop: Union[Unset, datetime.datetime] = isoparse("1010-10-10T00:00:00"),
        date_prop: Union[Unset, datetime.date] = isoparse("1010-10-10").date(),
        float_prop: Union[Unset, float] = 3.14,
        int_prop: Union[Unset, int] = 7,
        boolean_prop: Union[Unset, bool] = False,
        list_prop: Union[Unset, List[AnEnum]] = UNSET,
        union_prop: Union[Unset, float, str] = "not a float",
        union_prop_with_ref: Union[Unset, float, AnEnum] = 0.6,
        enum_prop: Union[Unset, AnEnum] = UNSET,
        model_prop: Union[ModelWithUnionProperty, Unset] = UNSET,
        required_model_prop: ModelWithUnionProperty,
    ) -> Response[Union[None, HTTPValidationError]]:
        client = self._client
        return await tests.defaults_tests_defaults_post.asyncio_detailed(
            client=client,
            string_prop=string_prop,
            datetime_prop=datetime_prop,
            date_prop=date_prop,
            float_prop=float_prop,
            int_prop=int_prop,
            boolean_prop=boolean_prop,
            list_prop=list_prop,
            union_prop=union_prop,
            union_prop_with_ref=union_prop_with_ref,
            enum_prop=enum_prop,
            model_prop=model_prop,
            required_model_prop=required_model_prop,
        )

    async def octet_stream_tests_octet_stream_get(
        self,
    ) -> Optional[File]:
        client = self._client
        return await tests.octet_stream_tests_octet_stream_get.asyncio(
            client=client,
        )

    async def octet_stream_tests_octet_stream_get_detailed(
        self,
    ) -> Response[File]:
        client = self._client
        return await tests.octet_stream_tests_octet_stream_get.asyncio_detailed(
            client=client,
        )

    async def no_response_tests_no_response_get_detailed(
        self,
    ) -> Response[None]:
        client = self._client
        return await tests.no_response_tests_no_response_get.asyncio_detailed(
            client=client,
        )

    async def unsupported_content_tests_unsupported_content_get_detailed(
        self,
    ) -> Response[None]:
        client = self._client
        return await tests.unsupported_content_tests_unsupported_content_get.asyncio_detailed(
            client=client,
        )

    async def int_enum_tests_int_enum_post(
        self,
        *,
        int_enum: AnIntEnum,
    ) -> Optional[Union[None, HTTPValidationError]]:
        client = self._client
        return await tests.int_enum_tests_int_enum_post.asyncio(
            client=client,
            int_enum=int_enum,
        )

    async def int_enum_tests_int_enum_post_detailed(
        self,
        *,
        int_enum: AnIntEnum,
    ) -> Response[Union[None, HTTPValidationError]]:
        client = self._client
        return await tests.int_enum_tests_int_enum_post.asyncio_detailed(
            client=client,
            int_enum=int_enum,
        )

    async def test_inline_objects(
        self,
        *,
        json_body: TestInlineObjectsJsonBody,
    ) -> Optional[TestInlineObjectsResponse_200]:
        client = self._client
        return await tests.test_inline_objects.asyncio(
            client=client,
            json_body=json_body,
        )

    async def test_inline_objects_detailed(
        self,
        *,
        json_body: TestInlineObjectsJsonBody,
    ) -> Response[TestInlineObjectsResponse_200]:
        client = self._client
        return await tests.test_inline_objects.asyncio_detailed(
            client=client,
            json_body=json_body,
        )

    async def optional_value_tests_optional_query_param(
        self,
        *,
        query_param: Union[Unset, List[str]] = UNSET,
    ) -> Optional[Union[None, HTTPValidationError]]:
        client = self._client
        return await tests.optional_value_tests_optional_query_param.asyncio(
            client=client,
            query_param=query_param,
        )

    async def optional_value_tests_optional_query_param_detailed(
        self,
        *,
        query_param: Union[Unset, List[str]] = UNSET,
    ) -> Response[Union[None, HTTPValidationError]]:
        client = self._client
        return await tests.optional_value_tests_optional_query_param.asyncio_detailed(
            client=client,
            query_param=query_param,
        )

    async def token_with_cookie_auth_token_with_cookie_get(
        self,
        *,
        my_token: str,
    ) -> Optional[Union[None, None]]:
        client = self._client
        return await tests.token_with_cookie_auth_token_with_cookie_get.asyncio(
            client=client,
            my_token=my_token,
        )

    async def token_with_cookie_auth_token_with_cookie_get_detailed(
        self,
        *,
        my_token: str,
    ) -> Response[Union[None, None]]:
        client = self._client
        return await tests.token_with_cookie_auth_token_with_cookie_get.asyncio_detailed(
            client=client,
            my_token=my_token,
        )


class SyncTestsApi:
    def __init__(self, client: InnerClient):
        self._client = client

    def get_user_list(
        self,
        *,
        an_enum_value: List[AnEnum],
        some_date: Union[datetime.date, datetime.datetime],
    ) -> Optional[Union[List[AModel], HTTPValidationError]]:
        client = self._client
        return tests.get_user_list.sync(
            client=client,
            an_enum_value=an_enum_value,
            some_date=some_date,
        )

    def get_user_list_detailed(
        self,
        *,
        an_enum_value: List[AnEnum],
        some_date: Union[datetime.date, datetime.datetime],
    ) -> Response[Union[List[AModel], HTTPValidationError]]:
        client = self._client
        return tests.get_user_list.sync_detailed(
            client=client,
            an_enum_value=an_enum_value,
            some_date=some_date,
        )

    def get_basic_list_of_strings(
        self,
    ) -> Optional[List[str]]:
        client = self._client
        return tests.get_basic_list_of_strings.sync(
            client=client,
        )

    def get_basic_list_of_strings_detailed(
        self,
    ) -> Response[List[str]]:
        client = self._client
        return tests.get_basic_list_of_strings.sync_detailed(
            client=client,
        )

    def get_basic_list_of_integers(
        self,
    ) -> Optional[List[int]]:
        client = self._client
        return tests.get_basic_list_of_integers.sync(
            client=client,
        )

    def get_basic_list_of_integers_detailed(
        self,
    ) -> Response[List[int]]:
        client = self._client
        return tests.get_basic_list_of_integers.sync_detailed(
            client=client,
        )

    def get_basic_list_of_floats(
        self,
    ) -> Optional[List[float]]:
        client = self._client
        return tests.get_basic_list_of_floats.sync(
            client=client,
        )

    def get_basic_list_of_floats_detailed(
        self,
    ) -> Response[List[float]]:
        client = self._client
        return tests.get_basic_list_of_floats.sync_detailed(
            client=client,
        )

    def get_basic_list_of_booleans(
        self,
    ) -> Optional[List[bool]]:
        client = self._client
        return tests.get_basic_list_of_booleans.sync(
            client=client,
        )

    def get_basic_list_of_booleans_detailed(
        self,
    ) -> Response[List[bool]]:
        client = self._client
        return tests.get_basic_list_of_booleans.sync_detailed(
            client=client,
        )

    def upload_file_tests_upload_post(
        self,
        *,
        multipart_data: BodyUploadFileTestsUploadPost,
        keep_alive: Union[Unset, bool] = UNSET,
    ) -> Optional[Union[None, HTTPValidationError]]:
        client = self._client
        return tests.upload_file_tests_upload_post.sync(
            client=client,
            multipart_data=multipart_data,
            keep_alive=keep_alive,
        )

    def upload_file_tests_upload_post_detailed(
        self,
        *,
        multipart_data: BodyUploadFileTestsUploadPost,
        keep_alive: Union[Unset, bool] = UNSET,
    ) -> Response[Union[None, HTTPValidationError]]:
        client = self._client
        return tests.upload_file_tests_upload_post.sync_detailed(
            client=client,
            multipart_data=multipart_data,
            keep_alive=keep_alive,
        )

    def json_body_tests_json_body_post(
        self,
        *,
        json_body: AModel,
    ) -> Optional[Union[None, HTTPValidationError]]:
        client = self._client
        return tests.json_body_tests_json_body_post.sync(
            client=client,
            json_body=json_body,
        )

    def json_body_tests_json_body_post_detailed(
        self,
        *,
        json_body: AModel,
    ) -> Response[Union[None, HTTPValidationError]]:
        client = self._client
        return tests.json_body_tests_json_body_post.sync_detailed(
            client=client,
            json_body=json_body,
        )

    def defaults_tests_defaults_post(
        self,
        *,
        string_prop: Union[Unset, str] = "the default string",
        datetime_prop: Union[Unset, datetime.datetime] = isoparse("1010-10-10T00:00:00"),
        date_prop: Union[Unset, datetime.date] = isoparse("1010-10-10").date(),
        float_prop: Union[Unset, float] = 3.14,
        int_prop: Union[Unset, int] = 7,
        boolean_prop: Union[Unset, bool] = False,
        list_prop: Union[Unset, List[AnEnum]] = UNSET,
        union_prop: Union[Unset, float, str] = "not a float",
        union_prop_with_ref: Union[Unset, float, AnEnum] = 0.6,
        enum_prop: Union[Unset, AnEnum] = UNSET,
        model_prop: Union[ModelWithUnionProperty, Unset] = UNSET,
        required_model_prop: ModelWithUnionProperty,
    ) -> Optional[Union[None, HTTPValidationError]]:
        client = self._client
        return tests.defaults_tests_defaults_post.sync(
            client=client,
            string_prop=string_prop,
            datetime_prop=datetime_prop,
            date_prop=date_prop,
            float_prop=float_prop,
            int_prop=int_prop,
            boolean_prop=boolean_prop,
            list_prop=list_prop,
            union_prop=union_prop,
            union_prop_with_ref=union_prop_with_ref,
            enum_prop=enum_prop,
            model_prop=model_prop,
            required_model_prop=required_model_prop,
        )

    def defaults_tests_defaults_post_detailed(
        self,
        *,
        string_prop: Union[Unset, str] = "the default string",
        datetime_prop: Union[Unset, datetime.datetime] = isoparse("1010-10-10T00:00:00"),
        date_prop: Union[Unset, datetime.date] = isoparse("1010-10-10").date(),
        float_prop: Union[Unset, float] = 3.14,
        int_prop: Union[Unset, int] = 7,
        boolean_prop: Union[Unset, bool] = False,
        list_prop: Union[Unset, List[AnEnum]] = UNSET,
        union_prop: Union[Unset, float, str] = "not a float",
        union_prop_with_ref: Union[Unset, float, AnEnum] = 0.6,
        enum_prop: Union[Unset, AnEnum] = UNSET,
        model_prop: Union[ModelWithUnionProperty, Unset] = UNSET,
        required_model_prop: ModelWithUnionProperty,
    ) -> Response[Union[None, HTTPValidationError]]:
        client = self._client
        return tests.defaults_tests_defaults_post.sync_detailed(
            client=client,
            string_prop=string_prop,
            datetime_prop=datetime_prop,
            date_prop=date_prop,
            float_prop=float_prop,
            int_prop=int_prop,
            boolean_prop=boolean_prop,
            list_prop=list_prop,
            union_prop=union_prop,
            union_prop_with_ref=union_prop_with_ref,
            enum_prop=enum_prop,
            model_prop=model_prop,
            required_model_prop=required_model_prop,
        )

    def octet_stream_tests_octet_stream_get(
        self,
    ) -> Optional[File]:
        client = self._client
        return tests.octet_stream_tests_octet_stream_get.sync(
            client=client,
        )

    def octet_stream_tests_octet_stream_get_detailed(
        self,
    ) -> Response[File]:
        client = self._client
        return tests.octet_stream_tests_octet_stream_get.sync_detailed(
            client=client,
        )

    def no_response_tests_no_response_get_detailed(
        self,
    ) -> Response[None]:
        client = self._client
        return tests.no_response_tests_no_response_get.sync_detailed(
            client=client,
        )

    def unsupported_content_tests_unsupported_content_get_detailed(
        self,
    ) -> Response[None]:
        client = self._client
        return tests.unsupported_content_tests_unsupported_content_get.sync_detailed(
            client=client,
        )

    def int_enum_tests_int_enum_post(
        self,
        *,
        int_enum: AnIntEnum,
    ) -> Optional[Union[None, HTTPValidationError]]:
        client = self._client
        return tests.int_enum_tests_int_enum_post.sync(
            client=client,
            int_enum=int_enum,
        )

    def int_enum_tests_int_enum_post_detailed(
        self,
        *,
        int_enum: AnIntEnum,
    ) -> Response[Union[None, HTTPValidationError]]:
        client = self._client
        return tests.int_enum_tests_int_enum_post.sync_detailed(
            client=client,
            int_enum=int_enum,
        )

    def test_inline_objects(
        self,
        *,
        json_body: TestInlineObjectsJsonBody,
    ) -> Optional[TestInlineObjectsResponse_200]:
        client = self._client
        return tests.test_inline_objects.sync(
            client=client,
            json_body=json_body,
        )

    def test_inline_objects_detailed(
        self,
        *,
        json_body: TestInlineObjectsJsonBody,
    ) -> Response[TestInlineObjectsResponse_200]:
        client = self._client
        return tests.test_inline_objects.sync_detailed(
            client=client,
            json_body=json_body,
        )

    def optional_value_tests_optional_query_param(
        self,
        *,
        query_param: Union[Unset, List[str]] = UNSET,
    ) -> Optional[Union[None, HTTPValidationError]]:
        client = self._client
        return tests.optional_value_tests_optional_query_param.sync(
            client=client,
            query_param=query_param,
        )

    def optional_value_tests_optional_query_param_detailed(
        self,
        *,
        query_param: Union[Unset, List[str]] = UNSET,
    ) -> Response[Union[None, HTTPValidationError]]:
        client = self._client
        return tests.optional_value_tests_optional_query_param.sync_detailed(
            client=client,
            query_param=query_param,
        )

    def token_with_cookie_auth_token_with_cookie_get(
        self,
        *,
        my_token: str,
    ) -> Optional[Union[None, None]]:
        client = self._client
        return tests.token_with_cookie_auth_token_with_cookie_get.sync(
            client=client,
            my_token=my_token,
        )

    def token_with_cookie_auth_token_with_cookie_get_detailed(
        self,
        *,
        my_token: str,
    ) -> Response[Union[None, None]]:
        client = self._client
        return tests.token_with_cookie_auth_token_with_cookie_get.sync_detailed(
            client=client,
            my_token=my_token,
        )


class MyTestAPIClient:
    def __init__(self, base_url: Optional[str] = None, timeout: float = 5.0, token: Optional[str] = None):
        if token is None:
            self.connection = InnerClient(base_url=base_url, timeout=timeout)
        else:
            self.connection = AuthenticatedClient(base_url=base_url, timeout=timeout, token=token)
        self.tests = TestsApi(self.connection)


class SyncMyTestAPIClient:
    def __init__(self, base_url: Optional[str] = None, timeout: float = 5.0, token: Optional[str] = None):
        if token is None:
            self.connection = InnerClient(base_url=base_url, timeout=timeout)
        else:
            self.connection = AuthenticatedClient(base_url=base_url, timeout=timeout, token=token)
        self.tests = SyncTestsApi(self.connection)
