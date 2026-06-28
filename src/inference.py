"""
Inference pipeline for PerMed.
"""

import torch

from prompts import SYSTEM_PROMPT, USER_TEMPLATE


def generate_answer(model, tokenizer, question):
    """
    Generate a Persian medical response.
    """

    prompt = SYSTEM_PROMPT + "\n\n" + USER_TEMPLATE.format(
        question=question
    )

    inputs = tokenizer(
        prompt,
        return_tensors="pt"
    )

    with torch.no_grad():

        outputs = model.generate(
            **inputs,
            max_new_tokens=512,
            temperature=0.2,
            top_p=0.9,
            do_sample=True,
        )

    answer = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return answer
