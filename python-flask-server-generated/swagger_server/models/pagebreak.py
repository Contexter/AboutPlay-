# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Pagebreak(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, page_break_id: int=None, script_id: int=None, page_number: int=None):  # noqa: E501
        """Pagebreak - a model defined in Swagger

        :param page_break_id: The page_break_id of this Pagebreak.  # noqa: E501
        :type page_break_id: int
        :param script_id: The script_id of this Pagebreak.  # noqa: E501
        :type script_id: int
        :param page_number: The page_number of this Pagebreak.  # noqa: E501
        :type page_number: int
        """
        self.swagger_types = {
            'page_break_id': int,
            'script_id': int,
            'page_number': int
        }

        self.attribute_map = {
            'page_break_id': 'page_break_id',
            'script_id': 'script_id',
            'page_number': 'page_number'
        }
        self._page_break_id = page_break_id
        self._script_id = script_id
        self._page_number = page_number

    @classmethod
    def from_dict(cls, dikt) -> 'Pagebreak':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The pagebreak of this Pagebreak.  # noqa: E501
        :rtype: Pagebreak
        """
        return util.deserialize_model(dikt, cls)

    @property
    def page_break_id(self) -> int:
        """Gets the page_break_id of this Pagebreak.

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :return: The page_break_id of this Pagebreak.
        :rtype: int
        """
        return self._page_break_id

    @page_break_id.setter
    def page_break_id(self, page_break_id: int):
        """Sets the page_break_id of this Pagebreak.

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :param page_break_id: The page_break_id of this Pagebreak.
        :type page_break_id: int
        """
        if page_break_id is None:
            raise ValueError("Invalid value for `page_break_id`, must not be `None`")  # noqa: E501

        self._page_break_id = page_break_id

    @property
    def script_id(self) -> int:
        """Gets the script_id of this Pagebreak.

        Note: This is a Foreign Key to `script.script_id`.<fk table='script' column='script_id'/>  # noqa: E501

        :return: The script_id of this Pagebreak.
        :rtype: int
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id: int):
        """Sets the script_id of this Pagebreak.

        Note: This is a Foreign Key to `script.script_id`.<fk table='script' column='script_id'/>  # noqa: E501

        :param script_id: The script_id of this Pagebreak.
        :type script_id: int
        """

        self._script_id = script_id

    @property
    def page_number(self) -> int:
        """Gets the page_number of this Pagebreak.


        :return: The page_number of this Pagebreak.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number: int):
        """Sets the page_number of this Pagebreak.


        :param page_number: The page_number of this Pagebreak.
        :type page_number: int
        """

        self._page_number = page_number