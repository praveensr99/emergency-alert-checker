# AI Message Compliance & Safety Checker - MVP

A pre-send validation tool to prevent emergency communication failures by ensuring messages meet complex federal regulations and accessibility standards.

## 🚨 Critical Incident Prevention

**Inspired by Hawaii False Missile Alert (January 13, 2018)**

The 2018 Hawaii emergency management failure exposed critical gaps:
- ❌ No confirmation mechanism
- ❌ Inadequate message verification
- ❌ Ambiguous alert messaging
- ❌ No clarity verification before sending

**Our Solution**: Multi-layer verification system that:
- ✅ Validates FEMA 5-element compliance (all required)
- ✅ Enforces WEA character limits (90/360 chars max)
- ✅ Ensures ADA readability (Grade 6.0 or below)
- ✅ Detects ambiguous/panic-inducing language
- ✅ Requires explicit sender confirmation
- ✅ Creates complete audit trail of all messages

**See [COMPLIANCE_COVERAGE.md](COMPLIANCE_COVERAGE.md) for full Hawaii false alert prevention details.**

---

## Features

### 🔍 Core Analysis Engine

1. **FEMA 5-Element Audit**: Automatically detects:
   - Source (who is issuing the alert)
   - Hazard (what the danger is)
   - Location (where it is)
   - Time (when it happens/expires)
   - Instruction (what to do)

2. **WEA Character Counter**: Real-time monitoring against:
   - 90-character limit (standard WEA)
   - 360-character limit (extended WEA)

3. **ADA Readability Scorer**: Ensures accessibility with:
   - 6th-grade reading level target
   - Multiple readability metrics
   - Plain-language recommendations

4. **Confusion Risk Detector**: Flags problematic language:
   - Ambiguous directives
   - Vague quantities/locations
   - Panic-inducing vocabulary
   - Lack of specificity

### 📊 Real-Time User Interface

- **Live Safety Score**: Dynamic 0-100 score that updates as you type
- **Error Highlighting**: Visual indicators for missing elements
- **AI-Suggested Rewrite**: Claude-powered compliant message alternatives
- **Priority Fixes**: Ranked list of issues to address
- **Detailed Breakdown**: Component-level analysis with recommendations

## Tech Stack

- **Framework**: Streamlit (real-time interactive UI)
- **AI**: Claude API (nuanced linguistic analysis)
- **Readability**: Python textstat library
- **Language**: Python 3.8+

## Installation

1. Clone the repository:
```bash
git clone <repository>
cd ai_msg_demo
```

2. Create virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
# or: source .venv/bin/activate  # On macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure API key (optional, for AI features):
```bash
# Set environment variable or add in the app Settings:
export ANTHROPIC_API_KEY="your-key-here"
# Or on Windows:
set ANTHROPIC_API_KEY=your-key-here
```

### Dependency Installation

If you encounter `ModuleNotFoundError` for `anthropic` or other packages:
```bash
# Ensure all dependencies are installed
pip install -r requirements.txt

# Or install individually:
pip install anthropic==0.7.6
pip install streamlit==1.28.1
pip install textstat==0.7.3
pip install python-dotenv==1.0.0
```

## Usage

### Running the Application

1. Activate your virtual environment:
```bash
.venv\Scripts\activate  # On Windows
# or: source .venv/bin/activate  # On macOS/Linux
```

2. Run the Streamlit application:
```bash
streamlit run app.py
```

3. Open your browser to `http://localhost:8501`

### Using the Tool

1. Enter your emergency message draft in the text area
2. View real-time analysis across:
   - **FEMA Elements**: Source, Hazard, Location, Time, Instruction
   - **WEA Limits**: 90-char and 360-char compliance
   - **Readability**: 6th-grade level accessibility
   - **Clarity**: Risk detection for ambiguous language
3. Check your **Safety Score** (target: 75+)
4. (Optional) Enter your Anthropic API key in Settings for AI-powered rewrites
5. Use AI suggestions or manually edit
6. Send when score reaches minimum threshold (75/100)

## Project Structure

```
ai_msg_demo/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── .env.example               # Environment template
├── .gitignore
├── README.md
├── analysis/                  # Core analysis modules
│   ├── __init__.py
│   ├── fema_analyzer.py      # FEMA 5-element audit
│   ├── wea_analyzer.py       # WEA character limits
│   ├── readability_analyzer.py # ADA readability
│   └── confusion_detector.py   # Confusion risk detection
└── utils/                     # Utility modules
    ├── __init__.py
    ├── claude_api.py          # Claude API integration
    └── safety_scorer.py       # Score aggregation
```

## Safety Score Components

The overall safety score (0-100) is calculated as:

- **FEMA Compliance (30%)**: Percentage of 5 required elements present
- **WEA Compliance (20%)**: Character count against 90/360 limits
- **Readability (25%)**: ADA accessibility scoring
- **Clarity (25%)**: Confusion risk detection

**Minimum threshold to send: 75/100**

## Compliance Standards

### FEMA Requirements
- All 5 elements (Source, Hazard, Location, Time, Instruction) required
- Clear, specific language
- Target audience awareness

### WEA Limits
- Standard: 90 characters
- Extended: 360 characters

### ADA Standards
- 6th-grade reading level
- Active voice preferred
- Clear formatting

### FCC Mandates
- No ambiguous language
- Specific action items
- Accessible to diverse audiences

## Future Enhancements

- Multilingual support (14+ languages)
- Integration with Hyper-Reach portal
- User authentication & audit logging
- Template library for quick alerts
- Historical analytics dashboard
- Team collaboration features
- Automated scheduled alerts

## License

[Add License Information]

## Support

For issues, questions, or suggestions, please contact the development team.
