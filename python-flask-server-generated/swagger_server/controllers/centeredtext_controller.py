import connexion
import six

from swagger_server.models.centeredtext import Centeredtext  # noqa: E501
from swagger_server import util


def centeredtext_delete(centered_id=None, script_id=None, text=None, prefer=None):  # noqa: E501
    """centeredtext_delete

     # noqa: E501

    :param centered_id: 
    :type centered_id: str
    :param script_id: 
    :type script_id: str
    :param text: 
    :type text: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    return 'do some magic!'


def centeredtext_get(centered_id=None, script_id=None, text=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """centeredtext_get

     # noqa: E501

    :param centered_id: 
    :type centered_id: str
    :param script_id: 
    :type script_id: str
    :param text: 
    :type text: str
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

    :rtype: List[Centeredtext]
    """
    return 'do some magic!'


def centeredtext_patch(body=None, prefer=None, centered_id=None, script_id=None, text=None):  # noqa: E501
    """centeredtext_patch

     # noqa: E501

    :param body: centeredtext
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param centered_id: 
    :type centered_id: str
    :param script_id: 
    :type script_id: str
    :param text: 
    :type text: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Centeredtext.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def centeredtext_post(body=None, prefer=None, select=None):  # noqa: E501
    """centeredtext_post

     # noqa: E501

    :param body: centeredtext
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Centeredtext.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
