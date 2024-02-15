import connexion
import six

from swagger_server.models.script import Script  # noqa: E501
from swagger_server import util


def script_delete(script_id=None, title=None, author_id=None, url=None, metadata_id=None, prefer=None):  # noqa: E501
    """script_delete

     # noqa: E501

    :param script_id: 
    :type script_id: str
    :param title: 
    :type title: str
    :param author_id: 
    :type author_id: str
    :param url: 
    :type url: str
    :param metadata_id: 
    :type metadata_id: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    return 'do some magic!'


def script_get(script_id=None, title=None, author_id=None, url=None, metadata_id=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """script_get

     # noqa: E501

    :param script_id: 
    :type script_id: str
    :param title: 
    :type title: str
    :param author_id: 
    :type author_id: str
    :param url: 
    :type url: str
    :param metadata_id: 
    :type metadata_id: str
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

    :rtype: List[Script]
    """
    return 'do some magic!'


def script_patch(body=None, prefer=None, script_id=None, title=None, author_id=None, url=None, metadata_id=None):  # noqa: E501
    """script_patch

     # noqa: E501

    :param body: script
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param script_id: 
    :type script_id: str
    :param title: 
    :type title: str
    :param author_id: 
    :type author_id: str
    :param url: 
    :type url: str
    :param metadata_id: 
    :type metadata_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Script.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def script_post(body=None, prefer=None, select=None):  # noqa: E501
    """script_post

     # noqa: E501

    :param body: script
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Script.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
