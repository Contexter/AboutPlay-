import connexion
import six

from swagger_server.models.transition import Transition  # noqa: E501
from swagger_server import util


def transition_delete(transition_id=None, scene_id=None, transition_text=None, prefer=None):  # noqa: E501
    """transition_delete

     # noqa: E501

    :param transition_id: 
    :type transition_id: str
    :param scene_id: 
    :type scene_id: str
    :param transition_text: 
    :type transition_text: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    return 'do some magic!'


def transition_get(transition_id=None, scene_id=None, transition_text=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """transition_get

     # noqa: E501

    :param transition_id: 
    :type transition_id: str
    :param scene_id: 
    :type scene_id: str
    :param transition_text: 
    :type transition_text: str
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

    :rtype: List[Transition]
    """
    return 'do some magic!'


def transition_patch(body=None, prefer=None, transition_id=None, scene_id=None, transition_text=None):  # noqa: E501
    """transition_patch

     # noqa: E501

    :param body: transition
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param transition_id: 
    :type transition_id: str
    :param scene_id: 
    :type scene_id: str
    :param transition_text: 
    :type transition_text: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Transition.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def transition_post(body=None, prefer=None, select=None):  # noqa: E501
    """transition_post

     # noqa: E501

    :param body: transition
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Transition.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
