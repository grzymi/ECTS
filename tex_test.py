from pylatex import Document, PageStyle, Head, MiniPage, Foot, LargeText, \
    MediumText, LineBreak, simple_page_number, StandAloneGraphic, Command
from pylatex.utils import bold, NoEscape


def generate_header():
    geometry_options = {"margin": "25mm", 'head':'25mm'}
    doc = Document(geometry_options=geometry_options)
    doc.preamble.append(Command('usepackage', 'Calibri'))
    # Add document header
    header = PageStyle("header")
    logo_image = "./logo/logo_ECTS.jpg"
    with header.create(Head("C")):
        header.append(StandAloneGraphic(filename=logo_image, image_options='width=170mm'))
    # Create right footer
    with header.create(Foot("R")):
        header.append("Right Footer")

    doc.preamble.append(header)
    doc.change_document_style("header")

    # Add Heading
    with doc.create(MiniPage(align='l')):
        doc.append(LargeText(bold("KARTA OPISU MODUŁU KSZTAŁCENIA")))
        doc.append(LineBreak())
        doc.append(MediumText("Nazwa modułu/przedmiotu"))

    doc.generate_pdf("karta", clean_tex=False, compiler='lualatex')

generate_header()