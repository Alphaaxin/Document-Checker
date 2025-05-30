import os
import json
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Any

@dataclass
class DocumentCheck:
    filename: str
    timestamp: str
    issues_found: int
    user_ip: str
    document_metadata: Dict[str, Any]

@dataclass
class Config:
    # Document checking settings
    skip_pages: int = 14  # Number of pages to skip at the beginning
    start_checking_from: str = 'abstract'  # 'page_number' or 'abstract'
    required_font: str = 'Times New Roman'
    required_font_size: int = 12
    required_line_spacing: float = 1.50
    
    # Admin settings
    admin_username: str = 'admin'
    admin_password: str = 'admin123'  # In production, use environment variables
    document_checks: List[Dict] = field(default_factory=list)
    
    @classmethod
    def load(cls, filename='config.json'):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                data = json.load(f)
                return cls(**data)
        return cls()
    
    def save(self, filename='config.json'):
        # Convert to dict and handle any non-serializable fields
        data = self.__dict__.copy()
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4, default=str)
    
    def log_document_check(self, filename: str, issues_found: int, user_ip: str, metadata: Dict[str, Any]):
        """Log a document check event"""
        check = {
            'filename': filename,
            'timestamp': datetime.now().isoformat(),
            'issues_found': issues_found,
            'user_ip': user_ip,
            'metadata': metadata
        }
        self.document_checks.append(check)
        # Keep only the last 100 checks
        if len(self.document_checks) > 100:
            self.document_checks = self.document_checks[-100:]
        self.save()

# Global config instance
config = Config.load()
