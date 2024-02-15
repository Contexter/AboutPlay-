# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Character(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, character_id: int=None, script_id: int=None, name: str=None, description: str=None):  # noqa: E501
        """Character - a model defined in Swagger

        :param character_id: The character_id of this Character.  # noqa: E501
        :type character_id: int
        :param script_id: The script_id of this Character.  # noqa: E501
        :type script_id: int
        :param name: The name of this Character.  # noqa: E501
        :type name: str
        :param description: The description of this Character.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {
            'character_id': int,
            'script_id': int,
            'name': str,
            'description': str
        }

        self.attribute_map = {
            'character_id': 'character_id',
            'script_id': 'script_id',
            'name': 'name',
            'description': 'description'
        }
        self._character_id = character_id
        self._script_id = script_id
        self._name = name
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'Character':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The character of this Character.  # noqa: E501
        :rtype: Character
        """
        return util.deserialize_model(dikt, cls)

    @property
    def character_id(self) -> int:
        """Gets the character_id of this Character.

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :return: The character_id of this Character.
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id: int):
        """Sets the character_id of this Character.

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :param character_id: The character_id of this Character.
        :type character_id: int
        """
        if character_id is None:
            raise ValueError("Invalid value for `character_id`, must not be `None`")  # noqa: E501

        self._character_id = character_id

    @property
    def script_id(self) -> int:
        """Gets the script_id of this Character.

        Note: This is a Foreign Key to `script.script_id`.<fk table='script' column='script_id'/>  # noqa: E501

        :return: The script_id of this Character.
        :rtype: int
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id: int):
        """Sets the script_id of this Character.

        Note: This is a Foreign Key to `script.script_id`.<fk table='script' column='script_id'/>  # noqa: E501

        :param script_id: The script_id of this Character.
        :type script_id: int
        """

        self._script_id = script_id

    @property
    def name(self) -> str:
        """Gets the name of this Character.


        :return: The name of this Character.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Character.


        :param name: The name of this Character.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this Character.


        :return: The description of this Character.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Character.


        :param description: The description of this Character.
        :type description: str
        """

        self._description = description