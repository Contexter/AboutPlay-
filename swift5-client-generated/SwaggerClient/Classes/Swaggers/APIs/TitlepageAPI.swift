//
// TitlepageAPI.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation
import Alamofire


open class TitlepageAPI {
    /**
     * enum for parameter prefer
     */
    public enum Prefer_titlepageDelete: String { 
        case representation = "return=representation"
        case minimal = "return=minimal"
        case _none = "return=none"
    }

    /**

     - parameter titlePageId: (query)  (optional)
     - parameter scriptId: (query)  (optional)
     - parameter text: (query)  (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func titlepageDelete(titlePageId: String? = nil, scriptId: String? = nil, text: String? = nil, prefer: Prefer_titlepageDelete? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        titlepageDeleteWithRequestBuilder(titlePageId: titlePageId, scriptId: scriptId, text: text, prefer: prefer).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     - DELETE /titlepage
     - 

     - parameter titlePageId: (query)  (optional)
     - parameter scriptId: (query)  (optional)
     - parameter text: (query)  (optional)
     - parameter prefer: (header) Preference (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func titlepageDeleteWithRequestBuilder(titlePageId: String? = nil, scriptId: String? = nil, text: String? = nil, prefer: Prefer_titlepageDelete? = nil) -> RequestBuilder<Void> {
        let path = "/titlepage"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "title_page_id": titlePageId, 
                        "script_id": scriptId, 
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
    public enum Prefer_titlepageGet: String { 
        case count&#x3D;none = "count=none"
    }

    /**

     - parameter titlePageId: (query)  (optional)
     - parameter scriptId: (query)  (optional)
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
    open class func titlepageGet(titlePageId: String? = nil, scriptId: String? = nil, text: String? = nil, select: String? = nil, order: String? = nil, range: String? = nil, rangeUnit: String? = nil, offset: String? = nil, limit: String? = nil, prefer: Prefer_titlepageGet? = nil, completion: @escaping ((_ data: [Titlepage]?,_ error: Error?) -> Void)) {
        titlepageGetWithRequestBuilder(titlePageId: titlePageId, scriptId: scriptId, text: text, select: select, order: order, range: range, rangeUnit: rangeUnit, offset: offset, limit: limit, prefer: prefer).execute { (response, error) -> Void in
            completion(response?.body, error)
        }
    }


    /**
     - GET /titlepage
     - 

     - examples: [{contentType=application/json, example=[ {
  "title_page_id" : 0,
  "script_id" : 6,
  "text" : "text"
}, {
  "title_page_id" : 0,
  "script_id" : 6,
  "text" : "text"
} ]}]
     - parameter titlePageId: (query)  (optional)
     - parameter scriptId: (query)  (optional)
     - parameter text: (query)  (optional)
     - parameter select: (query) Filtering Columns (optional)
     - parameter order: (query) Ordering (optional)
     - parameter range: (header) Limiting and Pagination (optional)
     - parameter rangeUnit: (header) Limiting and Pagination (optional, default to items)
     - parameter offset: (query) Limiting and Pagination (optional)
     - parameter limit: (query) Limiting and Pagination (optional)
     - parameter prefer: (header) Preference (optional)

     - returns: RequestBuilder<[Titlepage]> 
     */
    open class func titlepageGetWithRequestBuilder(titlePageId: String? = nil, scriptId: String? = nil, text: String? = nil, select: String? = nil, order: String? = nil, range: String? = nil, rangeUnit: String? = nil, offset: String? = nil, limit: String? = nil, prefer: Prefer_titlepageGet? = nil) -> RequestBuilder<[Titlepage]> {
        let path = "/titlepage"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "title_page_id": titlePageId, 
                        "script_id": scriptId, 
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

        let requestBuilder: RequestBuilder<[Titlepage]>.Type = SwaggerClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "GET", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false, headers: headerParameters)
    }
    /**
     * enum for parameter prefer
     */
    public enum Prefer_titlepagePatch: String { 
        case representation = "return=representation"
        case minimal = "return=minimal"
        case _none = "return=none"
    }

    /**

     - parameter body: (body) titlepage (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter titlePageId: (query)  (optional)
     - parameter scriptId: (query)  (optional)
     - parameter text: (query)  (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func titlepagePatch(body: Titlepage? = nil, prefer: Prefer_titlepagePatch? = nil, titlePageId: String? = nil, scriptId: String? = nil, text: String? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        titlepagePatchWithRequestBuilder(body: body, prefer: prefer, titlePageId: titlePageId, scriptId: scriptId, text: text).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     - PATCH /titlepage
     - 

     - parameter body: (body) titlepage (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter titlePageId: (query)  (optional)
     - parameter scriptId: (query)  (optional)
     - parameter text: (query)  (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func titlepagePatchWithRequestBuilder(body: Titlepage? = nil, prefer: Prefer_titlepagePatch? = nil, titlePageId: String? = nil, scriptId: String? = nil, text: String? = nil) -> RequestBuilder<Void> {
        let path = "/titlepage"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters = JSONEncodingHelper.encodingParameters(forEncodableObject: body)
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "title_page_id": titlePageId, 
                        "script_id": scriptId, 
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
    public enum Prefer_titlepagePost: String { 
        case return&#x3D;representation = "return=representation"
        case return&#x3D;minimal = "return=minimal"
        case return&#x3D;none = "return=none"
        case resolution&#x3D;ignoreDuplicates = "resolution=ignore-duplicates"
        case resolution&#x3D;mergeDuplicates = "resolution=merge-duplicates"
    }

    /**

     - parameter body: (body) titlepage (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter select: (query) Filtering Columns (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func titlepagePost(body: Titlepage? = nil, prefer: Prefer_titlepagePost? = nil, select: String? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        titlepagePostWithRequestBuilder(body: body, prefer: prefer, select: select).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     - POST /titlepage
     - 

     - parameter body: (body) titlepage (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter select: (query) Filtering Columns (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func titlepagePostWithRequestBuilder(body: Titlepage? = nil, prefer: Prefer_titlepagePost? = nil, select: String? = nil) -> RequestBuilder<Void> {
        let path = "/titlepage"
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
