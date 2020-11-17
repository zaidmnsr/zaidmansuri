# ORMAE Microservices App


#### Below are components of Application.

  - User Interface 
  - API Gateway 
  - Authentication API 
  - Public Endpoints 
  - Internal APIs 
  - OAuthorization Server 
  - Long Running Workers/Jobs (~30mins) 
  - Queues (Like RabbitMQ, Bull, etc) 
  - Database 
  - Redis

#### Note: 

  > The Microservices backend Application is built on Java

  > UI (Frontend) is built on ReactJS


#### Below is Planned Strategy to implement above components of Application.

  - User Interface 
    [*Frontend Application in ReactJS and hosted on AWS S3 as static website and DNS can be mapped to AWS Cloudfront*]
  - API Gateway 
    [*AWS API Gateway service*]
  - Authentication API 
    [*AWS IAM to authenticate the API*]
  - Public Endpoints 
    [*AWS Ingress to route traffic inside kubernetes cluster*]
  - Internal APIs 
    [*Will be developed by development team for internal communication between microservices*]
  - OAuthorization Server 
    [*AWS Cognito*]
  - Long Running Workers/Jobs (~30mins) 
    [*Implement the application as type JOB in kubernetes manifests file and schedule to a separate node to avoid load on running server*]
  - Queues (Like RabbitMQ, Bull, etc) 
    [*Install redis on AWS EC2 machine. Preferrably on docker via docker-compose file. Allow Redis ports in security group to communicate with application*]
  - Database 
    [*Choice 1: MongoDB on AWS EC2 machine. Preferrably on docker via docker-compose file. Allow MongoDB ports in security group to communicate with application*
    *Choice 2: AWS DynamoDB. But this will require to segragate environments by creating schema*]
  - Redis 
    [*AWS Elasticache Service*]

### Objective 1

  - Strategy to follow for code collaboration should be *Feature Branch Workflow* 
  - Create separate branches for each features developed and naming should be *feature/<JIRA-ID>-Title-of-JIRA-assigned-to-develop-feature*
  - Create Pullrequest to merge feature in *dev* branch and delete the feature branch
  - Merge changes to *uat* branch after testing on dev branch
  - Merge changes to *prod* branch after uat testing and confirmation from Senior management/Lead
  - Deploy code to prod as per the release cycle

### Objective 2 

  - Setup Jenkins for CI/CD on AWS EC2 machine. Preferrably on docker via docker-compose file.
  - Create secret in Jenkins for AWS Access and Secret Key, AWS Docker registry credentials, Kubernetes config file, Sonar host URl, Slack url and server credentials
  - Create separate Declarative pipeline for each microservices to deploy in development environment.
  - Run Linting on Dockerfile
  - Run Maven Unit tests
  - Run Maven Dependency Vulnerability Analysis
  - Run Sonarqube analysis
  - Compile code
  - Create Docker Image
  - Scan Docker Image for vulnerabilities
  - Push Image to AWS ECR 
  - Deploy to k8s cluster


 