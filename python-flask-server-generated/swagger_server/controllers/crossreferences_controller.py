import connexion
import six

from swagger_server.models.crossreferences import Crossreferences  # noqa: E501
from swagger_server import util


def crossreferences_delete(cross_reference_id=None, scene_id=None, referenced_scene_id=None, description=None, prefer=None):  # noqa: E501
    """crossreferences_delete

     # noqa: E501

    :param cross_reference_id: 
    :type cross_reference_id: str
    :param scene_id: 
    :type scene_id: str
    :param referenced_scene_id: 
    :type referenced_scene_id: str
    :param description: 
    :type description: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    return 'do some magic!'


def crossreferences_get(cross_reference_id=None, scene_id=None, referenced_scene_id=None, description=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """crossreferences_get

     # noqa: E501

    :param cross_reference_id: 
    :type cross_reference_id: str
    :param scene_id: 
    :type scene_id: str
    :param referenced_scene_id: 
    :type referenced_scene_id: str
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

    :rtype: List[Crossreferences]
    """
    return 'do some magic!'


def crossreferences_patch(body=None, prefer=None, cross_reference_id=None, scene_id=None, referenced_scene_id=None, description=None):  # noqa: E501
    """crossreferences_patch

     # noqa: E501

    :param body: crossreferences
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param cross_reference_id: 
    :type cross_reference_id: str
    :param scene_id: 
    :type scene_id: str
    :param referenced_scene_id: 
    :type referenced_scene_id: str
    :param description: 
    :type description: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Crossreferences.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def crossreferences_post(body=None, prefer=None, select=None):  # noqa: E501
    """crossreferences_post

     # noqa: E501

    :param body: crossreferences
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Crossreferences.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
