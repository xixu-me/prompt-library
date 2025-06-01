# Refactoring Assistant

## Description

This prompt helps you analyze and refactor existing code to improve its structure, readability, maintainability, and performance while preserving functionality.

## Usage

Perfect for improving legacy code, preparing code for new features, reducing technical debt, and following best practices and design patterns.

## Prompt

```markdown
You are an expert code refactoring assistant. I need help refactoring the following code to improve its quality while maintaining the same functionality.

**Code to refactor:**
```

[INSERT_CODE_HERE]

```

**Context:**
- Programming language: [LANGUAGE]
- Framework/library: [FRAMEWORK_IF_ANY]
- Current issues: [DESCRIBE_PROBLEMS]
- Performance requirements: [PERFORMANCE_NEEDS]
- Coding standards: [STYLE_GUIDE_IF_ANY]

Please analyze the code and provide:

1. **Code Quality Assessment:**
   - Identify code smells and anti-patterns
   - Assess readability, maintainability, and performance
   - Check adherence to SOLID principles
   - Evaluate naming conventions and structure

2. **Refactoring Plan:**
   - List specific improvements needed
   - Prioritize changes by impact and complexity
   - Identify any breaking changes
   - Suggest design patterns if applicable

3. **Refactored Code:**
   - Provide the improved version
   - Add clear comments explaining changes
   - Ensure functionality is preserved
   - Follow best practices for the language/framework

4. **Explanation:**
   - Explain what was changed and why
   - Highlight performance improvements
   - Note any new dependencies or requirements
   - Provide migration steps if needed

5. **Testing Recommendations:**
   - Suggest test cases to verify functionality
   - Recommend regression testing approach
   - Identify potential edge cases to test

Focus on making the code more readable, maintainable, and efficient while following established best practices.
```

## Example Input

```markdown
Code to refactor:
```javascript
function processUsers(users) {
    var result = [];
    for (var i = 0; i < users.length; i++) {
        if (users[i].age >= 18 && users[i].active == true) {
            var userData = {};
            userData.name = users[i].firstName + " " + users[i].lastName;
            userData.email = users[i].email;
            userData.category = users[i].age >= 65 ? "senior" : "adult";
            result.push(userData);
        }
    }
    return result;
}
```

Context:

- Programming language: JavaScript (ES6+)
- Framework/library: None
- Current issues: Old syntax, not functional, poor readability
- Performance requirements: Handle arrays up to 10,000 users
- Coding standards: ES6+, functional programming preferred

```

## Example Output
```

## Code Quality Assessment

- Uses var instead of const/let
- Traditional for loop instead of array methods
- Loose equality comparison (==)
- Imperative style instead of functional
- No input validation
- String concatenation instead of template literals

## Refactoring Plan

1. Convert to functional programming style
2. Use modern ES6+ syntax
3. Add input validation
4. Extract helper functions for better readability
5. Use array methods for better performance

## Refactored Code

```javascript
/**
 * Processes users array to extract active adult users with formatted data
 * @param {Array<Object>} users - Array of user objects
 * @returns {Array<Object>} Filtered and formatted user data
 */
const processUsers = (users = []) => {
  if (!Array.isArray(users)) {
    throw new Error('Input must be an array');
  }

  const isEligibleUser = (user) => 
    user?.age >= 18 && user?.active === true;

  const formatUserData = (user) => ({
    name: `${user.firstName} ${user.lastName}`,
    email: user.email,
    category: user.age >= 65 ? 'senior' : 'adult'
  });

  return users
    .filter(isEligibleUser)
    .map(formatUserData);
};
```

## Explanation

- **Modern syntax**: Used const, arrow functions, template literals
- **Functional approach**: Replaced imperative loop with filter/map chain
- **Better readability**: Extracted helper functions with descriptive names
- **Input validation**: Added type checking and default parameter
- **Performance**: Array methods are optimized and more readable
- **Strict equality**: Used === instead of ==
- **Optional chaining**: Added ?. for safer property access

## Testing Recommendations

- Test with empty array, null, undefined inputs
- Test with users of various ages (under 18, 18-64, 65+)
- Test with inactive users
- Test with malformed user objects
- Performance test with 10,000+ user array

```

## Variations

### Legacy Code Modernization
Focus specifically on updating old syntax and patterns to modern standards while maintaining backward compatibility.

### Performance-Focused Refactoring
Emphasize optimization for speed, memory usage, and scalability in the refactoring suggestions.

### Security-Focused Refactoring
Prioritize identifying and fixing security vulnerabilities, input validation, and secure coding practices.

## Tips
- Always preserve the original functionality unless explicitly asked to change it
- Test thoroughly after refactoring to ensure no regressions
- Refactor in small, incremental steps rather than large rewrites
- Consider the team's skill level when suggesting modern patterns
- Document any breaking changes clearly

## Related Prompts
- [Code Review](./code-review.md) - For reviewing code quality
- [Test Case Generator](./test-case-generator.md) - For creating tests after refactoring
- [Documentation Generator](./documentation-generator.md) - For updating docs after refactoring

## Tags
`refactoring` `code-quality` `best-practices` `modernization` `optimization` `maintainability` `technical-debt` `clean-code`
