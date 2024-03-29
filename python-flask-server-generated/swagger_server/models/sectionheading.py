# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Sectionheading(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, section_id: int=None, script_id: int=None, text: str=None):  # noqa: E501
        """Sectionheading - a model defined in Swagger

        :param section_id: The section_id of this Sectionheading.  # noqa: E501
        :type section_id: int
        :param script_id: The script_id of this Sectionheading.  # noqa: E501
        :type script_id: int
        :param text: The text of this Sectionheading.  # noqa: E501
        :type text: str
        """
        self.swagger_types = {
            'section_id': int,
            'script_id': int,
            'text': str
        }

        self.attribute_map = {
            'section_id': 'section_id',
            'script_id': 'script_id',
            'text': 'text'
        }
        self._section_id = section_id
        self._script_id = script_id
        self._text = text

    @classmethod
    def from_dict(cls, dikt) -> 'Sectionheading':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The sectionheading of this Sectionheading.  # noqa: E501
        :rtype: Sectionheading
        """
        return util.deserialize_model(dikt, cls)

    @property
    def section_id(self) -> int:
        """Gets the section_id of this Sectionheading.

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :return: The section_id of this Sectionheading.
        :rtype: int
        """
        return self._section_id

    @section_id.setter
    def section_id(self, section_id: int):
        """Sets the section_id of this Sectionheading.

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :param section_id: The section_id of this Sectionheading.
        :type section_id: int
        """
        if section_id is None:
            raise ValueError("Invalid value for `section_id`, must not be `None`")  # noqa: E501

        self._section_id = section_id

    @property
    def script_id(self) -> int:
        """Gets the script_id of this Sectionheading.

        Note: This is a Foreign Key to `script.script_id`.<fk table='script' column='script_id'/>  # noqa: E501

        :return: The script_id of this Sectionheading.
        :rtype: int
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id: int):
        """Sets the script_id of this Sectionheading.

        Note: This is a Foreign Key to `script.script_id`.<fk table='script' column='script_id'/>  # noqa: E501

        :param script_id: The script_id of this Sectionheading.
        :type script_id: int
        """

        self._script_id = script_id

    @property
    def text(self) -> str:
        """Gets the text of this Sectionheading.


        :return: The text of this Sectionheading.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """Sets the text of this Sectionheading.


        :param text: The text of this Sectionheading.
        :type text: str
        """

        self._text = text
