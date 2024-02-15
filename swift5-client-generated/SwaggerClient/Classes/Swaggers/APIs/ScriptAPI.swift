//
// ScriptAPI.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation
import Alamofire


open class ScriptAPI {
    /**
     * enum for parameter prefer
     */
    public enum Prefer_scriptDelete: String { 
        case representation = "return=representation"
        case minimal = "return=minimal"
        case _none = "return=none"
    }

    /**

     - parameter scriptId: (query)  (optional)
     - parameter title: (query)  (optional)
     - parameter authorId: (query)  (optional)
     - parameter url: (query)  (optional)
     - parameter metadataId: (query)  (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func scriptDelete(scriptId: String? = nil, title: String? = nil, authorId: String? = nil, url: String? = nil, metadataId: String? = nil, prefer: Prefer_scriptDelete? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        scriptDeleteWithRequestBuilder(scriptId: scriptId, title: title, authorId: authorId, url: url, metadataId: metadataId, prefer: prefer).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     - DELETE /script
     - 

     - parameter scriptId: (query)  (optional)
     - parameter title: (query)  (optional)
     - parameter authorId: (query)  (optional)
     - parameter url: (query)  (optional)
     - parameter metadataId: (query)  (optional)
     - parameter prefer: (header) Preference (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func scriptDeleteWithRequestBuilder(scriptId: String? = nil, title: String? = nil, authorId: String? = nil, url: String? = nil, metadataId: String? = nil, prefer: Prefer_scriptDelete? = nil) -> RequestBuilder<Void> {
        let path = "/script"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "script_id": scriptId, 
                        "title": title, 
                        "author_id": authorId, 
                        "url": url, 
                        "metadata_id": metadataId
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
    public enum Prefer_scriptGet: String { 
        case count&#x3D;none = "count=none"
    }

    /**

     - parameter scriptId: (query)  (optional)
     - parameter title: (query)  (optional)
     - parameter authorId: (query)  (optional)
     - parameter url: (query)  (optional)
     - parameter metadataId: (query)  (optional)
     - parameter select: (query) Filtering Columns (optional)
     - parameter order: (query) Ordering (optional)
     - parameter range: (header) Limiting and Pagination (optional)
     - parameter rangeUnit: (header) Limiting and Pagination (optional, default to items)
     - parameter offset: (query) Limiting and Pagination (optional)
     - parameter limit: (query) Limiting and Pagination (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func scriptGet(scriptId: String? = nil, title: String? = nil, authorId: String? = nil, url: String? = nil, metadataId: String? = nil, select: String? = nil, order: String? = nil, range: String? = nil, rangeUnit: String? = nil, offset: String? = nil, limit: String? = nil, prefer: Prefer_scriptGet? = nil, completion: @escaping ((_ data: [Script]?,_ error: Error?) -> Void)) {
        scriptGetWithRequestBuilder(scriptId: scriptId, title: title, authorId: authorId, url: url, metadataId: metadataId, select: select, order: order, range: range, rangeUnit: rangeUnit, offset: offset, limit: limit, prefer: prefer).execute { (response, error) -> Void in
            completion(response?.body, error)
        }
    }


    /**
     - GET /script
     - 

     - examples: [{contentType=application/json, example=[ {
  "metadata_id" : 1,
  "script_id" : 0,
  "title" : "title",
  "author_id" : 6,
  "url" : "url"
}, {
  "metadata_id" : 1,
  "script_id" : 0,
  "title" : "title",
  "author_id" : 6,
  "url" : "url"
} ]}]
     - parameter scriptId: (query)  (optional)
     - parameter title: (query)  (optional)
     - parameter authorId: (query)  (optional)
     - parameter url: (query)  (optional)
     - parameter metadataId: (query)  (optional)
     - parameter select: (query) Filtering Columns (optional)
     - parameter order: (query) Ordering (optional)
     - parameter range: (header) Limiting and Pagination (optional)
     - parameter rangeUnit: (header) Limiting and Pagination (optional, default to items)
     - parameter offset: (query) Limiting and Pagination (optional)
     - parameter limit: (query) Limiting and Pagination (optional)
     - parameter prefer: (header) Preference (optional)

     - returns: RequestBuilder<[Script]> 
     */
    open class func scriptGetWithRequestBuilder(scriptId: String? = nil, title: String? = nil, authorId: String? = nil, url: String? = nil, metadataId: String? = nil, select: String? = nil, order: String? = nil, range: String? = nil, rangeUnit: String? = nil, offset: String? = nil, limit: String? = nil, prefer: Prefer_scriptGet? = nil) -> RequestBuilder<[Script]> {
        let path = "/script"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "script_id": scriptId, 
                        "title": title, 
                        "author_id": authorId, 
                        "url": url, 
                        "metadata_id": metadataId, 
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

        let requestBuilder: RequestBuilder<[Script]>.Type = SwaggerClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "GET", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false, headers: headerParameters)
    }
    /**
     * enum for parameter prefer
     */
    public enum Prefer_scriptPatch: String { 
        case representation = "return=representation"
        case minimal = "return=minimal"
        case _none = "return=none"
    }

    /**

     - parameter body: (body) script (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter scriptId: (query)  (optional)
     - parameter title: (query)  (optional)
     - parameter authorId: (query)  (optional)
     - parameter url: (query)  (optional)
     - parameter metadataId: (query)  (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func scriptPatch(body: Script? = nil, prefer: Prefer_scriptPatch? = nil, scriptId: String? = nil, title: String? = nil, authorId: String? = nil, url: String? = nil, metadataId: String? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        scriptPatchWithRequestBuilder(body: body, prefer: prefer, scriptId: scriptId, title: title, authorId: authorId, url: url, metadataId: metadataId).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     - PATCH /script
     - 

     - parameter body: (body) script (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter scriptId: (query)  (optional)
     - parameter title: (query)  (optional)
     - parameter authorId: (query)  (optional)
     - parameter url: (query)  (optional)
     - parameter metadataId: (query)  (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func scriptPatchWithRequestBuilder(body: Script? = nil, prefer: Prefer_scriptPatch? = nil, scriptId: String? = nil, title: String? = nil, authorId: String? = nil, url: String? = nil, metadataId: String? = nil) -> RequestBuilder<Void> {
        let path = "/script"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters = JSONEncodingHelper.encodingParameters(forEncodableObject: body)
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "script_id": scriptId, 
                        "title": title, 
                        "author_id": authorId, 
                        "url": url, 
                        "metadata_id": metadataId
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
    public enum Prefer_scriptPost: String { 
        case return&#x3D;representation = "return=representation"
        case return&#x3D;minimal = "return=minimal"
        case return&#x3D;none = "return=none"
        case resolution&#x3D;ignoreDuplicates = "resolution=ignore-duplicates"
        case resolution&#x3D;mergeDuplicates = "resolution=merge-duplicates"
    }

    /**

     - parameter body: (body) script (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter select: (query) Filtering Columns (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func scriptPost(body: Script? = nil, prefer: Prefer_scriptPost? = nil, select: String? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        scriptPostWithRequestBuilder(body: body, prefer: prefer, select: select).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     - POST /script
     - 

     - parameter body: (body) script (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter select: (query) Filtering Columns (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func scriptPostWithRequestBuilder(body: Script? = nil, prefer: Prefer_scriptPost? = nil, select: String? = nil) -> RequestBuilder<Void> {
        let path = "/script"
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