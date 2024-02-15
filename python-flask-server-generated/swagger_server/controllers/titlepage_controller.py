import connexion
import six

from swagger_server.models.titlepage import Titlepage  # noqa: E501
from swagger_server import util


def titlepage_delete(title_page_id=None, script_id=None, text=None, prefer=None):  # noqa: E501
    """titlepage_delete

     # noqa: E501

    :param title_page_id: 
    :type title_page_id: str
    :param script_id: 
    :type script_id: str
    :param text: 
    :type text: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    return 'do some magic!'


def titlepage_get(title_page_id=None, script_id=None, text=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """titlepage_get

     # noqa: E501

    :param title_page_id: 
    :type title_page_id: str
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

    :rtype: List[Titlepage]
    """
    return 'do some magic!'


def titlepage_patch(body=None, prefer=None, title_page_id=None, script_id=None, text=None):  # noqa: E501
    """titlepage_patch

     # noqa: E501

    :param body: titlepage
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param title_page_id: 
    :type title_page_id: str
    :param script_id: 
    :type script_id: str
    :param text: 
    :type text: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Titlepage.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def titlepage_post(body=None, prefer=None, select=None):  # noqa: E501
    """titlepage_post

     # noqa: E501

    :param body: titlepage
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Titlepage.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
