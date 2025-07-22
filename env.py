import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
HEYGEN_API_KEY=os.getenv("HEYGEN_API_KEY")

