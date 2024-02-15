import connexion
import six

from swagger_server.models.note import Note  # noqa: E501
from swagger_server import util


def note_delete(note_id=None, script_id=None, type=None, text=None, prefer=None):  # noqa: E501
    """note_delete

     # noqa: E501

    :param note_id: 
    :type note_id: str
    :param script_id: 
    :type script_id: str
    :param type: 
    :type type: str
    :param text: 
    :type text: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    return 'do some magic!'


def note_get(note_id=None, script_id=None, type=None, text=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """note_get

     # noqa: E501

    :param note_id: 
    :type note_id: str
    :param script_id: 
    :type script_id: str
    :param type: 
    :type type: str
    :param text: 
    :type text: str
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

    :rtype: List[Note]
    """
    return 'do some magic!'


def note_patch(body=None, prefer=None, note_id=None, script_id=None, type=None, text=None):  # noqa: E501
    """note_patch

     # noqa: E501

    :param body: note
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param note_id: 
    :type note_id: str
    :param script_id: 
    :type script_id: str
    :param type: 
    :type type: str
    :param text: 
    :type text: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Note.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def note_post(body=None, prefer=None, select=None):  # noqa: E501
    """note_post

     # noqa: E501

    :param body: note
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Note.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
