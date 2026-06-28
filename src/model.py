AutoTokenizer.from_pretrained(...)
AutoModelForCausalLM.from_pretrained(...)


from transformers import AutoModelForCausalLM, AutoTokenizer

from config import MODEL_NAME


def load_model(token=None):
    """
    Load the Meditron model and tokenizer.
    """

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME,
        token=token
    )

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        token=token
    )

    return tokenizer, model
```
