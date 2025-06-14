import json
import os

MEMORY_FILE = "999_memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2, ensure_ascii=False)

def remember(message):
    memory = load_memory()
    memory.append(message)
    save_memory(memory)

def recall():
    return load_memory()