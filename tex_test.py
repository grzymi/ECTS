from pylatex import Document, PageStyle, Head, MiniPage, Foot, LargeText, \
    MediumText, LineBreak, simple_page_number, StandAloneGraphic, Command, TextColor, Package, HugeText, TextBlock, FlushLeft, NewLine, VerticalSpace
from pylatex.utils import bold, NoEscape


def generate_header(przedmiot='Podaj nazwę przedmiotu'):
    geometry_options = {"margin": "25mm", 'head':'10mm', 'includeheadfoot':False}
    doc = Document(geometry_options=geometry_options, lmodern=False, page_numbers=True)
    doc.packages.append(Package('roboto', 'default'))
    doc.add_color('PPblue', 'HTML', '006991')
    #doc.packages.append(Package('roboto', 'sfdefault'))
    # Add document header
    header = PageStyle("header")
    logo_image = "./logo/logo_ECTS.jpg"
    with header.create(Head("C")):
        header.append(StandAloneGraphic(filename=logo_image, image_options='width=17.07cm'))
    # Create right footer
    with header.create(Foot("R")):
        header.append("Right Footer")

    doc.preamble.append(header)
    doc.change_document_style("header")

    # Add Heading
    with doc.create(FlushLeft()):#align='l')):
        doc.append(VerticalSpace('20pt'))
        #doc.append(TextColor('white', LargeText(bold(" ")))) #Nie wiem, jak przesunąć tekst w dół
        #doc.append('\n')
        doc.append(LargeText("KARTA OPISU MODUŁU KSZTAŁCENIA"))
        doc.append(LineBreak())
        doc.append(LineBreak())
        doc.append(MediumText("Nazwa modułu/przedmiotu"))
        doc.append(LineBreak())
        doc.append(LargeText(przedmiot))
        doc.append(NewLine())
        doc.append(TextColor('PPblue', NoEscape(r"\noindent\rule{\textwidth}{1pt}")))
        doc.append(NewLine())
        doc.append(MediumText(TextColor('PPblue', bold('Przedmiot'))))

    # Dodanie opisu studiów
    with doc.create(MiniPage(width=r'0.6\textwidth')):
        doc.append(MediumText(TextColor('gray', 'Kierunek studiów')))
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText('Energetyka Cieplna i Przemysłowa'))
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText(TextColor('gray', 'Forma studiów')))
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText('Stacjonarne/Niestacjonarne'))	#wybierane z listy rozwijanej lub ustawiona stała wartość dla wersji studiów
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText(TextColor('gray', 'Profil studiów')))
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText('Ogólnoakademicki/Praktyczny'))	#wybierane z listy rozwijanej lub ustawiona stała wartość dla wersji studiów
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText(TextColor('gray', 'Język studiów')))
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText('polski'))
        #doc.append(LineBreak())
        #doc.append(VerticalSpace('20pt'))

    with doc.create(MiniPage(width=r'0.6\textwidth')):
        doc.append(MediumText(TextColor('gray', 'Studia w zakresie')))
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText('Chyba trzeba podać specjalność'))
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText(TextColor('gray', 'Poziom studiów')))
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText('I lub II stopień'))	#wybierane z listy rozwijanej lub ustawiona stała wartość dla wersji studiów
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText(TextColor('gray', 'Rok/semestr')))
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText('Podać rok i semesrt, z siatki'))	#wybierane z listy rozwijanej lub ustawiona stała wartość dla wersji studiów
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText(TextColor('gray', 'Wymagalność')))
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText('obligatoryjny/obieralny'))
        doc.append('\n')

    with doc.create(FlushLeft()):
        doc.append(TextColor('PPblue', NoEscape(r"\noindent\rule{\textwidth}{1pt}")))
        doc.append('\n')
        doc.append(VerticalSpace('15pt'))
        doc.append(MediumText(TextColor('PPblue', bold('Liczba godzin'))))
        #doc.append(VerticalSpace('5pt'))

    with doc.create(MiniPage(width=r'0.6\textwidth')):
        doc.append(MediumText(TextColor('gray', 'Wykład')))
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText('Wartość z siatki'))
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText(TextColor('gray', 'Ćwiczenia')))
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText('Wartość z siatki'))
        doc.append('\n')

    with doc.create(MiniPage(width=r'0.6\textwidth')):
        doc.append(MediumText(TextColor('gray', 'Laboratoria')))
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText('Wartość z siatki'))
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText(TextColor('gray', 'Projekty/seminaria')))
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText('Wartość z siatki'))
        doc.append('\n')

    with doc.create(FlushLeft()):
        #doc.append(VerticalSpace('5pt'))
        doc.append(MediumText(TextColor('gray', 'Inne (np. online)')))
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText('Wartość z siatki, trzeba dodać dodatkową opcję'))
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText(TextColor('PPblue', bold('Liczba punktów'))))
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(MediumText('Wartość z siatki'))
        doc.append('\n')
        doc.append(VerticalSpace('5pt'))
        doc.append(TextColor('PPblue', NoEscape(r"\noindent\rule{\textwidth}{1pt}")))



    doc.generate_pdf("karta", clean_tex=False, compiler='pdflatex')

generate_header(przedmiot='Programowanie')
