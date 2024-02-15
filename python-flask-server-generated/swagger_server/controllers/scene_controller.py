import connexion
import six

from swagger_server.models.scene import Scene  # noqa: E501
from swagger_server import util


def scene_delete(scene_id=None, act_id=None, scene_number=None, synopsis=None, notes=None, prefer=None):  # noqa: E501
    """scene_delete

     # noqa: E501

    :param scene_id: 
    :type scene_id: str
    :param act_id: 
    :type act_id: str
    :param scene_number: 
    :type scene_number: str
    :param synopsis: 
    :type synopsis: str
    :param notes: 
    :type notes: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    return 'do some magic!'


def scene_get(scene_id=None, act_id=None, scene_number=None, synopsis=None, notes=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """scene_get

     # noqa: E501

    :param scene_id: 
    :type scene_id: str
    :param act_id: 
    :type act_id: str
    :param scene_number: 
    :type scene_number: str
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

    :rtype: List[Scene]
    """
    return 'do some magic!'


def scene_patch(body=None, prefer=None, scene_id=None, act_id=None, scene_number=None, synopsis=None, notes=None):  # noqa: E501
    """scene_patch

     # noqa: E501

    :param body: scene
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param scene_id: 
    :type scene_id: str
    :param act_id: 
    :type act_id: str
    :param scene_number: 
    :type scene_number: str
    :param synopsis: 
    :type synopsis: str
    :param notes: 
    :type notes: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Scene.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def scene_post(body=None, prefer=None, select=None):  # noqa: E501
    """scene_post

     # noqa: E501

    :param body: scene
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Scene.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
