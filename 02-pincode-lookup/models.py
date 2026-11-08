from pydantic import BaseModel,field_validator

class PincodeRequest(BaseModel):
   pincode:str
   @field_validator("pincode")
   @classmethod
   def validate_pincode():
      pass
