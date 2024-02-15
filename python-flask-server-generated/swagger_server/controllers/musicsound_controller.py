import connexion
import six

from swagger_server.models.musicsound import Musicsound  # noqa: E501
from swagger_server import util


def musicsound_delete(music_sound_id=None, scene_id=None, cue=None, description=None, prefer=None):  # noqa: E501
    """musicsound_delete

     # noqa: E501

    :param music_sound_id: 
    :type music_sound_id: str
    :param scene_id: 
    :type scene_id: str
    :param cue: 
    :type cue: str
    :param description: 
    :type description: str
    :param prefer: Preference
    :type prefer: str

    :rtype: None
    """
    return 'do some magic!'


def musicsound_get(music_sound_id=None, scene_id=None, cue=None, description=None, select=None, order=None, range=None, range_unit=None, offset=None, limit=None, prefer=None):  # noqa: E501
    """musicsound_get

     # noqa: E501

    :param music_sound_id: 
    :type music_sound_id: str
    :param scene_id: 
    :type scene_id: str
    :param cue: 
    :type cue: str
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

    :rtype: List[Musicsound]
    """
    return 'do some magic!'


def musicsound_patch(body=None, prefer=None, music_sound_id=None, scene_id=None, cue=None, description=None):  # noqa: E501
    """musicsound_patch

     # noqa: E501

    :param body: musicsound
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param music_sound_id: 
    :type music_sound_id: str
    :param scene_id: 
    :type scene_id: str
    :param cue: 
    :type cue: str
    :param description: 
    :type description: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Musicsound.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def musicsound_post(body=None, prefer=None, select=None):  # noqa: E501
    """musicsound_post

     # noqa: E501

    :param body: musicsound
    :type body: dict | bytes
    :param prefer: Preference
    :type prefer: str
    :param select: Filtering Columns
    :type select: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Musicsound.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
