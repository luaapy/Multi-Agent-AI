"""
Prompt templates for comprehensive code analysis
"""

def get_review_prompt(code: str) -> str:
    return f"""Conduct thorough code analysis on the following implementation:

```python
{code}
```

CRITICAL RULES:
- Output ONLY ONE single Python file
- NO explanations, NO documentation text
- NO markdown code blocks (no ```)
- Just the final polished raw Python code
- Keep ALL code in ONE single file
- Do NOT create multiple files or suggest file structure

Analysis scope covering critical dimensions:

Code quality assessment examining structure and organization
Identify potential runtime errors and exception scenarios
Security vulnerability detection including injection risks
Performance bottlenecks affecting execution efficiency
Memory leak detection through allocation patterns
Resource management evaluating file and connection handling
Type safety verification checking annotations and conversions
Input validation gaps exposing attack vectors
Output sanitization preventing data leakage
Authentication weaknesses in access control
Authorization flaws allowing privilege escalation
Cryptographic implementation reviewing algorithm choices
Error handling completeness across all paths
Exception propagation examining stack traces
Logging practices balancing verbosity and security
Configuration hardening checking default values
Dependency vulnerabilities scanning imported libraries
API misuse detecting incorrect usage patterns
Concurrency issues including race conditions
Deadlock potential in locking mechanisms
Thread safety violations in shared state
Async/await correctness in coroutine usage
Database query optimization examining N+1 problems
SQL injection vulnerabilities in dynamic queries
NoSQL injection risks in document databases
Cross-site scripting vectors in output generation
Cross-site request forgery missing protections
Session management weaknesses in token handling
Password storage checking hashing algorithms
Encryption key management evaluating storage practices
TLS configuration reviewing cipher suites
Certificate validation ensuring proper checks
Path traversal vulnerabilities in file operations
Command injection risks in subprocess calls
XML external entity attacks in parser usage
Deserialization vulnerabilities in pickle usage
Regular expression denial of service patterns
Integer overflow possibilities in calculations
Buffer overflow risks in C extension usage
Time-of-check time-of-use race conditions
Symbolic link attacks in filesystem operations
Temporary file creation using secure methods
Random number generation checking cryptographic strength
Side-channel attack susceptibility in timing
Information disclosure through error messages
Business logic flaws violating requirements
Data validation enforcing constraints
State machine correctness in workflows
Idempotency ensuring safe retries
Atomicity checking transaction boundaries
Consistency maintaining invariants
Isolation preventing dirty reads
Durability guaranteeing persistence
Scalability limitations under load
Availability concerns affecting uptime
Maintainability evaluating code complexity
Testability assessing mock requirements
Documentation completeness for APIs
Code duplication identifying refactoring opportunities
Naming conventions following standards
Function length keeping functions focused
Class cohesion measuring single responsibility
Coupling minimizing dependencies
Abstraction levels maintaining appropriate layers
Design patterns applying correct solutions
SOLID principles adherence checking violations
DRY principle eliminating repetition
KISS principle avoiding unnecessary complexity
YAGNI principle removing unused features
Separation of concerns organizing by responsibility
Dependency inversion reducing concrete dependencies
Interface segregation avoiding fat interfaces
Open/closed principle enabling extension
Liskov substitution ensuring polymorphism
Single responsibility maintaining focus
Cyclomatic complexity measuring decision points
Cognitive complexity evaluating understandability
Code coverage identifying untested paths
Edge case handling for boundary conditions
Null reference prevention using optional types
Default value safety checking fallbacks
Magic number elimination using constants
Global state avoidance for predictability
Mutable state minimization reducing bugs
Side effect documentation making explicit
Pure function identification enabling testing
Referential transparency ensuring determinism
Function composition enabling reusability
Higher-order functions leveraging abstractions
Lazy evaluation optimizing performance
Memoization caching expensive computations
Tail call optimization enabling recursion
Generator usage for memory efficiency
Context manager proper resource cleanup
Decorator patterns enhancing functionality
Metaclass usage avoiding when simpler alternatives exist
Type hints completeness improving tooling
Generic types enabling reusable components
Protocol usage for structural subtyping
Literal types constraining values
Union types handling multiple cases
Optional types expressing nullability
TypedDict usage for structured dictionaries
NewType creating distinct types
Overload signatures documenting variants
Type guards narrowing types safely

Provide actionable recommendations prioritizing critical security issues and reliability improvements."""

def get_security_audit_prompt(code: str) -> str:
    return f"""Execute security-focused audit on implementation:

```python
{code}
```

CRITICAL RULES:
- Output ONLY ONE single Python file
- NO explanations, NO documentation text
- NO markdown code blocks (no ```)
- Just the final polished raw Python code
- Keep ALL code in ONE single file
- Do NOT create multiple files or suggest file structure

Security assessment framework:

Authentication mechanisms verifying identity proofs
Authorization controls enforcing access policies
Session management tracking user states
Token generation using cryptographic randomness
Token validation checking signatures and expiry
Password hashing using bcrypt or argon2
Salt generation ensuring uniqueness per password
Pepper usage adding server-side secret
Key derivation functions strengthening passwords
Multi-factor authentication adding verification layers
Brute force protection rate limiting attempts
Account lockout preventing credential stuffing
Password complexity enforcing strong policies
Credential rotation requiring periodic changes
Secrets management avoiding hardcoded values
Environment variables storing sensitive config
Secrets vault integration using dedicated systems
API key rotation automating credential refresh
Certificate management tracking expiration
Private key protection securing asymmetric keys
Public key pinning preventing MITM attacks
TLS version enforcement requiring modern protocols
Cipher suite selection choosing strong algorithms
Perfect forward secrecy enabling session keys
Certificate transparency checking CT logs
HSTS headers enforcing HTTPS usage
Content security policy preventing injection
X-Frame-Options defending against clickjacking
X-Content-Type-Options preventing MIME sniffing
Referrer policy controlling information leakage
Permissions policy restricting browser features
CORS configuration limiting cross-origin access
Input validation sanitizing untrusted data
Output encoding preventing script injection
Parameterized queries avoiding SQL injection
Prepared statements binding values safely
ORM usage abstracting database access
Whitelist validation accepting known good
Blacklist avoidance rejecting known bad insufficient
Length limits preventing buffer overflows
Format validation enforcing expected patterns
Character encoding preventing interpretation attacks
Canonicalization resolving equivalent representations
Path validation preventing traversal attacks
URL validation checking scheme and host
Email validation using RFC-compliant regex
Phone validation enforcing format standards
Credit card validation using Luhn algorithm
File upload restrictions limiting types and sizes
File content validation checking magic numbers
Antivirus scanning detecting malware
Sandbox execution isolating untrusted code
Least privilege principle minimizing permissions
Defense in depth layering security controls
Fail secure defaulting to safe state
Complete mediation checking every access
Security by design building in from start
Privacy by design protecting user data
Data minimization collecting only necessary
Purpose limitation using data as intended
Retention policies deleting old data
Right to erasure implementing deletion
Data portability enabling export
Consent management tracking permissions
Anonymization removing identifying information
Pseudonymization replacing with artificial identifiers
Differential privacy adding statistical noise
Homomorphic encryption computing on encrypted data
Secure multi-party computation distributing trust
Zero-knowledge proofs verifying without revealing
Blockchain immutability ensuring audit trail
Smart contract security avoiding reentrancy
Cryptographic signatures proving authenticity
Digital certificates establishing trust
Public key infrastructure managing certificates
Certificate revocation checking validity
OCSP stapling improving performance
DNS security extensions preventing spoofing
DNSSEC validation verifying responses
BGP security preventing route hijacking
Network segmentation isolating components
Firewall rules restricting traffic
Intrusion detection monitoring suspicious activity
Intrusion prevention blocking attacks
SIEM integration centralizing logs
Vulnerability scanning identifying weaknesses
Penetration testing simulating attacks
Red team exercises adversarial testing
Bug bounty programs crowdsourcing security
Responsible disclosure handling reports
Incident response planning for breaches
Disaster recovery maintaining business continuity
Backup encryption protecting archived data
Backup testing verifying restoration
Air-gapped backups offline protection
Immutable backups preventing tampering
Compliance requirements meeting regulations
GDPR adherence protecting EU citizens
CCPA compliance protecting California residents
HIPAA compliance protecting health information
PCI DSS compliance protecting payment data
SOC 2 certification demonstrating controls
ISO 27001 certification proving management system
NIST framework aligning with standards
OWASP guidelines following best practices
CWE classification categorizing weaknesses
CVE tracking known vulnerabilities

Deliver prioritized findings with remediation guidance and code examples for secure alternatives."""

def get_performance_review_prompt(code: str) -> str:
    return f"""Evaluate performance characteristics of implementation:

```python
{code}
```

CRITICAL RULES:
- Output ONLY ONE single Python file
- NO explanations, NO documentation text
- NO markdown code blocks (no ```)
- Just the final polished raw Python code
- Keep ALL code in ONE single file
- Do NOT create multiple files or suggest file structure

Performance analysis dimensions:

Time complexity analyzing algorithmic efficiency
Space complexity evaluating memory usage
Big O notation characterizing scaling behavior
Amortized analysis averaging over operations
Worst-case scenarios identifying bottlenecks
Best-case scenarios establishing lower bounds
Average-case scenarios typical performance
Profiling results measuring actual execution
Hotspot identification finding slow code
Call graph analysis tracing execution paths
Flame graph visualization showing time distribution
CPU utilization measuring processor usage
Memory utilization tracking allocation patterns
I/O operations counting disk and network access
Database queries analyzing execution plans
Query optimization improving SQL performance
Index usage leveraging database indexes
Denormalization trading normalization for speed
Caching strategies storing computed results
Cache invalidation ensuring freshness
Cache warming preloading frequently accessed data
Lazy loading deferring until needed
Eager loading fetching related data upfront
Batch processing grouping operations
Bulk operations reducing round trips
Connection pooling reusing database connections
Thread pooling managing concurrent execution
Process pooling distributing work
Async I/O non-blocking operations
Event loop utilizing single-threaded concurrency
Coroutines cooperative multitasking
Generators yielding values lazily
Iterators providing on-demand access
List comprehensions concise transformations
Generator expressions memory-efficient iteration
Map/filter/reduce functional operations
Lambda functions inline behavior
Memoization caching function results
Dynamic programming optimal substructure
Greedy algorithms local optimization
Divide and conquer problem decomposition
Binary search logarithmic lookup
Hash tables constant-time access
Balanced trees logarithmic operations
Heap data structures priority queues
Trie structures prefix matching
Bloom filters probabilistic membership
Skip lists probabilistic balancing
B-trees disk-optimized trees
LSM trees write-optimized storage
Columnar storage analytics optimization
Compression reducing data size
Serialization format choosing efficient encoding
Protocol buffers binary serialization
MessagePack compact representation
JSON parsing optimizing text processing
XML avoidance preferring alternatives
Regular expression optimization efficient patterns
String interning reducing duplicates
Copy-on-write sharing until modification
Object pooling reusing expensive objects
Flyweight pattern sharing common state
Singleton pattern single instance
Factory pattern object creation
Builder pattern complex construction
Prototype pattern cloning objects
Adapter pattern interface conversion
Decorator pattern behavior extension
Proxy pattern access control
Chain of responsibility request handling
Command pattern encapsulating actions
Iterator pattern sequential access
Mediator pattern centralized communication
Memento pattern state preservation
Observer pattern event notification
State pattern behavior variation
Strategy pattern algorithm selection
Template method pattern algorithm structure
Visitor pattern operation separation
Garbage collection minimizing pauses
Reference counting immediate reclamation
Generational collection focusing on young objects
Compacting collection defragmenting memory
Concurrent collection parallel processing
Incremental collection spreading work
Weak references allowing collection
Memory pools pre-allocating buffers
Stack allocation avoiding heap
Tail call elimination enabling recursion
Loop unrolling reducing overhead
Function inlining eliminating calls
Constant folding compile-time evaluation
Dead code elimination removing unused code
Common subexpression elimination reusing calculations
Strength reduction using cheaper operations
Vectorization SIMD parallelism
Parallelization multi-core utilization
Load balancing distributing work evenly
Sharding partitioning data
Replication copying for availability
Horizontal scaling adding machines
Vertical scaling bigger machines
Auto-scaling dynamic provisioning
CDN usage edge caching
DNS optimization reducing lookup time
HTTP/2 multiplexing concurrent streams
HTTP/3 QUIC protocol benefits
Compression reducing transfer size
Minification removing whitespace
Bundling combining files
Code splitting loading on demand
Tree shaking removing unused exports
Prefetching loading before needed
Prerendering generating static content
Service workers offline functionality
WebAssembly native performance
JIT compilation runtime optimization
AOT compilation upfront optimization

Provide concrete optimization recommendations with expected performance improvements and implementation examples."""