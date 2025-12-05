Student Toolkit

Student Toolkit is an all-in-one desktop application built in Python using CustomTkinter.
I made this project to learn Python, understand GUI development, and create something genuinely useful.
It is designed to solve common problems students face daily. Everything is available in one place, simple, fast, and clean.

Feature List
Attendance Calculator

Helps you calculate how many classes you need to attend or how many you can skip. Useful for maintaining attendance percentage without doing manual calculations.

GPA Calculator

Converts your marks into letter grades and calculates your GPA in a clear and straightforward way.

GPA Plus Plus

An advanced module that performs SGPA to CGPA conversion, grade to GPA conversion, and marks to GPA conversion. Built for students who need more detailed academic calculations.

LLM

A one stop assistant that answers any doubt you have. Works like a personal study bot integrated into the toolkit.

QR Resource Hub

Provides access to books, notes, slides, previous year questions, and other study material. Everything is organized in one place and accessible through quick QR scans.

Quiz

Generates MCQs from any topic or niche you choose. It uses a locally running model so it works even without an internet connection. Helps with revision and self testing.

To Do List

A simple task manager that stores your tasks on your PC. Lets you add tasks, update them, and keep track of your work easily.

Brain Teaser

A small collection of practice tools that currently includes Wordle and DSA question practice. This section can grow with more games or challenges over time.

Requirements

This project uses the following Python libraries and modules

customtkinter
qrcode
Pillow
google genai
ollama
pandas

Python version
Python 3 and above is used for this project.


Technical Overview

Student Toolkit is structured as a modular CustomTkinter application. Each feature is implemented in its own Python file, and the main application acts as the central launcher. This keeps the project organized and allows each tool to be updated or expanded independently.

Application Structure

The main file initializes the root window, sets the theme, loads the title screen, and displays the feature buttons.
Each feature is opened using a separate window created with the Toplevel widget.
Shared UI styles such as fonts, colors, and button properties are reused across the project for consistency.

User Interface System

The entire interface uses CustomTkinter for a cleaner and modern look.
Frames and buttons are arranged using a grid based layout.
Each tool has its own UI function and runs independently while sharing the same root window context.
The consistent design allows users to switch between tools easily without confusion.

Attendance Calculator Logic

The attendance tool takes the total classes and attended classes as input.
It calculates how many classes the user needs to attend or how many can be skipped based on standard attendance formulas.
All results are updated live on the UI without restarting the program.

GPA and GPA Plus Plus System

The GPA calculator converts marks into letter grades and calculates GPA according to preset grade boundaries.
GPA Plus Plus expands this by providing SGPA to CGPA conversion, grade to GPA conversion, and marks to GPA conversion.
These calculations are handled through clean functions and pandas is used wherever tabular processing is required.

LLM Integration

The DOOM BOT is powered by a local deepseek model running through Ollama.
The model uses a custom system prompt that defines the assistant as DR DOOMs personal helper.
The interface sends user prompts to the local model and displays the generated response inside the application window.
The model runs entirely offline, making the bot fast and consistent.

QR Resource Hub

This module uses the qrcode and Pillow libraries to generate and display QR codes.
Each QR code links to specific study resources such as notes, slides, books, or previous year questions.
The QR codes are regenerated dynamically based on user selection.

Quiz Generator

The quiz tool uses a locally running LLM model to generate MCQs from any topic the user provides.
The model output is parsed, cleaned, and displayed as a question with multiple options.
This allows rapid creation of practice tests without requiring an internet connection.

Brain Teaser

This section currently contains two components
Wordle
A simplified word guessing game with a fixed word list.
DSA Questions
A set of coding and data structure questions loaded from structured data or generated locally.
This module is designed to grow over time with more challenges.

Data Handling

Pandas is used for reading CSV files, managing datasets, and performing conversions.
Local storage is used for saving To Do tasks so that the user can close and reopen the toolkit without losing progress.