import connexion
import six

from swagger_server.models.extendednotesresearch import Extendednotesresearch  # noqa: E501
from swagger_server import util


def extendednotesresearch_delete(research_id=None, script_id=None, notes=None, research_details=None, prefer=None):  # noqa: E501
    """extendednotesresearch_delete

     # noqa: E501

    :param research_id: 
    :type research_id: str
    :param script_id: 
    :type script_id: str
    :param notes: 
    :type notes: str
    :param research_details: 
    :type research_details: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    return 'do some magic!'


def extendednotesresearch_get(research_id=None, script_id=None, notes=None, research_details=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """extendednotesresearch_get

     # noqa: E501

    :param research_id: 
    :type research_id: str
    :param script_id: 
    :type script_id: str
    :param notes: 
    :type notes: str
    :param research_details: 
    :type research_details: str
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

    :rtype: List[Extendednotesresearch]
    """
    return 'do some magic!'


def extendednotesresearch_patch(body=None, prefer=None, research_id=None, script_id=None, notes=None, research_details=None):  # noqa: E501
    """extendednotesresearch_patch

     # noqa: E501

    :param body: extendednotesresearch
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param research_id: 
    :type research_id: str
    :param script_id: 
    :type script_id: str
    :param notes: 
    :type notes: str
    :param research_details: 
    :type research_details: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Extendednotesresearch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def extendednotesresearch_post(body=None, prefer=None, select=None):  # noqa: E501
    """extendednotesresearch_post

     # noqa: E501

    :param body: extendednotesresearch
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Extendednotesresearch.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
