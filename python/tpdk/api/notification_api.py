# coding: utf-8

"""
    Tripartie

    Our API suite for the **Resolution Center** and the **Safe Checkout** features. Simple, yet elegant web interfaces for your convenience. One request away from your first automated resolution or safe-checkout.  # noqa: E501

    The version of the OpenAPI document: 2.0.20
    Contact: noc@tripartie.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictInt, StrictStr

from typing import List, Optional

from tpdk.models.notification_read import NotificationRead
from tpdk.models.notification_update import NotificationUpdate

from tpdk.api_client import ApiClient
from tpdk.api_response import ApiResponse
from tpdk.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class NotificationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def api_personas_idnotifications_get_collection(self, id : Annotated[StrictStr, Field(..., description="Persona identifier")], page : Annotated[Optional[StrictInt], Field(description="The collection page number")] = None, **kwargs) -> List[NotificationRead]:  # noqa: E501
        """Retrieve pending notifications for Persona  # noqa: E501

        Retrieves the collection of Notification resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_personas_idnotifications_get_collection(id, page, async_req=True)
        >>> result = thread.get()

        :param id: Persona identifier (required)
        :type id: str
        :param page: The collection page number
        :type page: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[NotificationRead]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the api_personas_idnotifications_get_collection_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_personas_idnotifications_get_collection_with_http_info(id, page, **kwargs)  # noqa: E501

    @validate_arguments
    def api_personas_idnotifications_get_collection_with_http_info(self, id : Annotated[StrictStr, Field(..., description="Persona identifier")], page : Annotated[Optional[StrictInt], Field(description="The collection page number")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve pending notifications for Persona  # noqa: E501

        Retrieves the collection of Notification resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_personas_idnotifications_get_collection_with_http_info(id, page, async_req=True)
        >>> result = thread.get()

        :param id: Persona identifier (required)
        :type id: str
        :param page: The collection page number
        :type page: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[NotificationRead], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'page'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_personas_idnotifications_get_collection" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        if _params.get('page') is not None:  # noqa: E501
            _query_params.append(('page', _params['page']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['personaAuthKey']  # noqa: E501

        _response_types_map = {
            '200': "List[NotificationRead]",
        }

        return self.api_client.call_api(
            '/personas/{id}/notifications', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def api_personas_persona_idnotifications_id_patch(self, persona_id : Annotated[StrictStr, Field(..., description="Persona identifier")], id : Annotated[StrictStr, Field(..., description="Notification identifier")], notification_update : Annotated[NotificationUpdate, Field(..., description="The updated Notification resource")], **kwargs) -> NotificationRead:  # noqa: E501
        """Mark as read/unread a notification for Persona  # noqa: E501

        Updates the Notification resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_personas_persona_idnotifications_id_patch(persona_id, id, notification_update, async_req=True)
        >>> result = thread.get()

        :param persona_id: Persona identifier (required)
        :type persona_id: str
        :param id: Notification identifier (required)
        :type id: str
        :param notification_update: The updated Notification resource (required)
        :type notification_update: NotificationUpdate
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NotificationRead
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the api_personas_persona_idnotifications_id_patch_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_personas_persona_idnotifications_id_patch_with_http_info(persona_id, id, notification_update, **kwargs)  # noqa: E501

    @validate_arguments
    def api_personas_persona_idnotifications_id_patch_with_http_info(self, persona_id : Annotated[StrictStr, Field(..., description="Persona identifier")], id : Annotated[StrictStr, Field(..., description="Notification identifier")], notification_update : Annotated[NotificationUpdate, Field(..., description="The updated Notification resource")], **kwargs) -> ApiResponse:  # noqa: E501
        """Mark as read/unread a notification for Persona  # noqa: E501

        Updates the Notification resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_personas_persona_idnotifications_id_patch_with_http_info(persona_id, id, notification_update, async_req=True)
        >>> result = thread.get()

        :param persona_id: Persona identifier (required)
        :type persona_id: str
        :param id: Notification identifier (required)
        :type id: str
        :param notification_update: The updated Notification resource (required)
        :type notification_update: NotificationUpdate
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(NotificationRead, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'persona_id',
            'id',
            'notification_update'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_personas_persona_idnotifications_id_patch" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['persona_id']:
            _path_params['personaId'] = _params['persona_id']

        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['notification_update'] is not None:
            _body_params = _params['notification_update']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['personaAuthKey']  # noqa: E501

        _response_types_map = {
            '200': "NotificationRead",
            '400': None,
            '422': None,
            '404': None,
        }

        return self.api_client.call_api(
            '/personas/{personaId}/notifications/{id}', 'PATCH',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def api_users_idnotifications_get_collection(self, id : Annotated[StrictStr, Field(..., description="User identifier")], page : Annotated[Optional[StrictInt], Field(description="The collection page number")] = None, **kwargs) -> List[NotificationRead]:  # noqa: E501
        """Retrieves the collection of Notification resources.  # noqa: E501

        Retrieves the collection of Notification resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_users_idnotifications_get_collection(id, page, async_req=True)
        >>> result = thread.get()

        :param id: User identifier (required)
        :type id: str
        :param page: The collection page number
        :type page: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[NotificationRead]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the api_users_idnotifications_get_collection_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_users_idnotifications_get_collection_with_http_info(id, page, **kwargs)  # noqa: E501

    @validate_arguments
    def api_users_idnotifications_get_collection_with_http_info(self, id : Annotated[StrictStr, Field(..., description="User identifier")], page : Annotated[Optional[StrictInt], Field(description="The collection page number")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieves the collection of Notification resources.  # noqa: E501

        Retrieves the collection of Notification resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_users_idnotifications_get_collection_with_http_info(id, page, async_req=True)
        >>> result = thread.get()

        :param id: User identifier (required)
        :type id: str
        :param page: The collection page number
        :type page: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[NotificationRead], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'page'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_users_idnotifications_get_collection" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        if _params.get('page') is not None:  # noqa: E501
            _query_params.append(('page', _params['page']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['jwtPersonalKey', 'personaAuthKey', 'oauth']  # noqa: E501

        _response_types_map = {
            '200': "List[NotificationRead]",
        }

        return self.api_client.call_api(
            '/users/{id}/notifications', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def api_users_user_idnotifications_id_patch(self, user_id : Annotated[StrictStr, Field(..., description="User identifier")], id : Annotated[StrictStr, Field(..., description="Notification identifier")], notification_update : Annotated[NotificationUpdate, Field(..., description="The updated Notification resource")], **kwargs) -> NotificationRead:  # noqa: E501
        """Mark as read/unread a notification for User  # noqa: E501

        Updates the Notification resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_users_user_idnotifications_id_patch(user_id, id, notification_update, async_req=True)
        >>> result = thread.get()

        :param user_id: User identifier (required)
        :type user_id: str
        :param id: Notification identifier (required)
        :type id: str
        :param notification_update: The updated Notification resource (required)
        :type notification_update: NotificationUpdate
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NotificationRead
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the api_users_user_idnotifications_id_patch_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_users_user_idnotifications_id_patch_with_http_info(user_id, id, notification_update, **kwargs)  # noqa: E501

    @validate_arguments
    def api_users_user_idnotifications_id_patch_with_http_info(self, user_id : Annotated[StrictStr, Field(..., description="User identifier")], id : Annotated[StrictStr, Field(..., description="Notification identifier")], notification_update : Annotated[NotificationUpdate, Field(..., description="The updated Notification resource")], **kwargs) -> ApiResponse:  # noqa: E501
        """Mark as read/unread a notification for User  # noqa: E501

        Updates the Notification resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_users_user_idnotifications_id_patch_with_http_info(user_id, id, notification_update, async_req=True)
        >>> result = thread.get()

        :param user_id: User identifier (required)
        :type user_id: str
        :param id: Notification identifier (required)
        :type id: str
        :param notification_update: The updated Notification resource (required)
        :type notification_update: NotificationUpdate
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(NotificationRead, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'user_id',
            'id',
            'notification_update'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_users_user_idnotifications_id_patch" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['user_id']:
            _path_params['userId'] = _params['user_id']

        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['notification_update'] is not None:
            _body_params = _params['notification_update']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['jwtPersonalKey']  # noqa: E501

        _response_types_map = {
            '200': "NotificationRead",
            '400': None,
            '422': None,
            '404': None,
        }

        return self.api_client.call_api(
            '/users/{userId}/notifications/{id}', 'PATCH',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
