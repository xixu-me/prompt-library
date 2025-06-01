# Documentation Generator

## Description

Automatically generates comprehensive documentation from code, including API documentation, README files, inline comments, and user guides. Supports multiple programming languages and documentation formats.

## Usage

Provide your code and specify the type of documentation needed. Works best with well-structured code that has clear function/class definitions. Specify the target audience and format requirements.

## Prompt

```markdown
Generate comprehensive documentation for the following code. Please create:

1. **API Documentation**
   - Function/method signatures
   - Parameter descriptions with types
   - Return value specifications
   - Usage examples
   - Error conditions

2. **Inline Comments**
   - Code explanation comments
   - Complex logic breakdown
   - Algorithm descriptions
   - Performance considerations

3. **README Section** (if applicable)
   - Purpose and overview
   - Installation/setup instructions
   - Basic usage examples
   - Configuration options

4. **User Guide Elements**
   - Step-by-step usage instructions
   - Common use cases
   - Troubleshooting tips
   - Best practices

Documentation requirements:
- Target audience: [developers/end-users/technical writers]
- Format: [Markdown/JSDoc/Sphinx/other]
- Documentation style: [comprehensive/concise/beginner-friendly]

Code to document:
```

[YOUR CODE HERE]

```

Additional context:
[PROJECT PURPOSE, DEPENDENCIES, SPECIAL REQUIREMENTS]
```

## Example Input

```markdown
```python
import requests
import json
from typing import Dict, List, Optional

class WeatherAPI:
    def __init__(self, api_key: str, base_url: str = "https://api.weather.com"):
        self.api_key = api_key
        self.base_url = base_url
    
    def get_current_weather(self, city: str, units: str = "metric") -> Dict:
        endpoint = f"{self.base_url}/current"
        params = {
            "city": city,
            "units": units,
            "api_key": self.api_key
        }
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_forecast(self, city: str, days: int = 5) -> List[Dict]:
        endpoint = f"{self.base_url}/forecast"
        params = {
            "city": city,
            "days": days,
            "api_key": self.api_key
        }
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()["forecast"]
```

```
## Example Output

```markdown
# WeatherAPI Documentation

## Overview
The WeatherAPI class provides a simple interface to fetch current weather data and forecasts for any city using a weather service API.

## Installation
```bash
pip install requests
```

## Quick Start

```python
from weather_api import WeatherAPI

# Initialize the API client
weather = WeatherAPI(api_key="your_api_key_here")

# Get current weather
current = weather.get_current_weather("New York")
print(f"Temperature: {current['temperature']}°C")

# Get 7-day forecast
forecast = weather.get_forecast("London", days=7)
for day in forecast:
    print(f"{day['date']}: {day['temperature']}°C, {day['description']}")
```

## API Reference

### Class: WeatherAPI

#### Constructor

```python
WeatherAPI(api_key: str, base_url: str = "https://api.weather.com")
```

**Parameters:**

- `api_key` (str): Your API key for the weather service
- `base_url` (str, optional): Base URL for the weather API. Defaults to "<https://api.weather.com>"

**Example:**

```python
weather = WeatherAPI("your_api_key", "https://custom-weather-api.com")
```

#### get_current_weather()

```python
get_current_weather(city: str, units: str = "metric") -> Dict
```

Retrieves current weather conditions for the specified city.

**Parameters:**

- `city` (str): Name of the city to get weather for
- `units` (str, optional): Temperature units ("metric", "imperial", "kelvin"). Defaults to "metric"

**Returns:**

- `Dict`: Weather data containing temperature, humidity, description, etc.

**Raises:**

- `requests.HTTPError`: If the API request fails
- `requests.ConnectionError`: If unable to connect to the API

**Example:**

```python
weather_data = weather.get_current_weather("Tokyo", units="imperial")
temp_f = weather_data["temperature"]  # Temperature in Fahrenheit
```

#### get_forecast()

```python
get_forecast(city: str, days: int = 5) -> List[Dict]
```

Retrieves weather forecast for the specified city.

**Parameters:**

- `city` (str): Name of the city to get forecast for
- `days` (int, optional): Number of days to forecast (1-10). Defaults to 5

**Returns:**

- `List[Dict]`: List of daily forecast data

**Raises:**

- `requests.HTTPError`: If the API request fails
- `ValueError`: If days parameter is outside valid range

**Example:**

```python
forecast = weather.get_forecast("Paris", days=3)
tomorrow = forecast[1]  # Second day (tomorrow)
```

## Error Handling

All methods may raise HTTP-related exceptions. Implement proper error handling:

```python
try:
    weather_data = weather.get_current_weather("InvalidCity")
except requests.HTTPError as e:
    print(f"API error: {e}")
except requests.ConnectionError:
    print("Unable to connect to weather service")
```

## Best Practices

- Store your API key securely (environment variables)
- Implement rate limiting to avoid API quota issues
- Cache responses when appropriate to reduce API calls
- Validate city names before making requests

```

## Variations
- **API-Only**: Focus only on API documentation with technical details
- **User Manual**: Create end-user focused documentation with tutorials
- **Inline Comments**: Generate only code comments and docstrings
- **Architecture Docs**: Create high-level system architecture documentation

## Tips
- Include the programming language for language-specific documentation standards
- Specify if you need examples for specific use cases
- Mention any existing documentation standards or tools used in your project
- Provide context about the intended users of the documentation

## Related Prompts
- `code-review.md` - For improving code before documenting
- `architecture-planner.md` - For system-level documentation
- `test-case-generator.md` - For creating documented test examples

## Tags
`documentation` `api-docs` `comments` `readme` `development` `technical-writing`
