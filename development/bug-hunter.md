# Bug Hunter - Debug Assistant

## Description

A systematic debugging assistant that helps identify, analyze, and resolve software bugs and errors. Provides step-by-step troubleshooting approaches and suggests fixes for various types of issues.

## Usage

Provide error messages, problematic code, or describe unexpected behavior. Include relevant context like environment, inputs, and expected vs. actual outcomes. Works across all programming languages.

## Prompt

```markdown
Help me debug the following issue. Please provide a systematic analysis:

**Problem Description:**
[Describe what's happening vs. what should happen]

**Error Message/Symptoms:**
```

[PASTE ERROR MESSAGE OR DESCRIBE SYMPTOMS]

```

**Code:**
```

[PASTE RELEVANT CODE]

```

**Environment:**
- Programming Language: [language and version]
- Framework/Libraries: [if applicable]
- Operating System: [OS details]
- Input Data: [sample inputs that cause the issue]

Please analyze this by:

1. **Root Cause Analysis**
   - Identify the likely cause of the issue
   - Explain why this error occurs
   - Point to specific lines or components

2. **Debugging Strategy**
   - Step-by-step debugging approach
   - What to check or test first
   - Logging/debugging techniques to use

3. **Solution Options**
   - Primary fix recommendation
   - Alternative approaches
   - Preventive measures

4. **Testing Approach**
   - How to verify the fix works
   - Edge cases to test
   - Regression testing recommendations

Additional context:
[ANY OTHER RELEVANT INFORMATION]
```

## Example Input

```markdown
**Problem Description:**
My Python web scraper randomly fails with connection errors, but the website is accessible in the browser.

**Error Message:**
```

requests.exceptions.ConnectionError: HTTPSConnectionPool(host='example.com', port=443):
Max retries exceeded with url: /api/data (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7f8b8c0b1d90>: Failed to establish a new connection: [Errno 111] Connection refused'))

```

**Code:**
```python
import requests
import time

def scrape_data():
    urls = ["https://example.com/api/data", "https://example.com/api/users"]
    results = []
    
    for url in urls:
        response = requests.get(url)
        results.append(response.json())
        time.sleep(0.1)
    
    return results
```

**Environment:**

- Python 3.9
- requests library 2.28.1
- Running on Ubuntu 20.04
- Input: Multiple URLs being scraped in sequence

```

## Example Output
```

### Debug Analysis Report

#### Root Cause Analysis

**Primary Issue:** Rate limiting and connection management
The error indicates connection refusal, which typically occurs when:

1. **Rate Limiting**: The server is blocking requests due to too many rapid connections
2. **Connection Pool Exhaustion**: Not properly managing HTTP connections
3. **Server-side blocking**: Anti-bot measures detecting automated requests

**Specific Issues in Code:**

- Line 8: No error handling for failed requests
- Line 9: Very short delay (0.1s) may trigger rate limiting
- No User-Agent header (common anti-bot trigger)
- No retry mechanism for transient failures

### Debugging Strategy

### Immediate Debugging Steps

1. **Test connectivity**: `curl -I https://example.com/api/data`
2. **Check rate limits**: Increase delay to 2-3 seconds
3. **Monitor network**: Use `netstat` or Wireshark to see connection states
4. **Add logging**: Log response status codes before the error

### Code for Debugging

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Add this before your request
print(f"Attempting to connect to: {url}")
response = requests.get(url, timeout=10)
print(f"Response status: {response.status_code}")
```

### Solution Options

#### Primary Fix (Recommended)

```python
import requests
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def scrape_data():
    # Configure session with retry strategy
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    
    # Add headers to appear more like a browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    
    urls = ["https://example.com/api/data", "https://example.com/api/users"]
    results = []
    
    for url in urls:
        try:
            response = session.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            results.append(response.json())
            # Respectful delay
            time.sleep(2)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            continue
    
    return results
```

### Alternative Approaches

1. **Use connection pooling**: Implement session reuse
2. **Implement exponential backoff**: Gradually increase delays
3. **Add proxy rotation**: If being blocked by IP
4. **Use async requests**: For better connection management

### Testing Approach

#### Verification Steps

1. **Unit test**: Test with single URL first
2. **Load test**: Gradually increase number of URLs
3. **Network simulation**: Test with poor connectivity
4. **Edge cases**: Test with invalid URLs, timeouts

### Test Code

```python
def test_scraper():
    # Test single URL
    result = scrape_data_single("https://httpbin.org/json")
    assert result is not None
    
    # Test with delay
    start_time = time.time()
    scrape_data()
    duration = time.time() - start_time
    assert duration >= 2  # Ensure delay is working
```

### Prevention Measures

- Always implement proper error handling
- Use session objects for connection reuse
- Add appropriate delays between requests
- Include realistic User-Agent headers
- Implement retry logic for transient failures
- Monitor rate limits and adjust accordingly

```

## Variations
- **Performance Issues**: Focus on optimization and profiling
- **Security Bugs**: Emphasize vulnerability analysis and secure coding
- **Integration Issues**: Focus on API and service integration problems
- **Frontend Debugging**: Specialized for JavaScript/browser issues

## Tips
- Include full error stack traces when possible
- Provide minimal reproducible examples
- Mention any recent changes that might have introduced the bug
- Include relevant log files or console output
- Specify if the issue is intermittent or consistent

## Related Prompts
- `code-review.md` - For preventing bugs through better code quality
- `test-case-generator.md` - For creating tests to catch bugs
- `refactoring-assistant.md` - For improving code structure to prevent issues

## Tags
`debugging` `troubleshooting` `error-analysis` `bug-fixing` `development` `problem-solving`
