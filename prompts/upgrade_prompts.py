"""
Prompt templates for comprehensive code modernization and enhancement
"""

def get_upgrade_prompt(code: str, focus: str) -> str:
    """Build upgrade analysis prompt with extensive focus areas"""
    
    base_prompt = f"""Conduct thorough modernization analysis on the following implementation with primary focus on {focus}:
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

"""

    if focus == 'security_modernization':
        return base_prompt + """
Security enhancement scope covering multiple layers:

Vulnerability remediation identifying exploitable weaknesses
Authentication strengthening using modern protocols
Authorization granularity implementing fine-grained controls
Cryptography modernization adopting current standards
TLS configuration enforcing strong cipher suites
Certificate management automating rotation and validation
Secrets management eliminating hardcoded credentials
Environment isolation separating sensitive data
Input sanitization preventing injection attacks
Output encoding defending against XSS vulnerabilities
SQL injection prevention using parameterized queries
Command injection blocking through input validation
Path traversal protection validating file operations
XML external entity prevention disabling dangerous features
Deserialization hardening avoiding pickle vulnerabilities
CSRF protection implementing token validation
Clickjacking defense adding frame options headers
MIME sniffing prevention setting content type headers
Content security policy restricting resource loading
CORS configuration limiting cross-origin access
Rate limiting preventing brute force attacks
Account lockout implementing progressive delays
Session management using secure token generation
Password hashing upgrading to argon2 or bcrypt
Salt generation ensuring cryptographic randomness
Key derivation strengthening password storage
Multi-factor authentication adding verification layers
OAuth2 implementation using authorization code flow
JWT validation checking signatures and claims
API key rotation automating credential refresh
Audit logging tracking security-relevant events
Error handling avoiding information disclosure
Exception sanitization removing sensitive details
Timing attack prevention using constant-time comparisons
Side-channel resistance avoiding observable differences
Memory scrubbing clearing sensitive data
Secure random generation using cryptographic sources
File permission enforcement applying least privilege
Temporary file creation using secure methods
Resource limits preventing denial of service
Input length validation blocking buffer overflows
Regex complexity limiting preventing ReDoS attacks
Upload validation checking file types and content
Antivirus integration scanning uploaded files
Sandbox execution isolating untrusted code
Code signing verifying integrity
Dependency scanning identifying vulnerable libraries
Supply chain security validating package sources
Container security hardening base images
Network segmentation isolating components
Firewall rules restricting unnecessary traffic
Intrusion detection monitoring anomalous behavior
Security headers implementing recommended protections
HSTS enforcement requiring HTTPS
Certificate pinning preventing MITM attacks
Subresource integrity verifying external resources
Feature policy restricting browser capabilities
Referrer policy controlling information leakage
Same-site cookies preventing CSRF
HTTP-only cookies blocking JavaScript access
Secure flag ensuring HTTPS transmission
Domain validation preventing cookie injection
Path validation limiting cookie scope
Expiration enforcement implementing timeout
Token revocation supporting logout
Concurrent session limiting preventing sharing
Device fingerprinting detecting anomalies
Geolocation tracking identifying suspicious access
Behavioral analysis detecting account takeover
Anomaly detection flagging unusual patterns
Threat intelligence integrating external feeds
Vulnerability disclosure establishing reporting process
Incident response planning breach procedures
Security training educating developers
Code review process mandatory inspection
Static analysis automated vulnerability detection
Dynamic analysis runtime security testing
Penetration testing simulating real attacks
Red team exercises adversarial simulation
Bug bounty program crowdsourcing discovery
Compliance adherence meeting regulatory requirements
GDPR implementation protecting privacy
HIPAA compliance securing health data
PCI DSS certification protecting payment information
SOC 2 audit demonstrating controls
ISO 27001 certification proving security management
NIST framework alignment following guidelines
OWASP top 10 addressing common vulnerabilities
CWE coverage preventing weakness classes
SANS top 25 mitigating dangerous errors
MITRE ATT&CK mapping attack techniques
Zero trust architecture assuming breach
Defense in depth layering controls
Fail secure defaulting to safe state
Complete mediation checking every access
Least privilege minimizing permissions
Separation of duties preventing fraud
Security by design building in protection
Privacy by design protecting user data
Data minimization collecting only necessary
Purpose limitation using as intended
Retention policies deleting old data
Encryption at rest protecting stored data
Encryption in transit securing communication
End-to-end encryption client-side protection
Homomorphic encryption computing on encrypted data
Secure multi-party computation distributing trust
Zero-knowledge proofs verifying without revealing
Blockchain integration ensuring immutability
Smart contract security avoiding common pitfalls
Quantum resistance preparing for future threats

Modern Python features adoption:
Structural pattern matching using match statements Python 3.10+
Union type syntax using pipe operator Python 3.10+
Type hinting improvements using Self and TypeGuard Python 3.11+
Exception groups handling multiple exceptions Python 3.11+
Task groups managing concurrent tasks Python 3.11+
Variadic generics supporting variable type parameters Python 3.11+
TypedDict inheritance combining typed dictionaries Python 3.11+
ParamSpec preserving callable signatures Python 3.10+
Concatenate combining parameter specifications Python 3.10+
TypeAlias explicit type alias declaration Python 3.10+
Final decorator preventing overriding Python 3.8+
Literal types constraining to specific values Python 3.8+
Protocol classes structural subtyping Python 3.8+
Positional-only parameters using slash syntax Python 3.8+
Assignment expressions walrus operator Python 3.8+
F-string debugging equals sign syntax Python 3.8+
Asyncio improvements performance enhancements Python 3.11+
Performance optimizations faster startup Python 3.11+
Error messages clarity improved debugging Python 3.11+
Deprecated function removal cleaning obsolete APIs
Security patches applying critical fixes
Cryptography updates using secure algorithms
Hash function upgrades avoiding MD5 and SHA1
Cipher upgrades removing RC4 and DES
TLS version enforcement requiring 1.2 or 1.3
Certificate validation improvements checking revocation
Random number generation using secrets module
Tempfile usage secure temporary file creation
Subprocess hardening preventing injection
Pickle avoidance using JSON or other formats
YAML safe loading preventing code execution
XML parsing disabling external entities
Regular expressions timeout preventing ReDoS
Path manipulation using pathlib for safety
Permission checking validating before operations
Resource cleanup using context managers
Exception handling avoiding bare except
Logging security redacting sensitive data
Configuration validation checking before use
Dependency management pinning versions
Virtual environments isolating dependencies
Package verification checking signatures
Supply chain security scanning dependencies
Container scanning identifying vulnerabilities
Infrastructure as code security policy enforcement
Secrets scanning preventing commits
Pre-commit hooks automated checks
CI/CD security scanning in pipeline
SAST integration static analysis
DAST integration dynamic analysis
IAST integration interactive analysis
RASP integration runtime protection
WAF deployment web application firewall
API gateway security centralized protection
Service mesh security mutual TLS
Zero trust networking micro-segmentation
Identity provider integration centralized authentication
Access management centralized authorization
Privilege management least privilege enforcement
Monitoring integration security event tracking
Alerting configuration anomaly notification
Dashboard creation security visibility
Compliance reporting automated evidence
Audit trail maintenance immutable logs
Forensic readiness evidence preservation
Backup encryption protecting archives
Disaster recovery security maintaining controls
Business continuity security sustaining operations

CRITICAL RULES:
- Output ONLY ONE single Python file
- NO explanations, NO documentation text
- NO markdown code blocks (no ```)
- Just the final polished raw Python code
- Keep ALL code in ONE single file
- Do NOT create multiple files or suggest file structure

Provide modernized code examples implementing current security best practices with detailed explanations of security improvements."""

    elif focus == 'performance':
        return base_prompt + """
Performance optimization scope across multiple dimensions:

Algorithmic complexity reduction improving time efficiency
Time complexity analysis Big O characterization
Space complexity optimization memory usage minimization
Amortized analysis averaging operation costs
Worst-case optimization eliminating bottlenecks
Data structure selection choosing optimal structures
Hash table usage constant-time lookups
Binary search tree logarithmic operations
Heap implementation priority queue efficiency
Trie structure prefix matching optimization
Graph algorithms shortest path and traversal
Dynamic programming optimal substructure exploitation
Memoization caching expensive computations
Tabulation bottom-up computation
Greedy algorithms local optimization strategies
Divide and conquer problem decomposition
Binary search logarithmic search efficiency
Two-pointer technique linear traversal optimization
Sliding window technique substring problem solving
Breadth-first search level-order traversal
Depth-first search exhaustive exploration
Topological sort dependency ordering
Union-find disjoint set operations
Segment tree range query optimization
Fenwick tree cumulative frequency
Sparse table static range queries
Suffix array string matching
KMP algorithm pattern matching
Rabin-Karp rolling hash matching
Bloom filter probabilistic membership
Skip list probabilistic balancing
B-tree disk-optimized operations
LSM tree write-optimized storage
Red-black tree balanced operations
AVL tree strictly balanced
Splay tree self-adjusting
Treap randomized balanced tree
Fibonacci heap efficient priority queue
Pairing heap simplified implementation
Van Emde Boas tree integer operations
Y-fast trie predecessor queries
Fusion tree word-level parallelism
Cache-oblivious algorithms automatic locality
External memory algorithms minimizing I/O
Streaming algorithms sublinear space
Approximation algorithms trading accuracy for speed
Randomized algorithms probabilistic guarantees
Online algorithms without future knowledge
Parallel algorithms utilizing multiple cores
Distributed algorithms coordinating machines
Lock-free algorithms avoiding contention
Wait-free algorithms guaranteed progress
Concurrent data structures thread-safe operations
Atomic operations hardware support
Memory barriers ordering guarantees
SIMD vectorization parallel processing
GPU acceleration massive parallelism
Quantum algorithms exponential speedup
Database optimization query performance
Index creation accelerating lookups
Composite index multi-column queries
Covering index avoiding table access
Partial index filtered indexing
Expression index computed columns
Full-text index text search
Spatial index geographic queries
Query rewriting logical optimization
Join optimization execution order
Subquery optimization flattening
Materialized view precomputed results
Partition pruning skipping irrelevant data
Parallel query execution multi-threaded
Connection pooling reusing connections
Prepared statements precompiled queries
Batch operations grouping modifications
Bulk inserts reducing round trips
Upsert operations atomic update-or-insert
Window functions analytical queries
Common table expressions query organization
Recursive queries hierarchical data
Lateral joins correlated subqueries
Array aggregation grouping results
JSON operations document queries
Explain plan analysis understanding execution
Vacuum operations reclaiming space
Analyze statistics query planner information
Reindex maintenance rebuilding indexes
Cluster ordering physical sorting
Partitioning horizontal splitting
Sharding distributing data
Replication read scaling
Read replicas load distribution
Write-ahead logging durability
Point-in-time recovery backup restoration
Streaming replication continuous sync
Logical replication selective sync
Foreign data wrappers external data
Caching strategies reducing computation
Memory caching in-memory storage
Disk caching SSD utilization
CDN caching edge distribution
Browser caching client storage
Application caching result storage
Query caching database results
Object caching ORM entities
Page caching rendered output
Fragment caching partial content
Cache invalidation freshness maintenance
Cache warming preloading data
Cache stampede prevention coordinated refresh
Cache aside read-through pattern
Write-through immediate persistence
Write-behind delayed persistence
Write-around bypass cache
Refresh-ahead proactive updates
Time-to-live expiration policy
Least recently used eviction strategy
Least frequently used access-based eviction
Most recently used inverse LRU
Random replacement simple eviction
Adaptive replacement cache size-aware
Two-queue frequency and recency
Multi-level cache hierarchical caching
Distributed cache cluster-wide sharing
Redis integration key-value caching
Memcached integration simple caching
Hazelcast integration in-memory grid
Async operations non-blocking I/O
Event loop single-threaded concurrency
Coroutines cooperative multitasking
Generators lazy evaluation
Asyncio framework Python async
ASGI servers asynchronous web
WebSockets real-time communication
Server-sent events one-way streaming
HTTP/2 multiplexing concurrent requests
HTTP/3 QUIC protocol
Compression reducing transfer size
Gzip compression general purpose
Brotli compression better ratios
Zstandard compression fast compression
Minification removing whitespace
Bundling combining files
Code splitting lazy loading
Tree shaking removing unused code
Lazy loading deferred initialization
Eager loading upfront fetching
Prefetching anticipatory loading
Prerendering static generation
Incremental static regeneration updating static
Server-side rendering dynamic generation
Client-side rendering browser rendering
Hydration attaching interactivity
Streaming rendering progressive display
Selective hydration partial interactivity
Islands architecture component isolation
Edge rendering proximity processing
Edge functions serverless computing
Lambda functions event-driven execution
Step functions workflow orchestration
SQS queuing asynchronous processing
SNS notifications pub-sub messaging
Kinesis streaming real-time data
DynamoDB NoSQL low-latency
ElastiCache managed caching
CloudFront CDN edge caching
S3 object storage static assets
CloudWatch monitoring performance metrics
X-Ray tracing distributed debugging
Resource optimization efficient utilization
CPU profiling identifying hotspots
Memory profiling tracking allocations
I/O profiling measuring throughput
Network profiling bandwidth analysis
Flame graphs visualizing time
Call graphs tracing execution
Line profiler statement timing
Memory profiler allocation tracking
Py-spy sampling profiler
cProfile standard profiler
profile deterministic profiling
timeit microbenchmarking
perf Linux profiling
dtrace system tracing
strace syscall tracing
ltrace library tracing
valgrind memory debugging
heaptrack heap profiling
massif heap visualization
cachegrind cache simulation
callgrind call graph profiling
helgrind thread debugging
drd data race detection
ThreadSanitizer race detection
AddressSanitizer memory errors
LeakSanitizer leak detection
MemorySanitizer uninitialized reads
UndefinedBehaviorSanitizer undefined behavior
Benchmark frameworks performance testing
Load testing scalability verification
Stress testing limit identification
Spike testing burst handling
Soak testing stability verification
Volume testing data handling
Scalability testing growth planning
Capacity planning resource estimation
Performance budgeting setting targets
Continuous profiling production monitoring
Distributed tracing request flow
APM tools application monitoring
Observability instrumentation visibility
Metrics collection quantitative data
Logging qualitative data
Alerting anomaly notification
Dashboards visual monitoring
SLIs service level indicators
SLOs service level objectives
SLAs service level agreements
Error budgets acceptable downtime
Canary deployments gradual rollout
Blue-green deployments zero downtime
Rolling updates sequential deployment
Feature flags conditional activation
Circuit breakers failure isolation
Bulkheads resource isolation
Rate limiting throttling requests
Backpressure flow control
Retry logic transient failure handling
Exponential backoff progressive delays
Jitter randomization thundering herd prevention
Timeout enforcement preventing hangs
Deadline propagation distributed timeouts
Graceful degradation partial functionality
Failover automatic switching
Disaster recovery backup systems
High availability redundancy
Fault tolerance error resilience
Chaos engineering failure injection
Game days incident simulation

Provide optimized code with performance measurements and expected improvements including Big O analysis and benchmark comparisons."""

    elif focus == 'quality':
        return base_prompt + """
Code quality enhancement scope covering maintainability and readability:

Style compliance adhering to community standards
PEP 8 compliance Python style guide
PEP 257 compliance docstring conventions
Black formatting automatic code style
isort imports import statement ordering
flake8 linting style checking
pylint analysis comprehensive checking
mypy type checking static type verification
pyright type checker Microsoft implementation
pyre type checker Facebook implementation
pytype type checker Google implementation
bandit security linter vulnerability detection
safety dependency checker known vulnerabilities
semgrep pattern matching custom rules
CodeQL semantic analysis GitHub security
SonarQube quality platform comprehensive analysis
Codacy automated review quality metrics
DeepSource continuous analysis AI-powered
Code Climate maintainability GPA
Coveralls coverage tracking test coverage
Codecov coverage analysis detailed reports
Radon complexity metrics cyclomatic complexity
McCabe complexity threshold complexity limit
Cognitive complexity understandability metric
Maintainability index composite metric
Technical debt quantification cost estimation
Naming conventions clarity and consistency
Variable naming descriptive identifiers
Function naming verb-based actions
Class naming noun-based entities
Module naming package organization
Constant naming uppercase convention
Private naming underscore prefix
Protected naming single underscore
Dunder methods double underscore
Abbreviation avoidance full words
Acronym clarity well-known only
Context specificity meaningful names
Length appropriateness not too short or long
Consistency maintenance uniform style
Pronounceability readable aloud
Searchability find and replace
Type encoding avoiding Hungarian notation
Boolean naming is/has/can prefix
Collection naming plural forms
Single responsibility one purpose
Open/closed principle extension without modification
Liskov substitution polymorphism correctness
Interface segregation focused interfaces
Dependency inversion abstraction dependency
DRY principle avoiding repetition
KISS principle simplicity over complexity
YAGNI principle no speculative features
Composition over inheritance favoring composition
Separation of concerns organizing by responsibility
Law of Demeter minimal coupling
Tell don't ask encapsulation respect
Command-query separation side effects clarity
Single level of abstraction consistent granularity
Principle of least surprise intuitive behavior
Convention over configuration sensible defaults
Explicit is better than implicit clarity
Simple is better than complex Zen of Python
Complex is better than complicated necessary complexity
Flat is better than nested shallow hierarchies
Sparse is better than dense whitespace usage
Readability counts understandability priority
Special cases aren't special enough consistency
Practicality beats purity pragmatic decisions
Errors should never pass silently explicit handling
Unless explicitly silenced intentional suppression
In the face of ambiguity refuse the temptation to guess
There should be one obvious way one clear path
Although that way may not be obvious at first learning curve
Now is better than never action over inaction
Although never is often better than right now careful timing
If the implementation is hard to explain bad idea
If the implementation is easy to explain good idea
Namespaces are one honking great idea explicit scope
Documentation completeness comprehensive coverage
Docstring presence function documentation
Module docstrings file-level description
Class docstrings type documentation
Method docstrings behavior documentation
Google style structured format
NumPy style scientific format
Sphinx style reStructuredText
Type hints static annotations
Return type documentation output specification
Parameter documentation input specification
Exception documentation error cases
Example usage code samples
Cross-references linking related
Version information change tracking
Author attribution contributor identification
License information usage rights
Deprecation warnings obsolescence notice
Since version introduction tracking
See also references related content
Notes additional information
Warnings important notices
References citations and links
Changelog modification history
Migration guide upgrade instructions
API reference complete documentation
Tutorial learning guide
How-to guide task instructions
Explanation conceptual understanding
Design decisions architectural rationale
Trade-offs compromise justification
Assumptions explicit statements
Limitations known constraints
Future work planned improvements
Contributing guidelines collaboration
Code of conduct behavior expectations
Issue templates problem reporting
Pull request templates change submission
Review checklist quality verification
Testing requirements coverage expectations
Continuous integration automated testing
Continuous deployment automated release
Version control Git best practices
Branch strategy workflow organization
Commit messages descriptive changes
Atomic commits single purpose
Feature branches isolated development
Hotfix branches urgent fixes
Release branches version preparation
Tag versions release marking
Semantic versioning version numbering
Changelog maintenance change documentation
Code review process peer inspection
Review etiquette constructive feedback
Approval requirements quality gate
Automated checks CI validation
Manual testing verification
Integration testing component interaction
End-to-end testing user workflows
Unit testing isolated components
Test coverage measurement percentage tested
Edge case testing boundary conditions
Error case testing failure scenarios
Performance testing speed verification
Security testing vulnerability scanning
Accessibility testing usability
Usability testing user experience
Compatibility testing platform support
Regression testing preventing breakage
Smoke testing basic functionality
Sanity testing quick verification
Alpha testing internal validation
Beta testing external validation
User acceptance testing stakeholder approval
Exploratory testing unscripted investigation
Fuzz testing random input
Mutation testing test effectiveness
Property-based testing generative testing
Snapshot testing output comparison
Visual regression testing UI changes
Contract testing API agreements
Load balancing distribution testing
Chaos testing failure injection
Canary testing gradual rollout
A/B testing variant comparison
Multivariate testing multiple factors
Analytics integration usage tracking
Error tracking exception monitoring
Performance monitoring speed tracking
User feedback collection satisfaction
Feature flags configuration
Configuration management environment handling
Environment variables external config
Secrets management credential protection
Dependency management version control
Package management distribution
Virtual environments isolation
Container images packaging
Docker optimization layer efficiency
Multi-stage builds size reduction
Health checks liveness probes
Readiness checks startup detection
Resource limits preventing overuse
Logging structured output
Metrics collection quantitative data
Tracing distributed debugging
Monitoring dashboards visualization
Alerting notification
On-call rotation responsibility
Incident response procedures
Postmortem analysis learning
Root cause analysis investigation
Corrective actions prevention
Continuous improvement iteration
Retrospectives team reflection
Knowledge sharing documentation
Mentoring skill transfer
Pair programming collaboration
Code walkthrough understanding
Architecture review design validation
Design patterns proven solutions
Refactoring improvement
Technical debt management
Legacy code modernization
Migration planning transition
Backward compatibility maintaining support
Deprecation process gradual removal
Sunset timeline end-of-life

Provide refactored code with improved readability, comprehensive documentation, and adherence to Python best practices with detailed explanations of improvements."""

    elif focus == 'modernization':
        return base_prompt + """
Comprehensive modernization scope leveraging latest Python capabilities:

Python version upgrade utilizing newest features
Structural pattern matching match/case statements Python 3.10+
Union type operator pipe syntax for unions Python 3.10+
Parameter specification ParamSpec for callables Python 3.10+
Type guard narrowing TypeGuard annotations Python 3.10+
Precise exception types more specific matching Python 3.10+
Parenthesized context managers multi-line with statements Python 3.10+
Better error messages enhanced debugging Python 3.10+
Faster performance CPython optimizations Python 3.11+
Exception groups handling multiple errors Python 3.11+
Task groups managing async tasks Python 3.11+
Self type referencing class type Python 3.11+
Variadic generics variable type parameters Python 3.11+
TypedDict inheritance combining typed dicts Python 3.11+
LiteralString string type safety Python 3.11+
Data class transforms custom decorators Python 3.11+
Tomllib standard library TOML parser Python 3.11+
Fine-grained error locations better tracebacks Python 3.11+
Zero-cost exceptions faster error handling Python 3.11+
Faster startup reduced initialization Python 3.11+
Adaptive specializing interpreter bytecode optimization Python 3.11+
Type parameter syntax generic classes Python 3.12+
Override decorator explicit overriding Python 3.12+
Buffer protocol improvements performance Python 3.12+
Per-interpreter GIL subinterpreter isolation Python 3.12+
Immortal objects shared immutables Python 3.12+
F-string improvements enhanced formatting Python 3.12+
Type statement explicit aliases Python 3.12+
Improved error suggestions helpful hints Python 3.12+
Pathlib improvements file operations Python 3.12+
asyncio improvements performance enhancements Python 3.12+
Deprecated removal cleaning obsolete APIs current version
Type annotations comprehensive coverage PEP 484
Generic types parameterized classes PEP 484
Protocol classes structural subtyping PEP 544
Literal types specific values PEP 586
Final decorator preventing override PEP 591
TypedDict typed dictionaries PEP 589
Positional-only parameters explicit syntax PEP 570
Assignment expressions walrus operator PEP 572
F-string equals debugging syntax PEP 498
Dataclasses structured data PEP 557
Dataclass transforms custom classes PEP 681
Context variables async-local state PEP 567
Asyncio improvements modern patterns PEP 492
Async generators async iteration PEP 525
Async comprehensions async expressions PEP 530
Coroutine definition async/await PEP 492
Module spec system import hooks PEP 451
Namespace packages implicit packages PEP 420
Importlib.resources resource access PEP 451
Path protocol os.PathLike PEP 519
Descriptor protocol attribute access PEP 252
Abstract base classes interface definition PEP 3119
Enum classes typed constants PEP 435
Integer division true division PEP 238
Print function print statement replacement PEP 3105
Exception chaining from clause PEP 3134
Unicode strings default strings PEP 3120
Dictionary comprehensions dict creation PEP 274
Set comprehensions set creation PEP 274
Set literals curly brace sets PEP 3100
Dictionary ordering insertion order guaranteed Python 3.7+
Underscores in numeric literals readability PEP 515
Keyword-only arguments explicit kwargs PEP 3102
Extended unpacking multiple assignment PEP 3132
Function annotations return types PEP 3107
Nonlocal statement closure modification PEP 3104
With statement context managers PEP 343
Yield expression generator send PEP 342
Absolute imports explicit imports PEP 328
Conditional expressions ternary operator PEP 308
Generator expressions lazy sequences PEP 289
Decorators function modification PEP 318
Built-in set set type PEP 218
Subprocess module process management PEP 324
Decimal type precise arithmetic PEP 327
Reversed iteration reverse traversal PEP 322
Collections module data structures PEP 3132
Itertools module iteration tools
Functools module higher-order functions
Operator module function versions
Heapq module heap operations
Bisect module binary search
Array module typed arrays
Struct module binary packing
Pickle protocol serialization
JSON module JavaScript objects
CSV module comma-separated
ConfigParser INI files
Argparse command-line
Logging framework log messages
Threading module concurrent threads
Multiprocessing module parallel processes
Concurrent.futures thread/process pools
Asyncio framework async I/O
Socket module network programming
Ssl module secure sockets
Http.client HTTP protocol
Urllib.request URL handling
Requests library HTTP for humans
Aiohttp async HTTP
Httpx modern HTTP
FastAPI web framework
Flask microframework
Django full-stack framework
SQLAlchemy ORM database
Alembic migrations schema versioning
Psycopg2 PostgreSQL adapter
Pymongo MongoDB driver
Redis-py Redis client
Celery task queue
RQ simple queue
Dramatiq distributed tasks
Pydantic data validation
Marshmallow serialization
Attrs classes without boilerplate
Cattrs structure/unstructure
Pytest testing framework
Unittest mock mocking
Hypothesis property testing
Tox test automation
Coverage.py coverage tool
Mypy type checker
Pyright type checker
Black formatter
Isort import sorter
Flake8 linter
Pylint checker
Bandit security
Pre-commit hooks
Poetry dependency management
Pipenv environment management
PDM modern package manager
Hatch project manager
Pyproject.toml metadata PEP 518
Build backend system PEP 517
Editable installs development mode PEP 660
Wheel format binary distribution PEP 427
Source distribution sdist format
Entry points plugin system
Package metadata standards PEP 621
Dependency specification version pinning
Lock files deterministic installs
Virtual environments isolation
Environment markers conditional dependencies
Extras optional dependencies
Development dependencies separate requirements
Production dependencies minimal runtime
CI integration automated testing
CD integration automated deployment
Container support Docker images
Cloud deployment AWS/GCP/Azure
Serverless functions Lambda/Cloud Functions
Kubernetes orchestration container management
Helm charts application packaging
Infrastructure as code Terraform/CloudFormation
Configuration management Ansible/Chef
Monitoring Prometheus/Grafana
Logging ELK/Loki
Tracing Jaeger/Zipkin
APM DataDog/New Relic
Error tracking Sentry/Rollbar
Analytics Mixpanel/Amplitude
Feature flags LaunchDarkly/Optimizely
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
Provide fully modernized code leveraging latest Python features with migration guide and compatibility notes."""

    elif focus == 'architecture':
        return base_prompt + """
Architectural improvement scope establishing robust foundation:

Design patterns implementing proven solutions
Creational patterns object creation
Factory method polymorphic construction
Abstract factory family creation
Builder complex construction
Prototype cloning objects
Singleton single instance
Object pool resource reuse
Dependency injection loose coupling
Structural patterns object composition
Adapter interface conversion
Bridge abstraction separation
Composite tree structures
Decorator behavior extension
Facade simplified interface
Flyweight shared state
Proxy access control
Behavioral patterns object collaboration
Chain of responsibility request passing
Command encapsulating actions
Interpreter language processing
Iterator sequential access
Mediator centralized communication
Memento state preservation
Observer event notification
State behavior variation
Strategy algorithm selection
Template method algorithm structure
Visitor operation separation
Architectural patterns system organization
Layered architecture horizontal separation
Hexagonal architecture ports and adapters
Clean architecture dependency inversion
Onion architecture concentric layers
Microservices architecture distributed services
Service-oriented architecture SOA
Event-driven architecture asynchronous messaging
CQRS command query separation
Event sourcing state from events
Domain-driven design business logic focus
Repository pattern data access
Unit of work transaction boundary
Specification pattern business rules
Factory pattern object creation
Service locator dependency lookup
Front controller request handling
Model-View-Controller separation of concerns
Model-View-ViewModel data binding
Model-View-Presenter view abstraction
Flux unidirectional data flow
Redux predictable state
Saga pattern distributed transactions
Outbox pattern reliable messaging
Inbox pattern idempotent processing
Circuit breaker fault tolerance
Bulkhead resource isolation
Retry pattern transient failures
Timeout pattern preventing hangs
Rate limiter throttling
Backpressure flow control
Load balancer distribution
Service mesh infrastructure
API gateway unified entry
Backend for frontend client-specific
Strangler fig gradual migration
Anti-corruption layer boundary protection
Published language shared model
Conformist downstream adherence
Customer-supplier upstream dependency
Partnership mutual dependency
Shared kernel shared code
Separate ways independent paths
Big ball of mud legacy chaos
SOLID principles object-oriented design
Single responsibility one reason to change
Open-closed extension without modification
Liskov substitution polymorphism correctness
Interface segregation client-specific interfaces
Dependency inversion abstraction dependency
DRY principle don't repeat yourself
KISS principle keep it simple
YAGNI principle you aren't gonna need it
Separation of concerns organizing responsibilities
Composition over inheritance flexible reuse
Program to interface not implementation
Encapsulation hiding implementation
Abstraction essential characteristics
Polymorphism multiple forms
Inheritance code reuse
Coupling degree of interdependence
Cohesion degree of relatedness
Modularity independent components
Reusability code sharing
Extensibility adding features
Maintainability ease of changes
Testability ease of testing
Scalability handling growth
Performance execution speed
Security protection measures
Reliability consistent behavior
Availability uptime guarantee
Durability data persistence
Consistency data correctness
Partition tolerance network failures
CAP theorem trade-offs
BASE basically available soft state eventual consistency
ACID atomicity consistency isolation durability
Transaction management data integrity
Locking strategies concurrency control
Optimistic locking version checking
Pessimistic locking row locking
Deadlock prevention ordering
Isolation levels read phenomena
Read uncommitted dirty reads
Read committed default level
Repeatable read phantom reads
Serializable strictest isolation
Saga coordination distributed transactions
Orchestration centralized control
Choreography decentralized events
Eventual consistency delayed propagation
Strong consistency immediate visibility
Causal consistency ordering guarantee
Sequential consistency program order
Linearizability real-time ordering
Serializability transaction ordering
Snapshot isolation consistent view
Multi-version concurrency control MVCC
Two-phase locking 2PL
Two-phase commit 2PC
Three-phase commit 3PC
Paxos consensus algorithm
Raft consensus algorithm
Byzantine fault tolerance malicious nodes
Gossip protocol peer-to-peer
Vector clocks causality tracking
Merkle trees efficient verification
Bloom filters membership testing
Consistent hashing distribution
Rendezvous hashing minimal disruption
Jump hash simple consistent
Virtual nodes load balancing
Sharding horizontal partitioning
Replication data copying
Master-slave replication write master
Master-master replication write anywhere
Multi-master replication conflict resolution
Leaderless replication quorum
Chain replication ordered writes
Quorum reads majority consensus
Quorum writes durability guarantee
Read repair fixing inconsistency
Anti-entropy background sync
Hinted handoff temporary storage
Conflict-free replicated data types CRDTs
Operational transformation concurrent edits
Differential synchronization delta sync
Load balancing request distribution
Round robin simple rotation
Least connections active tracking
Least response time performance
IP hash session affinity
Weighted round robin capacity
Weighted least connections balanced capacity
Random selection simple choice
Sticky sessions session affinity
Health checks liveness monitoring
Circuit breaker failure isolation
Retry logic transient failures
Timeout enforcement preventing hangs
Bulkhead resource isolation
Rate limiting request throttling
Token bucket rate algorithm
Leaky bucket smoothing
Fixed window simple counting
Sliding window accurate limiting
Sliding log precise tracking
Concurrency limiting simultaneous requests
Queue-based limiting backlog management
Priority queuing importance ordering
Fair queuing equitable sharing
Weighted fair queuing proportional
Class-based queuing traffic classes
Hierarchical queuing nested priorities
Cache replacement policies eviction
LRU least recently used
LFU least frequently used
MRU most recently used
Random replacement simple eviction
FIFO first in first out
LIFO last in first out
Adaptive replacement cache ARC
Two-queue 2Q
Multi-queue MQ
Clock approximation
Second chance modified FIFO
Cache coherence consistency
Cache invalidation freshness
Cache-aside lazy loading
Read-through automatic loading
Write-through synchronous persist
Write-behind asynchronous persist
Write-around bypass cache
Refresh-ahead proactive refresh
Message queue asynchronous communication
Point-to-point queue direct
Publish-subscribe broadcast
Request-reply synchronous
Fan-out parallel processing
Fan-in aggregation
Pipes and filters transformation
Message broker intermediary
Message bus shared infrastructure
Event bus event distribution
Command bus command routing
Query bus query handling
Dead letter queue failed messages
Poison message handling corruption
Idempotent consumer duplicate handling
Message deduplication uniqueness
Exactly-once delivery guarantee
At-least-once delivery retry
At-most-once delivery no retry
Message ordering sequence
Message priority importance
Message expiration time-to-live
Message routing destination
Content-based routing filter
Topic-based routing subscribe
Header-based routing metadata
Semantic router intelligent
Service discovery finding services
Service registry centralized directory
Health checking availability
Load balancing distribution
Circuit breaking fault tolerance
API versioning compatibility
Backward compatibility old clients
Forward compatibility new clients
Semantic versioning version numbering
API deprecation phasing out
API documentation specification
OpenAPI specification REST
GraphQL schema graph API
gRPC protocol buffers RPC
WebSocket bidirectional
Server-sent events one-way push
Webhook HTTP callbacks
Long polling simulated push
Comet streaming
BOSH bidirectional streams HTTP

CRITICAL RULES:
- Output ONLY ONE single Python file
- NO explanations, NO documentation text
- NO markdown code blocks (no ```)
- Just the final polished raw Python code
- Keep ALL code in ONE single file
- Do NOT create multiple files or suggest file structure

Provide architecturally sound code with design rationale, component diagrams, and implementation guide."""

    elif focus == 'testing':
        return base_prompt + """
Testing enhancement scope ensuring reliability and correctness:

Test strategy comprehensive coverage
Unit testing isolated components
Integration testing component interaction
System testing end-to-end flows
Acceptance testing user requirements
Regression testing preventing breakage
Smoke testing basic functionality
Sanity testing quick verification
Exploratory testing unscripted investigation
Performance testing speed benchmarks
Load testing capacity limits
Stress testing breaking points
Spike testing burst handling
Soak testing stability over time
Volume testing data handling
Scalability testing growth capability
Security testing vulnerability scanning
Penetration testing simulated attacks
Fuzz testing random inputs
Property-based testing generative
Mutation testing test effectiveness
Snapshot testing output comparison
Visual regression testing UI changes
Contract testing API agreements
Component testing React/Vue
E2E testing Selenium/Playwright
API testing REST/GraphQL
Database testing data layer
Mock testing isolated units
Stub testing simplified dependencies
Spy testing behavior verification
Fake testing lightweight alternatives
Test doubles general replacements
Test fixtures setup data
Test factories generating data
Test builders fluent creation
Test data management test databases
Test isolation independence
Test repeatability consistent results
Test automation CI integration
Test parallelization concurrent execution
Test reporting results visualization
Test coverage measuring percentage
Branch coverage decision paths
Statement coverage executed lines
Function coverage called functions
Condition coverage boolean expressions
Path coverage execution paths
MC/DC coverage critical systems
Boundary testing edge cases
Equivalence partitioning input classes
Decision table testing combinations
State transition testing state machines
Use case testing scenarios
Error guessing experience-based
Checklist-based testing structured
Risk-based testing priority areas
Pairwise testing parameter combinations
Orthogonal array testing systematic coverage
All-pairs testing interaction coverage
Combinatorial testing multiple factors
Model-based testing specification-driven
Keyword-driven testing abstraction layer
Data-driven testing parameterized
Behavior-driven testing BDD
Test-driven development TDD
Acceptance test-driven development ATDD
Specification by example executable specs
Given-When-Then scenario format
Arrange-Act-Assert test structure
Setup-Exercise-Verify-Teardown SEVT
Four-phase test pattern structure
AAA pattern common structure
Test naming conventions descriptive
Test organization folder structure
Test discovery automatic finding
Test selection running subsets
Test filtering criteria-based
Test tagging categorization
Test markers pytest markers
Test fixtures pytest fixtures
Test parametrization multiple inputs
Test mocking unittest.mock
Test patching temporary replacement
Test assertions verification
Custom assertions domain-specific
Soft assertions collecting failures
Assertion libraries rich comparisons
Hamcrest matchers expressive
AssertJ fluent assertions
Truth Google assertions
Chai JavaScript assertions
Jest expect API
Testing library queries
React testing library user-centric
Vue test utils component testing
Angular testing utilities
Enzyme React deprecated
Cypress modern E2E
Playwright cross-browser
Selenium WebDriver classic
Puppeteer Chrome automation
TestCafe no WebDriver
Nightwatch.js E2E framework
WebdriverIO sync API
Protractor Angular deprecated
Karma test runner
Jasmine BDD framework
Mocha test framework
QUnit jQuery testing
AVA concurrent tests
Tape minimal testing
Tap test anything protocol
Lab Hapi testing
Code test framework
Ava minimal config
Vitest Vite-native
Playwright component testing
Storybook component development
Chromatic visual testing
Percy visual review
Applitools visual AI
BackstopJS visual regression
Hermione screenshot testing
Gemini screenshot tool
WebdriverCSS visual regression
PhantomCSS headless visual
Wraith responsive testing
Shoov visual monitoring
Needle Python screenshots
Vizregress visual comparison
Pixelmatch image diff
Resemble.js image analysis
Looks same image comparison
Blink-diff perceptual diff
JUnit standard Java
TestNG flexible Java
NUnit .NET testing
xUnit .NET modern
MSTest Microsoft testing
RSpec Ruby BDD
Minitest Ruby simple
Cucumber BDD tool
SpecFlow .NET Cucumber
Behave Python BDD
Lettuce Python BDD
pytest Python modern
unittest Python standard
nose Python discovery
doctest Python embedded
Hypothesis property-based
faker fake data
factory_boy model factories
responses mock requests
requests-mock HTTP mock
responses HTTP stubbing
betamax record/replay
VCR.py HTTP recording
HTTPretty HTTP mock
aioresponses async mock
pytest-asyncio async testing
pytest-mock pytest fixtures
pytest-cov coverage plugin
pytest-xdist parallel tests
pytest-bdd BDD plugin
pytest-django Django plugin
pytest-flask Flask plugin
coverage.py measure coverage
tox test automation
nox flexible automation
invoke task execution
robot framework keyword-driven
Gauge Markdown specs
FitNesse wiki testing
Concordion spec by example
JBehave Java BDD
Serenity BDD reporting
Allure test reporting
ReportPortal test analysis
TestRail test management
Zephyr test management
qTest test management
PractiTest test platform
TestLodge simple management
Testpad manual testing
TestRail integration
Jira integration
Jenkins integration
GitLab CI integration
GitHub Actions workflows
CircleCI pipeline
Travis CI legacy
Azure Pipelines Microsoft
AWS CodePipeline Amazon
Google Cloud Build
Bitbucket Pipelines
Bamboo Atlassian
TeamCity JetBrains
Drone lightweight CI
Buildkite hybrid CI
Semaphore fast CI
CodeShip Docker CI
AppVeyor Windows CI
Wercker container CI
Codefresh Kubernetes
Spinnaker CD platform
ArgoCD GitOps CD
Flux GitOps operator
Tekton Kubernetes native
Jenkins X cloud native

CRITICAL RULES:
- Output ONLY ONE single Python file
- NO explanations, NO documentation text
- NO markdown code blocks (no ```)
- Just the final polished raw Python code
- Keep ALL code in ONE single file
- Do NOT create multiple files or suggest file structure

Provide comprehensive test suite with unit, integration, and E2E tests, achieving high coverage with clear documentation."""

    return base_prompt + """
General improvement analysis covering multiple dimensions:

Code quality overall assessment
Security review vulnerability identification
Performance optimization efficiency improvements
Maintainability enhancement readability upgrades
Architecture evaluation design patterns
Testing coverage test completeness
Documentation completeness clarity improvements
Dependency management version updates
Best practices adherence standard compliance
Modern features adoption latest capabilities
Scalability assessment growth readiness
Reliability verification robustness testing
Monitoring integration observability
Error handling resilience improvements
Configuration management environment handling
Deployment readiness production preparation

CRITICAL RULES:
- Output ONLY ONE single Python file
- NO explanations, NO documentation text
- NO markdown code blocks (no ```)
- Just the final polished raw Python code
- Keep ALL code in ONE single file
- Do NOT create multiple files or suggest file structure

Provide comprehensive upgrade recommendations with prioritized action items and implementation examples."""

def get_refactoring_prompt(code: str, pattern: str) -> str:
    """Build pattern-specific refactoring prompt"""
    
    return f"""Apply {pattern} refactoring pattern to the following code:

```python
{code}
```

Refactoring objectives and constraints:

Pattern application correctly implementing {pattern}
Code preservation maintaining existing functionality
Backward compatibility ensuring no breaking changes
Test coverage maintaining or improving tests
Performance consideration avoiding degradation
Readability improvement enhancing understandability
Maintainability enhancement simplifying future changes
Documentation updates reflecting changes
Type safety preservation static type correctness
Error handling maintaining robustness
Edge case coverage handling boundaries
Resource management proper cleanup
Concurrency safety thread-safe operations
Security maintenance preserving protections
API compatibility stable interfaces
Configuration compatibility existing settings
Database compatibility schema preservation
Dependency compatibility library versions
Migration guide providing upgrade path
Rollback strategy enabling reversion
Monitoring continuity maintaining observability
Logging consistency structured output
Metrics preservation quantitative tracking
Alerting compatibility notification consistency
Testing strategy verification approach
Integration testing component interaction
System testing end-to-end verification
Performance testing speed validation
Load testing capacity confirmation
Stress testing limit identification
Security testing vulnerability scanning
Regression testing preventing breakage
Smoke testing basic functionality
Sanity testing quick verification
Acceptance testing requirement satisfaction
User documentation updating guides
Developer documentation technical details
API documentation interface specification
Architecture documentation design rationale
Decision records documenting choices
Change log modification tracking
Version bump semantic versioning
Release notes user-facing changes
Breaking changes explicit warnings
Deprecation notices phase-out timeline
Migration timeline transition period
Support policy assistance duration
Training materials learning resources
Communication plan stakeholder notification
Stakeholder approval sign-off process
Code review inspection
Pair programming collaboration
Team consensus agreement
Risk assessment impact analysis
Contingency planning failure scenarios
Success criteria measurable goals
Performance benchmarks quantitative targets
Quality metrics assessment criteria
Security audit vulnerability assessment
Compliance check regulatory adherence
License compatibility legal review
Patent review intellectual property
Third-party approval external dependencies
Customer validation user acceptance
Beta testing early access
Canary deployment gradual rollout
Feature flag conditional activation
A/B testing variant comparison
Monitoring dashboard operational visibility
Alert configuration issue notification
Incident response problem handling
Rollback procedure failure recovery
Postmortem analysis learning process
Continuous improvement iteration cycle
Feedback collection user input
Issue tracking problem management
Feature requests enhancement proposals
Technical debt acknowledgment
Future work planned improvements
Known limitations documented constraints
Performance characteristics expected behavior
Scaling considerations growth planning
Operational requirements deployment needs
Infrastructure changes platform updates
Configuration changes settings modifications
Environment updates deployment environments
Dependency updates library upgrades
Database migrations schema changes
API version updates interface evolution
Protocol changes communication updates
Authentication changes security updates
Authorization changes access control
Logging format changes output structure
Metrics format changes measurement structure
Monitoring integration observability platform
Error tracking exception monitoring
Performance monitoring speed tracking
User analytics behavior tracking
Business metrics KPI monitoring
Cost monitoring resource tracking
Capacity planning growth estimation
Resource optimization efficiency improvements
Automation opportunities manual elimination
Tool integration workflow enhancement
Process improvement efficiency gains
Team collaboration communication enhancement
Knowledge sharing documentation
Skill development training
Best practice adoption standard implementation
Innovation opportunity exploration
Experiment design hypothesis testing
Prototype development proof of concept
Proof of value business justification
Return on investment financial analysis
Total cost ownership expense evaluation

CRITICAL RULES:
- Output ONLY ONE single Python file
- NO explanations, NO documentation text
- NO markdown code blocks (no ```)
- Just the final polished raw Python code
- Keep ALL code in ONE single file
- Do NOT create multiple files or suggest file structure

Provide refactored code implementing {pattern} with detailed explanation of changes, benefits, and any trade-offs or considerations."""
