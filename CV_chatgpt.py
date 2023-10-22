from datetime import date

# Personal Information
name = "John Doe"
email = "johndoe@example.com"
phone = "+1 123-456-7890"
address = "1234 Example Street, City, State ZIP"

# Education
education = [
    {
        "degree": "Doctor of Philosophy (PhD)",
        "field": "Computer Science",
        "university": "ABC University",
        "location": "City, State",
        "year": "2019-2022"
    },
    {
        "degree": "Master of Science (MS)",
        "field": "Computer Science",
        "university": "XYZ University",
        "location": "City, State",
        "year": "2017-2019"
    },
    {
        "degree": "Bachelor of Science (BS)",
        "field": "Computer Science",
        "university": "DEF University",
        "location": "City, State",
        "year": "2013-2017"
    }
]

# Work Experience
experience = [
    {
        "position": "Postdoctoral Researcher",
        "employer": "ABC University",
        "location": "City, State",
        "duration": "2022-present",
        "description": "Conducting research on the application of machine learning to computer networks."
    },
    {
        "position": "Graduate Research Assistant",
        "employer": "ABC University",
        "location": "City, State",
        "duration": "2019-2022",
        "description": "Conducted research on the design and evaluation of network protocols using simulation tools."
    },
    {
        "position": "Teaching Assistant",
        "employer": "XYZ University",
        "location": "City, State",
        "duration": "2017-2019",
        "description": "Assisted professors in teaching undergraduate courses on computer networks and programming."
    }
]

# Skills
skills = ["Python", "Java", "C++", "Machine Learning", "Deep Learning", "Data Analysis"]

# Generate CV
today = date.today().strftime("%B %d, %Y")
cv = f"""
                        Curriculum Vitae
                        ===================
                        
Personal Information
-------------------
Name: {name}
Email: {email}
Phone: {phone}
Address: {address}

Education
---------
"""

for edu in education:
    cv += f"""Degree: {edu['degree']}
Field of Study: {edu['field']}
University: {edu['university']}
Location: {edu['location']}
Year: {edu['year']}

"""

cv += "Work Experience\n---------------\n"

for exp in experience:
    cv += f"""Position: {exp['position']}
Employer: {exp['employer']}
Location: {exp['location']}
Duration: {exp['duration']}
Description: {exp['description']}

"""

cv += "Skills\n------\n"

for skill in skills:
    cv += f"{skill}, "

# Print the generated CV
print(cv)
