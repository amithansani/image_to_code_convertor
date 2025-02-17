from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os


class CodeFormatter:
    def __init__(self, model_name: str = "llama-3.3-70b-specdec"):
        load_dotenv()
        self.model = ChatGroq(model=model_name)



    def format_code(self, code: str) -> str:
        system = self._get_system_prompt()
        human = "{text}"
        prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
        chain = prompt | self.model
        response = chain.invoke({"text": code})
        return response.content

    def _get_system_prompt(self) -> str:
        return (
            """You are an expert Python programmer. The following code has been extracted from an image using OCR, """
            """which may have introduced minor errors such as missing colons, incorrect indentation, or misread characters."""
            """Your task:"""
            """1. Correct any minor syntax errors while maintaining the original logic."""
            """2. Also remove unwanted text, which is not part of the code."""
            """2. Ensure proper indentation and formatting."""
            """3. Return only the corrected Python code without any explanation."""
        )
