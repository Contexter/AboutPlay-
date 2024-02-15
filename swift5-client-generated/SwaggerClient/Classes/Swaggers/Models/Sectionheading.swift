//
// Sectionheading.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct Sectionheading: Codable {

    /** Note: This is a Primary Key.&lt;pk/&gt; */
    public var sectionId: Int
    /** Note: This is a Foreign Key to &#x60;script.script_id&#x60;.&lt;fk table&#x3D;&#x27;script&#x27; column&#x3D;&#x27;script_id&#x27;/&gt; */
    public var scriptId: Int?
    public var text: String?

    public init(sectionId: Int, scriptId: Int? = nil, text: String? = nil) {
        self.sectionId = sectionId
        self.scriptId = scriptId
        self.text = text
    }

    public enum CodingKeys: String, CodingKey { 
        case sectionId = "section_id"
        case scriptId = "script_id"
        case text
    }

}
