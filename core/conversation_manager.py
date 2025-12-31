"""
Conversation Manager to handle chat history
"""
import json
import os
from typing import List, Dict, Any

class ConversationManager:
    def __init__(self, history_file: str = "conversation_history.json"):
        self.history_file = history_file
        self.history: List[Dict[str, Any]] = []
        self._load_history()
        
    def _load_history(self):
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r') as f:
                    self.history = json.load(f)
            except json.JSONDecodeError:
                self.history = []
                
    def add_turn(self, request: str, response: Dict[str, Any]):
        """Add a conversation turn to history"""
        self.history.append({
            'request': request,
            'response': response
        })
        self._save_history()
        
    def _save_history(self):
        with open(self.history_file, 'w') as f:
            json.dump(self.history, f, indent=2)
            
    def get_history(self) -> List[Dict[str, Any]]:
        return self.history
        
    def clear_history(self):
        self.history = []
        if os.path.exists(self.history_file):
            os.remove(self.history_file)
