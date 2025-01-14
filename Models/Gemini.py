import os
import google.generativeai as genai


class Gemini:
    def __init__(self):
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
        self.model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-exp", generation_config=generation_config
        )

    @classmethod
    def start_chat(self):
        chat_session = self.model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [
                        "sera informado a voce a coordenada jogada em um jogo da velha e quero que me retorne somente a coordenada da sua jogada",
                    ],
                },
                {
                    "role": "model",
                    "parts": [
                        "Com certeza! Pode me informar a coordenada da sua jogada e eu retornarei a minha. 😉\n",
                    ],
                },
            ]
        )
        return chat_session

    @classmethod
    def send_message(self, chat_session, message):
        response = chat_session.send_message(message)
        return response

    def get_response(self, message):
        chat_session = self.start_chat()
        response = self.send_message(chat_session, message)
        return response