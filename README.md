# GenKavya — Sanskrit Padyam Generator

GenKavya is an AI-powered Sanskrit poetry generator that transforms English stories into Sanskrit verses following the Anuṣṭubh Śloka metre. It uses Google's Gemini API to generate verses and a rule-based validation component to check their metrical structure.

The project aims to make Sanskrit verse generation accessible through a simple web interface while exploring how large language models can be combined with traditional Sanskrit prosody rules.

## Project Status

**Phase 1 — Part 1: Single-padyam generation prototype**

The current version accepts an English story, generates Sanskrit verse candidates, validates their metrical structure, and displays the candidates that pass validation along with their meanings.

## Features

- **English story input:** Enter a short story of up to 500 characters.
- **AI-powered generation:** Uses the Gemini API to generate Sanskrit verse candidates from the input story.
- **Anuṣṭubh Śloka metre:** Guides generation toward the selected Sanskrit metrical form.
- **Metrical validation:** Checks the structure of generated verses, including the number of padas, syllable counts, and specified laghu–guru patterns.
- **Automatic retries:** Retries generation when none of the candidates pass validation, subject to a configured attempt limit.
- **Meaning display:** Shows the meaning supplied by the language model for each accepted verse.
- **Web interface:** Provides a Streamlit interface with a Sanskrit-inspired visual theme.

## How It Works

The application follows this workflow:

1. The user enters a story in English through the Streamlit interface.
2. The application constructs a prompt using the instructions defined in `prompt.py`.
3. The Gemini API generates verse candidates and returns the response in JSON format.
4. `generator.py` extracts the candidates and sends each verse to the validator.
5. `validator.py` checks the metrical structure of each candidate.
6. Candidates that pass validation are displayed with their Sanskrit text and meanings.
7. If no candidate passes validation, the application retries generation up to the configured limit and then reports the result.

## Project Structure

```text
GenKavya/
├── streamlit_app.py       # Streamlit web interface
├── generator.py           # Gemini API integration and generation workflow
├── prompt.py              # Prompt construction and generation instructions
├── validator.py           # Anuṣṭubh metre validation
├── requirements.txt       # Python dependencies
├── background.png         # Application background image
├── test_api.py            # API connectivity test
├── test_chanda.py         # Chanda library test
├── test_generation.py     # Verse generation test
├── test_generator.py      # Generator tests
├── test_patterns.py       # Metrical pattern tests
├── test_syllabification.py # Syllabification tests
├── test_validator.py      # Validator tests
├── .env                   # Local API configuration; not committed
├── .gitignore             # Files excluded from Git
└── .venv/                 # Local virtual environment; not committed
```

The `.env` and `.venv/` entries represent local development files and should not be uploaded to GitHub.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Web interface |
| Google Gemini API | Sanskrit verse generation |
| `google-genai` | Python SDK for Gemini |
| `python-dotenv` | Loading environment variables from `.env` |
| `chanda` | Metrical analysis used by the validator |
| Git and GitHub | Version control and source-code hosting |

## Requirements

Before running GenKavya, ensure you have:

- Python installed.
- Git installed.
- A Google AI Studio account and an API key for an eligible Gemini model.
- An internet connection for API requests.
- The project source files.

The Gemini API has model-dependent usage limits. Free-tier availability and quotas depend on the selected model and Google's current policies.

## Installation and Setup

The following instructions use Windows PowerShell.

### 1. Clone the repository

```powershell
git clone https://github.com/hemanth24408/GenKavya.git
cd GenKavya
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If activation is successful, PowerShell will normally display `(.venv)` at the beginning of the terminal prompt.

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a file named `.env` in the project's root directory.

Add your API key using the following format:

```dotenv
GEMINI_API_KEY=your_actual_api_key
```

If your local `generator.py` uses the `GEMINI_MODEL` environment variable, you can also specify a model supported by your API account:

```dotenv
GEMINI_MODEL=your_supported_model_name
```

Replace the example values with your actual configuration. Do not include quotation marks unless required by your configuration.

**Security:** Never commit `.env` to GitHub or share your API key publicly. The repository's `.gitignore` should exclude `.env` and `.venv/`.

### 5. Run the application

From the project root, with the virtual environment activated, execute:

```powershell
streamlit run streamlit_app.py
```

Streamlit will start a local web server and normally open the application in your browser. If it does not open automatically, follow the local URL printed in the terminal.

Enter a short English story and select **Generate Padyam** to try the application.

## Testing

The repository includes individual Python scripts for testing API connectivity, generation, syllabification, metrical patterns, and validation.

Run a test script from the project root using:

```powershell
python test_validator.py
```

Replace `test_validator.py` with the relevant test filename when testing another component.

API-dependent tests may require a valid Gemini API key, an internet connection, and available API quota. Check each test script before running it to understand its dependencies and whether it makes API requests.

## Current Scope and Limitations

The current prototype focuses on generating and validating individual Sanskrit verses from English stories.

- The initial target metre is Anuṣṭubh Śloka.
- The validator checks selected structural and metrical rules; passing validation does not guarantee perfect Sanskrit grammar, vocabulary, meaning, or classical poetic correctness.
- The language model may produce incorrect, awkward, or incomplete Sanskrit, so generated verses should be reviewed.
- The number of candidates and retry attempts is limited by the application configuration.
- The current interface accepts stories of up to 500 characters.
- API usage is subject to the selected Gemini model's quotas and rate limits.

## Future Scope

Planned extensions include:

- **Multiple-padyam generation:** Generate a sequence of verses for longer stories while preserving important events and their order.
- **Name integration:** Incorporate user-provided names into the generated poetry.
- **Additional metres:** Extend support beyond Anuṣṭubh Śloka.
- **Enhanced Sanskrit validation:** Improve grammatical, linguistic, and prosodic checks.
- **Additional input options:** Explore direct Sanskrit story input.

These are planned extensions and are not all implemented in the current prototype.

## Acknowledgements

GenKavya combines generative AI with traditional Sanskrit prosody concepts. It is a work in progress intended for learning, experimentation, and further development.

## License and Third-Party Dependencies

No project license has been specified yet. Before distributing the application, review the licensing terms of its dependencies, particularly the `chanda` package, and select an appropriate license for GenKavya.