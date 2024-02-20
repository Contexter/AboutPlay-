
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Example Pydantic models based on typical Swagger-generated client structures
class Character(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

class Dialogue(BaseModel):
    id: int
    character_id: int
    text: str

class Scene(BaseModel):
    id: int
    title: str
    description: Optional[str] = None

# Mock database
characters = [
    {"id": 1, "name": "Character One", "description": "Description One"},
    {"id": 2, "name": "Character Two", "description": "Description Two"}
]

dialogues = [
    {"id": 1, "character_id": 1, "text": "Dialogue One"},
    {"id": 2, "character_id": 2, "text": "Dialogue Two"}
]

scenes = [
    {"id": 1, "title": "Scene One", "description": "Scene Description One"},
    {"id": 2, "title": "Scene Two", "description": "Scene Description Two"}
]

@app.get("/characters", response_model=List[Character])
async def read_characters():
    return characters

@app.post("/characters", response_model=Character)
async def add_character(character: Character):
    characters.append(character.dict())
    return character

@app.get("/dialogues", response_model=List[Dialogue])
async def read_dialogues():
    return dialogues

@app.get("/scenes", response_model=List[Scene])
async def read_scenes():
    return scenes

