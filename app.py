from fastapi import FastAPI
from pydantic import BaseModel # basemodel is use for validation
from typing import List

app = FastAPI()

# defining the data structure of the python

class Tea(BaseModel):
    id : int
    name : str
    origin : str

teas: List[Tea] = []  #for collecting the database

@app.get("/")
def read_root():
    return {"message":"Welcome to finalBOSSxLive"}

@app.get("/teas")
def get_teas():
    return teas 

@app.post("/teas")
def add_tea(tea:Tea):
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def update_tea(tea_id:int , updated_tea : Tea):
    for index , tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index]==update_tea
            return update_tea
    return {"error" : "Tea not found"}

@app.delete("/teas/{teas_id}")
def delete_tea(tea_id:int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deleted = teas.pop(index) 
            return deleted
    return {"error" : "Tea not found"}