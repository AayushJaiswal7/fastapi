from fastapi import FastAPI,Query

app=FastAPI(
   title="Pincode Lookup API",
   description="Auto fill city and state from Indian Pincode during checkout"
)

@app.get("/")
def root():
   return{"message":"Pincode lookup api"}

