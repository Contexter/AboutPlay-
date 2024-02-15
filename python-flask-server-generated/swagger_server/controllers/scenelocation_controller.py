import connexion
import six

from swagger_server.models.scenelocation import Scenelocation  # noqa: E501
from swagger_server import util


def scenelocation_delete(location_id=None, description=None, historical_cultural_significance=None, prefer=None):  # noqa: E501
    """scenelocation_delete

     # noqa: E501

    :param location_id: 
    :type location_id: str
    :param description: 
    :type description: str
    :param historical_cultural_significance: 
    :type historical_cultural_significance: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    return 'do some magic!'


def scenelocation_get(location_id=None, description=None, historical_cultural_significance=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """scenelocation_get

     # noqa: E501

    :param location_id: 
    :type location_id: str
    :param description: 
    :type description: str
    :param historical_cultural_significance: 
    :type historical_cultural_significance: str
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

    :rtype: List[Scenelocation]
    """
    return 'do some magic!'


def scenelocation_patch(body=None, prefer=None, location_id=None, description=None, historical_cultural_significance=None):  # noqa: E501
    """scenelocation_patch

     # noqa: E501

    :param body: scenelocation
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param location_id: 
    :type location_id: str
    :param description: 
    :type description: str
    :param historical_cultural_significance: 
    :type historical_cultural_significance: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Scenelocation.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def scenelocation_post(body=None, prefer=None, select=None):  # noqa: E501
    """scenelocation_post

     # noqa: E501

    :param body: scenelocation
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Scenelocation.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
