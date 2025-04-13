import os
import subprocess
from .git_utils import get_git_diff
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-2.0-flash')

def generate_commit_message(staged_only: bool = True) -> str:
	git_changes = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True)
	return model.generate_content('''You are an expert at creating a github commit message 
		for a set of changes. Using semantic commit messages, here is a diff of changes we need a commit message for: ''' 
		+ str(get_git_diff(staged_only)))

if __name__ == '__main__':
	print(generate_commit_message().text)