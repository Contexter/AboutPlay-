import connexion
import six

from swagger_server.models.formattingrules import Formattingrules  # noqa: E501
from swagger_server import util


def formattingrules_delete(rule_id=None, script_id=None, rule_description=None, prefer=None):  # noqa: E501
    """formattingrules_delete

     # noqa: E501

    :param rule_id: 
    :type rule_id: str
    :param script_id: 
    :type script_id: str
    :param rule_description: 
    :type rule_description: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    return 'do some magic!'


def formattingrules_get(rule_id=None, script_id=None, rule_description=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """formattingrules_get

     # noqa: E501

    :param rule_id: 
    :type rule_id: str
    :param script_id: 
    :type script_id: str
    :param rule_description: 
    :type rule_description: str
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

    :rtype: List[Formattingrules]
    """
    return 'do some magic!'


def formattingrules_patch(body=None, prefer=None, rule_id=None, script_id=None, rule_description=None):  # noqa: E501
    """formattingrules_patch

     # noqa: E501

    :param body: formattingrules
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param rule_id: 
    :type rule_id: str
    :param script_id: 
    :type script_id: str
    :param rule_description: 
    :type rule_description: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Formattingrules.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def formattingrules_post(body=None, prefer=None, select=None):  # noqa: E501
    """formattingrules_post

     # noqa: E501

    :param body: formattingrules
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Formattingrules.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
