# Test Case Generator

## Description

Generates comprehensive test cases and testing strategies for software applications. Creates unit tests, integration tests, user acceptance tests, and edge case scenarios based on code, requirements, or functionality descriptions.

## Usage

Provide code, feature requirements, or API specifications that need testing. Specify the testing framework, level of coverage needed, and types of tests required. Works for all programming languages and testing approaches.

## Prompt

```markdown
Generate comprehensive test cases for the following:

**Testing Target:**
[Function/Class/API/Feature/User Story to be tested]

**Code/Requirements:**
```

[PROVIDE CODE, API SPEC, OR FEATURE REQUIREMENTS HERE]

```

**Testing Requirements:**
- **Test Types Needed:** [Unit tests / Integration tests / End-to-end tests / Performance tests]
- **Testing Framework:** [Jest/Mocha/PyTest/JUnit/Cypress/Other]
- **Coverage Goals:** [Basic functionality / Edge cases / Error conditions / Performance]
- **Programming Language:** [JavaScript/Python/Java/C#/Other]

**Test Scenarios to Include:**
1. **Happy Path Tests**
   - Normal operation with valid inputs
   - Expected successful outcomes
   - Standard use cases

2. **Edge Case Tests**
   - Boundary value testing
   - Unusual but valid inputs
   - Minimum and maximum values

3. **Error Handling Tests**
   - Invalid inputs and parameters
   - Network failures and timeouts
   - Resource limitations

4. **Integration Tests** (if applicable)
   - Component interactions
   - External service dependencies
   - Database operations

5. **Performance Tests** (if applicable)
   - Load testing scenarios
   - Response time requirements
   - Resource usage monitoring

**Additional Requirements:**
- [Mock external dependencies]
- [Test data setup/teardown]
- [Specific assertion patterns]
- [Documentation level needed]

Please provide:
- Test case descriptions and rationale
- Complete test code implementations
- Test data and setup requirements
- Expected outcomes and assertions
- Comments explaining complex test logic
```

## Example Input

```markdown
**Testing Target:** User authentication function

**Code/Requirements:**
```javascript
async function authenticateUser(email, password) {
    if (!email || !password) {
        throw new Error('Email and password are required');
    }
    
    if (!isValidEmail(email)) {
        throw new Error('Invalid email format');
    }
    
    const user = await getUserByEmail(email);
    if (!user) {
        throw new Error('User not found');
    }
    
    const isPasswordValid = await bcrypt.compare(password, user.hashedPassword);
    if (!isPasswordValid) {
        throw new Error('Invalid password');
    }
    
    return {
        userId: user.id,
        email: user.email,
        token: generateJWT(user.id)
    };
}
```

**Testing Requirements:**

- **Test Types:** Unit tests with mocking
- **Framework:** Jest
- **Coverage:** All branches and error conditions
- **Language:** JavaScript/Node.js

```

## Example Output
```javascript
// authenticateUser.test.js
const bcrypt = require('bcrypt');
const { authenticateUser } = require('./auth');
const { getUserByEmail, generateJWT, isValidEmail } = require('./utils');

// Mock dependencies
jest.mock('./utils');
jest.mock('bcrypt');

describe('authenticateUser', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('Happy Path Tests', () => {
    test('should authenticate user with valid credentials', async () => {
      // Arrange
      const email = 'user@example.com';
      const password = 'securePassword123';
      const mockUser = {
        id: 1,
        email: 'user@example.com',
        hashedPassword: 'hashedPassword123'
      };
      const mockToken = 'jwt.token.here';

      isValidEmail.mockReturnValue(true);
      getUserByEmail.mockResolvedValue(mockUser);
      bcrypt.compare.mockResolvedValue(true);
      generateJWT.mockReturnValue(mockToken);

      // Act
      const result = await authenticateUser(email, password);

      // Assert
      expect(result).toEqual({
        userId: 1,
        email: 'user@example.com',
        token: mockToken
      });
      expect(getUserByEmail).toHaveBeenCalledWith(email);
      expect(bcrypt.compare).toHaveBeenCalledWith(password, mockUser.hashedPassword);
      expect(generateJWT).toHaveBeenCalledWith(mockUser.id);
    });
  });

  describe('Input Validation Tests', () => {
    test('should throw error when email is missing', async () => {
      // Arrange & Act & Assert
      await expect(authenticateUser(null, 'password123'))
        .rejects
        .toThrow('Email and password are required');
    });

    test('should throw error when password is missing', async () => {
      // Arrange & Act & Assert
      await expect(authenticateUser('user@example.com', null))
        .rejects
        .toThrow('Email and password are required');
    });

    test('should throw error when both email and password are missing', async () => {
      // Arrange & Act & Assert
      await expect(authenticateUser(null, null))
        .rejects
        .toThrow('Email and password are required');
    });

    test('should throw error when email format is invalid', async () => {
      // Arrange
      const invalidEmail = 'invalid-email';
      const password = 'password123';
      
      isValidEmail.mockReturnValue(false);

      // Act & Assert
      await expect(authenticateUser(invalidEmail, password))
        .rejects
        .toThrow('Invalid email format');
      
      expect(isValidEmail).toHaveBeenCalledWith(invalidEmail);
    });
  });

  describe('Edge Case Tests', () => {
    test('should handle empty string email', async () => {
      // Arrange & Act & Assert
      await expect(authenticateUser('', 'password123'))
        .rejects
        .toThrow('Email and password are required');
    });

    test('should handle empty string password', async () => {
      // Arrange & Act & Assert
      await expect(authenticateUser('user@example.com', ''))
        .rejects
        .toThrow('Email and password are required');
    });

    test('should handle very long email', async () => {
      // Arrange
      const longEmail = 'a'.repeat(250) + '@example.com';
      const password = 'password123';
      
      isValidEmail.mockReturnValue(true);
      getUserByEmail.mockResolvedValue(null);

      // Act & Assert
      await expect(authenticateUser(longEmail, password))
        .rejects
        .toThrow('User not found');
    });
  });

  describe('User Not Found Tests', () => {
    test('should throw error when user does not exist', async () => {
      // Arrange
      const email = 'nonexistent@example.com';
      const password = 'password123';
      
      isValidEmail.mockReturnValue(true);
      getUserByEmail.mockResolvedValue(null);

      // Act & Assert
      await expect(authenticateUser(email, password))
        .rejects
        .toThrow('User not found');
      
      expect(getUserByEmail).toHaveBeenCalledWith(email);
    });
  });

  describe('Password Validation Tests', () => {
    test('should throw error when password is incorrect', async () => {
      // Arrange
      const email = 'user@example.com';
      const password = 'wrongPassword';
      const mockUser = {
        id: 1,
        email: 'user@example.com',
        hashedPassword: 'hashedPassword123'
      };

      isValidEmail.mockReturnValue(true);
      getUserByEmail.mockResolvedValue(mockUser);
      bcrypt.compare.mockResolvedValue(false);

      // Act & Assert
      await expect(authenticateUser(email, password))
        .rejects
        .toThrow('Invalid password');
      
      expect(bcrypt.compare).toHaveBeenCalledWith(password, mockUser.hashedPassword);
    });
  });

  describe('Error Handling Tests', () => {
    test('should handle database connection error', async () => {
      // Arrange
      const email = 'user@example.com';
      const password = 'password123';
      
      isValidEmail.mockReturnValue(true);
      getUserByEmail.mockRejectedValue(new Error('Database connection failed'));

      // Act & Assert
      await expect(authenticateUser(email, password))
        .rejects
        .toThrow('Database connection failed');
    });

    test('should handle bcrypt comparison error', async () => {
      // Arrange
      const email = 'user@example.com';
      const password = 'password123';
      const mockUser = {
        id: 1,
        email: 'user@example.com',
        hashedPassword: 'hashedPassword123'
      };

      isValidEmail.mockReturnValue(true);
      getUserByEmail.mockResolvedValue(mockUser);
      bcrypt.compare.mockRejectedValue(new Error('Bcrypt error'));

      // Act & Assert
      await expect(authenticateUser(email, password))
        .rejects
        .toThrow('Bcrypt error');
    });
  });

  describe('Integration Tests', () => {
    test('should call dependencies in correct order', async () => {
      // Arrange
      const email = 'user@example.com';
      const password = 'password123';
      const mockUser = {
        id: 1,
        email: 'user@example.com',
        hashedPassword: 'hashedPassword123'
      };

      isValidEmail.mockReturnValue(true);
      getUserByEmail.mockResolvedValue(mockUser);
      bcrypt.compare.mockResolvedValue(true);
      generateJWT.mockReturnValue('token');

      // Act
      await authenticateUser(email, password);

      // Assert - verify call order
      expect(isValidEmail).toHaveBeenCalledBefore(getUserByEmail);
      expect(getUserByEmail).toHaveBeenCalledBefore(bcrypt.compare);
      expect(bcrypt.compare).toHaveBeenCalledBefore(generateJWT);
    });
  });
});

// Performance test example
describe('authenticateUser Performance', () => {
  test('should complete authentication within 100ms', async () => {
    // Arrange
    const email = 'user@example.com';
    const password = 'password123';
    const mockUser = { id: 1, email, hashedPassword: 'hash' };

    isValidEmail.mockReturnValue(true);
    getUserByEmail.mockResolvedValue(mockUser);
    bcrypt.compare.mockResolvedValue(true);
    generateJWT.mockReturnValue('token');

    // Act
    const startTime = Date.now();
    await authenticateUser(email, password);
    const endTime = Date.now();

    // Assert
    expect(endTime - startTime).toBeLessThan(100);
  });
});
```

## Test Coverage Report

The above test suite provides:

- **Function Coverage**: 100% - All functions are tested
- **Branch Coverage**: 100% - All conditional paths tested
- **Statement Coverage**: 100% - All code lines executed
- **Edge Case Coverage**: Comprehensive boundary testing

## Test Data Setup

```javascript
// testData/users.js
export const validUsers = [
  {
    id: 1,
    email: 'user1@example.com',
    hashedPassword: '$2b$10$validHashedPassword1'
  },
  {
    id: 2,
    email: 'user2@example.com',
    hashedPassword: '$2b$10$validHashedPassword2'
  }
];

export const invalidEmails = [
  'invalid-email',
  'user@',
  '@example.com',
  'user..name@example.com',
  'user name@example.com'
];
```

## Variations

- **API Testing**: Focus on HTTP endpoint testing with request/response validation
- **Frontend Testing**: UI component testing with user interactions
- **Database Testing**: Data layer testing with setup/teardown procedures
- **Security Testing**: Penetration testing and vulnerability assessment

## Tips

- Always test both positive and negative scenarios
- Include boundary value testing for numeric inputs
- Mock external dependencies to isolate unit tests
- Use descriptive test names that explain the scenario
- Group related tests using `describe` blocks
- Include performance tests for critical functions
- Test error conditions as thoroughly as success conditions

## Related Prompts

- `code-review.md` - For reviewing test quality and coverage
- `bug-hunter.md` - For creating tests that reproduce bugs
- `documentation-generator.md` - For documenting test procedures

## Tags

`testing` `unit-tests` `test-automation` `quality-assurance` `development` `debugging`
