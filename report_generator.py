# enhanced_report_generator.py
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, Flowable
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from datetime import datetime
import cv2
import os

class HeaderFooter(Flowable):
    def __init__(self, page_type="header"):
        Flowable.__init__(self)
        self.page_type = page_type

    def draw(self):
        canvas = self.canv
        if self.page_type == "header":
            canvas.setFont('Helvetica-Bold', 10)
            canvas.setFillColor(colors.HexColor('#2E86C1'))
            canvas.drawString(0, 10, "🔐 Media search HUB")
            canvas.line(0, 0, 540, 0)
        else:
            canvas.setFont('Helvetica', 8)
            canvas.setFillColor(colors.grey)
            canvas.line(0, 10, 540, 10)
            canvas.drawRightString(540, 0, f"Page {canvas.getPageNumber()}")

class ReportGenerator:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self.setup_styles()

    def setup_styles(self):
        self.title_style = ParagraphStyle(
            'Title', fontSize=30, alignment=TA_CENTER,
            textColor=colors.HexColor('#34495E'), spaceAfter=20,
            fontName='Helvetica-Bold'
        )
        self.section_style = ParagraphStyle(
            'Section', fontSize=20, alignment=TA_LEFT,
            textColor=colors.HexColor('#2E86C1'), spaceBefore=30, spaceAfter=16,
            fontName='Helvetica-Bold'
        )
        self.body_style = ParagraphStyle(
            'Body', fontSize=11, leading=18, alignment=TA_LEFT,
            textColor=colors.HexColor('#2C3E50'), fontName='Helvetica'
        )

    def create_metadata_section(self, report_id):
        current_time = datetime.now()
        data = [
            ['📝 Report ID:', report_id],
            ['📅 Generated:', current_time.strftime("%Y-%m-%d %H:%M:%S")],
            ['⚠️ Priority:', 'HIGH'],
            ['📊 Type:', 'VIDEO SECURITY'],
        ]
        table = Table(data, colWidths=[2.5*inch, 4*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#F0F3F4')),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 0.25, colors.HexColor('#D5D8DC')),
        ]))
        return table

    def generate_report(self, report_id, report_text, output_filename="modern_report.pdf", video_path=None):
        doc = SimpleDocTemplate(output_filename, pagesize=A4,
                                leftMargin=1*inch, rightMargin=1*inch,
                                topMargin=1*inch, bottomMargin=1*inch)
        elements = [HeaderFooter("header"),
                    Paragraph("📄 Media Analysis Report", self.title_style),
                    Spacer(1, 12),
                    self.create_metadata_section(report_id),
                    Spacer(1, 20)]

        if video_path:
            try:
                cap = cv2.VideoCapture(video_path)
                ret, frame = cap.read()
                if ret:
                    thumbnail_path = "thumb.jpg"
                    cv2.imwrite(thumbnail_path, frame)
                    img = Image(thumbnail_path, width=5.5*inch, height=3.5*inch)
                    img.hAlign = 'CENTER'
                    elements += [img, Spacer(1, 12), Paragraph("🎥 Snapshot from Video", self.section_style)]
                    os.remove(thumbnail_path)
                cap.release()
            except Exception as e:
                print("Thumbnail error:", e)

        elements.append(Paragraph("🧠 Detailed Analysis", self.section_style))

        for para in report_text.strip().split('\n\n'):
            if para:
                elements.append(Paragraph(f"{para.strip()}", self.body_style))
                elements.append(Spacer(1, 10))

        elements.append(Spacer(1, 20))
        elements.append(HeaderFooter("footer"))

        doc.build(elements)
        return output_filename