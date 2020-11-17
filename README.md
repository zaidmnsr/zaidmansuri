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

  - User Interface [*Frontend Application in ReactJS and hosted on AWS S3 as static website and DNS can be mapped to AWS Cloudfront*]
  - API Gateway [*AWS API Gateway service*]
  - Authentication API [*AWS IAM to authenticate the API*]
  - Public Endpoints [*AWS Ingress to route traffic inside kubernetes cluster*]
  - Internal APIs [*Will be developed by development team for internal communication between microservices*]
  - OAuthorization Server [*AWS Cognito*]
  - Long Running Workers/Jobs (~30mins) [*Implement the application as type JOB in kubernetes manifests file and schedule to a separate node to avoid load on running server*]
  - Queues (Like RabbitMQ, Bull, etc) [*Install redis on AWS EC2 machine. Preferrably on docker via docker-compose file. Allow Redis ports in security group to communicate with application*]
  - Database [*Choice 1: MongoDB on AWS EC2 machine. Preferrably on docker via docker-compose file. Allow MongoDB ports in security group to communicate with application*
  *Choice 2: AWS DynamoDB. But this will require to segragate environments by creating schema*]
  - Redis [*AWS Elasticache Service*]

### Objective 1

  - Strategy to follow for code collaboration should be *Feature Branch Workflow* 
  - Create separate branches for each features developed and naming should be *feature/<JIRA-ID>-Title-of-JIRA-assigned-to-develop-feature*