import connexion
import six

from swagger_server.models.casting import Casting  # noqa: E501
from swagger_server import util


def casting_delete(casting_id=None, character_id=None, actor_characteristics_choices=None, prefer=None):  # noqa: E501
    """casting_delete

     # noqa: E501

    :param casting_id: 
    :type casting_id: str
    :param character_id: 
    :type character_id: str
    :param actor_characteristics_choices: 
    :type actor_characteristics_choices: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    return 'do some magic!'


def casting_get(casting_id=None, character_id=None, actor_characteristics_choices=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """casting_get

     # noqa: E501

    :param casting_id: 
    :type casting_id: str
    :param character_id: 
    :type character_id: str
    :param actor_characteristics_choices: 
    :type actor_characteristics_choices: str
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

    :rtype: List[Casting]
    """
    return 'do some magic!'


def casting_patch(body=None, prefer=None, casting_id=None, character_id=None, actor_characteristics_choices=None):  # noqa: E501
    """casting_patch

     # noqa: E501

    :param body: casting
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param casting_id: 
    :type casting_id: str
    :param character_id: 
    :type character_id: str
    :param actor_characteristics_choices: 
    :type actor_characteristics_choices: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Casting.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def casting_post(body=None, prefer=None, select=None):  # noqa: E501
    """casting_post

     # noqa: E501

    :param body: casting
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Casting.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
