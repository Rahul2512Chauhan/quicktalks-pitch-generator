# Prompt templates for 30s, 60s, resume bullets

def get_30s_pitch_prompt(title:str, description:str, keywords:str= "") -> str:
    return f"""
You are an expert communicator.
Create a confident, fluent 30-second pitch for the following project.

Project Title: {title}
Description: {description}
Keywords: {keywords}

Guidelines:
- Use a concise , engaging tone
- Avoid filler or repetition
- Emphasize your role , tech used , and outcome (if any)
- No bullet points

Output:
"""


def get_60s_pitch_prompt(title:str, description:str , keywords:str = "") -> str:
    return f"""
You are preparing for a technical interview.
Craft a clear and confident 1-minute explanation of the project below.

Project Title: {title}
Description: {description}
Keywords: {keywords}

Guidelines:
- Be conversational ,but detailed
- Exlplainn your role , contribution, tech stack , challenges and impact
- Avoid repetition
- End with a takeaway if possible

Output:
"""

def get_resume_bullets_prompts(title:str , description:str , keywords: str = "")->str:
    return f"""
You are a resume writing assistant.
Write 2–3 strong, quantified, action-oriented resume bullet points for this project.

Project Title: {title}
Description: {description}
Keywords: {keywords}

Guidelines:
- Use strong action verbs (e.g.,built , optimized ,automated)
- Include measurable results if possible (% ,time ,scale)
- Focus on clarity , impact and relevance
- Avoid using first person ("I" , "my")

Output:
-Bullet 1
-Bullet 2 
- (optional) Bullet 3
"""