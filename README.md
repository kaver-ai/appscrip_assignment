# Trade Opportunities API

## Overview
This project is a FastAPI-based service that analyzes market data and provides trade opportunity insights for different sectors in India.

## Features
- FastAPI backend
- REST API endpoint: /analyze/{sector}
- AI-based analysis using Gemini API
- Basic authentication
- Rate limiting
- Markdown response output

## How to Run
1. Install dependencies:
   pip install fastapi uvicorn requests python-dotenv google-generativeai

2. Run server:
   python -m uvicorn main:app --reload

3. Open:
   http://127.0.0.1:8000/docs

## Example API
GET /analyze/technology

## Tech Stack
- Python
- FastAPI
- Gemini API