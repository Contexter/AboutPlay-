# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Formattingrules(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, rule_id: int=None, script_id: int=None, rule_description: str=None):  # noqa: E501
        """Formattingrules - a model defined in Swagger

        :param rule_id: The rule_id of this Formattingrules.  # noqa: E501
        :type rule_id: int
        :param script_id: The script_id of this Formattingrules.  # noqa: E501
        :type script_id: int
        :param rule_description: The rule_description of this Formattingrules.  # noqa: E501
        :type rule_description: str
        """
        self.swagger_types = {
            'rule_id': int,
            'script_id': int,
            'rule_description': str
        }

        self.attribute_map = {
            'rule_id': 'rule_id',
            'script_id': 'script_id',
            'rule_description': 'rule_description'
        }
        self._rule_id = rule_id
        self._script_id = script_id
        self._rule_description = rule_description

    @classmethod
    def from_dict(cls, dikt) -> 'Formattingrules':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The formattingrules of this Formattingrules.  # noqa: E501
        :rtype: Formattingrules
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rule_id(self) -> int:
        """Gets the rule_id of this Formattingrules.

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :return: The rule_id of this Formattingrules.
        :rtype: int
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id: int):
        """Sets the rule_id of this Formattingrules.

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :param rule_id: The rule_id of this Formattingrules.
        :type rule_id: int
        """
        if rule_id is None:
            raise ValueError("Invalid value for `rule_id`, must not be `None`")  # noqa: E501

        self._rule_id = rule_id

    @property
    def script_id(self) -> int:
        """Gets the script_id of this Formattingrules.

        Note: This is a Foreign Key to `script.script_id`.<fk table='script' column='script_id'/>  # noqa: E501

        :return: The script_id of this Formattingrules.
        :rtype: int
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id: int):
        """Sets the script_id of this Formattingrules.

        Note: This is a Foreign Key to `script.script_id`.<fk table='script' column='script_id'/>  # noqa: E501

        :param script_id: The script_id of this Formattingrules.
        :type script_id: int
        """

        self._script_id = script_id

    @property
    def rule_description(self) -> str:
        """Gets the rule_description of this Formattingrules.


        :return: The rule_description of this Formattingrules.
        :rtype: str
        """
        return self._rule_description

    @rule_description.setter
    def rule_description(self, rule_description: str):
        """Sets the rule_description of this Formattingrules.


        :param rule_description: The rule_description of this Formattingrules.
        :type rule_description: str
        """

        self._rule_description = rule_description
