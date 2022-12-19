from transformers import pipeline

generator = pipeline("text-generation", "gpt2")


class Utils:
    def __init__(self):
        self.generator = generator

    def generate_text(self, text: str, text_len: int):
        """Text generation using user input
        - **text**: input user text
        - **text_len**: count of output symbols
        """
        try:
            result_text = self.generator(text, max_length=text_len)
        except Exception as e:
            return {"Message": f"Parameters are not valid. {e}. I don't know what to say"}
        return {"generated_text": result_text[0]['generated_text']}

    @staticmethod
    def add(x, y):
        return x + y
