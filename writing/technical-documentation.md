# Technical Documentation Writer

## Description

Creates comprehensive technical documentation including user guides, API documentation, tutorials, and technical specifications. Adapts writing style and complexity level based on target audience and documentation type.

## Usage

Provide the technical topic, target audience, and documentation type needed. Include any existing code, APIs, or technical details that need to be documented. Specify the level of technical detail required.

## Prompt

```markdown
Create technical documentation for the following:

### Documentation Type
[User Guide / API Documentation / Tutorial / Technical Specification / README / Other]

### Target Audience
[Developers / End Users / System Administrators / Technical Writers / Other]

### Technical Subject
[Describe what needs to be documented]

### Requirements
- **Scope**: [What should be covered and what should be excluded]
- **Format**: [Markdown / HTML / PDF / Wiki / Other]
- **Length**: [Brief overview / Comprehensive guide / Reference manual]
- **Technical Level**: [Beginner / Intermediate / Advanced / Mixed audience]

### Source Material
```

[CODE, APIs, SPECIFICATIONS, OR OTHER TECHNICAL CONTENT TO DOCUMENT]

```

### Special Requirements
- [Include examples / screenshots / diagrams]
- [SEO considerations for web documentation]
- [Translation requirements]
- [Accessibility standards]
- [Brand guidelines or style requirements]

Please structure the documentation with:
1. Clear introduction and purpose
2. Prerequisites and requirements
3. Step-by-step instructions where applicable
4. Code examples and use cases
5. Troubleshooting section
6. Reference materials and links

### Additional Context
[Any background information, existing documentation to reference, or specific pain points to address]
```

## Example Input

```markdown
### Documentation Type
API Documentation

### Target Audience
Frontend developers integrating with our REST API

### Technical Subject
User authentication and profile management API

### Requirements
- **Scope**: Authentication endpoints, profile CRUD operations, error handling
- **Format**: Markdown for developer portal
- **Length**: Comprehensive reference with examples
- **Technical Level**: Intermediate developers familiar with REST APIs

### Source Material
```python
# Authentication endpoints
@app.route('/api/auth/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    # Authentication logic here
    return jsonify({'token': jwt_token, 'user': user_data})

@app.route('/api/auth/logout', methods=['POST'])
def logout():
    # Logout logic
    return jsonify({'message': 'Logged out successfully'})

# Profile endpoints
@app.route('/api/profile', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    # Get user profile
    return jsonify(user_profile)

@app.route('/api/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    # Update profile logic
    return jsonify(updated_profile)
```

### Special Requirements

- Include curl examples for each endpoint
- Show both success and error response formats
- Include rate limiting information

```

## Example Output
```markdown
# User Authentication & Profile API

## Overview
This API provides endpoints for user authentication and profile management. All authenticated endpoints require a valid JWT token obtained through the login process.

## Base URL
```

<https://api.yourapp.com/v1>

```

## Authentication
This API uses JWT (JSON Web Tokens) for authentication. Include the token in the Authorization header:
```

Authorization: Bearer <your_jwt_token>

```

## Rate Limiting
- **Unauthenticated endpoints**: 100 requests per hour per IP
- **Authenticated endpoints**: 1000 requests per hour per user

---

## Authentication Endpoints

### Login
Authenticate a user and receive a JWT token.

**Endpoint:** `POST /api/auth/login`

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

**Success Response (200):**

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": 123,
    "email": "user@example.com",
    "name": "John Doe",
    "created_at": "2023-01-15T10:30:00Z"
  }
}
```

**Error Response (401):**

```json
{
  "error": "Invalid credentials",
  "code": "INVALID_CREDENTIALS"
}
```

**cURL Example:**

```bash
curl -X POST https://api.yourapp.com/v1/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepassword123"
  }'
```

### Logout

Invalidate the current JWT token.

**Endpoint:** `POST /api/auth/logout`

**Headers:**

- `Authorization: Bearer <token>` (required)

**Success Response (200):**

```json
{
  "message": "Logged out successfully"
}
```

**cURL Example:**

```bash
curl -X POST https://api.yourapp.com/v1/api/auth/logout \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

## Profile Endpoints

### Get Profile

Retrieve the authenticated user's profile information.

**Endpoint:** `GET /api/profile`

**Headers:**

- `Authorization: Bearer <token>` (required)

**Success Response (200):**

```json
{
  "id": 123,
  "email": "user@example.com",
  "name": "John Doe",
  "bio": "Software developer passionate about APIs",
  "avatar_url": "https://cdn.yourapp.com/avatars/123.jpg",
  "created_at": "2023-01-15T10:30:00Z",
  "updated_at": "2023-06-20T14:22:00Z"
}
```

**cURL Example:**

```bash
curl -X GET https://api.yourapp.com/v1/api/profile \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

### Update Profile

Update the authenticated user's profile information.

**Endpoint:** `PUT /api/profile`

**Headers:**

- `Authorization: Bearer <token>` (required)
- `Content-Type: application/json`

**Request Body:**

```json
{
  "name": "Jane Doe",
  "bio": "Senior software engineer with 5+ years experience"
}
```

**Success Response (200):**

```json
{
  "id": 123,
  "email": "user@example.com",
  "name": "Jane Doe",
  "bio": "Senior software engineer with 5+ years experience",
  "avatar_url": "https://cdn.yourapp.com/avatars/123.jpg",
  "updated_at": "2023-06-21T09:15:00Z"
}
```

**cURL Example:**

```bash
curl -X PUT https://api.yourapp.com/v1/api/profile \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Doe",
    "bio": "Senior software engineer with 5+ years experience"
  }'
```

---

## Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `INVALID_CREDENTIALS` | 401 | Email or password is incorrect |
| `TOKEN_EXPIRED` | 401 | JWT token has expired |
| `TOKEN_INVALID` | 401 | JWT token is malformed or invalid |
| `VALIDATION_ERROR` | 400 | Request data validation failed |
| `RATE_LIMIT_EXCEEDED` | 429 | Too many requests |
| `INTERNAL_ERROR` | 500 | Server encountered an unexpected error |

## Troubleshooting

### Common Issues

#### "Invalid credentials" error

- Verify email and password are correct
- Ensure email is properly formatted
- Check if account exists and is active

#### "Token expired" error

- Obtain a new token using the login endpoint
- Implement token refresh logic in your application

#### Rate limiting errors

- Implement exponential backoff in your requests
- Cache responses when possible to reduce API calls
- Contact support if you need higher rate limits

### Contact Support

For API issues or questions:

- Email: <api-support@yourapp.com>
- Documentation: <https://docs.yourapp.com>
- Status page: <https://status.yourapp.com>

```

## Variations
- **Quick Reference**: Create concise reference cards or cheat sheets
- **Tutorial Style**: Step-by-step learning-focused documentation
- **Troubleshooting Guide**: Focus on common problems and solutions
- **Migration Guide**: Document how to upgrade or migrate between versions

## Tips
- Always include practical examples and code snippets
- Structure information hierarchically with clear headings
- Include both happy path and error scenarios
- Use consistent formatting and terminology throughout
- Add visual aids like diagrams or screenshots when helpful
- Keep the target audience's expertise level in mind

## Related Prompts
- `code-review.md` - For improving code before documenting it
- `architecture-planner.md` - For documenting system architecture
- `email-templates.md` - For creating documentation distribution emails

## Tags
`technical-writing` `documentation` `api-docs` `user-guides` `tutorials` `writing`
