# FCC Alert Types & Examples

## Overview

The Federal Communications Commission (FCC) National Public Alert and Warning System (NPAWS) recognizes 18 distinct emergency alert types. This system validates messages against all 18 types to ensure proper categorization and prevent confusion.

---

## 18 FCC-Approved Alert Types

### 1. **EVACUATION ORDER**
**Definition**: Immediate departure from area required  
**Key Indicators**: "Evacuate", "Flee", "Leave immediately", "Abandon"

**✅ COMPLIANT EXAMPLE**:
```
Evacuation Order from City Emergency. Wildfire is approaching 
residential area now. Leave via Main Street immediately. 
Seek safety to the north. Go to the Community Center shelter.
```

**❌ NON-COMPLIANT EXAMPLE**:
```
Fire situation developing. Maybe evacuate soon if needed. 
Consider moving if you want to be safe.
```

---

### 2. **SHELTER IN PLACE**
**Definition**: Stay indoors, secure location  
**Key Indicators**: "Stay indoors", "Remain inside", "Do not leave", "Shelter"

**✅ COMPLIANT EXAMPLE**:
```
Shelter in Place from County Emergency. Chemical spill is 
hazardous now in downtown area. Remain indoors with windows 
closed until 8 PM today. Seal air intakes immediately.
```

---

### 3. **SEVERE WEATHER WARNING**
**Definition**: Dangerous weather condition imminent  
**Key Indicators**: "Tornado", "Hurricane", "Blizzard", "Flooding"

**✅ COMPLIANT EXAMPLE**:
```
Tornado Warning from National Weather Service. A tornado is 
occurring now in the northwest county near Highway 5. Seek 
shelter immediately in a building basement or interior room.
```

---

### 4. **HAZMAT RELEASE**
**Definition**: Dangerous chemical/biological release  
**Key Indicators**: "Chemical", "Hazardous", "Contamination", "Spill"

**✅ COMPLIANT EXAMPLE**:
```
Chemical Release Alert from Environmental Agency. Toxic gas 
release is happening now in Industrial Zone. Evacuate to 
west side immediately. Avoid breathing vapors.
```

---

### 5. **INFRASTRUCTURE FAILURE**
**Definition**: Critical system collapse (bridge, dam, power, water)  
**Key Indicators**: "Collapse", "Failure", "Bridge", "Dam", "Structure"

**✅ COMPLIANT EXAMPLE**:
```
Infrastructure Failure from Public Works. Bridge collapse is 
occurring now on Route 9. Evacuate the area immediately. 
Use alternate routes to the north.
```

---

### 6. **PUBLIC SAFETY THREAT**
**Definition**: General public danger  
**Key Indicators**: "Armed", "Threat", "Danger", "Intruder", "Suspicious"

**✅ COMPLIANT EXAMPLE**:
```
Public Safety Alert from Police Department. Armed individual 
is in the downtown area now. Shelter in place and avoid the 
downtown district. Stay locked indoors immediately.
```

---

### 7. **LAW ENFORCEMENT WARNING**
**Definition**: Active police operation requiring public awareness  
**Key Indicators**: "Police", "Law Enforcement", "Suspect", "Wanted"

**✅ COMPLIANT EXAMPLE**:
```
Law Enforcement Warning from Police Department. Escaped suspect 
is in residential area now near Oak Street. Avoid the area. 
Report sightings to Police immediately at 911.
```

---

### 8. **ALL CLEAR / CANCEL**
**Definition**: Previous alert is no longer in effect  
**Key Indicators**: "Cancelled", "All Clear", "Resume", "Cancel"

**✅ COMPLIANT EXAMPLE**:
```
All Clear from City Emergency. Tornado warning is cancelled. 
Flood warning is cancelled. Resume normal activities.
```

**⚠️ CRITICAL**: Must match the alert being cancelled exactly!

---

### 9. **TEST / EXERCISE**
**Definition**: Drill or system test (NOT real emergency)  
**Key Indicators**: "TEST", "EXERCISE", "DRILL", "This is a test"

**✅ COMPLIANT EXAMPLE**:
```
This is a TEST. This is a TEST. FEMA System Test. This is only 
a test of the Emergency Alert System. Do not evacuate. 
Repeat: This is a TEST.
```

**🚨 CRITICAL RULE**: TEST or EXERCISE alerts MUST:
- Be clearly marked at beginning AND end
- NOT contain real emergency language
- NOT request action or evacuation
- Have "TEST" in all caps

---

### 10. **TSUNAMI WARNING**
**Definition**: Ocean wave danger from earthquake/underwater event  
**Key Indicators**: "Tsunami", "Earthquake", "Ocean", "Coastal"

**✅ COMPLIANT EXAMPLE**:
```
Tsunami Warning from NOAA. Tsunami is possible now for coastal 
areas including beaches. Move to higher ground immediately. 
Avoid beaches and waterfront areas.
```

---

### 11. **WINTER STORM WARNING**
**Definition**: Dangerous cold weather, ice, snow  
**Key Indicators**: "Blizzard", "Ice", "Frozen", "Winter", "Snow"

**✅ COMPLIANT EXAMPLE**:
```
Winter Storm Warning from National Weather Service. Blizzard 
with 18-inch snow is developing now across the region. Remain 
indoors. Travel is prohibited until further notice.
```

---

### 12. **FIRE WARNING**
**Definition**: Active or imminent fire danger  
**Key Indicators**: "Fire", "Wildfire", "Burning", "Flames", "Structure"

**✅ COMPLIANT EXAMPLE**:
```
Fire Warning from Fire Department. Wildfire is spreading rapidly 
now in the northern hills near Hillcrest Road. Evacuate west 
immediately. Use Main Street evacuation route.
```

---

### 13. **HEALTH / MEDICAL EMERGENCY**
**Definition**: Disease, health crisis, contamination  
**Key Indicators**: "Disease", "Outbreak", "Epidemic", "Contamination", "Health"

**✅ COMPLIANT EXAMPLE**:
```
Health Emergency from Public Health Department. Contaminated 
water supply is affecting downtown area now. Do NOT use tap. 
Use bottled water until further notice.
```

---

### 14. **UTILITY ALERT**
**Definition**: Power, water, gas disruption  
**Key Indicators**: "Power", "Outage", "Utility", "Water", "Gas"

**✅ COMPLIANT EXAMPLE**:
```
Utility Alert from Water Department. Water main break is 
affecting downtown area starting now. Prepare with bottled 
water. Boil water until further notice if using tap.
```

---

### 15. **TRANSPORTATION DISRUPTION**
**Definition**: Road closure, transit impact, traffic danger  
**Key Indicators**: "Closure", "Transit", "Traffic", "Road", "Highway"

**✅ COMPLIANT EXAMPLE**:
```
Transportation Alert from Public Works. Highway 5 is closed 
now due to accidents. Use alternate Route 9. Expect delays 
of 45 minutes in downtown area.
```

---

### 16. **NATIONAL SECURITY WARNING**
**Definition**: Threat to nation, nuclear, military  
**Key Indicators**: "National", "Nuclear", "Security", "Missile", "Attack"

**✅ COMPLIANT EXAMPLE**:
```
National Security Alert from Department of Homeland Security. 
Missile threat is possible for coastal region now. Seek shelter 
immediately in buildings or basements below ground.
```

---

### 17. **ENVIRONMENTAL WARNING**
**Definition**: Air quality, radiation, contamination  
**Key Indicators**: "Air quality", "Dust", "Radiation", "Environmental"

**✅ COMPLIANT EXAMPLE**:
```
Environmental Alert from Air Quality Department. Dust storm 
with hazardous visibility is approaching the region now. 
Avoid outdoor activity. Close windows immediately.
```

---

### 18. **OTHER / MISCELLANEOUS**
**Definition**: Emergency not in other 17 categories  
**Key Indicators**: Unique emergency scenarios

**✅ COMPLIANT EXAMPLE**:
```
Emergency Alert from City. Large animal escaped from zoo 
is in downtown area now. Avoid parks and open spaces. 
Call Animal Control on sighting: [number]
```

---

## Implementation in System

### Alert Type Detection

The system automatically detects alert types through keyword matching:

```python
# Example from fema_analyzer.py
alert_types = {
    "evacuation": ["evacuate", "flee", "leave immediately"],
    "shelter_in_place": ["stay indoors", "remain inside", "shelter"],
    "severe_weather": ["tornado", "hurricane", "flood", "severe"],
    "hazmat": ["chemical", "hazardous", "contamination", "spill"],
    # ... 14 more types
}
```

### Testing Alert Types

Test each type with the Streamlit app:

```
Try these messages:

1. EVACUATION:
   "Evacuation Order. Wildfire is now at the northern residential 
   area. Evacuate south immediately via Main Street."

2. TORNADO:
   "Tornado Warning. A tornado is occurring now in the downtown 
   area. Seek shelter in a basement immediately."

3. TEST ALERT (should detect as TEST):
   "This is a TEST. NOAA test alert. This is only a test."
```

---

## False Alarm Prevention (Hawaii Example)

The 2018 Hawaii false missile alert was categorized as "National Security Warning" when it should have been marked "TEST".

**System Prevention**:
- ✅ Detects "TEST" keyword and flags it
- ✅ Warns if TEST contains emergency language
- ✅ Prevents sending if TEST/EVACUATION contradiction found
- ✅ Requires explicit confirmation

**Hawaii Message Would Have Been Flagged**:
```
Original (Jan 13, 2018):
"BALLISTIC MISSILE THREAT INBOUND TO HAWAII. SEEK IMMEDIATE SHELTER. 
THIS IS NOT A DRILL."

System Detection:
❌ ALERT: "This is NOT a DRILL" contradicts usual message format
❌ ALERT: No source organization specified
⚠️ WARNING: Extremely high panic language detected
⚠️ RECOMMENDATION: Is this real? Add source: "Confirm issuing agency"
```

---

## Compliance Verification

All 18 alert types are supported by the system:
- ✅ Keyword detection for each type
- ✅ FEMA 5-element validation for each
- ✅ WEA character limit enforcement
- ✅ ADA readability check
- ✅ Confusion risk detection

**Next Step**: Test your alert against the Streamlit app to verify proper categorization!

---

**Reference**: FCC National Public Alert and Warning System (NPAWS)  
**Updated**: February 17, 2026  
