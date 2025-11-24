# Statement of the Project – Digital Clone

## 1. Problem Statement

  In the modern digital world, people interact with various AI assistants for tasks like answering queries, performing calculations, telling jokes, providing time updates, or understanding user emotions.
However, most available assistants rely on heavy machine learning models, require high processing power, or are too complex for beginners to understand.

There is a need for a lightweight, modular, and easy-to-understand digital assistant that can respond intelligently to user inputs, detect emotions, and perform simple tasks without depending on large datasets or external APIs.
This project aims to solve this by building a Python-based Digital Clone with clean architecture and extendable skill modules.

## 2. Scope of the Project

The scope of the Digital Clone includes:

- A terminal-based assistant that interacts with users through text.

- A modular skill system where each feature (jokes, greetings, calculator, math, time, emotion, etc.) is written as a separate Python file.

- A central brain module that decides which skill should respond.

- A simple emotion engine that analyzes the tone of user input.

- Basic NLP utilities for message processing.

- A temporary memory system for storing short-term user information.

- The ability to easily add new skills in the future without modifying existing code.


-  Not included in the current scope:

 -  Voice recognition or speech output

 -  Internet-based features (weather, news, etc.)

 -  Machine learning-based emotional models

-  GUI interface


## 3. Target Users

- The target users for this project include:

- Students who want to learn modular Python programming and AI basics.

- Beginners in NLP who want a simple foundation to understand text processing.

- Developers looking for a lightweight assistant template to extend or customize.

- Educators who want to demonstrate AI logic without complex ML models.




## 4. High-Level Features

- The Digital Clone includes the following core features:

## Brain Module

 - Routes user input to the correct skill based on keywords

- Manages interaction flow


## Emotion Engine

- Detects user emotions like happy, sad, angry, neutral

- Enhances the personality of the assistant


## Modular Skills

- greeting_skill → Responds to greetings

- joke_skill → Tells simple jokes

- calculator_skill → Performs arithmetic

- math_skill → Solves math expressions

- time_skill → Gives current time

- emotion_skill → Emotion-based replies


## NLP Tools

- Cleans user text

- Extracts useful keywords


## Memory System

- Temporarily remembers user details during a session


 ## Plugin Architecture

- New skills can be added without modifying the main code
