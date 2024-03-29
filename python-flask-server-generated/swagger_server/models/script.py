# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Script(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, script_id: int=None, title: str=None, author_id: int=None, url: str=None, metadata_id: int=None):  # noqa: E501
        """Script - a model defined in Swagger

        :param script_id: The script_id of this Script.  # noqa: E501
        :type script_id: int
        :param title: The title of this Script.  # noqa: E501
        :type title: str
        :param author_id: The author_id of this Script.  # noqa: E501
        :type author_id: int
        :param url: The url of this Script.  # noqa: E501
        :type url: str
        :param metadata_id: The metadata_id of this Script.  # noqa: E501
        :type metadata_id: int
        """
        self.swagger_types = {
            'script_id': int,
            'title': str,
            'author_id': int,
            'url': str,
            'metadata_id': int
        }

        self.attribute_map = {
            'script_id': 'script_id',
            'title': 'title',
            'author_id': 'author_id',
            'url': 'url',
            'metadata_id': 'metadata_id'
        }
        self._script_id = script_id
        self._title = title
        self._author_id = author_id
        self._url = url
        self._metadata_id = metadata_id

    @classmethod
    def from_dict(cls, dikt) -> 'Script':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The script of this Script.  # noqa: E501
        :rtype: Script
        """
        return util.deserialize_model(dikt, cls)

    @property
    def script_id(self) -> int:
        """Gets the script_id of this Script.

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :return: The script_id of this Script.
        :rtype: int
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id: int):
        """Sets the script_id of this Script.

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :param script_id: The script_id of this Script.
        :type script_id: int
        """
        if script_id is None:
            raise ValueError("Invalid value for `script_id`, must not be `None`")  # noqa: E501

        self._script_id = script_id

    @property
    def title(self) -> str:
        """Gets the title of this Script.


        :return: The title of this Script.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Script.


        :param title: The title of this Script.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def author_id(self) -> int:
        """Gets the author_id of this Script.

        Note: This is a Foreign Key to `playwright.author_id`.<fk table='playwright' column='author_id'/>  # noqa: E501

        :return: The author_id of this Script.
        :rtype: int
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id: int):
        """Sets the author_id of this Script.

        Note: This is a Foreign Key to `playwright.author_id`.<fk table='playwright' column='author_id'/>  # noqa: E501

        :param author_id: The author_id of this Script.
        :type author_id: int
        """

        self._author_id = author_id

    @property
    def url(self) -> str:
        """Gets the url of this Script.


        :return: The url of this Script.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this Script.


        :param url: The url of this Script.
        :type url: str
        """

        self._url = url

    @property
    def metadata_id(self) -> int:
        """Gets the metadata_id of this Script.

        Note: This is a Foreign Key to `metadata.metadata_id`.<fk table='metadata' column='metadata_id'/>  # noqa: E501

        :return: The metadata_id of this Script.
        :rtype: int
        """
        return self._metadata_id

    @metadata_id.setter
    def metadata_id(self, metadata_id: int):
        """Sets the metadata_id of this Script.

        Note: This is a Foreign Key to `metadata.metadata_id`.<fk table='metadata' column='metadata_id'/>  # noqa: E501

        :param metadata_id: The metadata_id of this Script.
        :type metadata_id: int
        """

        self._metadata_id = metadata_id
