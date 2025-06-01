# Architecture Planner

## Description

Helps design and plan software architecture, including system design, component relationships, technology stack decisions, and scalability considerations. Provides structured architectural guidance for projects of any size.

## Usage

Describe your project requirements, constraints, and goals. Include information about expected scale, performance requirements, team size, and any existing systems. Works for both new projects and architectural refactoring.

## Prompt

```markdown
Help me design the software architecture for the following project:

**Project Overview:**
[Describe what the system should do and its main purpose]

**Requirements:**
- **Functional Requirements:**
  - [Core features and capabilities needed]
  - [User interactions and workflows]
  - [Data processing requirements]

- **Non-Functional Requirements:**
  - **Scale**: [Expected users, data volume, transaction volume]
  - **Performance**: [Response time, throughput requirements]
  - **Availability**: [Uptime requirements, disaster recovery needs]
  - **Security**: [Authentication, authorization, data protection needs]

**Constraints:**
- **Budget**: [Budget limitations or cost considerations]
- **Team**: [Team size, skill levels, experience with technologies]
- **Timeline**: [Development timeline and milestones]
- **Technology**: [Required technologies, existing systems to integrate]
- **Compliance**: [Regulatory or industry standards to follow]

**Current State:** [Existing systems, legacy code, or starting from scratch]

Please provide:

1. **High-Level Architecture**
   - System overview and major components
   - Architecture pattern recommendation (MVC, microservices, etc.)
   - Data flow and component interactions

2. **Technology Stack Recommendations**
   - Backend technologies and frameworks
   - Database choices and rationale
   - Frontend technologies
   - Infrastructure and deployment options

3. **Detailed Component Design**
   - Core services/modules breakdown
   - API design considerations
   - Data models and relationships

4. **Scalability Strategy**
   - How to handle growth
   - Performance optimization points
   - Caching strategies

5. **Security Architecture**
   - Authentication and authorization approach
   - Data protection measures
   - Security best practices

6. **Implementation Roadmap**
   - Development phases and priorities
   - MVP scope and incremental features
   - Risk mitigation strategies
```

## Example Input

```markdown
**Project Overview:**
A real-time collaboration platform for remote teams, similar to Slack but with integrated video calls, file sharing, and project management features.

**Requirements:**
- **Functional Requirements:**
  - Real-time messaging and channels
  - Video/audio calling for up to 50 participants
  - File upload and sharing (up to 100MB per file)
  - Task management and project boards
  - User authentication and team management

- **Non-Functional Requirements:**
  - **Scale**: 10,000 concurrent users, 100,000 total users
  - **Performance**: <200ms message delivery, <3s file upload
  - **Availability**: 99.9% uptime
  - **Security**: Enterprise-grade security, GDPR compliance

**Constraints:**
- **Budget**: $50k initial development budget
- **Team**: 5 full-stack developers, 1 DevOps engineer
- **Timeline**: 6 months to MVP, 12 months to full feature set
- **Technology**: Team has experience with React, Node.js, PostgreSQL
```

## Example Output

```markdown
# Collaboration Platform Architecture Design

## High-Level Architecture

### Architecture Pattern: Microservices with Event-Driven Communication
```

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Client    │    │  Mobile Client  │    │  Desktop App    │
│    (React)      │    │   (React Native)│    │   (Electron)    │
└─────────┬───────┘    └─────────┬───────┘    └─────────┬───────┘
          │                      │                      │
          └──────────────────────┼──────────────────────┘
                                 │
                    ┌─────────────┴─────────────┐
                    │     API Gateway           │
                    │   (Authentication +       │
                    │    Load Balancing)        │
                    └─────────────┬─────────────┘
                                  │
    ┌─────────────┬───────────────┼───────────────┬─────────────┐
    │             │               │               │             │
┌───▼───┐    ┌───▼───┐       ┌───▼───┐      ┌───▼───┐    ┌───▼───┐
│Message│    │ User  │       │ File  │      │Video  │    │Project│
│Service│    │Service│       │Service│      │Service│    │Service│
└───┬───┘    └───┬───┘       └───┬───┘      └───┬───┘    └───┬───┘
    │            │               │              │            │
    └────────────┼───────────────┼──────────────┼────────────┘
                 │               │              │
            ┌────▼────┐     ┌────▼────┐    ┌────▼────┐
            │PostgreSQL│     │   S3    │    │  Redis  │
            │(Primary) │     │(Files)  │    │(Cache)  │
            └─────────┘     └─────────┘    └─────────┘

```

## Technology Stack Recommendations

### Backend
- **Language**: Node.js with TypeScript (team familiarity)
- **Framework**: Express.js with Fastify for high-performance services
- **Real-time**: Socket.io for WebSocket connections
- **Message Queue**: Redis for pub/sub and job queues
- **Video**: WebRTC with Kurento Media Server for large calls

### Database
- **Primary**: PostgreSQL for structured data (users, teams, projects)
- **Cache**: Redis for sessions, real-time data, and message caching
- **File Storage**: AWS S3 or MinIO for file uploads
- **Search**: Elasticsearch for message search functionality

### Frontend
- **Framework**: React with TypeScript
- **State Management**: Redux Toolkit for complex state
- **Real-time**: Socket.io client
- **UI Library**: Material-UI or Ant Design for rapid development

### Infrastructure
- **Containerization**: Docker with Docker Compose for development
- **Orchestration**: Kubernetes for production (or start with simple VPS)
- **CI/CD**: GitHub Actions
- **Monitoring**: Prometheus + Grafana

## Detailed Component Design

### 1. Message Service
```typescript
interface MessageService {
  sendMessage(channelId: string, message: MessagePayload): Promise<void>
  getChannelHistory(channelId: string, limit: number): Promise<Message[]>
  subscribeToChannel(channelId: string, userId: string): void
}
```

- Real-time message delivery via Socket.io
- Message persistence in PostgreSQL
- Redis for message caching and pub/sub

### 2. User Service

```typescript
interface UserService {
  authenticate(credentials: LoginCredentials): Promise<AuthResult>
  createUser(userData: CreateUserRequest): Promise<User>
  updateUserStatus(userId: string, status: UserStatus): Promise<void>
}
```

- JWT-based authentication
- User management and team assignments
- Integration with external OAuth providers

### 3. File Service

- Secure file upload with virus scanning
- Progressive upload for large files
- Automatic thumbnail generation for images
- CDN integration for fast delivery

### 4. Video Service

- WebRTC peer-to-peer for small calls (<5 people)
- Selective Forwarding Unit (SFU) for larger calls
- Recording capabilities with cloud storage
- Screen sharing support

## Scalability Strategy

### Phase 1 (MVP): Monolithic Start

- Single Node.js application
- PostgreSQL primary database
- Redis for caching
- Supports up to 1,000 concurrent users

### Phase 2 (Growth): Service Separation

- Extract message service for independent scaling
- Add read replicas for database
- Implement horizontal scaling for video services
- CDN for static assets

### Phase 3 (Scale): Full Microservices

- Complete service decomposition
- Database sharding by team/organization
- Multi-region deployment
- Advanced caching strategies

## Security Architecture

### Authentication & Authorization

```
User → API Gateway → JWT Validation → Service Authorization
```

- JWT tokens with short expiry (15 minutes)
- Refresh token rotation
- Role-based access control (RBAC)
- Rate limiting per user/IP

### Data Protection

- End-to-end encryption for sensitive messages
- At-rest encryption for database and files
- HTTPS everywhere with HSTS headers
- Input validation and sanitization

## Implementation Roadmap

### Phase 1 (Months 1-2): Core MVP

**Goal**: Basic messaging and user management

- User authentication and team creation
- Real-time messaging in channels
- Basic file sharing
- Simple web client

**MVP Features:**

- Login/signup
- Create teams and channels
- Send/receive messages
- Upload/download files

### Phase 2 (Months 3-4): Enhanced Features

- Video calling (up to 10 participants)
- Message search
- Mobile-responsive design
- Basic project management features

### Phase 3 (Months 5-6): Production Ready

- Advanced video features (screen sharing, recording)
- Full project management integration
- Admin dashboard
- Comprehensive security features

### Risk Mitigation

1. **Technical Risks**:
   - Start with proven technologies
   - Build comprehensive testing early
   - Plan for database migration strategies

2. **Scalability Risks**:
   - Design with microservices in mind from day 1
   - Use feature flags for gradual rollouts
   - Monitor performance metrics continuously

3. **Security Risks**:
   - Regular security audits
   - Implement logging and monitoring
   - Have incident response plan ready

## Success Metrics

- Message delivery latency <200ms
- 99.9% uptime
- Support 10,000 concurrent users
- File upload success rate >99%
- Video call quality metrics

```

## Variations
- **Enterprise Architecture**: Focus on enterprise patterns and governance
- **Microservices Design**: Deep dive into service decomposition
- **Cloud-Native**: Emphasize cloud services and serverless architectures
- **Legacy Migration**: Focus on modernizing existing systems

## Tips
- Be specific about scale and performance requirements
- Include budget and timeline constraints for realistic recommendations
- Mention team expertise to align technology choices
- Consider starting simple and evolving the architecture over time
- Always include security and compliance considerations

## Related Prompts
- `code-review.md` - For reviewing architectural decisions in code
- `documentation-generator.md` - For creating architecture documentation
- `test-case-generator.md` - For testing architectural components

## Tags
`architecture` `system-design` `scalability` `technology-stack` `development` `planning`
