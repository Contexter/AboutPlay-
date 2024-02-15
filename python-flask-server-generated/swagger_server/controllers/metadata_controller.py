import connexion
import six

from swagger_server.models.metadata import Metadata  # noqa: E501
from swagger_server import util


def metadata_delete(metadata_id=None, creation_date=None, last_modified_date=None, version_number=None, additional_information=None, prefer=None):  # noqa: E501
    """metadata_delete

     # noqa: E501

    :param metadata_id: 
    :type metadata_id: str
    :param creation_date: 
    :type creation_date: str
    :param last_modified_date: 
    :type last_modified_date: str
    :param version_number: 
    :type version_number: str
    :param additional_information: 
    :type additional_information: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    creation_date = util.deserialize_date(creation_date)
    last_modified_date = util.deserialize_date(last_modified_date)
    return 'do some magic!'


def metadata_get(metadata_id=None, creation_date=None, last_modified_date=None, version_number=None, additional_information=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """metadata_get

     # noqa: E501

    :param metadata_id: 
    :type metadata_id: str
    :param creation_date: 
    :type creation_date: str
    :param last_modified_date: 
    :type last_modified_date: str
    :param version_number: 
    :type version_number: str
    :param additional_information: 
    :type additional_information: str
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

    :rtype: List[Metadata]
    """
    creation_date = util.deserialize_date(creation_date)
    last_modified_date = util.deserialize_date(last_modified_date)
    return 'do some magic!'


def metadata_patch(body=None, prefer=None, metadata_id=None, creation_date=None, last_modified_date=None, version_number=None, additional_information=None):  # noqa: E501
    """metadata_patch

     # noqa: E501

    :param body: metadata
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param metadata_id: 
    :type metadata_id: str
    :param creation_date: 
    :type creation_date: str
    :param last_modified_date: 
    :type last_modified_date: str
    :param version_number: 
    :type version_number: str
    :param additional_information: 
    :type additional_information: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Metadata.from_dict(connexion.request.get_json())  # noqa: E501
    creation_date = util.deserialize_date(creation_date)
    last_modified_date = util.deserialize_date(last_modified_date)
    return 'do some magic!'


def metadata_post(body=None, prefer=None, select=None):  # noqa: E501
    """metadata_post

     # noqa: E501

    :param body: metadata
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Metadata.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
