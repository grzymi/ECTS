# -*- coding: utf-8 -*-
from fpdf import FPDF, HTMLMixin

pdf = FPDF(format='A4')
pdf.set_margins(left=20, top=15, right=20)
pdf.add_page(orientation='P')
pdf.set_font('Arial', size=10)
pdf.cell(85, 5, txt='Politechnika Poznanska', align='L')
pdf.cell(85, 5, txt='ECTS', align='R', ln=1)
#pdf.ln(4)
pdf.set_font('Arial', size=10, style='B')
pdf.cell(170, 5, txt='Wydzial Inzynierii Srodowiska i Energetyki', align='L', ln=1)
pdf.cell(170, 7, border=1, txt='KARTA OPISU MODULU KSZTALCENIA', align='C', ln=1)
pdf.set_font('Arial', size=8)
pdf.cell(100, 6, border='L', txt=u'Nazwa modułu/przedmiotu', align='L')
pdf.cell(70, 6, border='L,R', txt='kod', align='L', ln=1)
pdf.set_font('Arial', size=10, style='B')
pdf.cell(100, 6, border='L', txt='Biogazownie i termiczne przetwarzanie biomasy', align='L')
pdf.cell(70, 6, border='L,R', txt='', align='L', ln=1)
pdf.output('test.pdf')







'''
spacing = 1

data = [['First Name', 'Last Name', 'email', 'zip'],
		['Mike', 'Driscoll', 'mike@somewhere.com', '55555'],
		['John', 'Doe', 'jdoe@doe.com', '12345'],
		['Nina', 'Ma', 'inane@where.com', '54321']
		]

pdf = FPDF()
pdf.set_font("Arial", size=12)
pdf.add_page()

col_width = pdf.w / 4.5
row_height = pdf.font_size
for row in data:
	for item in row:
		pdf.cell(col_width, row_height*spacing,
				 txt=item, border=1)
	pdf.ln(row_height*spacing)

pdf.output('simple_table.pdf')
'''
