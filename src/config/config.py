# config.py

# Danh sách các model có thể sử dụng
MODELS = {
    "gpt-4-turbo": {
        "max_queries_per_subsection": 10,
        "rate_limit_per_minute": 60,
        "default_temperature": 0.7
    },
    "gemini-pro": {
        "max_queries_per_subsection": 8,
        "rate_limit_per_minute": 50,
        "default_temperature": 0.6
    }
}

# Các tùy chọn chung
GENERAL_SETTINGS = {
    "enable_logging": True,
    "default_language": "en",
    "max_concurrent_users": 100
}

# Cấu hình sub-sections
SUB_SECTIONS = {
    "story_writing": {
        "max_queries": 10,
        "require_auth": True
    },
    "poetry": {
        "max_queries": 5,
        "require_auth": False
    }
}

REPORT_STRUCTURE = """

"""