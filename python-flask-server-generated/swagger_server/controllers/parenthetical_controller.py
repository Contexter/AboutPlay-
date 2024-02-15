import connexion
import six

from swagger_server.models.parenthetical import Parenthetical  # noqa: E501
from swagger_server import util


def parenthetical_delete(parenthetical_id=None, dialogue_id=None, original_text=None, modernized_text=None, prefer=None):  # noqa: E501
    """parenthetical_delete

     # noqa: E501

    :param parenthetical_id: 
    :type parenthetical_id: str
    :param dialogue_id: 
    :type dialogue_id: str
    :param original_text: 
    :type original_text: str
    :param modernized_text: 
    :type modernized_text: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    return 'do some magic!'


def parenthetical_get(parenthetical_id=None, dialogue_id=None, original_text=None, modernized_text=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """parenthetical_get

     # noqa: E501

    :param parenthetical_id: 
    :type parenthetical_id: str
    :param dialogue_id: 
    :type dialogue_id: str
    :param original_text: 
    :type original_text: str
    :param modernized_text: 
    :type modernized_text: str
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

    :rtype: List[Parenthetical]
    """
    return 'do some magic!'


def parenthetical_patch(body=None, prefer=None, parenthetical_id=None, dialogue_id=None, original_text=None, modernized_text=None):  # noqa: E501
    """parenthetical_patch

     # noqa: E501

    :param body: parenthetical
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param parenthetical_id: 
    :type parenthetical_id: str
    :param dialogue_id: 
    :type dialogue_id: str
    :param original_text: 
    :type original_text: str
    :param modernized_text: 
    :type modernized_text: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Parenthetical.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def parenthetical_post(body=None, prefer=None, select=None):  # noqa: E501
    """parenthetical_post

     # noqa: E501

    :param body: parenthetical
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Parenthetical.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
