# FoodRx: Agentic AI Recipe Generator (MVP)

## Overview
FoodRx is a **simple recipe generator** that retrieves recipes based on dietary restrictions. Users can input their dietary needs (e.g., "vegan", "gluten-free"), and the system will return matching recipes from a small dataset. This is the **Minimum Viable Product (MVP)**, with room for expansion into an AI-powered system.

## Features
- Retrieve recipes based on dietary restrictions  
- Uses a **local JSON dataset** for fast retrieval  
- REST API powered by **FastAPI**  
- **Streamlit UI** for user interaction  
- Lightweight & easily expandable  

## Tech Stack
- **Python 3.x**
- **FastAPI** (Backend API)
- **JSON / SQLite** (Recipe Storage)
- **Uvicorn** (FastAPI Server)
- **Streamlit** (UI)


## Installation & Setup

### Clone the Repository
```sh
git clone https://github.com/yourusername/agentic-ai-recipe-generator.git
cd FoodRx
```


### Install Dependencies
```sh
pip install -r requirements.txt
```

### Run the API Server
```sh
uvicorn backend.app:app --reload
```

**Test it in your browser:**  
`http://127.0.0.1:8000/recipes/?diet=vegan`

### Run the Streamlit UI
```sh
streamlit run frontend/ui.py
```


## API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| `GET` | `/recipes/` | Get all recipes |
| `GET` | `/recipes/?diet=<diet>` | Filter recipes by dietary restriction |

Example:
```sh
curl http://127.0.0.1:8000/recipes/?diet=gluten-free
```


## Future Enhancements
- **Expand recipe database (SQLite, PostgreSQL)**  
- **Improve search with vector embeddings (FAISS, Pinecone)**  
- **Use AI (GPT-4) for ingredient substitutions**  
- **User preferences & feedback tracking**  


## Contributing
Pull requests are welcome! Feel free to **fork** the repo and submit improvements.


## License
MIT License

