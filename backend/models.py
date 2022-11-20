import uuid
from pydantic import BaseModel, Field

class PoloSchema(BaseModel):
    _id: str = Field(...)
    ad_price: str = Field(...)
    model_year: str = Field(...)
    kms_driven: str = Field(...)
    ad_title: str = Field(...)
    ad_location: str = Field(...)
    ad_link: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "_id":"1704318164",
                "ad_price":"545000",
                "model_year":"2017",
                "kms_driven":"93500.0",
                "ad_title":"Volkswagen Polo",
                "ad_location":"Punkunnam",
                "ad_link":"/en-in/item/volkswagen-polo-15-tdi-comfortline-2017-diesel-iid-1704318164"
            }
        }
    
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}