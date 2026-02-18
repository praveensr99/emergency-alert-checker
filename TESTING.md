# Testing Guide & Sample Messages

This guide provides test cases and sample messages to validate the AI Message Compliance Checker MVP.

## Test Cases

### Test Case 1: Low Compliance Message

**Input:**
```
Take action immediately! Something bad might happen soon somewhere!
```

**Expected Output:**
- Overall Score: ~20-35/100 (CRITICAL)
- Missing FEMA Elements: All 5 elements
- WEA Compliance: ✓ Pass (67 chars)
- Readability: ⚠ Grade 7.5 (above target)
- Confusion Issues: 3-4 identified
  - Ambiguous: "take action immediately"
  - Panic language: "bad"
  - Vague location: "somewhere"

---

### Test Case 2: Medium Compliance Message

**Input:**
```
Weather Alert: Severe thunderstorm warning issued by National 
Weather Service. Damaging winds and heavy rain are expected in 
the downtown area starting at 3 PM today. Stay indoors and away 
from windows until further notice.
```

**Expected Output:**
- Overall Score: ~72-78/100 (IMPROVED)
- FEMA Elements: 4/5 present (missing specific instruction)
- WEA Compliance: ✓ Pass (180 chars)
- Readability: ✓ Grade 6.2 (near target)
- Confusion Issues: ~1-2 minor issues

---

### Test Case 3: High Compliance Message

**Input:**
```
Tornado Warning from County Emergency Management. A tornado 
is occurring now in the north county area near Highway 5. 
Seek shelter immediately in a building basement or interior 
room on the lowest floor.
```

**Expected Output:**
- Overall Score: ~88-95/100 (HIGH)
- FEMA Elements: 5/5 present ✓
- WEA Compliance: ✓ Pass (155 chars)
- Readability: ✓ Grade 5.8 (compliant)
- Confusion Issues: 0 identified
- Status: READY TO SEND

---

### Test Case 4: Perfect Compliance Message

**Input:**
```
Flood Warning from City Emergency. Flooding is happening now 
in downtown. Go to higher ground at once.
```

**Expected Output:**
- Overall Score: ~95-100/100 (CRITICAL)
- FEMA Elements: 5/5 present ✓
- WEA Compliance: ✓ Pass (90 chars exactly)
- Readability: ✓ Grade 4.2 (excellent)
- Confusion Issues: 0 identified
- Status: READY TO SEND ✓

---

### Test Case 5: Over WEA Character Limit

**Input:**
```
Critical Alert Notification: This is to inform all residents 
and stakeholders that a potentially catastrophic situation is 
developing in the metropolitan area. The situation may 
deteriorate rapidly and unpredictably at any moment. Please 
take immediate protective action. Avoid the affected zones 
entirely. Do not attempt to observe or investigate. Stay tuned 
to official channels for updates and additional information as 
the situation develops. We recommend all citizens to prepare 
emergency supplies immediately.
```

**Expected Output:**
- Overall Score: ~45-55/100
- WEA Compliance: ✗ Fail (over 360 chars)
- Recommendation: "Remove X characters to comply"
- Suggestion: AI-rewrite keeps essential info, cuts excess

---

## FEMA 5-Element Validation

Run these messages to test FEMA detection:

### Missing All Elements (0/5)
```
Emergency situation developing.
```

### Only Source (1/5)
```
Police Department alert.
```

### Source + Hazard (2/5)
```
Police Department: Tornado warning.
```

### Source + Hazard + Location (3/5)
```
Police Department: Tornado warning in downtown area.
```

### Source + Hazard + Location + Time (4/5)
```
Police Department: Tornado warning in downtown area starting now.
```

### All 5 Elements ✓ (5/5)
```
Police Department: Tornado warning in downtown area starting now. 
Go to shelter immediately.
```

---

## WEA Character Limit Tests

| Message | Chars | Compliant 90 | Compliant 360 | Expected Status |
|---------|-------|--------------|---------------|-----------------|
| "Alert!" | 6 | ✓ | ✓ | Excellent |
| "Tornado warning. Seek shelter." | 31 | ✓ | ✓ | Good |
| "A" × 90 | 90 | ✓ | ✓ | At limit |
| "A" × 91 | 91 | ✗ | ✓ | Extended OK |
| "A" × 360 | 360 | ✗ | ✓ | At extended limit |
| "A" × 361 | 361 | ✗ | ✗ | OVER LIMIT |

---

## Readability Level Tests

### Grade 4.0 (Very Simple)
```
Fire. Go out. Run fast. Stop.
```

### Grade 6.0 (Target)
```
Flood warning from County Emergency. A river is flooding now 
near Riverside Avenue. Leave your home and go to higher ground 
right now.
```

### Grade 8.5 (Too Complex)
```
Insufficient precipitation sustainability necessitates immediate 
residential relocation to geographically elevated topographic 
situations.
```

---

## Confusion Risk Tests

### Clear Message (Low Risk)
```
Earthquake. Feel safe. Go outside.
```

### Ambiguous Message (High Risk)
```
Something might happen soon in the area. Take action 
immediately. Be careful. Stay alert.
```

### Panic-Inducing (High Risk)
```
Catastrophic disaster is approaching! Apocalyptic event 
imminent! Flee your homes in terror!
```

### Vague Actions (Medium Risk)
```
Go there. Do something. Check it out. Pay attention.
```

---

## AI Rewrite Feature Tests

*Only available with Anthropic API key configured*

### Test 1: Low Compliance → High Compliance

**Before:**
```
Bad storm. Maybe. Somewhere. Do something!
```

**Expected AI Rewrite:**
```
Severe Storm Warning from Weather Service. Strong thunderstorm is 
developing over the west side now. Move to the basement or interior 
room immediately. Avoid windows.
```

### Test 2: Over Character Limit → Under Limit

**Before:** (450+ chars)
```
This is a comprehensive notification regarding a flood situation 
that has developed across multiple neighborhoods in the jurisdiction 
area. The flooding is widespread and serious. People should evacuate 
their homes and belongings and move to designated shelters or 
higher ground locations. Do not delay. Emergency services are 
stretched thin. Follow instructions from authorities...
```

**Expected AI Rewrite:** (Under 360 chars)
```
Flood Alert from County Emergency. Major flooding is happening now 
across the west side. Leave your homes and go to shelters or higher 
ground immediately.
```

---

## Performance Benchmarks

### Response Time Expected
- FEMA analysis: < 50ms
- WEA analysis: < 10ms
- Readability analysis: < 200ms
- Confusion detection: < 100ms
- Overall score: < 400ms
- AI rewrite: 2-5 seconds

### Score Stability
- Scores should be consistent for same input
- Small text changes should produce proportional score changes
- No sudden score jumps (0-100 range)

---

## Edge Cases to Test

### Empty Message
- Input: (empty text field)
- Expected: Show prompt to enter message

### Very Long Message
- Input: 1000+ character message
- Expected: Show "Over limit" in WEA, calculate readability anyway

### Only Numbers/Symbols
- Input: "123 !!! ###"
- Expected: Calculate readability (should be very simple)

### HTML/Markup
- Input: "Alert <b>DANGER</b> now!"
- Expected: Analyze as plain text (should ignore tags)

### Multiple Languages (Future)
- Input: "Alerta de tormenta." (Spanish)
- Expected: (Future feature) Detect and analyze

### Repeated Words
- Input: "Go go go go go go go go go"
- Expected: Flag as low readability and low information value

---

## Validation Checklist

- [ ] All FEMA elements detected correctly
- [ ] WEA character counting accurate
- [ ] Readability scores reasonable
- [ ] Confusion issues identified
- [ ] Overall score calculation correct
- [ ] Safety level labels appropriate
- [ ] Send button disabled until score ≥ 75
- [ ] AI rewrites helpful and compliant
- [ ] Recommendations are actionable
- [ ] UI responsive and intuitive

---

## Known Limitations (MVP)

1. **Language Detection**: Currently English-only (no language detection)
2. **Domain-Specific Terms**: Some emergency terminology may not be recognized
3. **Context**: Doesn't understand previous messages or ongoing situations
4. **Regional Variations**: Uses general US standards (no localization)
5. **Accessibility**: Limited support for vision/hearing impairments
6. **Integration**: Not yet integrated with Hyper-Reach portal

---

## Future Test Cases

- [ ] Multi-language support testing
- [ ] Integration testing with Hyper-Reach
- [ ] Historical message templates
- [ ] Performance at scale (100+ concurrent users)
- [ ] Mobile responsiveness testing
- [ ] Accessibility compliance (WCAG 2.1)

---

For issues or suggestions, contact the development team.
