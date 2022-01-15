from django.contrib import admin
from django.http import FileResponse

from encuestas.forms import EncuestaForm
from encuestas.models import Encuesta, InteresPersonal


@admin.action(description='Exportar a PDF la(s) encuesta(s) seleccionada(s)')
def exportar_to_pdf(modeladmin, request, queryset):
    from fpdf import FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    # Crear título con bordes y centrado. Luego salta a la siguiente línea.
    pdf.cell(0, 10, 'Encuestas', border=1, align='C')
    pdf.ln(20)
    pdf.set_font('Arial', '', 12)

    for encuesta in queryset:
        pdf.cell(0, 10, 'Nombre: %s' % encuesta.nombre, ln=1)
        pdf.cell(25, 10, 'Edad: %d' % encuesta.edad)
        pdf.cell(35, 10, 'Peso: %.2f Kg' % encuesta.peso_corporal)
        pdf.cell(35, 10, 'Sexo: %s' % encuesta.get_sexo_display())
        pdf.cell(80, 10, 'Grado de escolaridad: %s' % encuesta.get_grado_de_escolaridad_display(), ln=1)
        pdf.cell(0, 10, 'Intereses personales:', ln=1)
        for interes in encuesta.intereses_personales.all():
            width = pdf.get_string_width(interes.value) + 5
            pdf.cell(width, 10, interes.value, border=1, align='C')
        pdf.ln(20)
        pdf.dashed_line(pdf.get_x(), pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
        pdf.ln(10)

    filename = 'Listado de Encuestas.pdf'
    pdf.output(filename, dest='F')
    return FileResponse(open(filename, 'rb'), as_attachment=True, filename=filename)


# Register your models here.
@admin.register(Encuesta)
class EncuestaAdmin(admin.ModelAdmin):
    form = EncuestaForm
    list_display = ('nombre', 'edad', 'sexo')
    list_filter = ('grado_de_escolaridad', 'sexo')
    search_fields = ['nombre']
    actions = [exportar_to_pdf]


admin.site.register(InteresPersonal)
