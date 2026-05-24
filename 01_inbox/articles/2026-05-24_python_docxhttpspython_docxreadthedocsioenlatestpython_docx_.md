---
title: python-docx[¶](https://python-docx.readthedocs.io/en/latest/#python-docx "Permalink to this headline")
created: 2026-05-24
updated: 2026-05-24
tags: ["auto-capture", auto-compiled]
status: compiled
sources: [https://python-docx.readthedocs.io/en/latest/]
source_url: https://python-docx.readthedocs.io/en/latest/
---

# python-docx[¶](https://python-docx.readthedocs.io/en/latest/#python-docx "Permalink to this headline")

> 自动抓取自: [https://python-docx.readthedocs.io/en/latest/](https://python-docx.readthedocs.io/en/latest/)

### Navigation
  * [index](https://python-docx.readthedocs.io/en/latest/genindex.html "General Index")
  * [next](https://python-docx.readthedocs.io/en/latest/user/install.html "Installing") |
  * [python-docx 1.2.0 documentation](https://python-docx.readthedocs.io/en/latest/) »


# python-docx[¶](https://python-docx.readthedocs.io/en/latest/#python-docx "Permalink to this headline")
Release v1.2.0 ([Installation](https://python-docx.readthedocs.io/en/latest/user/install.html#install))
_python-docx_ is a Python library for creating and updating Microsoft Word (.docx) files.
## What it can do[¶](https://python-docx.readthedocs.io/en/latest/#what-it-can-do "Permalink to this headline")
Here’s an example of what `python-docx` can do:  
| ![img](https://python-docx.readthedocs.io/en/latest/_images/example-docx-01.png)  |  
```
from docx import Document
from docx.shared import Inches

document = Document()

document.add_heading('Document Title', 0)

p = document.add_paragraph('A plain paragraph having some ')
p.add_run('bold').bold = True
p.add_run(' and some ')
p.add_run('italic.').italic = True

document.add_heading('Heading, level 1', level=1)
document.add_paragraph('Intense quote', style='Intense Quote')

document.add_paragraph(
    'first item in unordered list', style='List Bullet'
)
document.add_paragraph(
    'first item in ordered list', style='List Number'
)

document.add_picture('monty-truth.png', width=Inches(1.25))

records = (
    (3, '101', 'Spam'),
    (7, '422', 'Eggs'),
    (4, '631', 'Spam, spam, eggs, and spam')
)

table = document.add_table(rows=1, cols=3)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Qty'
hdr_cells[1].text = 'Id'
hdr_cells[2].text = 'Desc'
for qty, id, desc in records:
    row_cells = table.add_row().cells
    row_cells[0].text = str(qty)
    row_cells[1].text = id
    row_cells[2].text = desc

document.add_page_break()

document.save('demo.docx')

```
 |  
| --- | --- |  
## User Guide[¶](https://python-docx.readthedocs.io/en/latest/#user-guide "Permalink to this headline")
  * [Installing](https://python-docx.readthedocs.io/en/latest/user/install.html)
  * [Quickstart](https://python-docx.readthedocs.io/en/latest/user/quickstart.html)
  * [Working with Documents](https://python-docx.readthedocs.io/en/latest/user/documents.html)
  * [Working with Tables](https://python-docx.readthedocs.io/en/latest/user/tables.html)
  * [Working with Text](https://python-docx.readthedocs.io/en/latest/user/text.html)
  * [Working with Sections](https://python-docx.readthedocs.io/en/latest/user/sections.html)
  * [Working with Headers and Footers](https://python-docx.readthedocs.io/en/latest/user/hdrftr.html)
  * [API basics](https://python-docx.readthedocs.io/en/latest/user/api-concepts.html)
  * [Understanding Styles](https://python-docx.readthedocs.io/en/latest/user/styles-understanding.html)
  * [Working with Styles](https://python-docx.readthedocs.io/en/latest/user/styles-using.html)
  * [Working with Comments](https://python-docx.readthedocs.io/en/latest/user/comments.html)
  * [Understanding pictures and other shapes](https://python-docx.readthedocs.io/en/latest/user/shapes.html)


## API Documentation[¶](https://python-docx.readthedocs.io/en/latest/#api-documentation "Permalink to this headline")
  * [Document objects](https://python-docx.readthedocs.io/en/latest/api/document.html)
    * [`Document` constructor](https://python-docx.readthedocs.io/en/latest/api/document.html#document-constructor)
    * [`Document` objects](https://python-docx.readthedocs.io/en/latest/api/document.html#id1)
    * [`CoreProperties` objects](https://python-docx.readthedocs.io/en/latest/api/document.html#coreproperties-objects)
  * [Document `Settings` objects](https://python-docx.readthedocs.io/en/latest/api/settings.html)
  * [Style-related objects](https://python-docx.readthedocs.io/en/latest/api/style.html)
    * [`Styles` objects](https://python-docx.readthedocs.io/en/latest/api/style.html#styles-objects)
    * [`BaseStyle` objects](https://python-docx.readthedocs.io/en/latest/api/style.html#basestyle-objects)
    * [`CharacterStyle` objects](https://python-docx.readthedocs.io/en/latest/api/style.html#characterstyle-objects)
    * [`ParagraphStyle` objects](https://python-docx.readthedocs.io/en/latest/api/style.html#paragraphstyle-objects)
    * [`_TableStyle` objects](https://python-docx.readthedocs.io/en/latest/api/style.html#tablestyle-objects)
    * [`_NumberingStyle` objects](https://python-docx.readthedocs.io/en/latest/api/style.html#numberingstyle-objects)
    * [`LatentStyles` objects](https://python-docx.readthedocs.io/en/latest/api/style.html#latentstyles-objects)
    * [`_LatentStyle` objects](https://python-docx.readthedocs.io/en/latest/api/style.html#latentstyle-objects)
  * [Text-related objects](https://python-docx.readthedocs.io/en/latest/api/text.html)
    * [`Paragraph` objects](https://python-docx.readthedocs.io/en/latest/api/text.html#paragraph-objects)
    * [`ParagraphFormat` objects](https://python-docx.readthedocs.io/en/latest/api/text.html#paragraphformat-objects)
    * [`Hyperlink` objects](https://python-docx.readthedocs.io/en/latest/api/text.html#hyperlink-objects)
    * [`Run` objects](https://python-docx.readthedocs.io/en/latest/api/text.html#run-objects)
    * [`Font` objects](https://python-docx.readthedocs.io/en/latest/api/text.html#font-objects)
    * [`RenderedPageBreak` objects](https://python-docx.readthedocs.io/en/latest/api/text.html#renderedpagebreak-objects)
    * [`TabStop` objects](https://python-docx.readthedocs.io/en/latest/api/text.html#tabstop-objects)
    * [`TabStops` objects](https://python-docx.readthedocs.io/en/latest/api/text.html#tabstops-objects)
  * [Table objects](https://python-docx.readthedocs.io/en/latest/api/table.html)
    * [`Table` objects](https://python-docx.readthedocs.io/en/latest/api/table.html#id1)
    * [`_Cell` objects](https://python-docx.readthedocs.io/en/latest/api/table.html#cell-objects)
    * [`_Row` objects](https://python-docx.readthedocs.io/en/latest/api/table.html#row-objects)
    * [`_Column` objects](https://python-docx.readthedocs.io/en/latest/api/table.html#column-objects)
    * [`_Rows` objects](https://python-docx.readthedocs.io/en/latest/api/table.html#rows-objects)
    * [`_Columns` objects](https://python-docx.readthedocs.io/en/latest/api/table.html#columns-objects)
  * [Section objects](https://python-docx.readthedocs.io/en/latest/api/section.html)
    * [`Sections` objects](https://python-docx.readthedocs.io/en/latest/api/section.html#sections-objects)
    * [`Section` objects](https://python-docx.readthedocs.io/en/latest/api/section.html#id1)
    * [`_Header` and `_Footer` objects](https://python-docx.readthedocs.io/en/latest/api/section.html#header-and-footer-objects)
  * [Comment-related objects](https://python-docx.readthedocs.io/en/latest/api/comments.html)
    * [`Comments` objects](https://python-docx.readthedocs.io/en/latest/api/comments.html#comments-objects)
    * [`Comment` objects](https://python-docx.readthedocs.io/en/latest/api/comments.html#comment-objects)
  * [Shape-related objects](https://python-docx.readthedocs.io/en/latest/api/shape.html)
    * [`InlineShapes` objects](https://python-docx.readthedocs.io/en/latest/api/shape.html#inlineshapes-objects)
    * [`InlineShape` objects](https://python-docx.readthedocs.io/en/latest/api/shape.html#inlineshape-objects)
  * [DrawingML objects](https://python-docx.readthedocs.io/en/latest/api/dml.html)
    * [`ColorFormat` objects](https://python-docx.readthedocs.io/en/latest/api/dml.html#colorformat-objects)
  * [Shared classes](https://python-docx.readthedocs.io/en/latest/api/shared.html)
    * [Length objects](https://python-docx.readthedocs.io/en/latest/api/shared.html#length-objects)
    * [`RGBColor` objects](https://python-docx.readthedocs.io/en/latest/api/shared.html#rgbcolor-objects)
  * [Enumerations](https://python-docx.readthedocs.io/en/latest/api/enum/index.html)
    * [`MSO_COLOR_TYPE`](https://python-docx.readthedocs.io/en/latest/api/enum/MsoColorType.html)
    * [`MSO_THEME_COLOR_INDEX`](https://python-docx.readthedocs.io/en/latest/api/enum/MsoThemeColorIndex.html)
    * [`WD_PARAGRAPH_ALIGNMENT`](https://python-docx.readthedocs.io/en/latest/api/enum/WdAlignParagraph.html)
    * [`WD_BUILTIN_STYLE`](https://python-docx.readthedocs.io/en/latest/api/enum/WdBuiltinStyle.html)
    * [`WD_CELL_VERTICAL_ALIGNMENT`](https://python-docx.readthedocs.io/en/latest/api/enum/WdCellVerticalAlignment.html)
    * [`WD_COLOR_INDEX`](https://python-docx.readthedocs.io/en/latest/api/enum/WdColorIndex.html)
    * [`WD_LINE_SPACING`](https://python-docx.readthedocs.io/en/latest/api/enum/WdLineSpacing.html)
    * [`WD_ORIENTATION`](https://python-docx.readthedocs.io/en/latest/api/enum/WdOrientation.html)
    * [`WD_TABLE_ALIGNMENT`](https://python-docx.readthedocs.io/en/latest/api/enum/WdRowAlignment.html)
    * [`WD_ROW_HEIGHT_RULE`](https://python-docx.readthedocs.io/en/latest/api/enum/WdRowHeightRule.html)
    * [`WD_SECTION_START`](https://python-docx.readthedocs.io/en/latest/api/enum/WdSectionStart.html)
    * [`WD_STYLE_TYPE`](https://python-docx.readthedocs.io/en/latest/api/enum/WdStyleType.html)
    * [`WD_TAB_ALIGNMENT`](https://python-docx.readthedocs.io/en/latest/api/enum/WdTabAlignment.html)
    * [`WD_TAB_LEADER`](https://python-docx.readthedocs.io/en/latest/api/enum/WdTabLeader.html)
    * [`WD_TABLE_DIRECTION`](https://python-docx.readthedocs.io/en/latest/api/enum/WdTableDirection.html)
    * [`WD_UNDERLINE`](https://python-docx.readthedocs.io/en/latest/api/enum/WdUnderline.html)


## Contributor Guide[¶](https://python-docx.readthedocs.io/en/latest/#contributor-guide "Permalink to this headline")
  * [Analysis](https://python-docx.readthedocs.io/en/latest/dev/analysis/index.html)


### [Table of Contents](https://python-docx.readthedocs.io/en/latest/)
  * [python-docx](https://python-docx.readthedocs.io/en/latest/)
    * [What it can do](https://python-docx.readthedocs.io/en/latest/#what-it-can-do)
    * [User Guide](https://python-docx.readthedocs.io/en/latest/#user-guide)
    * [API Documentation](https://python-docx.readthedocs.io/en/latest/#api-documentation)
    * [Contributor Guide](https://python-docx.readthedocs.io/en/latest/#contributor-guide)


#### Next topic
[Installing](https://python-docx.readthedocs.io/en/latest/user/install.html "next chapter")
### Useful Links
  * [python-docx @ GitHub](http://github.com/python-openxml/python-docx)
  * [python-docx @ PyPI](http://pypi.python.org/pypi/python-docx)
  * [Issue Tracker](http://github.com/python-openxml/python-docx/issues)


### Quick search
### Navigation
  * [index](https://python-docx.readthedocs.io/en/latest/genindex.html "General Index")
  * [next](https://python-docx.readthedocs.io/en/latest/user/install.html "Installing") |
  * [python-docx 1.2.0 documentation](https://python-docx.readthedocs.io/en/latest/) »


© Copyright 2013, Steve Canny. Created using [Sphinx](http://sphinx.pocoo.org/) 1.8.6.   
Theme based on [Read The Docs](http://readthedocs.org/)
