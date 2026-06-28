"""
Main entry point for PerMed.
"""

from model import load_model
from inference import generate_answer


def main():

    tokenizer, model = load_model()

    print("=" * 60)
    print("PerMed - Persian Medical AI")
    print("=" * 60)

    while True:

        question = input("\nMedical Question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        answer = generate_answer(
            model,
            tokenizer,
            question
        )

        print("\nAnswer:\n")
        print(answer)


if __name__ == "__main__":
    main()
