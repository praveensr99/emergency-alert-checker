# Getting Started Guide - AI Message Compliance Checker

## Quick Start (5 minutes)

### Prerequisites
- Python 3.8 or higher
- pip package manager
- (Optional) Anthropic API key for AI features

### Step 1: Setup Python Environment

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Configure API Keys (Optional)

```powershell
# Copy environment template
copy .env.example .env

# Edit .env and add your ANTHROPIC_API_KEY
# Get one from: https://console.anthropic.com/
```

### Step 3: Run the Application

```powershell
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## Using the Application

### Basic Workflow

1. **Input Draft Message**
   - Paste or type your emergency alert message
   - Real-time analysis begins immediately

2. **Review Safety Score**
   - See overall score (0-100) with safety level
   - Green (90+) = Ready to send
   - Yellow (75-89) = Minor issues
   - Red (<75) = Major issues

3. **Analyze Details**
   - Click tabs to explore each compliance area
   - Read specific recommendations

4. **Get AI Suggestions** (if API key configured)
   - Click "Generate Compliant Rewrite"
   - Compare original vs. AI suggestion
   - Copy and use improved version

5. **Send**
   - Click "READY TO SEND" when score ≥ 75

---

## Understanding the Scores

### Safety Score Components

```
Overall Score = 
  (FEMA Score × 0.30) +
  (WEA Score × 0.20) +
  (Readability Score × 0.25) +
  (Clarity Score × 0.25)
```

### Each Component

**FEMA (30%)** - Must include:
- ✓ Source: Who is sending alert
- ✓ Hazard: What is the threat
- ✓ Location: Where is affected
- ✓ Time: When does it happen
- ✓ Instruction: What to do

**WEA (20%)** - Character limits:
- ✓ ≤90 chars: Standard format
- ✓ 91-360 chars: Extended format
- ✗ >360 chars: Fails requirement

**Readability (25%)** - Reading level:
- ✓ Grade 6.0 or below: Pass
- ✗ Grade 6.0+: Reduce complexity

**Clarity (25%)** - Risk detection:
- ✓ Specific, unambiguous language
- ✗ Vague terms, panic language

---

## Example Messages

### ❌ LOW SCORE (28/100)

```
Take action immediately! Something bad might happen soon 
somewhere in the area. Be careful!
```

**Issues:**
- Missing FEMA elements (vague hazard, location)
- Panic language ("bad")
- Ambiguous instructions
- Reading level too high

---

### ✓ HIGH SCORE (92/100)

```
Flood Warning: This is a flood alert from County Emergency 
Management. A river flood is occurring now in the central 
county area. Move to high ground immediately. Go to 
shelters or higher floors.
```

**Strengths:**
- All FEMA elements present
- 90 characters (within WEA limit)
- 5th grade reading level
- Clear, specific actions

---

## Troubleshooting

### Issue: "ANTHROPIC_API_KEY not provided"
**Solution:** Either:
- Add API key to `.env` file, OR
- Enter API key in Settings sidebar (optional)

### Issue: "ModuleNotFoundError: textstat"
**Solution:** Reinstall dependencies:
```powershell
pip install -r requirements.txt --force-reinstall
```

### Issue: Port 8501 already in use
**Solution:** Use a different port:
```powershell
streamlit run app.py --server.port 8502
```

---

## File Structure Reference

```
📁 ai_msg_demo/
 ├── 📄 app.py                     # Main app (run this!)
 ├── 📄 requirements.txt           # Dependencies
 ├── 📄 README.md                  # Full documentation
 ├── 📄 QUICKSTART.md             # This file
 ├── 📄 .env.example              # Example config
 │
 ├── 📁 analysis/                 # Analysis modules
 │  ├── fema_analyzer.py
 │  ├── wea_analyzer.py
 │  ├── readability_analyzer.py
 │  └── confusion_detector.py
 │
 └── 📁 utils/                    # Utility modules
    ├── claude_api.py
    └── safety_scorer.py
```

---

## Key Functions

### Run Analysis on Message
```python
analyzers = initialize_analyzers()
message = "Your alert message here"
results = run_analysis(message, analyzers)
```

### Get Overall Score
```python
overall_score = analyzers["scorer"].calculate_overall_score(results)
print(overall_score['overall_score'])  # 0-100
print(overall_score['is_ready_to_send'])  # True/False
```

### Generate AI Rewrite
```python
claude = ClaudeAnalyzer()
suggestion = claude.suggest_rewrite(message, results)
print(suggestion['suggested_message'])
```

---

## Next Steps

1. ✅ Run the app with test messages
2. 📚 Explore each compliance area
3. 🤖 Try AI rewrites with API key
4. 📊 Review score breakdown details
5. 🔧 Understand priority fixes

---

## Support & Resources

- **Streamlit Docs**: https://docs.streamlit.io/
- **Anthropic Claude**: https://docs.anthropic.com/
- **Textstat**: https://pypi.org/project/textstat/

---

**Ready? Run `streamlit run app.py` now!** 🚀
