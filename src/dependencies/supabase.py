

from multiprocessing.connection import Client
import os

from storage3 import create_client


supabase_global: Client = create_client(
    os.getenv("NEXT_PUBLIC_URL"), os.getenv("NEXT_PUBLIC_KEY"))
