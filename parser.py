import fitz  # PyMuPDF
import openai

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

# Function to create ChatGPT prompt
def create_chatgpt_prompt(resume_text):
    prompt = f"""
    You are a Resume Parsing Assistant. Your job is to take a resume in plain text format and convert it into a structured JSON format.

    Input Resume:
    {resume_text}

    Output JSON:
    {{
      "name": "",
      "contact_information": {{
        "email": "",
        "phone": "",
        "location": "",
        "linkedin": "",
        "medium": "",
        "huggingface": ""
      }},
      "education": [],
      "professional_experience": [],
      "projects": [],
      "certifications": [],
      "skills": []
    }}
    """
    return prompt

# Function to parse resume using GPT
def parse_resume_with_gpt(prompt):
    openai.api_key = "your_api_key"

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=1500
    )

    return response.choices[0].text

# Path to the PDF file
pdf_path = "path/CV.pdf"

# Extract text from the PDF
resume_text = extract_text_from_pdf(pdf_path)

# Generate the ChatGPT prompt
prompt = create_chatgpt_prompt(resume_text)

# Parse the resume using GPT
resume_json = parse_resume_with_gpt(prompt)
print(resume_json)
