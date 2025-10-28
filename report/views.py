from django.shortcuts import render
import os
from datetime import datetime
from django.conf import settings
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from cart.models import Purchase
from report.models import Report
from django.http import FileResponse, Http404
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader

def generate_daily_purchase_report(request):
    today = datetime.now().date()
    purchases = Purchase.objects.filter(timestamp__date=today)

    if not purchases.exists():
        return HttpResponse("No purchases found today.")

    # File path
    filename = f"purchase_report_{today}.pdf"
    report_dir = os.path.join(settings.MEDIA_ROOT, 'reports')
    os.makedirs(report_dir, exist_ok=True)
    filepath = os.path.join(report_dir, filename)

    # Set up PDF
    c = canvas.Canvas(filepath, pagesize=A4)
    width, height = A4

    # Add logo
    logo_path = os.path.join(settings.BASE_DIR, 'static', 'img', 'logo.png')
    if os.path.exists(logo_path):
        logo = ImageReader(logo_path)
        c.drawImage(logo, 40, height - 80, width=60, height=60, mask='auto')

    # Header
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width / 2, height - 50, "Daily Purchase Report")
    c.setFont("Helvetica", 12)
    c.drawCentredString(width / 2, height - 70, f"Date: {today.strftime('%Y-%m-%d')}")

    # Table headers
    y = height - 110
    row_height = 20
    headers = ["Time", "Customer", "Product", "Quantity", "Total (₹)"]
    x_positions = [50, 130, 250, 370, 450]

    c.setFont("Helvetica-Bold", 12)
    for i, header in enumerate(headers):
        c.drawString(x_positions[i], y, header)

    c.setFont("Helvetica", 11)
    y -= row_height
    total_amount = 0

    for p in purchases:
        data = [
            p.timestamp.strftime("%H:%M") if p.timestamp else "N/A",
            p.customer.name if p.customer else "N/A",
            p.food.name if p.food else "N/A",
            str(p.quantity),
            f"{p.total_amount}"
        ]

        for i, item in enumerate(data):
            c.drawString(x_positions[i], y, item)

        total_amount += float(p.total_amount)
        y -= row_height

        # Page break
        if y < 100:
            c.showPage()
            y = height - 100
            for i, header in enumerate(headers):
                c.drawString(x_positions[i], y, header)
            y -= row_height

    # Total
    c.setFont("Helvetica-Bold", 12)
    c.drawString(370, y - 10, "Total:")
    c.drawString(450, y - 10, f"₹{total_amount}")
    c.save()

    # Save to Report model
    Report.objects.update_or_create(
        date=today,
        defaults={
            'time': datetime.now().time(),
            'report': f"reports/{filename}",
            'status': 'generated'
        }
    )

    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def download_report(request, rid):
    try:
        report = Report.objects.get(r_id=rid)
        file_path = os.path.join(settings.MEDIA_ROOT, str(report.report))
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
    except (Report.DoesNotExist, FileNotFoundError):
        raise Http404("Report not found")

def manage_report(request):
    obj = Report.objects.filter(status='generated')
    context = {
        'obj': obj
    }
    return render(request,'report/manage_report.html',context)

def aprv(request,idd):
    obj=Report.objects.get(r_id=idd)
    obj.status='approved'
    obj.save()
    return manage_report(request)

def rjct(request,idd):
    obj=Report.objects.get(r_id=idd)
    obj.status='rejected'
    obj.save()
    return manage_report(request)

def view_report(request):
    selected_date = request.GET.get('date')  # from query param
    if selected_date:
        obj = Report.objects.filter(status='generated', date=selected_date)
    else:
        obj = Report.objects.filter(status='generated')

    context = {
        'obj': obj,
        'selected_date': selected_date
    }
    return render(request, 'report/view_report.html', context)