# Contributing to the Prompt Library

Thank you for your interest in contributing to our prompt library! This document provides guidelines for adding new prompts, improving existing ones, and maintaining the quality of our collection.

## 🚀 Getting Started

### Types of Contributions

- **New Prompts**: Add prompts for common use cases or emerging needs
- **Prompt Improvements**: Enhance existing prompts with better examples or clearer instructions
- **Documentation**: Improve README files, templates, or usage guides
- **Examples**: Add real-world examples and use cases
- **Bug Fixes**: Correct errors or improve clarity in existing content

### Before You Start

1. Browse existing prompts to avoid duplication
2. Check open issues for requested prompts
3. Consider if your prompt fits into existing categories or needs a new one

## 📝 Contribution Guidelines

### Prompt Quality Standards

Every prompt should:

- **Solve a Real Problem**: Address a common, valuable use case
- **Be Well-Structured**: Follow our template format consistently
- **Include Examples**: Provide clear input/output examples
- **Be Tested**: Verify the prompt works as expected with AI models
- **Be Documented**: Include proper descriptions and usage instructions

### Template Compliance

All prompts must use our standard template structure:

```markdown
# Prompt Title

## Description
[Clear explanation of what this prompt does]

## Usage
[How to use this prompt effectively]

## Prompt
```markdown

[The actual prompt text]

```

## Example Input

```markdown

[Sample input]

```

## Example Output

```markdown

[Expected output]

```

## Variations

[Alternative versions or modifications]

## Tips

[Best practices and recommendations]

## Related Prompts

[Links to similar or complementary prompts]

## Tags

`[tag1]` `[tag2]` `[tag3]`

```

## 📁 File Organization

### Naming Conventions

- Use kebab-case for filenames: `code-review-assistant.md`
- Use descriptive names that clearly indicate purpose
- Avoid abbreviations unless commonly understood

### Category Placement

Choose the most appropriate category:

- **development/**: Programming, testing, architecture, debugging
- **writing/**: Documentation, content creation, communication
- **business/**: Strategy, planning, analysis, proposals
- **creative/**: Brainstorming, design, innovation
- **analysis/**: Data analysis, research, reporting
- **education/**: Learning, teaching, training
- **productivity/**: Organization, automation, efficiency

### Directory Structure

```plaintext

category/
├── README.md (category overview)
├── prompt-name.md
├── another-prompt.md
└── subcategory/ (if needed)
    ├── README.md
    └── specialized-prompt.md

```

## ✨ Writing Guidelines

### Tone and Style

- **Professional but Accessible**: Clear, concise, helpful
- **Actionable**: Focus on practical, implementable advice
- **Inclusive**: Use inclusive language and consider diverse perspectives
- **Consistent**: Maintain consistency with existing prompts

### Prompt Writing Best Practices

#### 1. Clear Instructions

```markdown
❌ "Help me with my code"
✅ "Review the following code for performance issues, security vulnerabilities, and best practices violations"
```

#### 2. Specific Context

```markdown
❌ "Create a document"
✅ "Create a technical specification document for a REST API, including endpoints, request/response formats, and error handling"
```

#### 3. Structured Output

```markdown
✅ "Please provide your analysis in the following format:
1. Summary of findings
2. Detailed recommendations
3. Implementation steps"
```

#### 4. Examples and Context

Always include:

- Sample inputs that demonstrate typical use cases
- Expected outputs that show quality standards
- Variations for different scenarios
- Tips for optimal results

## 🔍 Review Process

### Self-Review Checklist

Before submitting, ensure your contribution:

- [ ] Follows the template structure exactly
- [ ] Includes working examples with realistic inputs/outputs
- [ ] Has clear, actionable instructions
- [ ] Uses proper grammar and spelling
- [ ] Includes relevant tags and categorization
- [ ] Links to related prompts where appropriate
- [ ] Tests successfully with at least one AI model

### Testing Your Prompts

1. **Test with AI Models**: Verify the prompt works with ChatGPT, Claude, or similar
2. **Test Edge Cases**: Try with unusual inputs or edge cases
3. **Test Clarity**: Have someone else try the prompt without additional context
4. **Test Output Quality**: Ensure outputs meet professional standards

## 📋 Submission Process

### Step 1: Fork and Branch

1. Fork the repository
2. Create a new branch: `git checkout -b add-prompt-name`
3. Make your changes

### Step 2: Create Your Prompt

1. Choose the appropriate directory
2. Create your prompt file following the template
3. Update the category README.md to include your prompt
4. Add examples if you're contributing to the examples/ directory

### Step 3: Submit Pull Request

1. Commit your changes with a clear message
2. Push to your fork: `git push origin add-prompt-name`
3. Create a pull request with:
   - Clear title describing the contribution
   - Description of what the prompt does
   - Why it's valuable to the community
   - Any special considerations or testing notes

### Pull Request Template

```markdown
## Prompt Contribution: [Prompt Name]

**Category**: [development/writing/business/etc.]
**Type**: [New prompt/Improvement/Example/Documentation]

### Description
Brief description of what this prompt does and why it's valuable.

### Testing
- [ ] Tested with [AI model name]
- [ ] Examples verified to work
- [ ] Edge cases considered
- [ ] Documentation is clear

### Checklist
- [ ] Follows template structure
- [ ] Includes realistic examples
- [ ] Has appropriate tags
- [ ] Updated category README
- [ ] Proper file naming
```

## 🎯 Quality Standards

### Content Quality

- **Accuracy**: Information should be correct and up-to-date
- **Completeness**: Include all necessary information for successful use
- **Clarity**: Instructions should be unambiguous
- **Value**: Address real needs and provide practical solutions

### Technical Quality

- **Testing**: All prompts should be tested with AI models
- **Examples**: Include realistic, working examples
- **Edge Cases**: Consider and document limitations
- **Performance**: Prompts should be efficient and produce consistent results

## 🤝 Community Guidelines

### Code of Conduct

- Be respectful and constructive in discussions
- Focus on improving the prompt library for everyone
- Provide helpful feedback on others' contributions
- Report any issues or concerns to maintainers

### Getting Help

- Check existing issues and discussions first
- Use issue templates for bug reports or feature requests
- Ask questions in discussions rather than issues
- Tag maintainers only when necessary

## 📈 Recognition

### Contributors

All contributors are recognized in our README and contributor documentation.

### Maintainer Responsibilities

Active, high-quality contributors may be invited to become maintainers, helping review submissions and guide the project direction.

## 📋 Templates and Resources

### Quick Start Template

Copy this template for new prompts:

```markdown
# [Your Prompt Title]

## Description
[What this prompt does and its intended use case]

## Usage
[How to use this prompt effectively]

## Prompt
```markdown

[Your prompt text here]

```

## Example Input

```markdown

[Sample input]

```

## Example Output

```markdown

[Expected output]

```

## Variations

- **[Variation Name]**: [Description]

## Tips

- [Tip 1]
- [Tip 2]

## Related Prompts

- `related-prompt.md` - Brief description

## Tags

`tag1` `tag2` `tag3`

```

## 📞 Contact

- **Issues**: Use GitHub issues for bugs and feature requests
- **Discussions**: Use GitHub discussions for questions and community chat
- **Maintainers**: Tag @maintainer-username for urgent issues

Thank you for contributing to the Prompt Library! Your contributions help developers, writers, and professionals worldwide work more effectively with AI tools.
