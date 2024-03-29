//
// MusicsoundAPI.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation
import Alamofire


open class MusicsoundAPI {
    /**
     * enum for parameter prefer
     */
    public enum Prefer_musicsoundDelete: String { 
        case representation = "return=representation"
        case minimal = "return=minimal"
        case _none = "return=none"
    }

    /**

     - parameter musicSoundId: (query)  (optional)
     - parameter sceneId: (query)  (optional)
     - parameter cue: (query)  (optional)
     - parameter _description: (query)  (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func musicsoundDelete(musicSoundId: String? = nil, sceneId: String? = nil, cue: String? = nil, _description: String? = nil, prefer: Prefer_musicsoundDelete? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        musicsoundDeleteWithRequestBuilder(musicSoundId: musicSoundId, sceneId: sceneId, cue: cue, _description: _description, prefer: prefer).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     - DELETE /musicsound
     - 

     - parameter musicSoundId: (query)  (optional)
     - parameter sceneId: (query)  (optional)
     - parameter cue: (query)  (optional)
     - parameter _description: (query)  (optional)
     - parameter prefer: (header) Preference (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func musicsoundDeleteWithRequestBuilder(musicSoundId: String? = nil, sceneId: String? = nil, cue: String? = nil, _description: String? = nil, prefer: Prefer_musicsoundDelete? = nil) -> RequestBuilder<Void> {
        let path = "/musicsound"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "music_sound_id": musicSoundId, 
                        "scene_id": sceneId, 
                        "cue": cue, 
                        "description": _description
        ])
        let nillableHeaders: [String: Any?] = [
                        "Prefer": prefer?.rawValue
        ]
        let headerParameters = APIHelper.rejectNilHeaders(nillableHeaders)

        let requestBuilder: RequestBuilder<Void>.Type = SwaggerClientAPI.requestBuilderFactory.getNonDecodableBuilder()

        return requestBuilder.init(method: "DELETE", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false, headers: headerParameters)
    }
    /**
     * enum for parameter prefer
     */
    public enum Prefer_musicsoundGet: String { 
        case count&#x3D;none = "count=none"
    }

    /**

     - parameter musicSoundId: (query)  (optional)
     - parameter sceneId: (query)  (optional)
     - parameter cue: (query)  (optional)
     - parameter _description: (query)  (optional)
     - parameter select: (query) Filtering Columns (optional)
     - parameter order: (query) Ordering (optional)
     - parameter range: (header) Limiting and Pagination (optional)
     - parameter rangeUnit: (header) Limiting and Pagination (optional, default to items)
     - parameter offset: (query) Limiting and Pagination (optional)
     - parameter limit: (query) Limiting and Pagination (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func musicsoundGet(musicSoundId: String? = nil, sceneId: String? = nil, cue: String? = nil, _description: String? = nil, select: String? = nil, order: String? = nil, range: String? = nil, rangeUnit: String? = nil, offset: String? = nil, limit: String? = nil, prefer: Prefer_musicsoundGet? = nil, completion: @escaping ((_ data: [Musicsound]?,_ error: Error?) -> Void)) {
        musicsoundGetWithRequestBuilder(musicSoundId: musicSoundId, sceneId: sceneId, cue: cue, _description: _description, select: select, order: order, range: range, rangeUnit: rangeUnit, offset: offset, limit: limit, prefer: prefer).execute { (response, error) -> Void in
            completion(response?.body, error)
        }
    }


    /**
     - GET /musicsound
     - 

     - examples: [{contentType=application/json, example=[ {
  "cue" : "cue",
  "music_sound_id" : 0,
  "scene_id" : 6,
  "description" : "description"
}, {
  "cue" : "cue",
  "music_sound_id" : 0,
  "scene_id" : 6,
  "description" : "description"
} ]}]
     - parameter musicSoundId: (query)  (optional)
     - parameter sceneId: (query)  (optional)
     - parameter cue: (query)  (optional)
     - parameter _description: (query)  (optional)
     - parameter select: (query) Filtering Columns (optional)
     - parameter order: (query) Ordering (optional)
     - parameter range: (header) Limiting and Pagination (optional)
     - parameter rangeUnit: (header) Limiting and Pagination (optional, default to items)
     - parameter offset: (query) Limiting and Pagination (optional)
     - parameter limit: (query) Limiting and Pagination (optional)
     - parameter prefer: (header) Preference (optional)

     - returns: RequestBuilder<[Musicsound]> 
     */
    open class func musicsoundGetWithRequestBuilder(musicSoundId: String? = nil, sceneId: String? = nil, cue: String? = nil, _description: String? = nil, select: String? = nil, order: String? = nil, range: String? = nil, rangeUnit: String? = nil, offset: String? = nil, limit: String? = nil, prefer: Prefer_musicsoundGet? = nil) -> RequestBuilder<[Musicsound]> {
        let path = "/musicsound"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "music_sound_id": musicSoundId, 
                        "scene_id": sceneId, 
                        "cue": cue, 
                        "description": _description, 
                        "select": select, 
                        "order": order, 
                        "offset": offset, 
                        "limit": limit
        ])
        let nillableHeaders: [String: Any?] = [
                        "Range": range,
                        "Range-Unit": rangeUnit,
                        "Prefer": prefer?.rawValue
        ]
        let headerParameters = APIHelper.rejectNilHeaders(nillableHeaders)

        let requestBuilder: RequestBuilder<[Musicsound]>.Type = SwaggerClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "GET", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false, headers: headerParameters)
    }
    /**
     * enum for parameter prefer
     */
    public enum Prefer_musicsoundPatch: String { 
        case representation = "return=representation"
        case minimal = "return=minimal"
        case _none = "return=none"
    }

    /**

     - parameter body: (body) musicsound (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter musicSoundId: (query)  (optional)
     - parameter sceneId: (query)  (optional)
     - parameter cue: (query)  (optional)
     - parameter _description: (query)  (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func musicsoundPatch(body: Musicsound? = nil, prefer: Prefer_musicsoundPatch? = nil, musicSoundId: String? = nil, sceneId: String? = nil, cue: String? = nil, _description: String? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        musicsoundPatchWithRequestBuilder(body: body, prefer: prefer, musicSoundId: musicSoundId, sceneId: sceneId, cue: cue, _description: _description).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     - PATCH /musicsound
     - 

     - parameter body: (body) musicsound (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter musicSoundId: (query)  (optional)
     - parameter sceneId: (query)  (optional)
     - parameter cue: (query)  (optional)
     - parameter _description: (query)  (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func musicsoundPatchWithRequestBuilder(body: Musicsound? = nil, prefer: Prefer_musicsoundPatch? = nil, musicSoundId: String? = nil, sceneId: String? = nil, cue: String? = nil, _description: String? = nil) -> RequestBuilder<Void> {
        let path = "/musicsound"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters = JSONEncodingHelper.encodingParameters(forEncodableObject: body)
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "music_sound_id": musicSoundId, 
                        "scene_id": sceneId, 
                        "cue": cue, 
                        "description": _description
        ])
        let nillableHeaders: [String: Any?] = [
                        "Prefer": prefer?.rawValue
        ]
        let headerParameters = APIHelper.rejectNilHeaders(nillableHeaders)

        let requestBuilder: RequestBuilder<Void>.Type = SwaggerClientAPI.requestBuilderFactory.getNonDecodableBuilder()

        return requestBuilder.init(method: "PATCH", URLString: (url?.string ?? URLString), parameters: parameters, isBody: true, headers: headerParameters)
    }
    /**
     * enum for parameter prefer
     */
    public enum Prefer_musicsoundPost: String { 
        case return&#x3D;representation = "return=representation"
        case return&#x3D;minimal = "return=minimal"
        case return&#x3D;none = "return=none"
        case resolution&#x3D;ignoreDuplicates = "resolution=ignore-duplicates"
        case resolution&#x3D;mergeDuplicates = "resolution=merge-duplicates"
    }

    /**

     - parameter body: (body) musicsound (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter select: (query) Filtering Columns (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func musicsoundPost(body: Musicsound? = nil, prefer: Prefer_musicsoundPost? = nil, select: String? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        musicsoundPostWithRequestBuilder(body: body, prefer: prefer, select: select).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     - POST /musicsound
     - 

     - parameter body: (body) musicsound (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter select: (query) Filtering Columns (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func musicsoundPostWithRequestBuilder(body: Musicsound? = nil, prefer: Prefer_musicsoundPost? = nil, select: String? = nil) -> RequestBuilder<Void> {
        let path = "/musicsound"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters = JSONEncodingHelper.encodingParameters(forEncodableObject: body)
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "select": select
        ])
        let nillableHeaders: [String: Any?] = [
                        "Prefer": prefer?.rawValue
        ]
        let headerParameters = APIHelper.rejectNilHeaders(nillableHeaders)

        let requestBuilder: RequestBuilder<Void>.Type = SwaggerClientAPI.requestBuilderFactory.getNonDecodableBuilder()

        return requestBuilder.init(method: "POST", URLString: (url?.string ?? URLString), parameters: parameters, isBody: true, headers: headerParameters)
    }
}
