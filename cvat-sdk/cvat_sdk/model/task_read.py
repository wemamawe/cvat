# Copyright (C) 2022 CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

# CVAT REST API
#
# REST API for Computer Vision Annotation Tool (CVAT)  # noqa: E501
#
# The version of the OpenAPI document: alpha (2.0)
# Contact: support@cvat.ai
# Generated by: https://openapi-generator.tech


from __future__ import annotations

import re  # noqa: F401
import sys  # noqa: F401
import typing
from typing import TYPE_CHECKING

from cvat_sdk.exceptions import ApiAttributeError
from cvat_sdk.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    OpenApiModel,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

if TYPE_CHECKING:
    # Enable introspection. Can't work normally due to cyclic imports
    from cvat_sdk.apis import *
    from cvat_sdk.models import *


def lazy_import():
    from cvat_sdk.model.basic_user import BasicUser
    from cvat_sdk.model.chunk_type import ChunkType
    from cvat_sdk.model.comment_read_owner import CommentReadOwner
    from cvat_sdk.model.job_status import JobStatus
    from cvat_sdk.model.label import Label
    from cvat_sdk.model.segment import Segment
    from cvat_sdk.model.task_read_target_storage import TaskReadTargetStorage

    globals()["BasicUser"] = BasicUser
    globals()["ChunkType"] = ChunkType
    globals()["CommentReadOwner"] = CommentReadOwner
    globals()["JobStatus"] = JobStatus
    globals()["Label"] = Label
    globals()["Segment"] = Segment
    globals()["TaskReadTargetStorage"] = TaskReadTargetStorage


class TaskRead(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      url (str): [optional]  # noqa: E501

      id (int): [optional]  # noqa: E501

      name (str): [optional]  # noqa: E501

      project_id (int, none_type): [optional]  # noqa: E501

      mode (str): [optional]  # noqa: E501

      owner (BasicUser): [optional]  # noqa: E501

      assignee (CommentReadOwner): [optional]  # noqa: E501

      bug_tracker (str): [optional]  # noqa: E501

      created_date (datetime): [optional]  # noqa: E501

      updated_date (datetime): [optional]  # noqa: E501

      overlap (int): [optional]  # noqa: E501

      segment_size (int): [optional]  # noqa: E501

      status (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501

      labels ([Label]): [optional]  # noqa: E501

      segments ([Segment]): [optional]  # noqa: E501

      data_chunk_size (int, none_type): [optional]  # noqa: E501

      data_compressed_chunk_type (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501

      data_original_chunk_type (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501

      size (int): [optional]  # noqa: E501

      image_quality (int): [optional]  # noqa: E501

      data (int): [optional]  # noqa: E501

      dimension (str): [optional]  # noqa: E501

      subset (str): [optional]  # noqa: E501

      organization (int, none_type): [optional]  # noqa: E501

      target_storage (TaskReadTargetStorage): [optional]  # noqa: E501

      source_storage (TaskReadTargetStorage): [optional]  # noqa: E501


      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.

    """

    allowed_values = {}

    validations = {}

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (
            bool,
            date,
            datetime,
            dict,
            float,
            int,
            list,
            str,
            none_type,
        )  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            "url": (str,),  # noqa: E501
            "id": (int,),  # noqa: E501
            "name": (str,),  # noqa: E501
            "project_id": (
                int,
                none_type,
            ),  # noqa: E501
            "mode": (str,),  # noqa: E501
            "owner": (BasicUser,),  # noqa: E501
            "assignee": (CommentReadOwner,),  # noqa: E501
            "bug_tracker": (str,),  # noqa: E501
            "created_date": (datetime,),  # noqa: E501
            "updated_date": (datetime,),  # noqa: E501
            "overlap": (int,),  # noqa: E501
            "segment_size": (int,),  # noqa: E501
            "status": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                none_type,
            ),  # noqa: E501
            "labels": ([Label],),  # noqa: E501
            "segments": ([Segment],),  # noqa: E501
            "data_chunk_size": (
                int,
                none_type,
            ),  # noqa: E501
            "data_compressed_chunk_type": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                none_type,
            ),  # noqa: E501
            "data_original_chunk_type": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                none_type,
            ),  # noqa: E501
            "size": (int,),  # noqa: E501
            "image_quality": (int,),  # noqa: E501
            "data": (int,),  # noqa: E501
            "dimension": (str,),  # noqa: E501
            "subset": (str,),  # noqa: E501
            "organization": (
                int,
                none_type,
            ),  # noqa: E501
            "target_storage": (TaskReadTargetStorage,),  # noqa: E501
            "source_storage": (TaskReadTargetStorage,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    # member type declarations
    url: str  # noqa: E501
    """
    [optional]
    """

    id: int  # noqa: E501
    """
    [optional]
    """

    name: str  # noqa: E501
    """
    [optional]
    """

    project_id: typing.Union[int, none_type]  # noqa: E501
    """
    [optional]
    """

    mode: str  # noqa: E501
    """
    [optional]
    """

    owner: BasicUser  # noqa: E501
    """
    [optional]
    """

    assignee: CommentReadOwner  # noqa: E501
    """
    [optional]
    """

    bug_tracker: str  # noqa: E501
    """
    [optional]
    """

    created_date: datetime  # noqa: E501
    """
    [optional]
    """

    updated_date: datetime  # noqa: E501
    """
    [optional]
    """

    overlap: int  # noqa: E501
    """
    [optional]
    """

    segment_size: int  # noqa: E501
    """
    [optional]
    """

    status: typing.Union[typing.Any, none_type]  # noqa: E501
    """
    [optional]
    """

    labels: typing.List[Label]  # noqa: E501
    """
    [optional]
    [Label]
    """

    segments: typing.List[Segment]  # noqa: E501
    """
    [optional]
    [Segment]
    """

    data_chunk_size: typing.Union[int, none_type]  # noqa: E501
    """
    [optional]
    """

    data_compressed_chunk_type: typing.Union[typing.Any, none_type]  # noqa: E501
    """
    [optional]
    """

    data_original_chunk_type: typing.Union[typing.Any, none_type]  # noqa: E501
    """
    [optional]
    """

    size: int  # noqa: E501
    """
    [optional]
    """

    image_quality: int  # noqa: E501
    """
    [optional]
    """

    data: int  # noqa: E501
    """
    [optional]
    """

    dimension: str  # noqa: E501
    """
    [optional]
    """

    subset: str  # noqa: E501
    """
    [optional]
    """

    organization: typing.Union[int, none_type]  # noqa: E501
    """
    [optional]
    """

    target_storage: TaskReadTargetStorage  # noqa: E501
    """
    [optional]
    """

    source_storage: TaskReadTargetStorage  # noqa: E501
    """
    [optional]
    """

    attribute_map = {
        "url": "url",  # noqa: E501
        "id": "id",  # noqa: E501
        "name": "name",  # noqa: E501
        "project_id": "project_id",  # noqa: E501
        "mode": "mode",  # noqa: E501
        "owner": "owner",  # noqa: E501
        "assignee": "assignee",  # noqa: E501
        "bug_tracker": "bug_tracker",  # noqa: E501
        "created_date": "created_date",  # noqa: E501
        "updated_date": "updated_date",  # noqa: E501
        "overlap": "overlap",  # noqa: E501
        "segment_size": "segment_size",  # noqa: E501
        "status": "status",  # noqa: E501
        "labels": "labels",  # noqa: E501
        "segments": "segments",  # noqa: E501
        "data_chunk_size": "data_chunk_size",  # noqa: E501
        "data_compressed_chunk_type": "data_compressed_chunk_type",  # noqa: E501
        "data_original_chunk_type": "data_original_chunk_type",  # noqa: E501
        "size": "size",  # noqa: E501
        "image_quality": "image_quality",  # noqa: E501
        "data": "data",  # noqa: E501
        "dimension": "dimension",  # noqa: E501
        "subset": "subset",  # noqa: E501
        "organization": "organization",  # noqa: E501
        "target_storage": "target_storage",  # noqa: E501
        "source_storage": "source_storage",  # noqa: E501
    }

    read_only_vars = {
        "url",  # noqa: E501
        "id",  # noqa: E501
        "name",  # noqa: E501
        "mode",  # noqa: E501
        "bug_tracker",  # noqa: E501
        "created_date",  # noqa: E501
        "updated_date",  # noqa: E501
        "overlap",  # noqa: E501
        "segment_size",  # noqa: E501
        "status",  # noqa: E501
        "segments",  # noqa: E501
        "data_chunk_size",  # noqa: E501
        "data_compressed_chunk_type",  # noqa: E501
        "data_original_chunk_type",  # noqa: E501
        "size",  # noqa: E501
        "image_quality",  # noqa: E501
        "data",  # noqa: E501
        "subset",  # noqa: E501
        "organization",  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """TaskRead - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            url (str): [optional]  # noqa: E501
            id (int): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            project_id (int, none_type): [optional]  # noqa: E501
            mode (str): [optional]  # noqa: E501
            owner (BasicUser): [optional]  # noqa: E501
            assignee (CommentReadOwner): [optional]  # noqa: E501
            bug_tracker (str): [optional]  # noqa: E501
            created_date (datetime): [optional]  # noqa: E501
            updated_date (datetime): [optional]  # noqa: E501
            overlap (int): [optional]  # noqa: E501
            segment_size (int): [optional]  # noqa: E501
            status (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            labels ([Label]): [optional]  # noqa: E501
            segments ([Segment]): [optional]  # noqa: E501
            data_chunk_size (int, none_type): [optional]  # noqa: E501
            data_compressed_chunk_type (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            data_original_chunk_type (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            size (int): [optional]  # noqa: E501
            image_quality (int): [optional]  # noqa: E501
            data (int): [optional]  # noqa: E501
            dimension (str): [optional]  # noqa: E501
            subset (str): [optional]  # noqa: E501
            organization (int, none_type): [optional]  # noqa: E501
            target_storage (TaskReadTargetStorage): [optional]  # noqa: E501
            source_storage (TaskReadTargetStorage): [optional]  # noqa: E501
        """
        from cvat_sdk.configuration import Configuration

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", True)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", Configuration())
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                        % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """TaskRead - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            url (str): [optional]  # noqa: E501
            id (int): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            project_id (int, none_type): [optional]  # noqa: E501
            mode (str): [optional]  # noqa: E501
            owner (BasicUser): [optional]  # noqa: E501
            assignee (CommentReadOwner): [optional]  # noqa: E501
            bug_tracker (str): [optional]  # noqa: E501
            created_date (datetime): [optional]  # noqa: E501
            updated_date (datetime): [optional]  # noqa: E501
            overlap (int): [optional]  # noqa: E501
            segment_size (int): [optional]  # noqa: E501
            status (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            labels ([Label]): [optional]  # noqa: E501
            segments ([Segment]): [optional]  # noqa: E501
            data_chunk_size (int, none_type): [optional]  # noqa: E501
            data_compressed_chunk_type (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            data_original_chunk_type (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            size (int): [optional]  # noqa: E501
            image_quality (int): [optional]  # noqa: E501
            data (int): [optional]  # noqa: E501
            dimension (str): [optional]  # noqa: E501
            subset (str): [optional]  # noqa: E501
            organization (int, none_type): [optional]  # noqa: E501
            target_storage (TaskReadTargetStorage): [optional]  # noqa: E501
            source_storage (TaskReadTargetStorage): [optional]  # noqa: E501
        """
        from cvat_sdk.configuration import Configuration

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", Configuration())
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                        % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(
                    f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                    f"class with read only attributes."
                )
