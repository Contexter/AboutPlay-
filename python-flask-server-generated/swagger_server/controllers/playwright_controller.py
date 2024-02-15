import connexion
import six

from swagger_server.models.playwright import Playwright  # noqa: E501
from swagger_server import util


def playwright_delete(author_id=None, name=None, biography=None, contact_information=None, prefer=None):  # noqa: E501
    """playwright_delete

     # noqa: E501

    :param author_id: 
    :type author_id: str
    :param name: 
    :type name: str
    :param biography: 
    :type biography: str
    :param contact_information: 
    :type contact_information: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    return 'do some magic!'


def playwright_get(author_id=None, name=None, biography=None, contact_information=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """playwright_get

     # noqa: E501

    :param author_id: 
    :type author_id: str
    :param name: 
    :type name: str
    :param biography: 
    :type biography: str
    :param contact_information: 
    :type contact_information: str
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

    :rtype: List[Playwright]
    """
    return 'do some magic!'


def playwright_patch(body=None, prefer=None, author_id=None, name=None, biography=None, contact_information=None):  # noqa: E501
    """playwright_patch

     # noqa: E501

    :param body: playwright
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param author_id: 
    :type author_id: str
    :param name: 
    :type name: str
    :param biography: 
    :type biography: str
    :param contact_information: 
    :type contact_information: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Playwright.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def playwright_post(body=None, prefer=None, select=None):  # noqa: E501
    """playwright_post

     # noqa: E501

    :param body: playwright
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Playwright.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
