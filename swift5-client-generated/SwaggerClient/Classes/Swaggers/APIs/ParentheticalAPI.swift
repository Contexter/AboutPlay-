//
// ParentheticalAPI.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation
import Alamofire


open class ParentheticalAPI {
    /**
     * enum for parameter prefer
     */
    public enum Prefer_parentheticalDelete: String { 
        case representation = "return=representation"
        case minimal = "return=minimal"
        case _none = "return=none"
    }

    /**

     - parameter parentheticalId: (query)  (optional)
     - parameter dialogueId: (query)  (optional)
     - parameter originalText: (query)  (optional)
     - parameter modernizedText: (query)  (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func parentheticalDelete(parentheticalId: String? = nil, dialogueId: String? = nil, originalText: String? = nil, modernizedText: String? = nil, prefer: Prefer_parentheticalDelete? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        parentheticalDeleteWithRequestBuilder(parentheticalId: parentheticalId, dialogueId: dialogueId, originalText: originalText, modernizedText: modernizedText, prefer: prefer).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     - DELETE /parenthetical
     - 

     - parameter parentheticalId: (query)  (optional)
     - parameter dialogueId: (query)  (optional)
     - parameter originalText: (query)  (optional)
     - parameter modernizedText: (query)  (optional)
     - parameter prefer: (header) Preference (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func parentheticalDeleteWithRequestBuilder(parentheticalId: String? = nil, dialogueId: String? = nil, originalText: String? = nil, modernizedText: String? = nil, prefer: Prefer_parentheticalDelete? = nil) -> RequestBuilder<Void> {
        let path = "/parenthetical"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "parenthetical_id": parentheticalId, 
                        "dialogue_id": dialogueId, 
                        "original_text": originalText, 
                        "modernized_text": modernizedText
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
    public enum Prefer_parentheticalGet: String { 
        case count&#x3D;none = "count=none"
    }

    /**

     - parameter parentheticalId: (query)  (optional)
     - parameter dialogueId: (query)  (optional)
     - parameter originalText: (query)  (optional)
     - parameter modernizedText: (query)  (optional)
     - parameter select: (query) Filtering Columns (optional)
     - parameter order: (query) Ordering (optional)
     - parameter range: (header) Limiting and Pagination (optional)
     - parameter rangeUnit: (header) Limiting and Pagination (optional, default to items)
     - parameter offset: (query) Limiting and Pagination (optional)
     - parameter limit: (query) Limiting and Pagination (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func parentheticalGet(parentheticalId: String? = nil, dialogueId: String? = nil, originalText: String? = nil, modernizedText: String? = nil, select: String? = nil, order: String? = nil, range: String? = nil, rangeUnit: String? = nil, offset: String? = nil, limit: String? = nil, prefer: Prefer_parentheticalGet? = nil, completion: @escaping ((_ data: [Parenthetical]?,_ error: Error?) -> Void)) {
        parentheticalGetWithRequestBuilder(parentheticalId: parentheticalId, dialogueId: dialogueId, originalText: originalText, modernizedText: modernizedText, select: select, order: order, range: range, rangeUnit: rangeUnit, offset: offset, limit: limit, prefer: prefer).execute { (response, error) -> Void in
            completion(response?.body, error)
        }
    }


    /**
     - GET /parenthetical
     - 

     - examples: [{contentType=application/json, example=[ {
  "modernized_text" : "modernized_text",
  "dialogue_id" : 6,
  "original_text" : "original_text",
  "parenthetical_id" : 0
}, {
  "modernized_text" : "modernized_text",
  "dialogue_id" : 6,
  "original_text" : "original_text",
  "parenthetical_id" : 0
} ]}]
     - parameter parentheticalId: (query)  (optional)
     - parameter dialogueId: (query)  (optional)
     - parameter originalText: (query)  (optional)
     - parameter modernizedText: (query)  (optional)
     - parameter select: (query) Filtering Columns (optional)
     - parameter order: (query) Ordering (optional)
     - parameter range: (header) Limiting and Pagination (optional)
     - parameter rangeUnit: (header) Limiting and Pagination (optional, default to items)
     - parameter offset: (query) Limiting and Pagination (optional)
     - parameter limit: (query) Limiting and Pagination (optional)
     - parameter prefer: (header) Preference (optional)

     - returns: RequestBuilder<[Parenthetical]> 
     */
    open class func parentheticalGetWithRequestBuilder(parentheticalId: String? = nil, dialogueId: String? = nil, originalText: String? = nil, modernizedText: String? = nil, select: String? = nil, order: String? = nil, range: String? = nil, rangeUnit: String? = nil, offset: String? = nil, limit: String? = nil, prefer: Prefer_parentheticalGet? = nil) -> RequestBuilder<[Parenthetical]> {
        let path = "/parenthetical"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "parenthetical_id": parentheticalId, 
                        "dialogue_id": dialogueId, 
                        "original_text": originalText, 
                        "modernized_text": modernizedText, 
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

        let requestBuilder: RequestBuilder<[Parenthetical]>.Type = SwaggerClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "GET", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false, headers: headerParameters)
    }
    /**
     * enum for parameter prefer
     */
    public enum Prefer_parentheticalPatch: String { 
        case representation = "return=representation"
        case minimal = "return=minimal"
        case _none = "return=none"
    }

    /**

     - parameter body: (body) parenthetical (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter parentheticalId: (query)  (optional)
     - parameter dialogueId: (query)  (optional)
     - parameter originalText: (query)  (optional)
     - parameter modernizedText: (query)  (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func parentheticalPatch(body: Parenthetical? = nil, prefer: Prefer_parentheticalPatch? = nil, parentheticalId: String? = nil, dialogueId: String? = nil, originalText: String? = nil, modernizedText: String? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        parentheticalPatchWithRequestBuilder(body: body, prefer: prefer, parentheticalId: parentheticalId, dialogueId: dialogueId, originalText: originalText, modernizedText: modernizedText).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     - PATCH /parenthetical
     - 

     - parameter body: (body) parenthetical (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter parentheticalId: (query)  (optional)
     - parameter dialogueId: (query)  (optional)
     - parameter originalText: (query)  (optional)
     - parameter modernizedText: (query)  (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func parentheticalPatchWithRequestBuilder(body: Parenthetical? = nil, prefer: Prefer_parentheticalPatch? = nil, parentheticalId: String? = nil, dialogueId: String? = nil, originalText: String? = nil, modernizedText: String? = nil) -> RequestBuilder<Void> {
        let path = "/parenthetical"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters = JSONEncodingHelper.encodingParameters(forEncodableObject: body)
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "parenthetical_id": parentheticalId, 
                        "dialogue_id": dialogueId, 
                        "original_text": originalText, 
                        "modernized_text": modernizedText
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
    public enum Prefer_parentheticalPost: String { 
        case return&#x3D;representation = "return=representation"
        case return&#x3D;minimal = "return=minimal"
        case return&#x3D;none = "return=none"
        case resolution&#x3D;ignoreDuplicates = "resolution=ignore-duplicates"
        case resolution&#x3D;mergeDuplicates = "resolution=merge-duplicates"
    }

    /**

     - parameter body: (body) parenthetical (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter select: (query) Filtering Columns (optional)
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func parentheticalPost(body: Parenthetical? = nil, prefer: Prefer_parentheticalPost? = nil, select: String? = nil, completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        parentheticalPostWithRequestBuilder(body: body, prefer: prefer, select: select).execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     - POST /parenthetical
     - 

     - parameter body: (body) parenthetical (optional)
     - parameter prefer: (header) Preference (optional)
     - parameter select: (query) Filtering Columns (optional)

     - returns: RequestBuilder<Void> 
     */
    open class func parentheticalPostWithRequestBuilder(body: Parenthetical? = nil, prefer: Prefer_parentheticalPost? = nil, select: String? = nil) -> RequestBuilder<Void> {
        let path = "/parenthetical"
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
