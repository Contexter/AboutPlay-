import connexion
import six

from swagger_server.models.characterrelationship import Characterrelationship  # noqa: E501
from swagger_server import util


def characterrelationship_delete(relationship_id=None, character1_id=None, character2_id=None, relationship_type=None, prefer=None):  # noqa: E501
    """characterrelationship_delete

     # noqa: E501

    :param relationship_id: 
    :type relationship_id: str
    :param character1_id: 
    :type character1_id: str
    :param character2_id: 
    :type character2_id: str
    :param relationship_type: 
    :type relationship_type: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    return 'do some magic!'


def characterrelationship_get(relationship_id=None, character1_id=None, character2_id=None, relationship_type=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """characterrelationship_get

     # noqa: E501

    :param relationship_id: 
    :type relationship_id: str
    :param character1_id: 
    :type character1_id: str
    :param character2_id: 
    :type character2_id: str
    :param relationship_type: 
    :type relationship_type: str
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

    :rtype: List[Characterrelationship]
    """
    return 'do some magic!'


def characterrelationship_patch(body=None, prefer=None, relationship_id=None, character1_id=None, character2_id=None, relationship_type=None):  # noqa: E501
    """characterrelationship_patch

     # noqa: E501

    :param body: characterrelationship
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param relationship_id: 
    :type relationship_id: str
    :param character1_id: 
    :type character1_id: str
    :param character2_id: 
    :type character2_id: str
    :param relationship_type: 
    :type relationship_type: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Characterrelationship.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def characterrelationship_post(body=None, prefer=None, select=None):  # noqa: E501
    """characterrelationship_post

     # noqa: E501

    :param body: characterrelationship
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Characterrelationship.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
