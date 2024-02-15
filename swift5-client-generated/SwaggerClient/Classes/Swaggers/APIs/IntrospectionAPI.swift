//
// IntrospectionAPI.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation
import Alamofire


open class IntrospectionAPI {
    /**
     OpenAPI description (this document)

     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func rootGet(completion: @escaping ((_ data: Void?,_ error: Error?) -> Void)) {
        rootGetWithRequestBuilder().execute { (response, error) -> Void in
            if error == nil {
                completion((), error)
            } else {
                completion(nil, error)
            }
        }
    }


    /**
     OpenAPI description (this document)
     - GET /
     - 


     - returns: RequestBuilder<Void> 
     */
    open class func rootGetWithRequestBuilder() -> RequestBuilder<Void> {
        let path = "/"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters: [String:Any]? = nil
        let url = URLComponents(string: URLString)


        let requestBuilder: RequestBuilder<Void>.Type = SwaggerClientAPI.requestBuilderFactory.getNonDecodableBuilder()

        return requestBuilder.init(method: "GET", URLString: (url?.string ?? URLString), parameters: parameters, isBody: false)
    }
}
