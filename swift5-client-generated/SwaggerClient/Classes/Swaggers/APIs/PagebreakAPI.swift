//
// PagebreakAPI.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation
import Alamofire


open class PagebreakAPI {
    /**
     * enum for parameter prefer
     */
    public enum Prefer_pagebreakDelete: String { 
        case representation = "return=representation"
        case minimal = "return=minimal"
        case _none = "return=none"
    }

    /**

     - parameter pageBreakId: (query)  (optional)
     - parameter scriptId: (query)  (optional)
     - parameter pageNumber: (query)  (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func pagebreakDelete(pageBreakId: String? = nil, scriptId: String? = nil, pageNumber: String? = nil, prefer: Prefer_pagebreakDelete? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        pagebreakDeleteWithRequestBuilder(pageBreakId: pageBreakId, scriptId: scriptId, pageNumber: pageNumber, prefer: prefer).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     - DELETE /pagebreak
     - 

     - parameter pageBreakId: (query)  (optional)
     - parameter scriptId: (query)  (optional)
     - parameter pageNumber: (query)  (optional)
     - parameter prefer: (header) Preference (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func pagebreakDeleteWithRequestBuilder(pageBreakId: String? = nil, scriptId: String? = nil, pageNumber: String? = nil, prefer: Prefer_pagebreakDelete? = nil) -> RequestBuilder<Void> {
        let path = "/pagebreak"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "page_break_id": pageBreakId, 
                        "script_id": scriptId, 
                        "page_number": pageNumber
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
    public enum Prefer_pagebreakGet: String { 
        case count&#x3D;none = "count=none"
    }

    /**

     - parameter pageBreakId: (query)  (optional)
     - parameter scriptId: (query)  (optional)
     - parameter pageNumber: (query)  (optional)
     - parameter select: (query) Filtering Columns (optional)
     - parameter order: (query) Ordering (optional)
     - parameter range: (header) Limiting and Pagination (optional)
     - parameter rangeUnit: (header) Limiting and Pagination (optional, default to items)
     - parameter offset: (query) Limiting and Pagination (optional)
     - parameter limit: (query) Limiting and Pagination (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func pagebreakGet(pageBreakId: String? = nil, scriptId: String? = nil, pageNumber: String? = nil, select: String? = nil, order: String? = nil, range: String? = nil, rangeUnit: String? = nil, offset: String? = nil, limit: String? = nil, prefer: Prefer_pagebreakGet? = nil, completion: @escaping ((_ data: [Pagebreak]?,_ error: Error?) -> Void)) {
        pagebreakGetWithRequestBuilder(pageBreakId: pageBreakId, scriptId: scriptId, pageNumber: pageNumber, select: select, order: order, range: range, rangeUnit: rangeUnit, offset: offset, limit: limit, prefer: prefer).execute { (response, error) -> Void in
            completion(response?.body, error)
        }
    }


    /**
     - GET /pagebreak
     - 

     - examples: [{contentType=application/json, example=[ {
  "page_number" : 1,
  "page_break_id" : 0,
  "script_id" : 6
}, {
  "page_number" : 1,
  "page_break_id" : 0,
  "script_id" : 6
} ]}]
     - parameter pageBreakId: (query)  (optional)
     - parameter scriptId: (query)  (optional)
     - parameter pageNumber: (query)  (optional)
     - parameter select: (query) Filtering Columns (optional)
     - parameter order: (query) Ordering (optional)
     - parameter range: (header) Limiting and Pagination (optional)
     - parameter rangeUnit: (header) Limiting and Pagination (optional, default to items)
     - parameter offset: (query) Limiting and Pagination (optional)
     - parameter limit: (query) Limiting and Pagination (optional)
     - parameter prefer: (header) Preference (optional)

     - returns: RequestBuilder<[Pagebreak]> 
     */
    open class func pagebreakGetWithRequestBuilder(pageBreakId: String? = nil, scriptId: String? = nil, pageNumber: String? = nil, select: String? = nil, order: String? = nil, range: String? = nil, rangeUnit: String? = nil, offset: String? = nil, limit: String? = nil, prefer: Prefer_pagebreakGet? = nil) -> RequestBuilder<[Pagebreak]> {
        let path = "/pagebreak"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "page_break_id": pageBreakId, 
                        "script_id": scriptId, 
                        "page_number": pageNumber, 
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

        let requestBuilder: RequestBuilder<[Pagebreak]>.Type = SwaggerClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "GET", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false, headers: headerParameters)
    }
    /**
     * enum for parameter prefer
     */
    public enum Prefer_pagebreakPatch: String { 
        case representation = "return=representation"
        case minimal = "return=minimal"
        case _none = "return=none"
    }

    /**

     - parameter body: (body) pagebreak (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter pageBreakId: (query)  (optional)
     - parameter scriptId: (query)  (optional)
     - parameter pageNumber: (query)  (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func pagebreakPatch(body: Pagebreak? = nil, prefer: Prefer_pagebreakPatch? = nil, pageBreakId: String? = nil, scriptId: String? = nil, pageNumber: String? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        pagebreakPatchWithRequestBuilder(body: body, prefer: prefer, pageBreakId: pageBreakId, scriptId: scriptId, pageNumber: pageNumber).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     - PATCH /pagebreak
     - 

     - parameter body: (body) pagebreak (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter pageBreakId: (query)  (optional)
     - parameter scriptId: (query)  (optional)
     - parameter pageNumber: (query)  (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func pagebreakPatchWithRequestBuilder(body: Pagebreak? = nil, prefer: Prefer_pagebreakPatch? = nil, pageBreakId: String? = nil, scriptId: String? = nil, pageNumber: String? = nil) -> RequestBuilder<Void> {
        let path = "/pagebreak"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters = JSONEncodingHelper.encodingParameters(forEncodableObject: body)
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "page_break_id": pageBreakId, 
                        "script_id": scriptId, 
                        "page_number": pageNumber
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
    public enum Prefer_pagebreakPost: String { 
        case return&#x3D;representation = "return=representation"
        case return&#x3D;minimal = "return=minimal"
        case return&#x3D;none = "return=none"
        case resolution&#x3D;ignoreDuplicates = "resolution=ignore-duplicates"
        case resolution&#x3D;mergeDuplicates = "resolution=merge-duplicates"
    }

    /**

     - parameter body: (body) pagebreak (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter select: (query) Filtering Columns (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func pagebreakPost(body: Pagebreak? = nil, prefer: Prefer_pagebreakPost? = nil, select: String? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        pagebreakPostWithRequestBuilder(body: body, prefer: prefer, select: select).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     - POST /pagebreak
     - 

     - parameter body: (body) pagebreak (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter select: (query) Filtering Columns (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func pagebreakPostWithRequestBuilder(body: Pagebreak? = nil, prefer: Prefer_pagebreakPost? = nil, select: String? = nil) -> RequestBuilder<Void> {
        let path = "/pagebreak"
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