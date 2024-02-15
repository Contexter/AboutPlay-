import connexion
import six

from swagger_server.models.revisionhistory import Revisionhistory  # noqa: E501
from swagger_server import util


def revisionhistory_delete(revision_id=None, script_id=None, _date=None, change_description=None, editor=None, prefer=None):  # noqa: E501
    """revisionhistory_delete

     # noqa: E501

    :param revision_id: 
    :type revision_id: str
    :param script_id: 
    :type script_id: str
    :param _date: 
    :type _date: str
    :param change_description: 
    :type change_description: str
    :param editor: 
    :type editor: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    _date = util.deserialize_date(_date)
    return 'do some magic!'


def revisionhistory_get(revision_id=None, script_id=None, _date=None, change_description=None, editor=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """revisionhistory_get

     # noqa: E501

    :param revision_id: 
    :type revision_id: str
    :param script_id: 
    :type script_id: str
    :param _date: 
    :type _date: str
    :param change_description: 
    :type change_description: str
    :param editor: 
    :type editor: str
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

    :rtype: List[Revisionhistory]
    """
    _date = util.deserialize_date(_date)
    return 'do some magic!'


def revisionhistory_patch(body=None, prefer=None, revision_id=None, script_id=None, _date=None, change_description=None, editor=None):  # noqa: E501
    """revisionhistory_patch

     # noqa: E501

    :param body: revisionhistory
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param revision_id: 
    :type revision_id: str
    :param script_id: 
    :type script_id: str
    :param _date: 
    :type _date: str
    :param change_description: 
    :type change_description: str
    :param editor: 
    :type editor: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Revisionhistory.from_dict(connexion.request.get_json())  # noqa: E501
    _date = util.deserialize_date(_date)
    return 'do some magic!'


def revisionhistory_post(body=None, prefer=None, select=None):  # noqa: E501
    """revisionhistory_post

     # noqa: E501

    :param body: revisionhistory
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Revisionhistory.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
