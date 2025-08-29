import json
import streamlit as st

with open("data.json", "r") as f:
  data = json.load(f)["questions"]

def get_predefined_answer(user_input):
  user_input_lower = user_input.lower()
  for item in data:
    if item["question"].lower() in user_input_lower:
      return item["answer"]
  return None

st.title("Thoughtful AI Customer Support Agent")

user_input = st.text_input("Ask me a question about Thoughtful AI:")

if user_input:
  answer = get_predefined_answer(user_input)

  if answer:
    st.success(answer)
  else:
    st.info("I couldn't find an exact answer to that, but Thoughtful AI is constantly improving its automation solutions for healthcare.")
    