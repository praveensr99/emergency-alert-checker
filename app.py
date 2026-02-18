"""
AI Message Compliance & Safety Checker
MVP Application using Streamlit
"""

import re
import streamlit as st
import os
from dotenv import load_dotenv
from analysis.fema_analyzer import FEMAAnalyzer
from analysis.wea_analyzer import WEAAnalyzer
from analysis.readability_analyzer import ReadabilityAnalyzer
from analysis.confusion_detector import ConfusionDetector
from utils.safety_scorer import SafetyScorer
from utils.message_delivery import MessageDeliverySystem
from utils.email_service import EmailService

load_dotenv()

# --- Page Config: wide layout, sidebar always open ---
st.set_page_config(
    page_title="Emergency Alert Safety Checker",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Minimal CSS ---
st.markdown("""
<style>
    .score-badge {
        padding: 18px 12px;
        border-radius: 12px;
        text-align: center;
        font-weight: 700;
        margin: 4px 0 12px 0;
    }
    .score-green {
        background: linear-gradient(135deg, #28a745 0%, #218838 100%);
        color: #fff;
    }
    .score-yellow {
        background: linear-gradient(135deg, #f9a825 0%, #f57f17 100%);
        color: #fff;
    }
    .score-red {
        background: linear-gradient(135deg, #dc3545 0%, #c82333 100%);
        color: #fff;
    }
    .pill-pass {
        display: inline-block;
        background: #e8f5e9;
        color: #2e7d32;
        padding: 2px 10px;
        border-radius: 12px;
        font-size: 13px;
        font-weight: 600;
    }
    .pill-fail {
        display: inline-block;
        background: #ffebee;
        color: #c62828;
        padding: 2px 10px;
        border-radius: 12px;
        font-size: 13px;
        font-weight: 600;
    }
    .pill-off {
        display: inline-block;
        background: #f5f5f5;
        color: #bdbdbd;
        padding: 2px 10px;
        border-radius: 12px;
        font-size: 13px;
        font-weight: 600;
    }
    .step-label {
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        color: #9e9e9e;
        margin-bottom: 2px;
    }
    .char-counter {
        font-size: 13px;
        color: #757575;
        margin-top: -8px;
    }
    .char-counter .over { color: #c62828; font-weight: 600; }
    .char-counter .ok { color: #2e7d32; }
    .block-container { padding-top: 1rem; }
</style>
""", unsafe_allow_html=True)

# --- Example templates ---
EXAMPLE_TEMPLATES = {
    "— Select an example —": "",
    "Tsunami (Good - Passes)": (
        "City of Honolulu Emergency Management: Tsunami warning for Waikiki Beach "
        "and surrounding coastal areas until 6:00 PM today. Move to higher ground "
        "immediately. Avoid shoreline areas."
    ),
    "Tornado (Needs Work)": (
        "Tornado warning for the downtown area. Seek shelter now."
    ),
    "Wildfire (Good)": (
        "Cal Fire Alert: Wildfire spreading near Oak Valley residential zone. "
        "Evacuate to Riverside High School by 3:00 PM today. Avoid Highway 101."
    ),
    "Vague Alert (Fails)": (
        "Something dangerous might happen soon. Be careful and stay alert."
    ),
}

# --- Validation helpers ---
_EMAIL_RE = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')
_PHONE_RE = re.compile(r'^[\d\s\-\+\(\)]{7,}$')


def validate_emails(raw_lines: list[str]) -> tuple[list[str], list[str]]:
    valid, invalid = [], []
    for line in raw_lines:
        if _EMAIL_RE.match(line):
            valid.append(line)
        else:
            invalid.append(line)
    return valid, invalid


def validate_phones(raw_lines: list[str]) -> tuple[list[str], list[str]]:
    valid, invalid = [], []
    for line in raw_lines:
        if _PHONE_RE.match(line):
            valid.append(line)
        else:
            invalid.append(line)
    return valid, invalid


# --- Cached init ---
@st.cache_resource
def initialize_analyzers():
    return {
        "fema": FEMAAnalyzer(),
        "wea": WEAAnalyzer(),
        "readability": ReadabilityAnalyzer(),
        "confusion": ConfusionDetector(),
        "scorer": SafetyScorer(),
        "delivery": MessageDeliverySystem()
    }


def get_ai_analyzer():
    api_key = st.session_state.get("ai_api_key") or os.getenv("GENAI_API_KEY")
    if not api_key:
        return None
    try:
        from utils.claude_api import ClaudeAnalyzer
        return ClaudeAnalyzer(api_key=api_key)
    except Exception:
        return None


def run_analysis(message: str, analyzers: dict) -> dict:
    return {
        "fema": analyzers["fema"].analyze(message),
        "wea": analyzers["wea"].analyze(message),
        "readability": analyzers["readability"].analyze(message),
        "confusion": analyzers["confusion"].analyze(message)
    }


# --- UI helpers ---
def _score_css(score: float) -> str:
    if score >= 80:
        return "score-green"
    elif score >= 60:
        return "score-yellow"
    return "score-red"


def _pill(passed: bool, label_pass: str = "Pass", label_fail: str = "Fail") -> str:
    if passed:
        return f'<span class="pill-pass">{label_pass}</span>'
    return f'<span class="pill-fail">{label_fail}</span>'


def _fema_pill(present: bool, name: str) -> str:
    if present:
        return f'<span class="pill-pass">{name}</span>'
    return f'<span class="pill-off">{name}</span>'


# ====================================================
# MAIN
# ====================================================
def main():
    analyzers = initialize_analyzers()

    # ================================================
    # SIDEBAR — Settings (always visible)
    # ================================================
    with st.sidebar:
        st.markdown("### Settings")

        # AI key
        st.markdown("**AI Suggestions**")
        api_key_input = st.text_input(
            "Generative AI API Key",
            type="password",
            help="Google Generative AI key for AI-powered rewrites",
            label_visibility="collapsed",
            placeholder="Paste GENAI API key...",
        )
        if api_key_input:
            st.session_state.ai_api_key = api_key_input
        has_key = bool(st.session_state.get("ai_api_key") or os.getenv("GENAI_API_KEY"))
        st.caption("Status: " + ("Connected" if has_key else "Not configured"))

        st.divider()

        # Email service
        st.markdown("**Email Service**")
        email_service = EmailService()
        email_status = email_service.get_status()
        if email_status["configured"]:
            st.caption(f"SMTP: {email_status['smtp_server']} — Ready")
        else:
            st.caption("Not configured — set SMTP vars in .env")

        st.divider()

        # Delivery history
        st.markdown("**Delivery History**")
        delivery_system = analyzers["delivery"]
        total_delivered = delivery_system.get_total_messages_delivered()
        st.metric("Messages Sent", total_delivered)
        if total_delivered > 0:
            with st.expander("View history"):
                history = delivery_system.get_delivery_history(10)
                for msg in history:
                    st.caption(f"{msg['message_id'][:18]}... — Score {msg['safety_score']}/100")

        st.divider()

        # About
        st.markdown("**About**")
        st.markdown(
            "This tool helps ensure emergency messages "
            "compliance with:\n"
            "- **FEMA** regulations (5 essential elements)\n"
            "- **WEA** character limits (90/360 chars)\n"
            "- **ADA** accessibility standards (6th grade reading level)\n"
            "- **FCC** clarity requirements",
            help=None
        )

    # ================================================
    # MAIN CONTENT
    # ================================================
    st.markdown("## 🚨 Emergency Alert Safety Checker")

    # Callbacks
    def _clear_form():
        st.session_state.message_input = ""
        st.session_state.message_sent = False
        st.session_state.last_sent_message = ""
        st.session_state.sent_message_id = None

    def _load_example():
        selected = st.session_state.get("example_selector", "")
        text = EXAMPLE_TEMPLATES.get(selected, "")
        if text:
            st.session_state.message_input = text
            st.session_state.message_sent = False

    # --- Two-column layout: left = input, right = results ---
    col_input, col_results = st.columns([1, 1], gap="large")

    with col_input:
        # STEP 1
        st.markdown('<div class="step-label">Step 1</div>', unsafe_allow_html=True)
        st.markdown("**Draft Your Emergency Message**")

        message = st.text_area(
            "Emergency Message",
            height=160,
            placeholder="e.g. 'City of Honolulu: Tsunami warning for Waikiki until 6 PM. Move to higher ground immediately.'",
            label_visibility="collapsed",
            key="message_input"
        )

        # Character counter + FEMA pills inline under the text area
        if message:
            char_count = len(message)
            if char_count <= 90:
                cc_html = f'<div class="char-counter"><span class="ok">{char_count}/90</span> chars — fits standard WEA</div>'
            elif char_count <= 360:
                cc_html = f'<div class="char-counter">{char_count}/360 chars — extended WEA</div>'
            else:
                over = char_count - 360
                cc_html = f'<div class="char-counter"><span class="over">{char_count} chars — {over} over 360 limit</span></div>'
            st.markdown(cc_html, unsafe_allow_html=True)

            # Live FEMA indicators
            quick_fema = analyzers["fema"].analyze(message)
            pills = " ".join(
                _fema_pill(quick_fema[key], label)
                for key, label in [("source", "Source"), ("hazard", "Hazard"),
                                   ("location", "Location"), ("time", "Time"),
                                   ("instruction", "Instruction")]
            )
            st.markdown(pills, unsafe_allow_html=True)

        # Buttons row: Example selector | Load | Clear
        b1, b2, b3 = st.columns([3, 1, 1])
        with b1:
            st.selectbox(
                "Example",
                options=list(EXAMPLE_TEMPLATES.keys()),
                key="example_selector",
                label_visibility="collapsed",
            )
        with b2:
            st.button("Load", on_click=_load_example, use_container_width=True)
        with b3:
            st.button("Clear", on_click=_clear_form, use_container_width=True)

    # Reset sent flag when message changes
    if message != st.session_state.get("last_sent_message", "") and st.session_state.get("message_sent"):
        st.session_state.message_sent = False
        st.session_state.sent_message_id = None

    # --- Right column: compliance results ---
    with col_results:
        if not message:
            st.markdown('<div class="step-label">Step 2</div>', unsafe_allow_html=True)
            st.markdown("**Compliance Review**")
            st.info("Enter a message or load an example to see compliance results.")
        else:
            analysis_results = run_analysis(message, analyzers)
            overall = analyzers["scorer"].calculate_overall_score(analysis_results)
            score = overall["overall_score"]

            st.markdown('<div class="step-label">Step 2</div>', unsafe_allow_html=True)
            st.markdown("**Compliance Review**")

            # Score badge
            css = _score_css(score)
            st.markdown(
                f'<div class="score-badge {css}">'
                f'<div style="font-size:36px;">{score}/100</div>'
                f'<div style="font-size:13px;margin-top:2px;">{overall["safety_level"]}</div>'
                f'</div>',
                unsafe_allow_html=True
            )

            # FEMA hard gate warning
            if not overall.get("fema_gate_passed", True):
                fema_data = analysis_results["fema"]
                st.error(
                    f"Requires {overall['min_fema_elements']}/5 FEMA elements. "
                    f"Currently: {fema_data['elements_present']}/5. "
                    f"Missing: {', '.join(fema_data['missing_elements'])}."
                )

            # 4 mini-metrics
            fema = analysis_results["fema"]
            wea = analysis_results["wea"]
            read = analysis_results["readability"]
            conf = analysis_results["confusion"]

            m1, m2, m3, m4 = st.columns(4)
            m1.metric("FEMA", f"{fema['elements_present']}/5")
            m2.metric("WEA", f"{wea['character_count']} ch")
            m3.metric("Grade", read["average_grade_level"])
            m4.metric("Risk", f"{conf['risk_score']}/100")

            # Priority fixes
            if overall["priority_fixes"]:
                for fix in overall["priority_fixes"]:
                    icon = {"high": "🔴", "medium": "🟡", "low": "🔵"}.get(fix["impact"], "⚪")
                    st.caption(f"{icon} {fix['issue']}")

            # Detailed breakdown
            with st.expander(
                f"FEMA — {fema['elements_present']}/5 elements",
                expanded=fema["compliance_percentage"] < 100
            ):
                elements = [
                    ("Source", fema["source"]),
                    ("Hazard", fema["hazard"]),
                    ("Location", fema["location"]),
                    ("Time", fema["time"]),
                    ("Instruction", fema["instruction"]),
                ]
                pills_html = " ".join(
                    _pill(present, f"✓ {name}", f"✗ {name}") for name, present in elements
                )
                st.markdown(pills_html, unsafe_allow_html=True)
                if fema["missing_elements"]:
                    st.warning(f"Missing: {', '.join(fema['missing_elements'])}")

            wea_ok = wea["compliant_360"]
            with st.expander(
                f"WEA — {wea['character_count']} characters",
                expanded=not wea_ok
            ):
                st.markdown(
                    f"90-char: {_pill(wea['compliant_90'])} &nbsp; "
                    f"360-char: {_pill(wea['compliant_360'])}",
                    unsafe_allow_html=True
                )
                if wea["character_count"] <= 360:
                    limit = 90 if wea["character_count"] <= 90 else 360
                    st.progress(min(wea["character_count"] / limit, 1.0))
                    st.caption(f"{wea['character_count']}/{limit} characters")
                else:
                    st.progress(1.0)
                    st.error(f"Over limit by {wea['chars_over_long']} characters")
                st.caption(wea["recommendation"])

            with st.expander(
                f"Readability — Grade {read['average_grade_level']}",
                expanded=not read["is_compliant"]
            ):
                grade_label = f"Grade {read['average_grade_level']}"
                pill_html = _pill(read['is_compliant'], 'Compliant', grade_label)
                st.markdown(
                    f"Status: {pill_html} &nbsp; Score: **{read['compliance_score']}/100**",
                    unsafe_allow_html=True
                )
                st.caption("All Metrics")
                rm1, rm2, rm3 = st.columns(3)
                rm1.metric("Flesch-Kincaid", read["flesch_kincaid_grade"])
                rm2.metric("Reading Ease", read["flesch_reading_ease"])
                rm3.metric("Gunning Fog", read["gunning_fog_index"])
                rm4, rm5, _ = st.columns(3)
                rm4.metric("SMOG Index", read["smog_index"])
                rm5.metric("Auto Readability", read["automated_readability_index"])
                if read["recommendations"]:
                    for rec in read["recommendations"]:
                        st.caption(f"• {rec}")

            with st.expander(
                f"Clarity — Risk {conf['risk_score']}/100",
                expanded=conf["risk_score"] >= 30
            ):
                issues = conf["identified_issues"]
                if issues:
                    for issue in issues:
                        st.markdown(
                            f"**{issue['type']}:** \"{issue['text']}\" — {issue['reason']}"
                        )
                else:
                    st.success("No clarity issues detected.")
                if conf["recommendations"]:
                    for rec in conf["recommendations"]:
                        st.caption(f"• {rec}")

            # Score breakdown — color-coded highlighted points
            st.markdown("**Score Breakdown**")
            comp = overall["component_scores"]
            breakdown_items = [
                ("FEMA Elements", comp["fema"], "40%"),
                ("WEA Compliance", comp["wea"], "20%"),
                ("Readability", comp["readability"], "20%"),
                ("Clarity", comp["confusion"], "20%"),
            ]
            breakdown_html = ""
            for label, val, weight in breakdown_items:
                if val >= 80:
                    bg, fg = "#e8f5e9", "#2e7d32"
                elif val >= 60:
                    bg, fg = "#fff8e1", "#f57f17"
                else:
                    bg, fg = "#ffebee", "#c62828"
                breakdown_html += (
                    f'<div style="display:flex;align-items:center;gap:8px;'
                    f'margin-bottom:5px;padding:5px 10px;border-radius:8px;'
                    f'background:{bg};">'
                    f'<span style="font-weight:600;color:{fg};min-width:28px;">'
                    f'{val:.0f}%</span>'
                    f'<span style="color:{fg};font-size:13px;">'
                    f'{label} <span style="opacity:0.6;">({weight} weight)</span>'
                    f'</span></div>'
                )
            st.markdown(breakdown_html, unsafe_allow_html=True)

    # ====================================================
    # Below the two columns: AI rewrite + Send
    # ====================================================
    if not message:
        return

    # Re-fetch analysis for sections below (already computed inside col_results)
    analysis_results = run_analysis(message, analyzers)
    overall = analyzers["scorer"].calculate_overall_score(analysis_results)
    score = overall["overall_score"]

    st.divider()

    # AI Rewrite + Step 3 side by side
    col_ai, col_send = st.columns([1, 1], gap="large")

    # --- AI Rewrite ---
    with col_ai:
        ai_analyzer = get_ai_analyzer()
        if ai_analyzer:
            st.markdown('<div class="step-label">AI Assistant</div>', unsafe_allow_html=True)
            st.markdown("**AI-Powered Rewrite**")
            if st.button("✨ Generate Compliant Rewrite", use_container_width=True):
                with st.spinner("Generating..."):
                    suggestion = ai_analyzer.suggest_rewrite(message, analysis_results)
                if suggestion["success"]:
                    suggested_msg = suggestion["suggested_message"]
                    st.success("Suggestion generated!")

                    suggested_analysis = run_analysis(suggested_msg, analyzers)
                    suggested_overall = analyzers["scorer"].calculate_overall_score(suggested_analysis)
                    new_score = suggested_overall["overall_score"]
                    delta = new_score - score
                    delta_text = f"+{delta:.0f}" if delta >= 0 else f"{delta:.0f}"
                    delta_color = "#2e7d32" if delta > 0 else ("#c62828" if delta < 0 else "#757575")

                    st.markdown(
                        f'Score: **{score}** &rarr; **{new_score}** '
                        f'(<span style="color:{delta_color};font-weight:600;">{delta_text}</span>)',
                        unsafe_allow_html=True
                    )
                    st.code(suggested_msg, language="text")

                    def _use_suggestion():
                        st.session_state.message_input = suggested_msg
                        st.session_state.message_sent = False

                    st.button("Use This Message", on_click=_use_suggestion, use_container_width=True)
                else:
                    st.error(f"Failed: {suggestion.get('error', 'Unknown error')}")
        else:
            st.markdown('<div class="step-label">AI Assistant</div>', unsafe_allow_html=True)
            st.markdown("**AI-Powered Rewrite**")
            st.caption("Add your Generative AI API key in the sidebar to enable AI rewrites.")

    # --- Step 3: Send ---
    with col_send:
        st.markdown('<div class="step-label">Step 3</div>', unsafe_allow_html=True)
        st.markdown("**Send Alert**")

        is_ready = overall["is_ready_to_send"]
        already_sent = st.session_state.get("message_sent", False)

        if not is_ready:
            reasons = []
            if score < overall["min_threshold"]:
                reasons.append(f"Score {score} < {overall['min_threshold']}")
            if not overall.get("fema_gate_passed", True):
                reasons.append(f"Need {overall['min_fema_elements']}/5 FEMA elements")
            st.warning("Cannot send yet. " + ". ".join(reasons) + ".")

        elif already_sent:
            st.success("Sent! Clear the form to draft a new alert.")
            _show_sent_confirmation()

        else:
            # Delivery config
            default_sender = os.getenv("SENDER_NAME", "")
            sender_name = st.text_input(
                "Sender Name",
                value=st.session_state.get("sender_name", default_sender),
                placeholder="e.g. Emergency Management Agency",
                key="sender_name"
            )
            delivery_method = st.selectbox(
                "Method",
                ["Phone (SMS)", "Email", "Both (SMS & Email)"],
                key="delivery_method"
            )

            phones, emails = [], []
            phone_errors, email_errors = [], []

            if delivery_method in ["Phone (SMS)", "Both (SMS & Email)"]:
                phone_input = st.text_area("Phone Numbers (one per line)", height=60, key="phone_input", placeholder="+1 555-123-4567\n+1 555-987-6543")
                raw_phones = [p.strip() for p in phone_input.split("\n") if p.strip()]
                phones, phone_errors = validate_phones(raw_phones)
                if phone_errors:
                    st.error(f"Invalid: {', '.join(phone_errors)}")

            if delivery_method in ["Email", "Both (SMS & Email)"]:
                email_input = st.text_area("Email Addresses (one per line)", height=60, key="email_input", placeholder="john@example.com\njane@example.com")
                raw_emails = [e.strip() for e in email_input.split("\n") if e.strip()]
                emails, email_errors = validate_emails(raw_emails)
                if email_errors:
                    st.error(f"Invalid: {', '.join(email_errors)}")

            total_recipients = len(phones) + len(emails)
            has_validation_errors = bool(phone_errors or email_errors)

            if total_recipients > 0:
                parts = []
                if phones:
                    parts.append(f"**{len(phones)}** phone{'s' if len(phones) != 1 else ''}")
                if emails:
                    parts.append(f"**{len(emails)}** email{'s' if len(emails) != 1 else ''}")
                st.caption(f"Sending to {' and '.join(parts)}.")

            if st.button(
                "🚀 Send Alert",
                type="primary",
                use_container_width=True,
                disabled=(total_recipients == 0 or not sender_name or has_validation_errors)
            ):
                recipients = {"phone": phones, "email": emails, "method": delivery_method}
                delivery_sys = analyzers["delivery"]
                result = delivery_sys.deliver_message(
                    message, analysis_results, overall,
                    sender=sender_name, recipients=recipients
                )

                if result["success"]:
                    st.session_state.message_sent = True
                    st.session_state.last_sent_message = message
                    st.session_state.sent_message_id = result["message_id"]
                    st.session_state.sent_timestamp = result["timestamp"]
                    st.session_state.sent_result = result
                    st.session_state.sent_score = overall
                    st.success(result["message"])
                    st.rerun()
                else:
                    st.error(result["message"])

            if not sender_name:
                st.caption("Enter a sender name to enable sending.")
            elif total_recipients == 0 and not has_validation_errors:
                st.caption("Add at least one recipient.")


def _show_sent_confirmation():
    result = st.session_state.get("sent_result")
    score_data = st.session_state.get("sent_score")
    if not result:
        return

    with st.expander("Delivery Confirmation", expanded=True):
        c1, c2, c3 = st.columns(3)
        c1.metric("Message ID", result["message_id"][:16] + "...")
        c2.metric("Recipients", result["recipient_count"])
        c3.metric("Score", f"{score_data['overall_score']}/100" if score_data else "N/A")

        st.caption(f"Sender: {result['sender']} | Method: {result.get('method', 'N/A')}")

        email_status = result.get("email_delivery_status", {})
        if email_status.get("attempted"):
            st.divider()
            st.markdown("**Email Delivery**")
            for detail in email_status.get("details", []):
                if detail["status"] == "sent":
                    st.caption(f"✅ {detail['recipient']}")
                else:
                    st.caption(f"❌ {detail['recipient']} — {detail.get('error', 'Unknown')}")


if __name__ == "__main__":
    main()
