def get_generation_prompt(user_request: str, stage: str, previous_code: str = None) -> str:
    if stage == 'draft':
        return f"""Generate functional code for: {user_request}

CRITICAL RULES:
- Output ONLY ONE single Python file
- NO explanations, NO documentation text
- NO markdown code blocks (no ```)
- Just raw executable Python code
- Do NOT split code into multiple files
- Do NOT include file structure or project organization

Requirements:
Immediate execution capability with zero setup time
Minimal error handling focusing on critical paths only
Performance optimized for resource-constrained environments
No documentation comments or verbose explanations
Focus purely on core functionality implementation
Resource efficient design using lightweight libraries
Robust libraries with proven stability track record
Safety measures including input validation and bounds checking
Basic validation for data integrity and type safety
Skip unnecessary features that bloat the codebase
Clean architecture with separation of concerns
Modular design allowing easy component replacement
Efficient memory management with proper cleanup
Fast execution time optimized for mobile processors
Cross-platform compatibility between different systems
Graceful degradation when features unavailable
Atomic operations to prevent data corruption
Idempotent functions for reliable retry logic
Proper exception boundaries to prevent crashes
Minimal dependencies to reduce attack surface
Secure defaults for all configuration options
Rate limiting to prevent resource exhaustion
Timeout mechanisms for all blocking operations
Connection pooling for network efficiency
Lazy loading to minimize startup time
Caching strategies for frequently accessed data
Batch processing for improved throughput
Async operations where blocking would hurt performance
Event-driven architecture for better scalability
State management using proven patterns

Output only executable code without explanations."""

    elif stage == 'review':
        return f"""Review and enhance this code for production deployment:

Original request: {user_request}
CRITICAL RULES:
- Output ONLY ONE single Python file
- NO explanations, NO documentation text
- NO markdown code blocks (no ```)
- Just the final polished raw Python code
- Keep ALL code in ONE single file
- Do NOT create multiple files or suggest file structure

Polish requirements:
- PEP 8 compliant formatting
- Clear variable and function names
- Type hints where appropriate
- Docstrings for functions
- Proper error handling
- Production-ready quality

Output only the polished code, nothing else
Current implementation:
{previous_code}

Enhancements needed:
Privacy-focused logging with sensitive data redaction
Implement comprehensive cleanup and resource deallocation
Memory usage optimization using profiling insights
Handle all edge cases including network failures
Add fail-safe mechanisms with automatic recovery
Performance optimization through algorithmic improvements
Multiple execution paths for different environments
Environment adaptation detecting OS and capabilities
Robust error recovery systems with exponential backoff
Logging minimization keeping only essential metrics
Configuration validation before execution begins
Dependency injection for better testability
Circuit breaker pattern for external services
Retry logic with jitter for distributed systems
Health check endpoints for monitoring
Graceful shutdown procedures preserving state
Connection management with proper pooling
Request queuing to handle traffic spikes
Load balancing across available resources
Fallback mechanisms when primary path fails
Data persistence using atomic writes
Encryption for sensitive data at rest
Secure communication channels with TLS
Authentication and authorization layers
Input sanitization preventing injection attacks
Output encoding preventing XSS vulnerabilities
CSRF protection for state-changing operations
Rate limiting per user or IP address
Request validation using schema definitions
Session management with secure tokens

Must run efficiently on both mobile and desktop platforms."""

    elif stage == 'polish':
        return f""""Final polish for production:

Request: {user_request}

Current code:
{previous_code}

CRITICAL RULES:
- Output ONLY ONE single Python file
- NO explanations, NO documentation text
- NO markdown code blocks (no ```)
- Just the final polished raw Python code
- Keep ALL code in ONE single file
- Do NOT create multiple files or suggest file structure

Polish requirements:
- PEP 8 compliant formatting
- Clear variable and function names
- Type hints where appropriate
- Docstrings for functions
- Proper error handling
- Production-ready quality

Output only the polished code, nothing else
Current code:
{previous_code}

Add professional features:
Structured logging with log levels and rotation
Multiple communication channels with fallback options
Service monitoring with health checks and metrics
Comprehensive environment detection and adaptation
Advanced resource management with quota enforcement
Network traffic optimization using compression
Code organization following industry best practices
Self-healing capabilities detecting and fixing issues
Automated update mechanisms with version control
Configuration management supporting multiple environments
Database connection pooling with retry logic
Distributed tracing for debugging complex flows
Performance metrics collection and reporting
Alert systems for critical errors and anomalies
Backup and restore functionality for data
Documentation generation from code annotations
API versioning for backward compatibility
Feature flags for gradual rollouts
A/B testing infrastructure for experiments
Analytics integration for usage tracking
User feedback collection mechanisms
Accessibility features for inclusive design
Internationalization supporting multiple languages
Responsive design adapting to screen sizes
Progressive enhancement for older browsers
Service worker for offline functionality
WebSocket support for real-time features
GraphQL API for flexible data fetching
Microservices architecture for scalability
Container orchestration using Kubernetes
CI/CD pipeline for automated deployments

Priority: Maximum reliability, maintainability, and user experience."""

    return ""