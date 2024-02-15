import connexion
import six

from swagger_server.models.dialogue import Dialogue  # noqa: E501
from swagger_server import util


def dialogue_delete(dialogue_id=None, scene_id=None, character_id=None, original_text=None, modernized_text=None, prefer=None):  # noqa: E501
    """dialogue_delete

     # noqa: E501

    :param dialogue_id: 
    :type dialogue_id: str
    :param scene_id: 
    :type scene_id: str
    :param character_id: 
    :type character_id: str
    :param original_text: 
    :type original_text: str
    :param modernized_text: 
    :type modernized_text: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    return 'do some magic!'


def dialogue_get(dialogue_id=None, scene_id=None, character_id=None, original_text=None, modernized_text=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """dialogue_get

     # noqa: E501

    :param dialogue_id: 
    :type dialogue_id: str
    :param scene_id: 
    :type scene_id: str
    :param character_id: 
    :type character_id: str
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

    :rtype: List[Dialogue]
    """
    return 'do some magic!'


def dialogue_patch(body=None, prefer=None, dialogue_id=None, scene_id=None, character_id=None, original_text=None, modernized_text=None):  # noqa: E501
    """dialogue_patch

     # noqa: E501

    :param body: dialogue
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param dialogue_id: 
    :type dialogue_id: str
    :param scene_id: 
    :type scene_id: str
    :param character_id: 
    :type character_id: str
    :param original_text: 
    :type original_text: str
    :param modernized_text: 
    :type modernized_text: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Dialogue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def dialogue_post(body=None, prefer=None, select=None):  # noqa: E501
    """dialogue_post

     # noqa: E501

    :param body: dialogue
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Dialogue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
