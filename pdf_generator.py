"""
PDF Generation Utility for Emergency Alert Safety Checker
Generates downloadable PDF documentation and reports
"""

import os
from datetime import datetime
from pathlib import Path

try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
except ImportError:
    print("Error: reportlab not installed. Install with: pip install reportlab")
    exit(1)


class PDFGenerator:
    """Generate PDF documents for the Emergency Alert Safety Checker"""
    
    def __init__(self, output_dir: str = "pdf_exports"):
        """Initialize PDF generator"""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
    
    def _setup_custom_styles(self):
        """Setup custom paragraph styles for the document"""
        # Title style
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#d32f2f'),
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))
        
        # Heading 2 style
        self.styles.add(ParagraphStyle(
            name='CustomHeading2',
            parent=self.styles['Heading2'],
            fontSize=14,
            textColor=colors.HexColor('#1976d2'),
            spaceAfter=12,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        ))
        
        # Heading 3 style
        self.styles.add(ParagraphStyle(
            name='CustomHeading3',
            parent=self.styles['Heading3'],
            fontSize=12,
            textColor=colors.HexColor('#388e3c'),
            spaceAfter=10,
            spaceBefore=10,
            fontName='Helvetica-Bold'
        ))
        
        # Normal body text
        self.styles.add(ParagraphStyle(
            name='CustomBody',
            parent=self.styles['BodyText'],
            fontSize=10,
            alignment=TA_JUSTIFY,
            spaceAfter=10
        ))
        
        # Info box style
        self.styles.add(ParagraphStyle(
            name='InfoBox',
            parent=self.styles['Normal'],
            fontSize=9,
            textColor=colors.HexColor('#1b5e20'),
            leftIndent=20,
            spaceAfter=8
        ))
    
    def generate_functional_guide_pdf(self) -> str:
        """Generate PDF from FUNCTIONAL_GUIDE.md"""
        output_file = self.output_dir / f"Emergency_Alert_Functional_Guide_{datetime.now().strftime('%Y%m%d')}.pdf"
        
        doc = SimpleDocTemplate(
            str(output_file),
            pagesize=letter,
            rightMargin=0.75*inch,
            leftMargin=0.75*inch,
            topMargin=0.75*inch,
            bottomMargin=0.75*inch,
            title="Emergency Alert Safety Checker - Functional Guide"
        )
        
        story = []
        
        # Title
        story.append(Paragraph("🚨 Emergency Alert Safety Checker", self.styles['CustomTitle']))
        story.append(Paragraph("Functional Guide & User Manual", self.styles['Heading2']))
        story.append(Spacer(1, 0.3*inch))
        
        # Document info
        info_text = f"<b>Version:</b> 1.0 | <b>Date:</b> {datetime.now().strftime('%B %d, %Y')} | <b>Status:</b> Production Ready"
        story.append(Paragraph(info_text, self.styles['Normal']))
        story.append(Spacer(1, 0.2*inch))
        
        # Executive Summary
        story.append(Paragraph("Executive Summary", self.styles['CustomHeading2']))
        story.append(Paragraph(
            "The Emergency Alert Safety Checker is a comprehensive web application that validates emergency alert messages "
            "for compliance with federal regulations (FEMA, WEA, FCC) and best practices. The system analyzes messages across "
            "multiple dimensions and provides actionable feedback to prevent false alerts, ensure clarity, and guarantee compliance "
            "before sending. This system prevents incidents like the 2018 Hawaii false missile alert by implementing a 4-layer verification system.",
            self.styles['CustomBody']
        ))
        story.append(Spacer(1, 0.2*inch))
        
        # Purpose & Benefits
        story.append(Paragraph("Purpose & Key Benefits", self.styles['CustomHeading2']))
        benefits = [
            "Real-time compliance feedback as you type",
            "Prevents false alerts before sending",
            "AI-powered message improvement suggestions",
            "Multi-layer verification (4-element system)",
            "Complete audit trail and delivery logging",
            "Support for SMS & Email delivery",
            "Compliance with FEMA, WEA, FCC, and ADA standards"
        ]
        
        for benefit in benefits:
            story.append(Paragraph(f"✓ {benefit}", self.styles['InfoBox']))
        story.append(Spacer(1, 0.2*inch))
        
        # Score System
        story.append(Paragraph("Safety Score System", self.styles['CustomHeading2']))
        story.append(Paragraph(
            "Every message receives a single overall score (0-100) that determines its compliance status. "
            "The score combines analysis from four weighted components:",
            self.styles['CustomBody']
        ))
        story.append(Spacer(1, 0.1*inch))
        
        # Score table
        score_data = [
            ['Component', 'What It Checks', 'Weight'],
            ['FEMA Elements', 'Source, Hazard, Location, Time, Instruction', '30%'],
            ['WEA Compliance', 'Character limits (90/360 chars)', '20%'],
            ['Readability', 'Grade level (≤6th grade for ADA)', '25%'],
            ['Clarity/Confusion', 'Ambiguous or panic language', '25%']
        ]
        
        score_table = Table(score_data, colWidths=[1.5*inch, 3*inch, 0.8*inch])
        score_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1976d2')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5f5f5')])
        ]))
        story.append(score_table)
        story.append(Spacer(1, 0.2*inch))
        
        # Color coding
        story.append(Paragraph("Compliance Status Indicators", self.styles['CustomHeading2']))
        status_data = [
            ['Score Range', 'Color', 'Status', 'Action Required'],
            ['80-100', '🟢 Green', 'Compliant', 'Ready to Send'],
            ['60-79', '🟡 Yellow', 'Needs Improvement', 'Review Recommended'],
            ['0-59', '🔴 Red', 'Non-Compliant', 'Must Revise']
        ]
        
        status_table = Table(status_data, colWidths=[1.2*inch, 0.8*inch, 1.3*inch, 1.5*inch])
        status_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#388e3c')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#e8f5e9'), colors.HexColor('#fff3e0'), colors.HexColor('#ffebee')])
        ]))
        story.append(status_table)
        story.append(Spacer(1, 0.2*inch))
        
        # FEMA Elements
        story.append(Paragraph("FEMA 5-Element Requirement", self.styles['CustomHeading2']))
        story.append(Paragraph(
            "Every emergency message MUST contain all 5 FEMA elements for compliance:",
            self.styles['CustomBody']
        ))
        story.append(Spacer(1, 0.1*inch))
        
        fema_elements = [
            ("SOURCE", "Who is sending the alert?", "City Emergency Services (avoid: 'Someone')"),
            ("HAZARD", "What is the emergency?", "Tornado warning (avoid: 'Something bad')"),
            ("LOCATION", "Where is it happening?", "Downtown area (avoid: 'In the city')"),
            ("TIME", "How long? When does it expire?", "Until 6 PM (avoid: 'Soon')"),
            ("INSTRUCTION", "What should people do?", "Move to shelter (avoid: 'Be careful')")
        ]
        
        for element, question, example in fema_elements:
            text = f"<b>{element}:</b> {question}<br/><i>{example}</i>"
            story.append(Paragraph(text, self.styles['CustomBody']))
            story.append(Spacer(1, 0.05*inch))
        
        story.append(Spacer(1, 0.2*inch))
        
        # How to Use
        story.append(PageBreak())
        story.append(Paragraph("How to Use the Application", self.styles['CustomHeading2']))
        
        steps = [
            ("Step 1: Launch", "Run 'streamlit run app.py' and open http://localhost:8501"),
            ("Step 2: Enter Message", "Type or paste your alert message in the text area"),
            ("Step 3: Review Analysis", "Read the compliance analysis results (automatic)"),
            ("Step 4: Review Recommendations", "Check Priority Fixes section for improvements"),
            ("Step 5A: Use AI Rewrite", "Generate AI-improved version for reference (optional)"),
            ("Step 5B: Manual Edit", "Edit your message directly based on feedback"),
            ("Step 6: Configure Delivery", "When score ≥80, add sender info and recipients"),
            ("Step 7: Send", "Click 'READY TO SEND' to deliver message"),
            ("Step 8: Clear & Repeat", "Click 'Clear Form' to start next alert")
        ]
        
        for step_num, (step_name, description) in enumerate(steps, 1):
            text = f"<b>{step_name}:</b> {description}"
            story.append(Paragraph(text, self.styles['CustomBody']))
        
        story.append(Spacer(1, 0.2*inch))
        
        # Message Examples
        story.append(Paragraph("Example Messages", self.styles['CustomHeading2']))
        story.append(Paragraph("<b>EXCELLENT (Score 92+):</b>", self.styles['CustomHeading3']))
        story.append(Paragraph(
            '"Flood Warning from County Emergency Services. Flash flooding is occurring now in downtown areas near Highway 5. Move to higher ground immediately. Update expected at 3 PM.",',
            self.styles['CustomBody']
        ))
        
        story.append(Paragraph("<b>GOOD (Score 78):</b>", self.styles['CustomHeading3']))
        story.append(Paragraph(
            '"Flooding is happening in multiple areas of the city. Please be cautious and avoid affected zones. More information will be provided soon.",',
            self.styles['CustomBody']
        ))
        
        story.append(Paragraph("<b>POOR (Score 45):</b>", self.styles['CustomHeading3']))
        story.append(Paragraph(
            '"Critical alert notification. Potentially catastrophic situation developing. Please take immediate protective action and stay tuned.",',
            self.styles['CustomBody']
        ))
        
        story.append(Spacer(1, 0.3*inch))
        
        # Footer
        story.append(Spacer(1, 0.5*inch))
        footer_text = "Generated for Emergency Management and Public Safety Officials | Version 1.0 | February 2026"
        story.append(Paragraph(footer_text, self.styles['Normal']))
        
        # Build PDF
        doc.build(story)
        return str(output_file)
    
    def generate_compliance_checklist_pdf(self) -> str:
        """Generate compliance checklist PDF"""
        output_file = self.output_dir / f"Compliance_Checklist_{datetime.now().strftime('%Y%m%d')}.pdf"
        
        doc = SimpleDocTemplate(
            str(output_file),
            pagesize=letter,
            rightMargin=0.75*inch,
            leftMargin=0.75*inch,
            topMargin=0.75*inch,
            bottomMargin=0.75*inch,
            title="Emergency Alert Compliance Checklist"
        )
        
        story = []
        
        # Title
        story.append(Paragraph("🚨 Emergency Alert Compliance Checklist", self.styles['CustomTitle']))
        story.append(Spacer(1, 0.3*inch))
        
        # Instructions
        story.append(Paragraph("Before Sending Any Alert - Verify All Items Below", self.styles['CustomHeading2']))
        story.append(Spacer(1, 0.2*inch))
        
        # FEMA Section
        story.append(Paragraph("FEMA Requirements - All 5 Elements Present?", self.styles['CustomHeading2']))
        fema_checklist = [
            "☐ SOURCE: Message identifies the issuing agency/official",
            "☐ HAZARD: Message describes the emergency clearly",
            "☐ LOCATION: Message specifies the affected geographic area",
            "☐ TIME: Message includes when the alert ends or when update is expected",
            "☐ INSTRUCTION: Message provides clear, actionable steps for the public"
        ]
        
        for item in fema_checklist:
            story.append(Paragraph(item, self.styles['CustomBody']))
        story.append(Spacer(1, 0.2*inch))
        
        # WEA Requirements
        story.append(Paragraph("WEA Compliance - Character Limits?", self.styles['CustomHeading2']))
        story.append(Paragraph("☐ Message is ≤ 90 characters (SMS recommended)", self.styles['CustomBody']))
        story.append(Paragraph("☐ Message is ≤ 360 characters maximum (required)", self.styles['CustomBody']))
        story.append(Spacer(1, 0.2*inch))
        
        # Readability
        story.append(Paragraph("Readability - 6th Grade Level?", self.styles['CustomHeading2']))
        story.append(Paragraph("☐ Average sentence length < 15 words", self.styles['CustomBody']))
        story.append(Paragraph("☐ No words with more than 3 syllables (unless necessary)", self.styles['CustomBody']))
        story.append(Paragraph("☐ Use active voice (move TO shelter vs. shelter should be moved TO)", self.styles['CustomBody']))
        story.append(Spacer(1, 0.2*inch))
        
        # Clarity
        story.append(Paragraph("Clarity - No Ambiguous Language?", self.styles['CustomHeading2']))
        story.append(Paragraph("☐ Avoid vague terms ('soon', 'immediately', 'be careful')", self.styles['CustomBody']))
        story.append(Paragraph("☐ No contradictory statements", self.styles['CustomBody']))
        story.append(Paragraph("☐ Instructions are specific and actionable", self.styles['CustomBody']))
        story.append(Spacer(1, 0.2*inch))
        
        # System Verification
        story.append(Paragraph("System Score Verification", self.styles['CustomHeading2']))
        story.append(Paragraph("☐ FEMA Score: 100% (all 5 elements present)", self.styles['CustomBody']))
        story.append(Paragraph("☐ WEA Score: 100% (within character limits)", self.styles['CustomBody']))
        story.append(Paragraph("☐ Readability Score: ≥ 80 (grade level 6 or better)", self.styles['CustomBody']))
        story.append(Paragraph("☐ Clarity Score: ≥ 80 (low confusion risk)", self.styles['CustomBody']))
        story.append(Paragraph("☐ <b>Overall Score: ≥ 80 (GREEN - READY TO SEND)</b>", self.styles['CustomBody']))
        story.append(Spacer(1, 0.2*inch))
        
        # Authority
        story.append(Paragraph("Authority & Approval", self.styles['CustomHeading2']))
        story.append(Paragraph("☐ Message authorized by agency decision-maker", self.styles['CustomBody']))
        story.append(Paragraph("☐ Message routing is appropriate", self.styles['CustomBody']))
        story.append(Paragraph("☐ Recipients list is complete and accurate", self.styles['CustomBody']))
        
        doc.build(story)
        return str(output_file)
    
    def generate_all_pdfs(self) -> dict:
        """Generate all available PDFs"""
        results = {}
        try:
            results['functional_guide'] = self.generate_functional_guide_pdf()
            print(f"✓ Functional Guide PDF generated: {results['functional_guide']}")
        except Exception as e:
            results['functional_guide_error'] = str(e)
            print(f"✗ Error generating Functional Guide: {e}")
        
        try:
            results['compliance_checklist'] = self.generate_compliance_checklist_pdf()
            print(f"✓ Compliance Checklist PDF generated: {results['compliance_checklist']}")
        except Exception as e:
            results['compliance_checklist_error'] = str(e)
            print(f"✗ Error generating Compliance Checklist: {e}")
        
        return results


def main():
    """Generate all PDFs"""
    print("\n" + "="*70)
    print("Emergency Alert Safety Checker - PDF Generator")
    print("="*70 + "\n")
    
    generator = PDFGenerator(output_dir="pdf_exports")
    results = generator.generate_all_pdfs()
    
    print("\n" + "="*70)
    print("PDF Generation Summary")
    print("="*70)
    
    successful = {k: v for k, v in results.items() if not k.endswith('_error')}
    errors = {k: v for k, v in results.items() if k.endswith('_error')}
    
    print(f"\n✓ Successfully generated {len(successful)} PDF(s)")
    print(f"✗ Failed to generate {len(errors)} PDF(s)")
    
    if successful:
        print("\nGenerated Documents:")
        for doc_type, filepath in successful.items():
            print(f"  • {doc_type}: {filepath}")
    
    if errors:
        print("\nErrors:")
        for error_type, error_msg in errors.items():
            print(f"  • {error_type}: {error_msg}")
    
    print(f"\nAll PDFs saved to: {Path('pdf_exports').resolve()}\n")


if __name__ == "__main__":
    main()
