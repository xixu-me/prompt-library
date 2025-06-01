# Security Policy

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability in the Prompt Library, please report it responsibly:

### How to Report

1. **Email**: Send details to <i@xi-xu.me> or create a private security advisory on GitHub
2. **Include**:
   - Description of the vulnerability
   - Steps to reproduce the issue
   - Potential impact assessment
   - Suggested fix (if available)

### What to Expect

- **Acknowledgment**: We'll acknowledge receipt within 48 hours
- **Assessment**: Initial assessment within 5 business days
- **Disclosure**: Coordinated disclosure after fix is available

### Security Considerations for Prompts

While this is primarily a documentation repository, please be aware that:

1. **Prompt Injection**: Some prompts may be vulnerable to injection attacks when used with AI systems
2. **Sensitive Data**: Avoid including real sensitive data in examples
3. **Malicious Use**: Consider how prompts might be misused and include appropriate warnings

### Safe Usage Guidelines

- Always validate and sanitize inputs when using prompts in production
- Be cautious with prompts that handle user-generated content
- Review prompt outputs before using in sensitive contexts
- Follow your AI provider's security guidelines and terms of service

## Security Best Practices

When contributing to or using the Prompt Library:

1. **No Secrets**: Never include API keys, passwords, or sensitive information in prompts or examples
2. **Sanitize Examples**: Use placeholder data or properly anonymized examples
3. **Consider Context**: Think about how prompts might be misused or exploited
4. **Report Issues**: If you notice potential security concerns in existing prompts, please report them

Thank you for helping keep the Prompt Library secure for everyone!
