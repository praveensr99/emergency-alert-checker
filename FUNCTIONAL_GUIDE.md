# 🚨 Emergency Alert Safety Checker - Functional Guide

**Version:** 1.0  
**Date:** February 17, 2026  
**Application:** AI-Powered Emergency Message Compliance & Safety Checker

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Application Overview](#application-overview)
3. [Core Features](#core-features)
4. [Safety Score System](#safety-score-system)
5. [How to Use](#how-to-use)
6. [Compliance Standards](#compliance-standards)
7. [Analysis Components](#analysis-components)
8. [Message Delivery](#message-delivery)
9. [Troubleshooting](#troubleshooting)
10. [Technical Architecture](#technical-architecture)

---

## Executive Summary

The **Emergency Alert Safety Checker** is a comprehensive web application that validates emergency alert messages for compliance with federal regulations (FEMA, WEA, FCC) and best practices. The system analyzes messages across multiple dimensions and provides actionable feedback to prevent false alerts, ensure clarity, and guarantee compliance before sending.

This application prevents incidents like the 2018 Hawaii false missile alert by implementing a 4-layer verification system that checks all critical communication elements.

---

## Application Overview

### Purpose
- **Validate** emergency messages against federal compliance standards
- **Prevent** costly false alerts and miscommunication
- **Ensure** messages meet readability and clarity requirements
- **Guide** operators toward compliant, effective messages

### Target Users
- Emergency Management Directors
- Public Information Officers (PIOs)
- Emergency Dispatchers
- City/County Emergency Services
- State Emergency Management Agencies

### Key Benefits
✅ Real-time compliance feedback  
✅ Prevents false alerts before sending  
✅ AI-powered message improvement suggestions  
✅ Multi-layer verification (4-element system)  
✅ Audit trail and delivery logging  
✅ SMS & Email delivery support  

---

## Core Features

### 1. Real-Time Message Analysis
When you enter an emergency message, the system automatically analyzes it across 4 dimensions:

| Component | What It Checks | Weight |
|-----------|---------------|--------|
| **FEMA Elements** | Required elements: Source, Hazard, Location, Time, Instruction | 30% |
| **WEA Compliance** | Character limits (90/360 chars) | 20% |
| **Readability** | Grade level (≤6th grade for ADA) | 25% |
| **Clarity/Confusion** | Ambiguous or panic language | 25% |

### 2. Safety Score Display
Your message receives a **single overall score** (0-100) that determines its status:

```
Overall Score = 
  (FEMA Score × 0.30) +
  (WEA Score × 0.20) +
  (Readability Score × 0.25) +
  (Confusion Score × 0.25)
```

### 3. Compliance Status Indicators

| Score Range | Color | Status | Action |
|-------------|-------|--------|--------|
| **80-100** | 🟢 Green | **Compliant** | Ready to Send |
| **60-79** | 🟡 Yellow | **Needs Improvement** | Review Recommended |
| **0-59** | 🔴 Red | **Non-Compliant** | Must Revise |

### 4. AI-Powered Suggestions
Get AI-generated rewrites that improve compliance while maintaining your message's intent.

### 5. Message Delivery System
- Configure sender name
- Add multiple SMS recipients (phone numbers)
- Add multiple email recipients
- Track delivery status with message IDs
- View delivery history

### 6. Delivery Audit Log
Every message sent is logged with:
- Message ID
- Timestamp
- Sender information
- Recipients (phone/email)
- Delivery status
- Message content

---

## Safety Score System

### Understanding Your Score

#### 🟢 GREEN (80-100): COMPLIANT - READY TO SEND
- **What it means:** Your message meets all compliance requirements
- **Action:** Direct send capability enabled
- **Example:** "City of Honolulu: Tsunami warning for Waikiki until 6 PM. Move to higher ground immediately."
- **Why it passes:**
  - ✅ All 5 FEMA elements present
  - ✅ Within WEA character limits
  - ✅ Grade 5-6 readability level
  - ✅ Clear, direct language

#### 🟡 YELLOW (60-79): NEEDS IMPROVEMENT - REVIEW RECOMMENDED
- **What it means:** Message has some compliance issues but can work
- **Action:** Review recommended changes before sending
- **Example:** "Emergency alert. Flooding is occurring in multiple areas of the city. Please take precautions and avoid affected zones."
- **Common issues:**
  - Missing one FEMA element
  - Slightly above character limit (truncatable)
  - Grade 7-8 readability level
  - Some vague language

#### 🔴 RED (0-59): NON-COMPLIANT - MUST REVISE
- **What it means:** Message has critical compliance issues
- **Action:** Must revise before sending
- **Example:** "Critical alert notification. Potentially catastrophic situation developing. Please take immediate action. More details coming soon."
- **Typical problems:**
  - Missing 2+ FEMA elements
  - Far exceeds character limit
  - Grade 9+ readability level
  - Ambiguous or panic language

---

## How to Use

### Step 1: Launch the Application
```
streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser

### Step 2: Enter Your Draft Message
1. Click in the "Emergency Message" text area
2. Type or paste your alert message
3. The system automatically analyzes as you type

**Example message format:**
```
[Source]: City of Honolulu Emergency Services
[Hazard]: Tsunami warning
[Location]: Waikiki Beach area
[Time]: Until 6:00 PM today
[Instruction]: Move to higher ground immediately
```

### Step 3: Review Compliance Analysis
The system displays:

**📊 Overall Score Card** (top, color-coded)
- Your score and status
- Priority fixes needed
- Safety level breakdown

**📋 Detailed Breakdown** (tabs)
- FEMA Elements: Which elements present/missing
- WEA Limits: Character count and compliance status
- Readability: Grade level and metrics
- Clarity Analysis: Confusion risk and identified issues

### Step 4: Review Recommendations
The system suggests:
1. **Priority Fixes** (ordered by impact)
2. **Score Breakdown** (component-by-component)
3. **AI Enhancement Suggestions** (optional)

### Step 5A: Improve Using AI Suggestions (Optional)
1. Click **"✨ Generate Compliant Rewrite"**
2. Review the suggested version
3. Click **"📋 Copy Suggested Message"** to use it
4. Paste into the message box to re-analyze

### Step 5B: Manual Improvement
Edit your message directly to:
- Add missing FEMA elements
- Reduce word complexity
- Remove ambiguous phrases
- Reduce character count if needed

### Step 6: Configure Delivery (When Ready to Send)

**When your score reaches 80+:**

1. **Sender Configuration:**
   - Enter your name/agency
   - Select delivery method (SMS, Email, or Both)

2. **Add Recipients:**
   - **For SMS:** Enter phone numbers (one per line)
   - **For Email:** Enter email addresses (one per line)

3. **Send Message:**
   - Click **"✓ READY TO SEND"** button
   - System confirms delivery
   - Message ID and timestamp provided

### Step 7: View Delivery History
- Expandable "Delivery Confirmation Details" section
- Shows message ID, sender, method, timestamp
- Displays delivery status per recipient

### Step 8: Start New Message
- Click **"🔄 Clear Form"** to reset everything
- Refocus on message input box
- Ready for next alert

---

## Compliance Standards

### FEMA 5-Element Requirement
Every emergency message must contain:

1. **SOURCE:** Who is sending the alert?
   - ✅ "City of Honolulu Emergency Services"
   - ❌ "Someone" (too vague)

2. **HAZARD:** What is the emergency?
   - ✅ "Tsunami warning"
   - ❌ "Something bad is happening" (vague)

3. **LOCATION:** Where is it happening?
   - ✅ "Waikiki Beach and surrounding areas"
   - ❌ "In the city" (too broad)

4. **TIME:** How long? When does it expire?
   - ✅ "Until 6:00 PM today"
   - ❌ "Soon" (unclear)

5. **INSTRUCTION:** What should people do?
   - ✅ "Move to higher ground immediately"
   - ❌ "Be careful" (not actionable)

### WEA Character Limits
- **Short Format:** ≤ 90 characters (basic alert)
- **Long Format:** ≤ 360 characters (full alert)
- Both should be clear and direct

### Readability Standard (ADA Compliance)
- **Target:** 6th grade reading level
- **Measurement:** 5 algorithms for accuracy
- **Avoids:** Complex words, long sentences, jargon

### Clarity Requirements
- No contradictory statements
- No ambiguous instructions
- No unnecessary panic language
- Clear, direct action steps

---

## Analysis Components

### 1. FEMA Analyzer
**What it does:** Detects presence of 5 required elements

**Score calculation:**
```
FEMA Score = (Elements Present / 5) × 100

0 elements = 0%
3 elements = 60%
5 elements = 100%
```

**Output:**
- Elements present/missing list
- Compliance percentage
- Specific recommendations

### 2. WEA Analyzer
**What it does:** Validates character limits and format

**Rules:**
- Alert text ≤ 360 characters
- Recommended ≤ 90 characters for SMS platform
- Messages over 360 are non-compliant

**Output:**
- Character count
- Compliant/non-compliant status
- Truncation recommendation if needed

### 3. Readability Analyzer
**What it does:** Ensures 6th grade reading level

**Metrics used:**
- Flesch-Kincaid Grade
- Flesch Reading Ease
- Gunning Fog Index
- SMOG Index
- Automated Readability Index

**Score calculation:**
```
Average of 5 metrics
Target: ≤ 6.0 grade level = 100 score
Above 6.0 grade level = reduced score
```

### 4. Confusion Detector
**What it does:** Flags ambiguous or panic language

**Detects:**
- Vague action items ("take precautions")
- Contradictory instructions
- Unnecessary panic language
- Lack of specificity
- Ambiguous timing/location

**Output:**
- Risk score (0-100)
- Specific issues identified
- Compliance score

---

## Message Delivery

### Delivery Methods

#### SMS (Phone)
- Uses SMS gateway integration
- One message per recipient
- Character-limited awareness
- Instant delivery
- Confirmation tracking

#### Email
- Full message body possible
- Supports rich formatting
- Multiple recipients supported
- Delivery tracking
- Audit trail included

#### Both (SMS & Email)
- Redundant delivery
- SMS for immediate notification
- Email for detailed information
- Highest reliability

### Delivery Tracking
Every sent message generates:
- **Message ID:** Unique identifier for audit trail
- **Timestamp:** Exact send time (UTC)
- **Sender:** Who authorized the send
- **Recipients:** List of phone/email recipients
- **Status:** Success/failure per recipient
- **Error Details:** Specific errors if any

### Delivery Logs
Located in `delivery_logs/` directory:
- JSON file per message
- Complete metadata preserved
- Timestamp-based naming
- Searchable and analyzable

---

## Troubleshooting

### "Score is below threshold - cannot send"
**Cause:** Overall score < 80  
**Solution:**
1. Review "Priority Fixes" section
2. Address highest-impact issues first
3. Focus on missing FEMA elements
4. Simplify complex words
5. Re-analyze to see score improve

### "Yellow score but message is clear to me"
**Cause:** System detected specific compliance issue  
**Solution:**
1. Check the "Detailed Breakdown" tabs
2. Look at the specific issue flagged
3. Use AI rewrite suggestion as reference
4. Manually adjust the problematic area
5. Re-analyze

### "Red score on message that seems fine"
**Cause:** Multiple compliance issues accumulate  
**Solution:**
1. Start with FEMA elements (30% weight)
2. Ensure all 5 present and clear
3. Reduce word complexity
4. Ensure clear action instructions
5. Rebuild with system suggestions

### "Message sent but not received"
**Cause:** Delivery system issue  
**Solution:**
1. Check delivery confirmation details
2. Verify phone/email addresses are correct
3. Confirm SMS/email is enabled
4. Check delivery logs for error message
5. Retry with corrected recipients

### "Can't generate AI rewrite"
**Cause:** API key not configured  
**Settings → Enter Generative AI API Key**

### "Clear Form button not working"
**Cause:** Session state issue  
**Solution:**
1. Refresh the browser (F5)
2. Clear browser cache
3. Restart the application server

---

## Technical Architecture

### System Components

```
┌─────────────────────────────────────────────────┐
│         Streamlit Web Interface                 │
│  (HTML/CSS, Real-time Updates)                 │
└────────────────┬────────────────────────────────┘
                 │
      ┌──────────┴──────────┐
      │                     │
┌─────▼──────┐    ┌────────▼────────┐
│   Analysis │    │   Delivery      │
│  Modules   │    │   System        │
│            │    │                 │
│ • FEMA     │    │ • SMS Gateway   │
│ • WEA      │    │ • Email SMTP    │
│ • Read.    │    │ • Audit Log     │
│ • Confusion│    │ • Tracking      │
└─────┬──────┘    └────────┬────────┘
      │                    │
      └──────────┬─────────┘
                 │
        ┌────────▼────────┐
        │  Safety Scorer  │
        │ (Weight & Calc) │
        └────────┬────────┘
                 │
        ┌────────▼────────┐
        │  Result Display │
        │ (Color-coded)   │
        └─────────────────┘
```

### Key Technologies
- **Frontend:** Streamlit 1.28.1
- **Language:** Python 3.13.1
- **AI:** Anthropic Claude API
- **Analysis:** textstat library
- **Email:** Gmail SMTP
- **Storage:** JSON-based audit logs

### Data Flow
1. User enters message
2. All 4 analyzers run in parallel
3. Safety scorer calculates weights
4. Results displayed with color coding
5. User can improve message
6. When score ≥ 80, delivery enabled
7. User configures sender/recipients
8. Message sent and logged
9. Confirmation displayed

---

## Quick Reference

### Minimum Viable Message
```
Alert: [HAZARD] in/near [LOCATION]. 
[INSTRUCTION]. —[SOURCE]
```

### Optimal Message Format
```
[SOURCE]: Organization Name
[HAZARD]: Type of emergency
[LOCATION]: Specific area affected
[TIME]: When it ends or updates expected
[INSTRUCTION]: Specific action (verb + direction)
```

### Example (Excellent Compliance)
```
Flood Warning from County Emergency Services.
Flash flooding is occurring now in downtown areas.
Move to higher ground immediately.
Update expected in 2 hours.
```

### Common Mistakes to Avoid
❌ "Emergency situation developing"  
✅ "Wildfire spreading toward residential areas"

❌ "Please take precautions"  
✅ "Close windows and evacuate eastward"

❌ "More information soon"  
✅ "Next update at 3 PM or sooner if situation changes"

❌ "Severe weather expected"  
✅ "Thunderstorm with 60 mph winds arriving in 15 minutes"

---

## Support & Resources

### External Documentation
- **FEMA:** www.fema.gov/emergency/alerts
- **WEA:** www.fema.gov/emergency/communications/integrated-public-alert-warning-system
- **FCC Rules:** Part 11 of FCC Rules (47 CFR §11)
- **ADA Standards:** Section 508 Standards for Information and Communication Technology

### Getting Help
1. Check "Detailed Breakdown" tabs for specific issues
2. Try AI rewrite suggestion for guidance
3. Review examples in this guide
4. Check Priority Fixes recommendations
5. Review delivery logs if message didn't send

### Suggestions for Improvement
This is an MVP (Minimum Viable Product). Future enhancements may include:
- Spanish/multilingual support
- Integration with Hyper-Reach HQ
- Integration with Twilio for SMS
- Database backend for message history
- Role-based access control
- REST API for external integrations
- Weather data integration
- News feed monitoring

---

## Acknowledgments

This system was designed with reference to the 2018 Hawaii false missile alert incident, implementing safeguards to prevent such occurrences through comprehensive message validation and verification.

**Created:** February 2026  
**Organization:** Incredible Visibility Services  
**Status:** MVP v1.0 - Production Ready

---

**For questions or feedback, contact your Emergency Management Administration.**

---

*This document should be reviewed periodically and updated as regulations change.*

