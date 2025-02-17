# Deer Facts Validator

A web application that validates whether submitted text contains factual information about deer species using OpenAI's GPT-4 model.

## Description

The Deer Facts Validator is an interactive web tool that allows users to input text and determine if it contains valid information about deer species. The application uses artificial intelligence to analyze the content and provides detailed feedback on the validity of the deer-related facts.

## Tech Stack

### Frontend
- HTML5
- CSS3 (Bootstrap 3.3.7)
- JavaScript (Vanilla JS)

### Backend
- Python 3.x
- Flask
- Flask-CORS
- OpenAI API (GPT-4)

## Prerequisites

- Python 3.x
- OpenAI API key
- Node.js and npm (for Bootstrap dependencies)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/deer-facts-validator.git
    cd deer-facts-validator
    ```

2. Install Python dependencies:
    ```bash
    pip install flask flask-cors openai
    ```

3. Set up your OpenAI API key:
    ```bash
    # Windows (Command Prompt)
    set OPENAI_API_KEY=your_api_key_here

    # Windows (PowerShell)
    $env:OPENAI_API_KEY="your_api_key_here"
    ```

## Usage

1. Start the Flask server:
    ```bash
    python server.py
    ```

2. Open `index.html` in your web browser or serve it using a local server:
    ```bash
    python -m http.server 8000
    ```

3. Visit `http://localhost:8000` in your web browser
4. Enter a deer-related fact in the text area
5. Click "Check Fact!" to validate the information

## Features

- Real-time fact validation using GPT-4
- User-friendly interface
- Detailed explanations for valid/invalid facts
- Support for multiple deer species
- Error handling and user feedback
- Responsive design

## Supported Deer Species

The validator recognizes facts about the following deer species:
- White-tailed deer
- Red deer
- Caribou
- Reindeer
- Moose
- Water deer
- Muntjac
- Axis deer
- Chital deer
- Elk
- Sika deer
- Eld's deer
- Sambar deer
- Visayan spotted deer
- Fallow deer
- Key deer
- Mule deer
- Pampas deer
- Pudu
- Roe deer

## API Reference

### Validate Fact Endpoint

```http
POST /validate
```

Request body:
```json
{
  "fact": "string"
}
```

Response:
```json
{
  "valid": boolean,
  "explanation": "string"
}
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the GPT-4 API
- Bootstrap team for the frontend framework
- All contributors and testers

## Future Improvements

- [ ] Add user authentication
- [ ] Implement fact history
- [ ] Add more detailed species information
- [ ] Improve validation accuracy
- [ ] Add support for more languages
- [ ] Create a fact submission system for verified facts



