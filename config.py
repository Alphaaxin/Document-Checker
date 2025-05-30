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
        default_config = cls()
        try:
            if os.path.exists(filename) and os.access(filename, os.R_OK):
                with open(filename, 'r') as f:
                    data = json.load(f)
                    return cls(**data)
        except Exception as e:
            print(f"Warning: Could not load config file: {e}")
        return default_config
    
    def save(self, filename='config.json'):
        try:
            # Check if we can write to the directory
            dir_path = os.path.dirname(os.path.abspath(filename))
            if not os.access(dir_path, os.W_OK):
                print("Warning: Running in read-only mode, config not saved")
                return
                
            # Convert to dict and handle any non-serializable fields
            data = self.__dict__.copy()
            temp_file = f"{filename}.tmp"
            
            # Write to temporary file first
            with open(temp_file, 'w') as f:
                json.dump(data, f, indent=4, default=str)
                
            # Rename temp file to actual file (atomic operation)
            if os.path.exists(filename):
                os.replace(temp_file, filename)
            else:
                os.rename(temp_file, filename)
                
        except Exception as e:
            print(f"Warning: Could not save config: {e}")
            # Clean up temp file if it exists
            if 'temp_file' in locals() and os.path.exists(temp_file):
                try:
                    os.unlink(temp_file)
                except:
                    pass
    
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
