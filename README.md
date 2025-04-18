# PDF Text Extraction API

This project provides a simple API for extracting text from PDF documents. Built using NextJS 14 and FastAPI, it offers an endpoint that can process PDF content either directly or via URLs.

## API Summary

The PDF Text Extraction API takes either PDF file content or a URL to a PDF file and returns the extracted text. It uses the PyMuPDF (fitz) library to process PDF documents, converting them to clean, normalized text with formatting adjustments.

## Features

- Extract text from PDF documents
- Accept PDF content directly or via URL
- Clean and normalize extracted text
- Simple REST API interface
- Built with FastAPI and Next.js 14

## Endpoints

### `/api/py/extractPdfText` (POST)

Extracts text from a PDF.

- **Input**: PDF file content as bytes or URL to a PDF document
- **Output**: Extracted text, converted to lowercase with line breaks replaced by spaces

### `/api/py/helloFastApi` (GET)

Simple test endpoint.

- **Output**: JSON response with a hello message

## Getting Started

First, create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Then, install the dependencies:

```bash
npm install
# or
yarn
# or
pnpm install
```

Then, run the development server (python dependencies will be installed automatically):

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

The FastAPI server will be running on [http://127.0.0.1:8000](http://127.0.0.1:8000).

## API Documentation

When running locally, view the interactive API documentation at:
[http://localhost:8000/api/py/docs](http://localhost:8000/api/py/docs)

## Dependencies

- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/) - PDF processing library
- [Next.js 14](https://nextjs.org/) - React framework for the frontend
- [Requests](https://requests.readthedocs.io/) - For downloading PDFs from URLs
