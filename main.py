from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import openai
from openai import OpenAIError
from dotenv import load_dotenv
import os
import logging
import time

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="Trip Planner GPT")

# Set up templates
templates = Jinja2Templates(directory="templates")

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize OpenAI client with timeout
api_key = os.getenv("OPENAI_API_KEY")
if not api_key or api_key == "your_api_key_here":
    logger.error("OpenAI API key is not set or is using the default placeholder value")

client = openai.OpenAI(
    api_key=api_key,
    timeout=60.0  # 60 second timeout
)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.post("/plan_trip")
async def plan_trip(
    destination: str = Form(...),
    dates: str = Form(...),
    budget: str = Form(...),
    preferences: str = Form(...)
):
    # Log the request
    logger.info(f"Planning trip to {destination} for {dates}")
    
    # Construct the prompt for GPT
    prompt = f"""Help plan a trip to {destination} for the dates {dates} with a budget of {budget}.
    Additional preferences: {preferences}
    
    Please provide:
    1. Suggested areas to stay
    2. Recommended Airbnb search criteria
    3. Must-see attractions
    4. Daily itinerary outline
    5. Budget breakdown"""

    try:
        # Call OpenAI API with timeout
        start_time = time.time()
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a helpful travel planner with expertise in finding great Airbnb accommodations and creating detailed itineraries."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000  # Limit response size
        )
        logger.info(f"OpenAI API call completed in {time.time() - start_time:.2f} seconds")
        
        return {"plan": response.choices[0].message.content}
    
    except OpenAIError as e:
        logger.error(f"OpenAI API error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating trip plan: {str(e)}")
    
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred while planning your trip")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 