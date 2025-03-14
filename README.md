# Trip Planner GPT with Airbnb Integration

A custom OpenAI GPT that helps users plan trips with Airbnb accommodations, local attractions, and detailed itineraries.

## Project Overview

This project consists of two main components:

1. **Custom GPT Configuration**: Files needed to create a custom GPT in the OpenAI GPT Store
2. **API Backend**: A FastAPI application that serves as the backend for the GPT, providing Airbnb listings and travel information

## Features

- Search for Airbnb listings based on location, dates, and preferences
- Discover local attractions and activities
- Generate personalized trip itineraries
- Get budget-aware recommendations
- Interactive conversation with the GPT

## Project Structure

```
trip-planner-gpt/
├── gpt_config/           # Configuration files for the OpenAI GPT
│   ├── config.json       # GPT configuration
│   └── openapi.yaml      # OpenAPI specification for the API
├── api/                  # Backend API
│   ├── main.py           # FastAPI application
│   └── mock_data/        # Mock data for development
├── venv/                 # Python virtual environment
├── .env                  # Environment variables
└── requirements.txt      # Python dependencies
```

## Setup

### API Backend

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

4. Run the API backend:
   ```bash
   cd api
   uvicorn main:app --reload
   ```

5. The API will be available at `http://localhost:8000`

### Creating the Custom GPT

1. Go to [OpenAI GPT Builder](https://chat.openai.com/gpt-builder)
2. Click "Create a GPT"
3. Configure the GPT:
   - Name: "Trip Planner with Airbnb"
   - Description: "A specialized GPT that helps you plan trips using Airbnb listings and local attractions."
   - Instructions: Copy the instructions from `gpt_config/config.json`
   - Capabilities: Enable "Web Browsing" and "DALL-E Image Generation"
   - Actions: Upload the `gpt_config/openapi.yaml` file
   - Set the API authentication if needed

4. Test your GPT by asking it to plan a trip
5. Publish your GPT (optional)

## Using the GPT

Once your GPT is set up, you can interact with it by:

1. Asking it to plan a trip to a specific destination
2. Specifying your travel dates, budget, and preferences
3. Requesting Airbnb recommendations
4. Getting suggestions for attractions and activities
5. Creating a daily itinerary

Example prompts:
- "Plan a trip to Paris for June 15-22, 2024 with a budget of $3000"
- "Find me Airbnb listings in Tokyo for a family of 4"
- "What are the must-see attractions in Barcelona?"
- "Create an itinerary for my 5-day trip to New York"

## Notes

- The current implementation uses mock data for Airbnb listings and attractions
- In a production environment, you would need to deploy the API to a public server
- You may need to implement proper authentication for the API
- To use real Airbnb data, you would need to integrate with Airbnb's API or use a third-party service

## Resources

- [OpenAI GPT Documentation](https://platform.openai.com/docs/guides/gpt)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [OpenAPI Specification](https://swagger.io/specification/) 