# Dialogue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dialogue_id** | **int** | Note: This is a Primary Key.&lt;pk/&gt; | 
**scene_id** | **int** | Note: This is a Foreign Key to &#x60;scene.scene_id&#x60;.&lt;fk table&#x3D;&#x27;scene&#x27; column&#x3D;&#x27;scene_id&#x27;/&gt; | [optional] 
**character_id** | **int** | Note: This is a Foreign Key to &#x60;character.character_id&#x60;.&lt;fk table&#x3D;&#x27;character&#x27; column&#x3D;&#x27;character_id&#x27;/&gt; | [optional] 
**original_text** | **str** |  | [optional] 
**modernized_text** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

