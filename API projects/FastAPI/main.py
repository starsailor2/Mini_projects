from fastapi import FastAPI  # type: ignore #core 
from pydantic import BaseModel #define guildelines for syntax
from typing import List

#define an app instance
app = FastAPI()

# pydantic contain 2 models (data input for web requests and data output for web responses)
class Tea(BaseModel):  #data model name Tea
    id:int
    name:str  # defines the data structure for tea name
    origin:str

# create a database (in-memory list for simplicity)
teas: List[Tea] = [
    Tea(id=1, name="Green", origin="China"),
    Tea(id=2, name="Black", origin="India"),
    Tea(id=3, name="Oolong", origin="Taiwan"),
]  # teas would be list data type containing Tea data

# decorator to define a GET endpoint at the root URL
@app.get("/") # in bracket there is this route define
def read_root(): #method definition
    return {"message": "Welcome to the Tea API!"} #return a welcome message

@app.get("/teas")
def get_teas():  #method to get all teas
    return teas  #return the list of teas

@app.post("/teas")
def add_tea(tea: Tea):
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")  # in put request , we add the id also
def update_tea(tea_id: int, updated_tea: Tea):   #(value:data_type), Tea is use as a pydantic value
    for index, tea in enumerate(teas):
        if tea.id == tea_id: #if the given id matches with the id in the teas array, then that id will get updated to the given value
            teas[index] = updated_tea
            return updated_tea
    return {"error": "Tea not found"} 

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id: #if the given input id matches with the id in the teas array(list in python) then that id will get pop and stored in deleted variable 
            deleted = teas.pop(index)
            return deleted
    return {"error": "Tea not found"}
