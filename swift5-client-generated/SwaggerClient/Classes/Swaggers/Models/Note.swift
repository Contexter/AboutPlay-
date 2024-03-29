//
// Note.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct Note: Codable {

    /** Note: This is a Primary Key.&lt;pk/&gt; */
    public var noteId: Int
    /** Note: This is a Foreign Key to &#x60;script.script_id&#x60;.&lt;fk table&#x3D;&#x27;script&#x27; column&#x3D;&#x27;script_id&#x27;/&gt; */
    public var scriptId: Int?
    public var type: String?
    public var text: String?

    public init(noteId: Int, scriptId: Int? = nil, type: String? = nil, text: String? = nil) {
        self.noteId = noteId
        self.scriptId = scriptId
        self.type = type
        self.text = text
    }

    public enum CodingKeys: String, CodingKey { 
        case noteId = "note_id"
        case scriptId = "script_id"
        case type
        case text
    }

}
