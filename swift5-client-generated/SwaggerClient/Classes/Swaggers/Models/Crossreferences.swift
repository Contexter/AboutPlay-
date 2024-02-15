//
// Crossreferences.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation



public struct Crossreferences: Codable {

    /** Note: This is a Primary Key.&lt;pk/&gt; */
    public var crossReferenceId: Int
    /** Note: This is a Foreign Key to &#x60;scene.scene_id&#x60;.&lt;fk table&#x3D;&#x27;scene&#x27; column&#x3D;&#x27;scene_id&#x27;/&gt; */
    public var sceneId: Int?
    /** Note: This is a Foreign Key to &#x60;scene.scene_id&#x60;.&lt;fk table&#x3D;&#x27;scene&#x27; column&#x3D;&#x27;scene_id&#x27;/&gt; */
    public var referencedSceneId: Int?
    public var _description: String?

    public init(crossReferenceId: Int, sceneId: Int? = nil, referencedSceneId: Int? = nil, _description: String? = nil) {
        self.crossReferenceId = crossReferenceId
        self.sceneId = sceneId
        self.referencedSceneId = referencedSceneId
        self._description = _description
    }

    public enum CodingKeys: String, CodingKey { 
        case crossReferenceId = "cross_reference_id"
        case sceneId = "scene_id"
        case referencedSceneId = "referenced_scene_id"
        case _description = "description"
    }

}