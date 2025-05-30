# Document Format Checker

A web application that checks Microsoft Word documents (.docx) against specific formatting guidelines for project reports.

## Features

- Checks font type (Times New Roman)
- Validates font sizes for different heading levels
- Verifies text justification and color
- Checks line spacing
- Validates page margins
- Provides a detailed report of formatting issues
- User-friendly web interface with drag-and-drop support

## Requirements

- Python 3.7+
- pip

## Installation

1. Clone the repository or download the source code
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:

```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`
3. Upload your .docx file using the upload interface
4. View the formatting issues and recommendations

## Formatting Rules Checked

- **Font**: Times New Roman only
- **Font Sizes**:
  - Chapter titles: 16pt
  - Subheadings: 14pt
  - Normal text: 12pt
- **Text**:
  - Justified alignment
  - Black color only
- **Line Spacing**: 1.79
- **Margins**: At least 1.75 inches on both sides
- **Alignment**: Chapter names and images center aligned

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Built with [Flask](https://flask.palletsprojects.com/)
- Uses [python-docx](https://python-docx.readthedocs.io/) for document processing
- Styled with [Bootstrap 5](https://getbootstrap.com/)
