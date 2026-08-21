# Engineering Trainer Flashcards

A configurable Python-based knowledge-training application for practicing engineering concepts through randomized question sessions.

The project is designed as a reusable training framework rather than a single fixed quiz. Question content and application categories are stored separately from the Python program, allowing the training material to expand without requiring changes to the core application logic.

## Version 1

Version 1 implements the core question-session engine.

### Current Features

- Category selection from an external configuration file
- JSON-based question bank
- Category-based question filtering
- User-selected session length
- Randomized question selection
- Multiple-choice question presentation
- Case-insensitive answer input
- Answer-key evaluation
- Correct/incorrect feedback
- Session scoring
- Final accuracy calculation

### Current Workflow

```text
Load configuration
        ↓
Select training category
        ↓
Load question bank
        ↓
Filter questions by category
        ↓
Select session length
        ↓
Randomly generate session
        ↓
Present questions and choices
        ↓
Evaluate answers
        ↓
Track score
        ↓
Display final accuracy
```

## Version 1.1

Version 1.1 adds question-type selection and filtering to the core training engine.

### New in Version 1.1

- Automatically identifies the question types available within the selected channel
- Presents available question types for user selection
- Filters the question bank by both selected channel and selected question type
- Keeps question types data-driven through the JSON question bank rather than hard-coding them into the Python application
- Added code documentation to clarify the application's data flow and Python implementation

### Updated Workflow

```text
Select channel
      ↓
Filter questions by channel
      ↓
Identify available question types
      ↓
Select question type
      ↓
Filter questions by type
      ↓
Select session size
      ↓
Randomly generate session
      ↓
Evaluate answers
      ↓
Calculate score and accuracy
```

This establishes the foundation for future controlled question sessions in which different engineering question formats can be intentionally combined or weighted.

## Development Roadmap

The following is an initial development plan for the application. Version boundaries are provisional and may change as the system develops.

| Version | Planned Development |
|---|---|
| **1.0** | Basic question/session engine, category selection, randomized sessions, answer evaluation, and scoring |
| **1.1** | Question-type discovery, selection, and filtering |
| **1.2** | Multiple question formats beyond the initial multiple-choice implementation |
| **1.3** | Controlled session composition and configurable mixes of question types |
| **1.4** | Per-question/card performance states and learning progress data |
| **1.5** | Review and repetition logic for previously missed or developing material |
| **1.6** | Initial graphical user interface and performance/session controls |
| **1.7** | Weak-topic targeting and more intelligent session selection |
| **2.0** | Adaptive training engine combining question selection, performance history, review logic, and user progress |

The roadmap is intentionally incremental. The goal is to establish and test the underlying training engine before building the full user interface and adaptive system.

## Project Structure

```text
engineering_trainer_flashcards/
├── engineering_trainer.py
├── config.json
├── questions.json
└── readme.md
```

### `engineering_trainer.py`

Contains the application logic, including:

- Configuration loading
- Question-bank loading
- Category selection
- Question filtering
- Random session generation
- Answer evaluation
- Score tracking

### `config.json`

Contains application-level configuration such as:

- Application name
- Available training categories

Keeping these values outside the Python program allows the application structure to be modified without changing the core code.

### `questions.json`

Contains the training question bank and answer keys.

Questions are stored as structured data so that new questions and categories can be added independently of the application logic.

## Initial Training Categories

The application is being developed to support engineering knowledge across areas including:

- Electrical Engineering
- Psychoacoustics
- Acoustics
- Electroacoustics
- DSP
- Automotive Audio

The question bank will expand as additional engineering study material is developed.

## Design Goal

The long-term goal is to develop the application into a flexible engineering training system capable of supporting different question formats, controlled question distributions, performance tracking, and increasingly adaptive practice sessions.

Version 1 intentionally focuses on establishing the underlying question-session architecture before adding those more advanced capabilities.

## Development Approach

This project is being developed incrementally through working software milestones.

Each feature is implemented and tested locally before being incorporated into the repository. The project is also being used as a practical exercise in Python programming, software structure, JSON data handling, Git, and GitHub-based development.

## Status

**Version 1.1 — Core question-session engine with question-type selection implemented**

Current version is a functional command-line application with an initial question bank.

Future development will expand the question model, training formats, session selection logic, performance tracking, and user interface.
