//
// Titlepage.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct Titlepage: Codable {

    /** Note: This is a Primary Key.&lt;pk/&gt; */
    public var titlePageId: Int
    /** Note: This is a Foreign Key to &#x60;script.script_id&#x60;.&lt;fk table&#x3D;&#x27;script&#x27; column&#x3D;&#x27;script_id&#x27;/&gt; */
    public var scriptId: Int?
    public var text: String?

    public init(titlePageId: Int, scriptId: Int? = nil, text: String? = nil) {
        self.titlePageId = titlePageId
        self.scriptId = scriptId
        self.text = text
    }

    public enum CodingKeys: String, CodingKey { 
        case titlePageId = "title_page_id"
        case scriptId = "script_id"
        case text
    }

}
