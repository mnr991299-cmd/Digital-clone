  # Digital Clone – AI Based Personal Assistant

A modular Python-based digital assistant that interacts with users using predefined skills such as greetings, jokes, calculations, emotion detection, time responses, and more. The project showcases modular design, NLP basics, and clean Python architecture.



## 1. Project Title

Digital Clone – Modular Python AI Assistant


## 2. Overview of the Project

The Digital Clone is a simple yet flexible personal assistant designed to understand user messages and reply intelligently. It uses individual “skills” (modules) to handle different types of queries.
The project is created to demonstrate clean architecture, modularity, and practical implementation of Python concepts for beginners.


## 3. Features

- Core Features
- Greeting responses
- Joke generator
- Basic calculator
- Math problem solver
- Current time responses
- Emotion analysis (happy, sad, angry, neutral)
- NLP tools for text cleaning and keyword extraction
- In-memory session data storage
- System Highlights
- Skill-based modular design
- Easy to extend (add new skills anytime)
- Lightweight and fast
- Terminal-based interaction


## 4. Technologies / Tools Used

- Python 3.8+
- VS Code
- Git & GitHub
- OOP principles
- Basic NLP techniques



## 5. Steps to Install & Run the Project

- Clone the Repository
- git clone <your-repository-link>
- Open in VS Code
- File → Open Folder → Select "Digital-clone"
- Run the Project
- python main.py
- Start Chatting
- Try:
        “hi”
        “tell me a joke”
        “time now”
        “add 5 and 6”
        “i am sad”
        “solve 5*9”


## 6. Instructions for Testing

-  Open terminal and run the project
- Test each skill with sample input
- Check if correct skill gets activated
- Validate emotion detection with different tones
- Test invalid input handling
-  Capture screenshots of terminal output


## 7. Screenshots (Recommended)
Terminal conversation
<img width="1042" height="266" alt="conversation chat skill" src="https://github.com/user-attachments/assets/3ec296c5-4711-4147-940c-26ffb698c027" />



## 8. Project Statement Summary (statement.md)

- Problem Statement
- Users need an interactive assistant that can respond to basic queries, detect emotions, and perform tasks without heavy AI models.
## Scope
  Text-based interaction
  Modular skill execution
  Basic emotion detection
  Skill expansion support
## Target Users
  Students
  Beginners learning NLP
  Developers practicing modular Python
  High-Level Features
  Multi-skill support
  Emotion engin
  Simple NLP utilities
  Memory system

## 9. System Architecture

main.py → Brain → Skills → Response
                 ↓
         Emotion Engine
                 ↓
               Memory




## 10. Design Diagrams (Descriptions)

Use Case
User interacts → Digital Clone → Responds using skill modules.
Workflow
 1. User inputs message
 2. Brain analyses message
 3. Selects matching skill
 4. Executes skill
 5. Runs emotion engine
 6. Returns final response

Sequence
     User → main.py → brain.py → skill → response
Class Diagram
    Classes:
           Brain
           Each Skill class
           Memory
           EmotionEngine
 

## 11. Design Decisions & Rationale

- Modular design for scalability
- Central brain routing simplifies logic
- Keyword-based emotion detection avoids ML dependency
- Simple NLP tools improve accuracy


## 12. Implementation Details
    
- Skills contain two methods:
- can_handle(message)
- handle(message)
- Plugins register all skills
- Brain iterates through skills to find the best match
- Memory stores temporary session data
- Emotion engine uses rule-based classification

## 13. Screenshots / Results

<img width="877" height="225" alt="calculator and math skill" src="https://github.com/user-attachments/assets/c8ba731e-6743-4222-ba03-ddc7d73489bd" />


## 14. Testing Approach
- Functional testing for each skill
- Input variety testing
- Negative/invalid input testing
- Emotion detection testing
- Flow validation through brain module

## 15. Challenges Faced
- Designing clean modular architecture
- Routing text to correct skil
- Ensuring readable code structure
- Creating emotion classification logic

## 16. Learnings & Key Takeaways
- Practical understanding of NLP
- Modular architecture implementation
- Efficient Python OOP usage
- Debugging and testing workflows

## 17. Future Enhancements
- Voice input/output
- ML-based emotional AI
- GUI interface
- Database-based long-term memory
- Internet-powered skills (weather, news, etc.)

## 18. References
- Python Official Docs
- VS Code Documentation
- GitHub Guides


