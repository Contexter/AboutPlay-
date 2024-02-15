import connexion
import six

from swagger_server.models.act import Act  # noqa: E501
from swagger_server import util


def act_delete(act_id=None, script_id=None, act_number=None, synopsis=None, notes=None, prefer=None):  # noqa: E501
    """act_delete

     # noqa: E501

    :param act_id: 
    :type act_id: str
    :param script_id: 
    :type script_id: str
    :param act_number: 
    :type act_number: str
    :param synopsis: 
    :type synopsis: str
    :param notes: 
    :type notes: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    return 'do some magic!'


def act_get(act_id=None, script_id=None, act_number=None, synopsis=None, notes=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """act_get

     # noqa: E501

    :param act_id: 
    :type act_id: str
    :param script_id: 
    :type script_id: str
    :param act_number: 
    :type act_number: str
    :param synopsis: 
    :type synopsis: str
    :param notes: 
    :type notes: str
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

    :rtype: List[Act]
    """
    return 'do some magic!'


def act_patch(body=None, prefer=None, act_id=None, script_id=None, act_number=None, synopsis=None, notes=None):  # noqa: E501
    """act_patch

     # noqa: E501

    :param body: act
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param act_id: 
    :type act_id: str
    :param script_id: 
    :type script_id: str
    :param act_number: 
    :type act_number: str
    :param synopsis: 
    :type synopsis: str
    :param notes: 
    :type notes: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Act.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def act_post(body=None, prefer=None, select=None):  # noqa: E501
    """act_post

     # noqa: E501

    :param body: act
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Act.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
