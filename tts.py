from talon import Module, Context, actions
import json, requests

mod = Module()
ctx = Context()

ctx.matches = """
os: mac
"""

def speak(text: str):
  url = "http://localhost:5050/speak"
  payload = {"message": text }
  response = requests.post(url, json=payload)
  print(f"Response Body: {response.text}")

@mod.action_class
class Actions:
  def tts_speak(text: str) -> None:
    """Speak supplied text"""
    speak(text)



