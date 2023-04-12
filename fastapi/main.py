
from geocoding_api import get_coordinates_current_location
from weather_api import get_weather

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_all():
    weather_data = get_weather(*get_coordinates_current_location())
    return weather_data["current"]

#@app.get("/{city}")
#def get_all(city: str):
#    weather_data = get_weather(*get_coordinates_current_location())
#    
#    return {
#        city: {
#            "temp": weather_data["current"]["temp"],
#            "sunrise": weather_data["current"]["sunrise"],
#            "sunset": weather_data["current"]["sunset"],
#        }
#    }


#@app.get("/temp")
#def get_temp():
#    return {"Hello": "World"}
#
#@app.get("/temp/{city}")
#def get_temp_for_city():
#    return {"Hello": "World"}
#
#
#@app.get("/items/{item_id}")
#def get_temp_for_cities(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}