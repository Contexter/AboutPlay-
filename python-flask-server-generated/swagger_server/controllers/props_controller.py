import connexion
import six

from swagger_server.models.props import Props  # noqa: E501
from swagger_server import util


def props_delete(prop_id=None, scene_id=None, description=None, prefer=None):  # noqa: E501
    """props_delete

     # noqa: E501

    :param prop_id: 
    :type prop_id: str
    :param scene_id: 
    :type scene_id: str
    :param description: 
    :type description: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    return 'do some magic!'


def props_get(prop_id=None, scene_id=None, description=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """props_get

     # noqa: E501

    :param prop_id: 
    :type prop_id: str
    :param scene_id: 
    :type scene_id: str
    :param description: 
    :type description: str
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

    :rtype: List[Props]
    """
    return 'do some magic!'


def props_patch(body=None, prefer=None, prop_id=None, scene_id=None, description=None):  # noqa: E501
    """props_patch

     # noqa: E501

    :param body: props
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param prop_id: 
    :type prop_id: str
    :param scene_id: 
    :type scene_id: str
    :param description: 
    :type description: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Props.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def props_post(body=None, prefer=None, select=None):  # noqa: E501
    """props_post

     # noqa: E501

    :param body: props
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Props.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
