import connexion
import six

from swagger_server.models.pagebreak import Pagebreak  # noqa: E501
from swagger_server import util


def pagebreak_delete(page_break_id=None, script_id=None, page_number=None, prefer=None):  # noqa: E501
    """pagebreak_delete

     # noqa: E501

    :param page_break_id: 
    :type page_break_id: str
    :param script_id: 
    :type script_id: str
    :param page_number: 
    :type page_number: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    return 'do some magic!'


def pagebreak_get(page_break_id=None, script_id=None, page_number=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """pagebreak_get

     # noqa: E501

    :param page_break_id: 
    :type page_break_id: str
    :param script_id: 
    :type script_id: str
    :param page_number: 
    :type page_number: str
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

    :rtype: List[Pagebreak]
    """
    return 'do some magic!'


def pagebreak_patch(body=None, prefer=None, page_break_id=None, script_id=None, page_number=None):  # noqa: E501
    """pagebreak_patch

     # noqa: E501

    :param body: pagebreak
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param page_break_id: 
    :type page_break_id: str
    :param script_id: 
    :type script_id: str
    :param page_number: 
    :type page_number: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Pagebreak.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def pagebreak_post(body=None, prefer=None, select=None):  # noqa: E501
    """pagebreak_post

     # noqa: E501

    :param body: pagebreak
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Pagebreak.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
