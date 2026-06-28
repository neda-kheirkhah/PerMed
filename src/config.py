```python
"""
Configuration file for PerMed
"""

MODEL_NAME = "epfl-llm/meditron-7b"

MAX_NEW_TOKENS = 512

TEMPERATURE = 0.2

TOP_P = 0.9

DEVICE = "cuda"

DEFAULT_SYSTEM_PROMPT = (
    "You are PerMed, a medical AI assistant specialized in "
    "providing informative healthcare responses in Persian."
)
```

