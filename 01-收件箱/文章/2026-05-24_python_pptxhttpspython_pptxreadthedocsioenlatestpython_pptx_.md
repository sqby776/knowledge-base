---
title: python-pptx[¶](https://python-pptx.readthedocs.io/en/latest/#python-pptx "Permalink to this headline")
created: 2026-05-24
updated: 2026-05-24
tags: ["auto-capture", auto-compiled]
status: compiled
sources: [https://python-pptx.readthedocs.io/en/latest/]
source_url: https://python-pptx.readthedocs.io/en/latest/
---

# python-pptx[¶](https://python-pptx.readthedocs.io/en/latest/#python-pptx "Permalink to this headline")

> 自动抓取自: [https://python-pptx.readthedocs.io/en/latest/](https://python-pptx.readthedocs.io/en/latest/)

### Navigation
  * [index](https://python-pptx.readthedocs.io/en/latest/genindex.html "General Index")
  * [modules](https://python-pptx.readthedocs.io/en/latest/py-modindex.html "Python Module Index") |
  * [next](https://python-pptx.readthedocs.io/en/latest/user/intro.html "Introduction") |
  * [python-pptx 1.0.0 documentation](https://python-pptx.readthedocs.io/en/latest/) »


# python-pptx[¶](https://python-pptx.readthedocs.io/en/latest/#python-pptx "Permalink to this headline")
Release v1.0.0 ([Installation](https://python-pptx.readthedocs.io/en/latest/user/install.html#install))
_python-pptx_ is a Python library for creating, reading, and updating PowerPoint (.pptx) files.
A typical use would be generating a PowerPoint presentation from dynamic content such as a database query, analytics output, or a JSON payload, perhaps in response to an HTTP request and downloading the generated PPTX file in response. It runs on any Python capable platform, including macOS and Linux, and does not require the PowerPoint application to be installed or licensed.
It can also be used to analyze PowerPoint files from a corpus, perhaps to extract search indexing text and images.
In can also be used to simply automate the production of a slide or two that would be tedious to get right by hand, which is how this all got started.
More information is available in the [python-pptx documentation](https://python-pptx.readthedocs.org/en/latest/).
Browse [examples with screenshots](https://python-pptx.readthedocs.org/en/latest/user/quickstart.html) to get a quick idea what you can do with python-pptx.
## Philosophy[¶](https://python-pptx.readthedocs.io/en/latest/#philosophy "Permalink to this headline")
python-pptx aims to broadly support the PowerPoint format (PPTX, PowerPoint 2007 and later), but its primary commitment is to be _industrial-grade_ , that is, suitable for use in a commercial setting. Maintaining this robustness requires a high engineering standard which includes a comprehensive two-level (e2e + unit) testing regimen. This discipline comes at a cost in development effort/time, but we consider reliability to be an essential requirement.
## Feature Support[¶](https://python-pptx.readthedocs.io/en/latest/#feature-support "Permalink to this headline")
python-pptx has the following capabilities:
  * Round-trip any Open XML presentation (.pptx file) including all its elements
  * Add slides
  * Populate text placeholders, for example to create a bullet slide
  * Add image to slide at arbitrary position and size
  * Add textbox to a slide; manipulate text font size and bold
  * Add table to a slide
  * Add auto shapes (e.g. polygons, flowchart shapes, etc.) to a slide
  * Add and manipulate column, bar, line, and pie charts
  * Access and change core document properties such as title and subject
  * And many others …


Even with all python-pptx does, the PowerPoint document format is very rich and there are still features python-pptx does not support.
## New features/releases[¶](https://python-pptx.readthedocs.io/en/latest/#new-features-releases "Permalink to this headline")
New features are generally added via sponsorship. If there’s a new feature you need for your use case, feel free to reach out at the email address on the github.com/scanny profile page. Many of the most used features such as charts were added this way.
## User Guide[¶](https://python-pptx.readthedocs.io/en/latest/#user-guide "Permalink to this headline")
  * [Introduction](https://python-pptx.readthedocs.io/en/latest/user/intro.html)
  * [Installing](https://python-pptx.readthedocs.io/en/latest/user/install.html)
  * [Getting Started](https://python-pptx.readthedocs.io/en/latest/user/quickstart.html)
  * [Working with Presentations](https://python-pptx.readthedocs.io/en/latest/user/presentations.html)
  * [Working with Slides](https://python-pptx.readthedocs.io/en/latest/user/slides.html)
  * [Understanding Shapes](https://python-pptx.readthedocs.io/en/latest/user/understanding-shapes.html)
  * [Working with AutoShapes](https://python-pptx.readthedocs.io/en/latest/user/autoshapes.html)
  * [Understanding placeholders](https://python-pptx.readthedocs.io/en/latest/user/placeholders-understanding.html)
  * [Working with placeholders](https://python-pptx.readthedocs.io/en/latest/user/placeholders-using.html)
  * [Working with text](https://python-pptx.readthedocs.io/en/latest/user/text.html)
  * [Working with charts](https://python-pptx.readthedocs.io/en/latest/user/charts.html)
  * [Working with tables](https://python-pptx.readthedocs.io/en/latest/user/table.html)
  * [Working with Notes Slides](https://python-pptx.readthedocs.io/en/latest/user/notes.html)
  * [Use cases](https://python-pptx.readthedocs.io/en/latest/user/use-cases.html)
  * [Concepts](https://python-pptx.readthedocs.io/en/latest/user/concepts.html)


## Community Guide[¶](https://python-pptx.readthedocs.io/en/latest/#community-guide "Permalink to this headline")
  * [Frequently Asked Questions](https://python-pptx.readthedocs.io/en/latest/community/faq.html)
  * [Support](https://python-pptx.readthedocs.io/en/latest/community/support.html)
  * [Software Updates](https://python-pptx.readthedocs.io/en/latest/community/updates.html)


## API Documentation[¶](https://python-pptx.readthedocs.io/en/latest/#api-documentation "Permalink to this headline")
  * [Presentations](https://python-pptx.readthedocs.io/en/latest/api/presentation.html)
    * [`Presentation` function](https://python-pptx.readthedocs.io/en/latest/api/presentation.html#presentation-function)
    * [`Presentation` objects](https://python-pptx.readthedocs.io/en/latest/api/presentation.html#presentation-objects)
    * [`CoreProperties` objects](https://python-pptx.readthedocs.io/en/latest/api/presentation.html#coreproperties-objects)
  * [Slides](https://python-pptx.readthedocs.io/en/latest/api/slides.html)
    * [`Slides` objects](https://python-pptx.readthedocs.io/en/latest/api/slides.html#slides-objects)
    * [`Slide` objects](https://python-pptx.readthedocs.io/en/latest/api/slides.html#slide-objects)
    * [`SlideLayouts` objects](https://python-pptx.readthedocs.io/en/latest/api/slides.html#slidelayouts-objects)
    * [`SlideLayout` objects](https://python-pptx.readthedocs.io/en/latest/api/slides.html#slidelayout-objects)
    * [`SlideMasters` objects](https://python-pptx.readthedocs.io/en/latest/api/slides.html#slidemasters-objects)
    * [`SlideMaster` objects](https://python-pptx.readthedocs.io/en/latest/api/slides.html#slidemaster-objects)
    * [`SlidePlaceholders` objects](https://python-pptx.readthedocs.io/en/latest/api/slides.html#slideplaceholders-objects)
    * [`NotesSlide` objects](https://python-pptx.readthedocs.io/en/latest/api/slides.html#notesslide-objects)
  * [Shapes](https://python-pptx.readthedocs.io/en/latest/api/shapes.html)
    * [`SlideShapes` objects](https://python-pptx.readthedocs.io/en/latest/api/shapes.html#slideshapes-objects)
    * [`GroupShapes` objects](https://python-pptx.readthedocs.io/en/latest/api/shapes.html#groupshapes-objects)
    * [Shape objects in general](https://python-pptx.readthedocs.io/en/latest/api/shapes.html#shape-objects-in-general)
    * [`Shape` objects (AutoShapes)](https://python-pptx.readthedocs.io/en/latest/api/shapes.html#shape-objects-autoshapes)
    * [`Connector` objects](https://python-pptx.readthedocs.io/en/latest/api/shapes.html#connector-objects)
    * [`FreeformBuilder` objects](https://python-pptx.readthedocs.io/en/latest/api/shapes.html#freeformbuilder-objects)
    * [`Picture` objects](https://python-pptx.readthedocs.io/en/latest/api/shapes.html#picture-objects)
    * [`GraphicFrame` objects](https://python-pptx.readthedocs.io/en/latest/api/shapes.html#graphicframe-objects)
    * [`GroupShape` objects](https://python-pptx.readthedocs.io/en/latest/api/shapes.html#groupshape-objects)
  * [Placeholders](https://python-pptx.readthedocs.io/en/latest/api/placeholders.html)
    * [`MasterPlaceholder` objects](https://python-pptx.readthedocs.io/en/latest/api/placeholders.html#masterplaceholder-objects)
    * [`LayoutPlaceholder` objects](https://python-pptx.readthedocs.io/en/latest/api/placeholders.html#layoutplaceholder-objects)
    * [ChartPlaceholder objects](https://python-pptx.readthedocs.io/en/latest/api/placeholders.html#chartplaceholder-objects)
    * [PicturePlaceholder objects](https://python-pptx.readthedocs.io/en/latest/api/placeholders.html#pictureplaceholder-objects)
    * [TablePlaceholder objects](https://python-pptx.readthedocs.io/en/latest/api/placeholders.html#tableplaceholder-objects)
    * [PlaceholderGraphicFrame objects](https://python-pptx.readthedocs.io/en/latest/api/placeholders.html#placeholdergraphicframe-objects)
    * [PlaceholderPicture objects](https://python-pptx.readthedocs.io/en/latest/api/placeholders.html#placeholderpicture-objects)
    * [_PlaceholderFormat objects](https://python-pptx.readthedocs.io/en/latest/api/placeholders.html#placeholderformat-objects)
  * [Table-related objects](https://python-pptx.readthedocs.io/en/latest/api/table.html)
    * [`Table` objects](https://python-pptx.readthedocs.io/en/latest/api/table.html#table-objects)
    * [`_Column` objects](https://python-pptx.readthedocs.io/en/latest/api/table.html#column-objects)
    * [`_Row` objects](https://python-pptx.readthedocs.io/en/latest/api/table.html#row-objects)
    * [`_Cell` objects](https://python-pptx.readthedocs.io/en/latest/api/table.html#cell-objects)
  * [ChartData objects](https://python-pptx.readthedocs.io/en/latest/api/chart-data.html)
  * [Charts](https://python-pptx.readthedocs.io/en/latest/api/chart.html)
    * [`Chart` objects](https://python-pptx.readthedocs.io/en/latest/api/chart.html#chart-objects)
    * [`Legend` objects](https://python-pptx.readthedocs.io/en/latest/api/chart.html#legend-objects)
    * [`Axis` objects](https://python-pptx.readthedocs.io/en/latest/api/chart.html#axis-objects)
    * [`MajorGridlines` objects](https://python-pptx.readthedocs.io/en/latest/api/chart.html#majorgridlines-objects)
    * [`TickLabels` objects](https://python-pptx.readthedocs.io/en/latest/api/chart.html#ticklabels-objects)
    * [`_BasePlot` objects](https://python-pptx.readthedocs.io/en/latest/api/chart.html#baseplot-objects)
    * [`DataLabels` objects](https://python-pptx.readthedocs.io/en/latest/api/chart.html#datalabels-objects)
    * [`Series` objects](https://python-pptx.readthedocs.io/en/latest/api/chart.html#series-objects)
    * [`Point` objects](https://python-pptx.readthedocs.io/en/latest/api/chart.html#point-objects)
  * [Text-related objects](https://python-pptx.readthedocs.io/en/latest/api/text.html)
    * [`TextFrame` objects](https://python-pptx.readthedocs.io/en/latest/api/text.html#textframe-objects)
    * [`Font` objects](https://python-pptx.readthedocs.io/en/latest/api/text.html#font-objects)
    * [`_Paragraph` objects](https://python-pptx.readthedocs.io/en/latest/api/text.html#paragraph-objects)
    * [`_Run` objects](https://python-pptx.readthedocs.io/en/latest/api/text.html#run-objects)
  * [Click Action-related Objects](https://python-pptx.readthedocs.io/en/latest/api/action.html)
    * [`ActionSetting` objects](https://python-pptx.readthedocs.io/en/latest/api/action.html#actionsetting-objects)
    * [`Hyperlink` objects](https://python-pptx.readthedocs.io/en/latest/api/action.html#hyperlink-objects)
  * [DrawingML objects](https://python-pptx.readthedocs.io/en/latest/api/dml.html)
    * [`ChartFormat` objects](https://python-pptx.readthedocs.io/en/latest/api/dml.html#chartformat-objects)
    * [`FillFormat` objects](https://python-pptx.readthedocs.io/en/latest/api/dml.html#fillformat-objects)
    * [`LineFormat` objects](https://python-pptx.readthedocs.io/en/latest/api/dml.html#lineformat-objects)
    * [`ColorFormat` objects](https://python-pptx.readthedocs.io/en/latest/api/dml.html#colorformat-objects)
    * [`RGBColor` objects](https://python-pptx.readthedocs.io/en/latest/api/dml.html#rgbcolor-objects)
    * [`ShadowFormat` objects](https://python-pptx.readthedocs.io/en/latest/api/dml.html#shadowformat-objects)
  * [Image](https://python-pptx.readthedocs.io/en/latest/api/image.html)
    * [`Image` objects](https://python-pptx.readthedocs.io/en/latest/api/image.html#image-objects)
  * [Exceptions](https://python-pptx.readthedocs.io/en/latest/api/exc.html)
  * [`util` Module](https://python-pptx.readthedocs.io/en/latest/api/util.html)
  * [Enumerations](https://python-pptx.readthedocs.io/en/latest/api/enum/index.html)
    * [`MSO_AUTO_SHAPE_TYPE`](https://python-pptx.readthedocs.io/en/latest/api/enum/MsoAutoShapeType.html)
    * [`MSO_AUTO_SIZE`](https://python-pptx.readthedocs.io/en/latest/api/enum/MsoAutoSize.html)
    * [`MSO_COLOR_TYPE`](https://python-pptx.readthedocs.io/en/latest/api/enum/MsoColorType.html)
    * [`MSO_CONNECTOR_TYPE`](https://python-pptx.readthedocs.io/en/latest/api/enum/MsoConnectorType.html)
    * [`MSO_FILL_TYPE`](https://python-pptx.readthedocs.io/en/latest/api/enum/MsoFillType.html)
    * [`MSO_LANGUAGE_ID`](https://python-pptx.readthedocs.io/en/latest/api/enum/MsoLanguageId.html)
    * [`MSO_LINE_DASH_STYLE`](https://python-pptx.readthedocs.io/en/latest/api/enum/MsoLineDashStyle.html)
    * [`MSO_PATTERN_TYPE`](https://python-pptx.readthedocs.io/en/latest/api/enum/MsoPatternType.html)
    * [`MSO_SHAPE_TYPE`](https://python-pptx.readthedocs.io/en/latest/api/enum/MsoShapeType.html)
    * [`MSO_TEXT_UNDERLINE_TYPE`](https://python-pptx.readthedocs.io/en/latest/api/enum/MsoTextUnderlineType.html)
    * [`MSO_THEME_COLOR_INDEX`](https://python-pptx.readthedocs.io/en/latest/api/enum/MsoThemeColorIndex.html)
    * [`MSO_VERTICAL_ANCHOR`](https://python-pptx.readthedocs.io/en/latest/api/enum/MsoVerticalAnchor.html)
    * [`PP_ACTION_TYPE`](https://python-pptx.readthedocs.io/en/latest/api/enum/PpActionType.html)
    * [`PP_MEDIA_TYPE`](https://python-pptx.readthedocs.io/en/latest/api/enum/PpMediaType.html)
    * [`PP_PARAGRAPH_ALIGNMENT`](https://python-pptx.readthedocs.io/en/latest/api/enum/PpParagraphAlignment.html)
    * [`PP_PLACEHOLDER_TYPE`](https://python-pptx.readthedocs.io/en/latest/api/enum/PpPlaceholderType.html)
    * [`XL_AXIS_CROSSES`](https://python-pptx.readthedocs.io/en/latest/api/enum/XlAxisCrosses.html)
    * [`XL_CATEGORY_TYPE`](https://python-pptx.readthedocs.io/en/latest/api/enum/XlCategoryType.html)
    * [`XL_CHART_TYPE`](https://python-pptx.readthedocs.io/en/latest/api/enum/XlChartType.html)
    * [`XL_DATA_LABEL_POSITION`](https://python-pptx.readthedocs.io/en/latest/api/enum/XlDataLabelPosition.html)
    * [`XL_LEGEND_POSITION`](https://python-pptx.readthedocs.io/en/latest/api/enum/XlLegendPosition.html)
    * [`XL_MARKER_STYLE`](https://python-pptx.readthedocs.io/en/latest/api/enum/XlMarkerStyle.html)
    * [`XL_TICK_LABEL_POSITION`](https://python-pptx.readthedocs.io/en/latest/api/enum/XlTickLabelPosition.html)
    * [`XL_TICK_MARK`](https://python-pptx.readthedocs.io/en/latest/api/enum/XlTickMark.html)
    * [Excel Number Formats](https://python-pptx.readthedocs.io/en/latest/api/enum/ExcelNumFormat.html)


## Contributor Guide[¶](https://python-pptx.readthedocs.io/en/latest/#contributor-guide "Permalink to this headline")
  * [Running the test suite](https://python-pptx.readthedocs.io/en/latest/dev/runtests.html)
  * [Understanding `xmlchemy`](https://python-pptx.readthedocs.io/en/latest/dev/xmlchemy.html)
  * [Development Practices](https://python-pptx.readthedocs.io/en/latest/dev/development_practices.html)
  * [Vision](https://python-pptx.readthedocs.io/en/latest/dev/philosophy.html)
  * [Analysis](https://python-pptx.readthedocs.io/en/latest/dev/analysis/index.html)
  * [Resources](https://python-pptx.readthedocs.io/en/latest/dev/resources/index.html)


### [Table of Contents](https://python-pptx.readthedocs.io/en/latest/)
  * [python-pptx](https://python-pptx.readthedocs.io/en/latest/)
    * [Philosophy](https://python-pptx.readthedocs.io/en/latest/#philosophy)
    * [Feature Support](https://python-pptx.readthedocs.io/en/latest/#feature-support)
    * [New features/releases](https://python-pptx.readthedocs.io/en/latest/#new-features-releases)
    * [User Guide](https://python-pptx.readthedocs.io/en/latest/#user-guide)
    * [Community Guide](https://python-pptx.readthedocs.io/en/latest/#community-guide)
    * [API Documentation](https://python-pptx.readthedocs.io/en/latest/#api-documentation)
    * [Contributor Guide](https://python-pptx.readthedocs.io/en/latest/#contributor-guide)


#### Next topic
[Introduction](https://python-pptx.readthedocs.io/en/latest/user/intro.html "next chapter")
### Useful Links
  * [python-pptx @ GitHub](http://github.com/scanny/python-pptx)
  * [python-pptx @ PyPI](http://pypi.python.org/pypi/python-pptx)
  * [Issue Tracker](http://github.com/scanny/python-pptx/issues)


### Quick search
### Navigation
  * [index](https://python-pptx.readthedocs.io/en/latest/genindex.html "General Index")
  * [modules](https://python-pptx.readthedocs.io/en/latest/py-modindex.html "Python Module Index") |
  * [next](https://python-pptx.readthedocs.io/en/latest/user/intro.html "Introduction") |
  * [python-pptx 1.0.0 documentation](https://python-pptx.readthedocs.io/en/latest/) »


© Copyright 2012, 2013, Steve Canny. Created using [Sphinx](http://sphinx.pocoo.org/) 1.8.6.   
Theme based on [Read The Docs](http://readthedocs.org/)
