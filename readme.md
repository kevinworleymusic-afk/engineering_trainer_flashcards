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
