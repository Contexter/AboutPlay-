//
// Pagebreak.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct Pagebreak: Codable {

    /** Note: This is a Primary Key.&lt;pk/&gt; */
    public var pageBreakId: Int
    /** Note: This is a Foreign Key to &#x60;script.script_id&#x60;.&lt;fk table&#x3D;&#x27;script&#x27; column&#x3D;&#x27;script_id&#x27;/&gt; */
    public var scriptId: Int?
    public var pageNumber: Int?

    public init(pageBreakId: Int, scriptId: Int? = nil, pageNumber: Int? = nil) {
        self.pageBreakId = pageBreakId
        self.scriptId = scriptId
        self.pageNumber = pageNumber
    }

    public enum CodingKeys: String, CodingKey { 
        case pageBreakId = "page_break_id"
        case scriptId = "script_id"
        case pageNumber = "page_number"
    }

}
