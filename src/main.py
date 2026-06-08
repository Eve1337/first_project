from dotenv import load_dotenv
import os


load_dotenv(dotenv_path='.env')

def print_author():
    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")

print_author()
