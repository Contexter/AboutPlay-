//
// NoteAPI.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation
import Alamofire


open class NoteAPI {
    /**
     * enum for parameter prefer
     */
    public enum Prefer_noteDelete: String { 
        case representation = "return=representation"
        case minimal = "return=minimal"
        case _none = "return=none"
    }

    /**

     - parameter noteId: (query)  (optional)
     - parameter scriptId: (query)  (optional)
     - parameter type: (query)  (optional)
     - parameter text: (query)  (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func noteDelete(noteId: String? = nil, scriptId: String? = nil, type: String? = nil, text: String? = nil, prefer: Prefer_noteDelete? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        noteDeleteWithRequestBuilder(noteId: noteId, scriptId: scriptId, type: type, text: text, prefer: prefer).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     - DELETE /note
     - 

     - parameter noteId: (query)  (optional)
     - parameter scriptId: (query)  (optional)
     - parameter type: (query)  (optional)
     - parameter text: (query)  (optional)
     - parameter prefer: (header) Preference (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func noteDeleteWithRequestBuilder(noteId: String? = nil, scriptId: String? = nil, type: String? = nil, text: String? = nil, prefer: Prefer_noteDelete? = nil) -> RequestBuilder<Void> {
        let path = "/note"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "note_id": noteId, 
                        "script_id": scriptId, 
                        "type": type, 
                        "text": text
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
    public enum Prefer_noteGet: String { 
        case count&#x3D;none = "count=none"
    }

    /**

     - parameter noteId: (query)  (optional)
     - parameter scriptId: (query)  (optional)
     - parameter type: (query)  (optional)
     - parameter text: (query)  (optional)
     - parameter select: (query) Filtering Columns (optional)
     - parameter order: (query) Ordering (optional)
     - parameter range: (header) Limiting and Pagination (optional)
     - parameter rangeUnit: (header) Limiting and Pagination (optional, default to items)
     - parameter offset: (query) Limiting and Pagination (optional)
     - parameter limit: (query) Limiting and Pagination (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func noteGet(noteId: String? = nil, scriptId: String? = nil, type: String? = nil, text: String? = nil, select: String? = nil, order: String? = nil, range: String? = nil, rangeUnit: String? = nil, offset: String? = nil, limit: String? = nil, prefer: Prefer_noteGet? = nil, completion: @escaping ((_ data: [Note]?,_ error: Error?) -> Void)) {
        noteGetWithRequestBuilder(noteId: noteId, scriptId: scriptId, type: type, text: text, select: select, order: order, range: range, rangeUnit: rangeUnit, offset: offset, limit: limit, prefer: prefer).execute { (response, error) -> Void in
            completion(response?.body, error)
        }
    }


    /**
     - GET /note
     - 

     - examples: [{contentType=application/json, example=[ {
  "note_id" : 0,
  "script_id" : 6,
  "text" : "text",
  "type" : "type"
}, {
  "note_id" : 0,
  "script_id" : 6,
  "text" : "text",
  "type" : "type"
} ]}]
     - parameter noteId: (query)  (optional)
     - parameter scriptId: (query)  (optional)
     - parameter type: (query)  (optional)
     - parameter text: (query)  (optional)
     - parameter select: (query) Filtering Columns (optional)
     - parameter order: (query) Ordering (optional)
     - parameter range: (header) Limiting and Pagination (optional)
     - parameter rangeUnit: (header) Limiting and Pagination (optional, default to items)
     - parameter offset: (query) Limiting and Pagination (optional)
     - parameter limit: (query) Limiting and Pagination (optional)
     - parameter prefer: (header) Preference (optional)

     - returns: RequestBuilder<[Note]> 
     */
    open class func noteGetWithRequestBuilder(noteId: String? = nil, scriptId: String? = nil, type: String? = nil, text: String? = nil, select: String? = nil, order: String? = nil, range: String? = nil, rangeUnit: String? = nil, offset: String? = nil, limit: String? = nil, prefer: Prefer_noteGet? = nil) -> RequestBuilder<[Note]> {
        let path = "/note"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "note_id": noteId, 
                        "script_id": scriptId, 
                        "type": type, 
                        "text": text, 
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

        let requestBuilder: RequestBuilder<[Note]>.Type = SwaggerClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "GET", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false, headers: headerParameters)
    }
    /**
     * enum for parameter prefer
     */
    public enum Prefer_notePatch: String { 
        case representation = "return=representation"
        case minimal = "return=minimal"
        case _none = "return=none"
    }

    /**

     - parameter body: (body) note (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter noteId: (query)  (optional)
     - parameter scriptId: (query)  (optional)
     - parameter type: (query)  (optional)
     - parameter text: (query)  (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func notePatch(body: Note? = nil, prefer: Prefer_notePatch? = nil, noteId: String? = nil, scriptId: String? = nil, type: String? = nil, text: String? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        notePatchWithRequestBuilder(body: body, prefer: prefer, noteId: noteId, scriptId: scriptId, type: type, text: text).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     - PATCH /note
     - 

     - parameter body: (body) note (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter noteId: (query)  (optional)
     - parameter scriptId: (query)  (optional)
     - parameter type: (query)  (optional)
     - parameter text: (query)  (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func notePatchWithRequestBuilder(body: Note? = nil, prefer: Prefer_notePatch? = nil, noteId: String? = nil, scriptId: String? = nil, type: String? = nil, text: String? = nil) -> RequestBuilder<Void> {
        let path = "/note"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters = JSONEncodingHelper.encodingParameters(forEncodableObject: body)
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "note_id": noteId, 
                        "script_id": scriptId, 
                        "type": type, 
                        "text": text
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
    public enum Prefer_notePost: String { 
        case return&#x3D;representation = "return=representation"
        case return&#x3D;minimal = "return=minimal"
        case return&#x3D;none = "return=none"
        case resolution&#x3D;ignoreDuplicates = "resolution=ignore-duplicates"
        case resolution&#x3D;mergeDuplicates = "resolution=merge-duplicates"
    }

    /**

     - parameter body: (body) note (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter select: (query) Filtering Columns (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func notePost(body: Note? = nil, prefer: Prefer_notePost? = nil, select: String? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        notePostWithRequestBuilder(body: body, prefer: prefer, select: select).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     - POST /note
     - 

     - parameter body: (body) note (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter select: (query) Filtering Columns (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func notePostWithRequestBuilder(body: Note? = nil, prefer: Prefer_notePost? = nil, select: String? = nil) -> RequestBuilder<Void> {
        let path = "/note"
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
