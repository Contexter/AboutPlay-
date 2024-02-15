import connexion
import six

from swagger_server.models.sectionheading import Sectionheading  # noqa: E501
from swagger_server import util


def sectionheading_delete(section_id=None, script_id=None, text=None, prefer=None):  # noqa: E501
    """sectionheading_delete

     # noqa: E501

    :param section_id: 
    :type section_id: str
    :param script_id: 
    :type script_id: str
    :param text: 
    :type text: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    return 'do some magic!'


def sectionheading_get(section_id=None, script_id=None, text=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """sectionheading_get

     # noqa: E501

    :param section_id: 
    :type section_id: str
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

    :rtype: List[Sectionheading]
    """
    return 'do some magic!'


def sectionheading_patch(body=None, prefer=None, section_id=None, script_id=None, text=None):  # noqa: E501
    """sectionheading_patch

     # noqa: E501

    :param body: sectionheading
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param section_id: 
    :type section_id: str
    :param script_id: 
    :type script_id: str
    :param text: 
    :type text: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Sectionheading.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def sectionheading_post(body=None, prefer=None, select=None):  # noqa: E501
    """sectionheading_post

     # noqa: E501

    :param body: sectionheading
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Sectionheading.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
