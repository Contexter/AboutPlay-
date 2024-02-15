import connexion
import six

from swagger_server.models.character import Character  # noqa: E501
from swagger_server import util


def character_delete(character_id=None, script_id=None, name=None, description=None, prefer=None):  # noqa: E501
    """character_delete

     # noqa: E501

    :param character_id: 
    :type character_id: str
    :param script_id: 
    :type script_id: str
    :param name: 
    :type name: str
    :param description: 
    :type description: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    return 'do some magic!'


def character_get(character_id=None, script_id=None, name=None, description=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """character_get

     # noqa: E501

    :param character_id: 
    :type character_id: str
    :param script_id: 
    :type script_id: str
    :param name: 
    :type name: str
    :param description: 
    :type description: str
    :param select: Filtering Columns
    :type select: str
    :param order: Ordering
    :type order: str
    :param range: Limiting and Pagination
    :type range: str
    :param range_unit: Limiting and Pagination
    :type range_unit: str
    :param offset: Limiting and Pagination
    :type offset: str
    :param limit: Limiting and Pagination
    :type limit: str
    :param prefer: Preference
    :type prefer: str

    :rtype: List[Character]
    """
    return 'do some magic!'


def character_patch(body=None, prefer=None, character_id=None, script_id=None, name=None, description=None):  # noqa: E501
    """character_patch

     # noqa: E501

    :param body: character
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param character_id: 
    :type character_id: str
    :param script_id: 
    :type script_id: str
    :param name: 
    :type name: str
    :param description: 
    :type description: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Character.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def character_post(body=None, prefer=None, select=None):  # noqa: E501
    """character_post

     # noqa: E501

    :param body: character
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Character.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
