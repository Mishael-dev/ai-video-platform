import os
from supabase import create_client, Client
from env import SUPABASE_KEY, SUPABASE_URL

url: str = SUPABASE_URL
key: str = SUPABASE_KEY

supabase: Client = create_client(url, key)
