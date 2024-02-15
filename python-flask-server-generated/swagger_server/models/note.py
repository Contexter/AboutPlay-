# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Note(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, note_id: int=None, script_id: int=None, type: str=None, text: str=None):  # noqa: E501
        """Note - a model defined in Swagger

        :param note_id: The note_id of this Note.  # noqa: E501
        :type note_id: int
        :param script_id: The script_id of this Note.  # noqa: E501
        :type script_id: int
        :param type: The type of this Note.  # noqa: E501
        :type type: str
        :param text: The text of this Note.  # noqa: E501
        :type text: str
        """
        self.swagger_types = {
            'note_id': int,
            'script_id': int,
            'type': str,
            'text': str
        }

        self.attribute_map = {
            'note_id': 'note_id',
            'script_id': 'script_id',
            'type': 'type',
            'text': 'text'
        }
        self._note_id = note_id
        self._script_id = script_id
        self._type = type
        self._text = text

    @classmethod
    def from_dict(cls, dikt) -> 'Note':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The note of this Note.  # noqa: E501
        :rtype: Note
        """
        return util.deserialize_model(dikt, cls)

    @property
    def note_id(self) -> int:
        """Gets the note_id of this Note.

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :return: The note_id of this Note.
        :rtype: int
        """
        return self._note_id

    @note_id.setter
    def note_id(self, note_id: int):
        """Sets the note_id of this Note.

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :param note_id: The note_id of this Note.
        :type note_id: int
        """
        if note_id is None:
            raise ValueError("Invalid value for `note_id`, must not be `None`")  # noqa: E501

        self._note_id = note_id

    @property
    def script_id(self) -> int:
        """Gets the script_id of this Note.

        Note: This is a Foreign Key to `script.script_id`.<fk table='script' column='script_id'/>  # noqa: E501

        :return: The script_id of this Note.
        :rtype: int
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id: int):
        """Sets the script_id of this Note.

        Note: This is a Foreign Key to `script.script_id`.<fk table='script' column='script_id'/>  # noqa: E501

        :param script_id: The script_id of this Note.
        :type script_id: int
        """

        self._script_id = script_id

    @property
    def type(self) -> str:
        """Gets the type of this Note.


        :return: The type of this Note.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Note.


        :param type: The type of this Note.
        :type type: str
        """

        self._type = type

    @property
    def text(self) -> str:
        """Gets the text of this Note.


        :return: The text of this Note.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text: str):
        """Sets the text of this Note.


        :param text: The text of this Note.
        :type text: str
        """

        self._text = text