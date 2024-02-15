# coding: utf-8

"""
    standard public schema

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 12.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Formattingrules(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'rule_id': 'int',
        'script_id': 'int',
        'rule_description': 'str'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'script_id': 'script_id',
        'rule_description': 'rule_description'
    }

    def __init__(self, rule_id=None, script_id=None, rule_description=None):  # noqa: E501
        """Formattingrules - a model defined in Swagger"""  # noqa: E501
        self._rule_id = None
        self._script_id = None
        self._rule_description = None
        self.discriminator = None
        self.rule_id = rule_id
        if script_id is not None:
            self.script_id = script_id
        if rule_description is not None:
            self.rule_description = rule_description

    @property
    def rule_id(self):
        """Gets the rule_id of this Formattingrules.  # noqa: E501

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :return: The rule_id of this Formattingrules.  # noqa: E501
        :rtype: int
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this Formattingrules.

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :param rule_id: The rule_id of this Formattingrules.  # noqa: E501
        :type: int
        """
        if rule_id is None:
            raise ValueError("Invalid value for `rule_id`, must not be `None`")  # noqa: E501

        self._rule_id = rule_id

    @property
    def script_id(self):
        """Gets the script_id of this Formattingrules.  # noqa: E501

        Note: This is a Foreign Key to `script.script_id`.<fk table='script' column='script_id'/>  # noqa: E501

        :return: The script_id of this Formattingrules.  # noqa: E501
        :rtype: int
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """Sets the script_id of this Formattingrules.

        Note: This is a Foreign Key to `script.script_id`.<fk table='script' column='script_id'/>  # noqa: E501

        :param script_id: The script_id of this Formattingrules.  # noqa: E501
        :type: int
        """

        self._script_id = script_id

    @property
    def rule_description(self):
        """Gets the rule_description of this Formattingrules.  # noqa: E501


        :return: The rule_description of this Formattingrules.  # noqa: E501
        :rtype: str
        """
        return self._rule_description

    @rule_description.setter
    def rule_description(self, rule_description):
        """Sets the rule_description of this Formattingrules.


        :param rule_description: The rule_description of this Formattingrules.  # noqa: E501
        :type: str
        """

        self._rule_description = rule_description

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Formattingrules, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Formattingrules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
