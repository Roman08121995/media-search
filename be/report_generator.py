from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.units import inch, cm
from reportlab.platypus import Flowable, BaseDocTemplate, PageTemplate, Frame
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from datetime import datetime
from PIL import Image as PILImage
import cv2
import io
import os

class HeaderFooter(Flowable):
    def __init__(self, page_type="header"):
        Flowable.__init__(self)
        self.page_type = page_type

    def draw(self):
        canvas = self.canv
        if self.page_type == "header":
            canvas.setStrokeColor(colors.HexColor('#1B4F72'))
            canvas.setLineWidth(2)
            canvas.line(0, 0, 540, 0)

            canvas.setFillColor(colors.HexColor('#1B4F72'))
            canvas.rect(0, 5, 50, 20, fill=True)
            canvas.setFillColor(colors.white)
            canvas.setFont('Helvetica-Bold', 8)
            canvas.drawString(5, 10, "SECURE")
        else:
            canvas.setStrokeColor(colors.HexColor('#1B4F72'))
            canvas.setLineWidth(1)
            canvas.line(0, 10, 540, 10)

            canvas.setFont('Helvetica', 8)
            page_num = canvas.getPageNumber()
            canvas.drawRightString(540, 0, f"Page {page_num}")

class ReportGenerator:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self.setup_styles()

    def setup_styles(self):
        self.title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=28,
            spaceAfter=30,
            textColor=colors.HexColor('#1B4F72'),
            alignment=1,
            fontName='Helvetica-Bold'
        )

        self.section_style = ParagraphStyle(
            'SectionTitle',
            parent=self.styles['Heading2'],
            fontSize=18,
            textColor=colors.HexColor('#2874A6'),
            spaceBefore=20,
            spaceAfter=20,
            fontName='Helvetica-Bold',
            borderPadding=(10, 0, 10, 0),
            borderWidth=0,
            borderColor=colors.HexColor('#2874A6'),
            borderRadius=5
        )

        self.body_style = ParagraphStyle(
            'CustomBody',
            parent=self.styles['Normal'],
            fontSize=11,
            leading=16,
            textColor=colors.HexColor('#2C3E50'),
            fontName='Helvetica',
            alignment=TA_LEFT,
            spaceBefore=6,
            spaceAfter=6
        )

    def create_metadata_section(self, report_id):
 
        current_time = datetime.now()

        metadata = [
            ['REPORT DETAILS', ''],
            ['Report ID:', report_id],
            ['Generated Date:', current_time.strftime("%Y-%m-%d %H:%M:%S")],
            ['Priority Level:', 'HIGH'],
            ['Analysis Type:', 'VIDEO SECURITY'],
        ]

        table = Table(metadata, colWidths=[2.5*inch, 4*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1B4F72')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#F8F9F9')),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#BDC3C7')),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ]))

        return table

    def generate_report(self, report_id, report_text, output_filename="enhanced_security_report.pdf", video_path=None):
        
        doc = SimpleDocTemplate(
            output_filename,
            pagesize=A4,
            rightMargin=1*inch,
            leftMargin=1*inch,
            topMargin=1*inch,
            bottomMargin=1*inch
        )

        elements = []

        elements.append(HeaderFooter("header"))
        elements.append(Paragraph("SECURITY ANALYSIS REPORT", self.title_style))
        elements.append(Spacer(1, 20))
        elements.append(self.create_metadata_section(report_id))
        elements.append(Spacer(1, 20))

        if video_path:
            try:
                cap = cv2.VideoCapture(video_path)
                ret, frame = cap.read()
                if ret:
                    thumbnail_path = "temp_thumbnail.jpg"
                    cv2.imwrite(thumbnail_path, frame)

                    img = Image(thumbnail_path, width=6*inch, height=4*inch)
                    elements.append(img)
                    elements.append(Paragraph("Video Security Footage", self.section_style))

                    os.remove(thumbnail_path)
                cap.release()
            except Exception as e:
                print(f"Error processing video thumbnail: {e}")

        elements.append(Paragraph("DETAILED ANALYSIS", self.section_style))

        paragraphs = report_text.split('\n\n')
        for para in paragraphs:
            if para.strip():
                elements.append(Paragraph(para, self.body_style))

        elements.append(Spacer(1, 30))
        elements.append(HeaderFooter("footer"))

        doc.build(elements)

        return output_filename