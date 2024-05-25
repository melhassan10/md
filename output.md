```
1
One of the criteria for a new deployment is that the customer wants to use AWS Storage Gateway. However you are not sure whether you should use gateway-
cached volumes or gateway-stored volumes or even what the differences are. Which statement below best describes those differences?
A. Gateway-cached lets you store your data in Amazon Simple Storage Service (Amazon S3) and retain a copy of frequently accessed data subsets locall
B. Gateway-stored enables you to configure youron-premises gateway to store all your data locally and then asynchronously back up point-in-time snapshots of
this data to Amazon S3.
C. Gateway-cached is free whilst gateway-stored is not.
D. Gateway-cached is up to 10 times faster than gateway-stored.
E. Gateway-stored lets you store your data in Amazon Simple Storage Service (Amazon S3) and retain a copy of frequently accessed data subsets locall
F. Gateway-cached enables you to configure youron-premises gateway to store all your data locally and then asynchronously back up point-in-time snapshots of
this data to Amazon S3.
```

```
2
A user is storing a large number of objects on AWS S3. The user wants to implement the search functionality among the objects. How can the user achieve this?
A. Use the indexing feature of S3.
B. Tag the objects with the metadata to search on that.
C. Use the query functionality of S3.
D. Make your own DB system which stores the S3 metadata for the search functionalit
```

```
3
You are migrating an internal sewer on your DC to an EC2 instance with EBS volume. Your server disk usage is around 500GB so you just copied all your data to
a 2TB disk to be used with AWS Import/Export. Where will the data be imported once it arrives at Amazon?
A. to a 2TB EBS volume
B. to an S3 bucket with 2 objects of 1TB
C. to an 500GB EBS volume
D. to an S3 bucket as a 2TB snapshot
```

```
4
A client needs you to import some existing infrastructure from a dedicated hosting provider to AWS to try and save on the cost of running his current website. He
also needs an automated process that manages backups, software patching, automatic failure detection, and recovery. You are aware that his existing set up
currently uses an Oracle database. Which of the following AWS databases would be best for accomplishing this task?
A. Amazon RDS
B. Amazon Redshift
C. Amazon SimpIeDB
D. Amazon EIastiCache
```

```
5
Do Amazon EBS volumes persist independently from the running life of an Amazon EC2 instance?
A. Yes, they do but only if they are detached from the instance.
B. No, you cannot attach EBS volumes to an instance.
C. No, they are dependent.
D. Yes, they d
```

```
6
Does DynamoDB support in-place atomic updates?
A. Yes
B. No
C. It does support in-place non-atomic updates
D. It is not defined
```

```
7
Your manager has just given you access to multiple VPN connections that someone else has recently set up between all your company's offices. She needs you to
make sure that the communication between the VPNs is secure. Which of the following services would be best for providing a low-cost hub-and-spoke model for
primary or backup connectMty between these remote offices?
A. Amazon C|oudFront
B. AWS Direct Connect
C. AWS C|oudHSM
D. AWS VPN CIoudHub
```

```
8
You are in the process of creating a Route 53 DNS failover to direct traffic to two EC2 zones. Obviously, if one fails, you would like Route 53 to direct traffic to the
other region. Each region has an ELB with some instances being distributed. What is the best way for you to configure the Route 53 health check?
A. Route 53 doesn't support ELB with an internal health check.You need to create your own Route 53 health check of the ELB
B. Route 53 natively supports ELB with an internal health chec
C. Turn "Eva|uate target health" off and "Associate with Health Check" on and R53 will use the ELB's internal health check.
D. Route 53 doesn't support ELB with an internal health chec
E. You need to associate your resource record set for the ELB with your own health check
F. Route 53 natively supports ELB with an internal health chec
G. Turn "Eva|uate target health" on and "Associate with Health Check" off and R53 will use the ELB's internal health check.
```

```
9
While using the EC2 GET requests as URLs, the is the URL that serves as the entry point for the web service.
A. token
B. endpoint
Passing Certification Exams Made Easy
visit - https://www.2PassEasy.com
Welcome to download the Newest 2passeasy AWS-Solution-Architect-Associate dumps
https://www.2passeasy.com/dumps/AWS-Solution-Architect-Associate/ (1487 New Questions)
C. action
D. None of these
```

```
10
You are checking the workload on some of your General Purpose (SSD) and Provisioned IOPS (SSD) volumes and it seems that the I/O latency is higher than you
require. You should probably check the to make sure that your application is not trying to drive more IOPS than you have
provisioned.
A. Amount of IOPS that are available
B. Acknowledgement from the storage subsystem
C. Average queue length
D. Time it takes for the I/O operation to complete
```

```
10
Which of the below mentioned options is not available when an instance is launched by Auto Scaling with EC2 Classic?
A. Public IP
B. Elastic IP
C. Private DNS
D. Private IP
```

```
13
You have been given a scope to deploy some AWS infrastructure for a large organisation. The requirements are that you will have a lot of EC2 instances but may
need to add more when the average utilization of your Amazon EC2 fileet is high and conversely remove them when CPU utilization is low. Which AWS services
would be best to use to accomplish this?
A. Auto Scaling, Amazon CIoudWatch and AWS Elastic Beanstalk
B. Auto Scaling, Amazon CIoudWatch and Elastic Load Balancing.
C. Amazon CIoudFront, Amazon CIoudWatch and Elastic Load Balancing.
D. AWS Elastic Beanstalk , Amazon CIoudWatch and Elastic Load Balancin
```

```
17
You are building infrastructure for a data warehousing solution and an extra request has come through that there will be a lot of business reporting queries running
all the time and you are not sure if your current DB instance will be able to handle it. What would be the best solution for this?
A. DB Parameter Groups
B. Read Replicas
C. Multi-AZ DB Instance deployment
D. Database Snapshots
```

```
22
Much of your company's data does not need to be accessed often, and can take several hours for retrieval time, so it's stored on Amazon Glacier. However
someone within your organization has expressed concerns that his data is more sensitive than the other data, and is wondering whether the high
level of encryption that he knows is on S3 is also used on the much cheaper Glacier service. Which of the following statements would be most applicable in
regards to this concern?
A. There is no encryption on Amazon Glacier, that's why it is cheaper.
B. Amazon Glacier automatically encrypts the data using AES-128 a lesser encryption method than Amazon S3 but you can change it to AES-256 if you are willing
to pay more.
C. Amazon Glacier automatically encrypts the data using AES-256, the same as Amazon S3.
D. Amazon Glacier automatically encrypts the data using AES-128 a lesser encryption method than Amazon S3.
```

```
27
In Amazon RDS, security groups are ideally used to:
A. Define maintenance period for database engines
B. Launch Amazon RDS instances in a subnet
C. Create, describe, modify, and delete DB instances
D. Control what IP addresses or EC2 instances can connect to your databases on a DB instance
```

```
29
A user has launched 10 EC2 instances inside a placement group. Which of the below mentioned statements is true with respect to the placement group?
A. All instances must be in the same AZ
B. All instances can be across multiple regions
C. The placement group cannot have more than 5 instances
D. All instances must be in the same region
```

```
32
You have been doing a lot of testing of your VPC Network by deliberately failing EC2 instances to test whether instances are failing over properly. Your customer
who will be paying the AWS bill for all this asks you if he being charged for all these instances. You try to explain to him how the billing works on EC2 instances to
the best of your knowledge. What would be an appropriate response to give to the customer
in regards to this?
A. Billing commences when Amazon EC2 AM instance is completely up and billing ends as soon as the instance starts to shutdown.
B. Billing only commences only after 1 hour of uptime and billing ends when the instance terminates.
C. Billing commences when Amazon EC2 initiates the boot sequence of an AM instance and billing ends when the instance shuts down.
D. Billing commences when Amazon EC2 initiates the boot sequence of an AM instance and billing ends as soon as the instance starts to shutdown.
```

```
37
You log in to IAM on your AWS console and notice the following message. "Delete your root access keys." Why do you think IAM is requesting this?
A. Because the root access keys will expire as soon as you log out.
B. Because the root access keys expire after 1 week.
C. Because the root access keys are the same for all users.
D. Because they provide unrestricted access to your AWS resource
```

```
39
Once again your customers are concerned about the security of their sensitive data and with their latest enquiry ask about what happens to old storage devices on
AWS. What would be the best answer to this QUESTION ?
A. AWS reformats the disks and uses them again.
B. AWS uses the techniques detailed in DoD 5220.22-M to destroy data as part of the decommissioning process.
C. AWS uses their own proprietary software to destroy data as part of the decommissioning process.
D. AWS uses a 3rd party security organization to destroy data as part of the decommissioning proces
```

```
43
A customer enquires about whether all his data is secure on AWS and is especially concerned about Elastic Map Reduce (EMR) so you need to inform him of
some of the security features in place for AWS. Which of the below statements would be an incorrect response to your customers enquiry?
A. Amazon ENIR customers can choose to send data to Amazon S3 using the HTTPS protocol for secure transmission.
B. Amazon S3 provides authentication mechanisms to ensure that stored data is secured against unauthorized access.
C. Every packet sent in the AWS network uses Internet Protocol Security (IPsec).
D. Customers may encrypt the input data before they upload it to Amazon S3.
```

```
48
You are in the process of building an online gaming site for a client and one of the requirements is that it must be able to process vast amounts of data easily.
Which AWS Service would be very helpful in processing all this data?
A. Amazon S3
B. AWS Data Pipeline
C. AWS Direct Connect
D. Amazon EMR
```

```
50
You need to change some settings on Amazon Relational Database Service but you do not want the database to reboot immediately which you know might
happen depending on the setting that you change. Which of the following will cause an immediate DB instance reboot to occur?
A. You change storage type from standard to PIOPS, and Apply Immediately is set to true.
B. You change the DB instance class, and Apply Immediately is set to false.
C. You change a static parameter in a DB parameter group.
D. You change the backup retention period for a DB instance from 0 to a nonzero value or from a nonzero value to 0, and Apply Immediately is set to false.
```

```
52
Having set up a website to automatically be redirected to a backup website if it fails, you realize that there are different types of failovers that are possible. You
need all your resources to be available the majority of the time. Using Amazon Route 53 which configuration would best suit this requirement?
A. Active-active failover.
B. Non
C. Route 53 can't failover.
D. Active-passive failover.
E. Active-active-passive and other mixed configuration
```

```
53
You have been storing massive amounts of data on Amazon Glacier for the past 2 years and now start to wonder if there are any limitations on this. What is the
correct answer to your QUESTION ?
A. The total volume of data is limited but the number of archives you can store are unlimited.
B. The total volume of data is unlimited but the number of archives you can store are limited.
C. The total volume of data and number of archives you can store are unlimited.
D. The total volume of data is limited and the number of archives you can store are limite
```

```
58
You are setting up your first Amazon Virtual Private Cloud (Amazon VPC) so you decide to use the VPC wizard in the AWS console to help make it easier for you.
Which of the following statements is correct regarding instances that you launch into a default subnet via the VPC wizard?
A. Instances that you launch into a default subnet receive a public IP address and 10 private IP addresses.
B. Instances that you launch into a default subnet receive both a public IP address and a private IP address.
C. Instances that you launch into a default subnet don't receive any ip addresses and you need to define them manually.
D. Instances that you launch into a default subnet receive a public IP address and 5 private IP addresse
Passing Certification Exams Made Easy
visit - https://www.2PassEasy.com
Welcome to download the Newest 2passeasy AWS-Solution-Architect-Associate dumps
https://www.2passeasy.com/dumps/AWS-Solution-Architect-Associate/ (1487 New Questions)
```

```
62
An existing client comes to you and says that he has heard that launching instances into a VPC (virtual private cloud) is a better strategy than launching instances
into a EC2-classic which he knows is what you currently do. You suspect that he is correct and he has asked you to do some research about this and get back to
him. Which of the following statements is true in regards to what ability launching your instances into a VPC instead of EC2-Classic gives you?
A. All of the things listed here.
B. Change security group membership for your instances while they're running
C. Assign static private IP addresses to your instances that persist across starts and stops
D. Define network interfaces, and attach one or more network interfaces to your instances
```

```
66
Amazon S3 allows you to set per-file permissions to grant read and/or write access. However you have decided that you want an entire bucket with 100 files
already in it to be accessible to the public. You don't want to go through 100 files indMdually and set permissions. What would be the best way to do this?
A. Move the bucket to a new region
B. Add a bucket policy to the bucket.
C. Move the files to a new bucket.
D. Use Amazon EBS instead of S3
```

```
69
A user is accessing an EC2 instance on the SSH port for IP 10.20.30.40. Which one is a secure way to configure that the instance can be accessed only from this
IP?
A. In the security group, open port 22 for IP 10.20.30.40
B. In the security group, open port 22 for IP 10.20.30.40/32
C. In the security group, open port 22 for IP 10.20.30.40/24
D. In the security group, open port 22 for IP 10.20.30.40/0
```

```
73
An accountant asks you to design a small VPC network for him and, due to the nature of his business, just needs something where the workload on the network
will be low, and dynamic data will be accessed infrequently. Being an accountant, low cost is also a major factor. Which EBS volume type would best suit his
requirements?
A. Magnetic
B. Any, as they all perform the same and cost the same.
C. General Purpose (SSD)
D. Magnetic or Provisioned IOPS (SSD)
```

```
77
A user is planning to launch a scalable web application. Which of the below mentioned options will not affect the latency of the application?
A. Region.
B. Provisioned IOPS.
C. Availability Zone.
D. Instance siz
```

```
80
In Amazon EC2, if your EBS volume stays in the detaching state, you can force the detachment by clicking .
A. Force Detach
B. Detach Instance
C. AttachVoIume
D. Attachlnstance
```

```
81
Which IAM role do you use to grant AWS Lambda permission to access a DynamoDB Stream?
A. Dynamic role
B. Invocation role
C. Execution role
D. Event Source role
```

```
83
You are signed in as root user on your account but there is an Amazon S3 bucket under your account that you cannot access. What is a possible reason for this?
A. An IAM user assigned a bucket policy to an Amazon S3 bucket and didn't specify the root user as a principal
B. The S3 bucket is full.
C. The S3 bucket has reached the maximum number of objects allowed.
D. You are in the wrong availability zone
```

```
86
Select the correct statement: Within Amazon EC2, when using Linux instances, the device name
/dev/sda1 is .
A. reserved for EBS volumes
B. recommended for EBS volumes
C. recommended for instance store volumes
Passing Certification Exams Made Easy
visit - https://www.2PassEasy.com
Welcome to download the Newest 2passeasy AWS-Solution-Architect-Associate dumps
https://www.2passeasy.com/dumps/AWS-Solution-Architect-Associate/ (1487 New Questions)
D. reserved for the root device
```

```
88
A user is planning to make a mobile game which can be played online or offline and will be hosted on EC2.
The user wants to ensure that if someone breaks the highest score or they achieve some milestone they can inform all their colleagues through email. Which of the
below mentioned AWS services helps achieve this goal?
A. AWS Simple Workflow Service.
B. AWS Simple Email Service.
C. Amazon Cognito
D. AWS Simple Queue Servic
```

```
92
You receive the following request from a client to quickly deploy a static website for them, specifically on AWS. The requirements are low-cost, reliable, online
storage, and a reliable and cost-effective way to route customers to the website, as well as a way to deliver content with low latency and high data transfer speeds
so that visitors to his website don't experience unnecessary delays. What do you think would be the minimum AWS services that could fulfill the cIient's request?
A. Amazon Route 53, Amazon CIoudFront and Amazon VPC.
B. Amazon S3, Amazon Route 53 and Amazon RDS
C. Amazon S3, Amazon Route 53 and Amazon CIoudFront
D. Amazon S3 and Amazon Route 53.
```

```
93
How long does an AWS free usage tier EC2 last for?
A. Forever
B. 12 Months upon signup
C. 1 Month upon signup
D. 6 Months upon signup
```

```
95
Which of the following statements is true of tagging an Amazon EC2 resource?
A. You don't need to specify the resource identifier while terminating a resource.
B. You can terminate, stop, or delete a resource based solely on its tags.
C. You can't terminate, stop, or delete a resource based solely on its tags.
D. You don't need to specify the resource identifier while stopping a resourc
```

```
98
A user has created a CIoudFormation stack. The stack creates AWS services, such as EC2 instances, ELB, AutoScaIing, and RDS. While creating the stack it
created EC2, ELB and AutoScaIing but failed to create RDS. What will C|oudFormation do in this scenario?
Passing Certification Exams Made Easy
visit - https://www.2PassEasy.com
Welcome to download the Newest 2passeasy AWS-Solution-Architect-Associate dumps
https://www.2passeasy.com/dumps/AWS-Solution-Architect-Associate/ (1487 New Questions)
A. Rollback all the changes and terminate all the created services
B. It will wait for the user’s input about the error and correct the mistake after the input
C. CIoudFormation can never throw an error after launching a few services since it verifies all the steps before launching
D. It will warn the user about the error and ask the user to manually create RDS
```

```
103
A major client who has been spending a lot of money on his internet service provider asks you to set up an AWS Direct Connection to try and save him some
money. You know he needs high-speed connectMty. Which connection port speeds are available on AWS Direct Connect?
A. 500Mbps and 1Gbps
B. 1Gbps and 10Gbps
C. 100Mbps and 1Gbps
D. 1Gbps
```

```
106
Is it possible to get a history of all EC2 API calls made on your account for security analysis and operational troubleshooting purposes?
A. Yes, by default, the history of your API calls is logged.
B. Yes, you should turn on the CIoudTraiI in the AWS console.
C. No, you can only get a history of VPC API calls.
D. No, you cannot store history of EC2 API calls on Amazon.
```

```
109
You have just set up yourfirst Elastic Load Balancer (ELB) but it does not seem to be configured properly. You discover that before you start using ELB, you have
to configure the listeners for your load balancer. Which protocols does ELB use to support the load balancing of applications?
A. HTTP and HTTPS
B. HTTP, HTTPS , TCP, SSL and SSH
C. HTTP, HTTPS , TCP, and SSL
D. HTTP, HTTPS , TCP, SSL and SFTP
```

```
111
What happens to Amazon EBS root device volumes, by default, when an instance terminates?
A. Amazon EBS root device volumes are moved to IAM.
B. Amazon EBS root device volumes are copied into Amazon RDS.
C. Amazon EBS root device volumes are automatically deleted.
D. Amazon EBS root device volumes remain in the database until you delete the
```

```
113
Having just set up your first Amazon Virtual Private Cloud (Amazon VPC) network, which defined a default network interface, you decide that you need to create
and attach an additional network interface, known as an elastic network interface (ENI) to one of your instances. Which of the following statements is true
regarding attaching network interfaces to your instances in your VPC?
A. You can attach 5 EN|s per instance type.
B. You can attach as many ENIs as you want.
C. The number of ENIs you can attach varies by instance type.
D. You can attach 100 ENIs total regardless of instance typ
```

```
118
A for a VPC is a collection of subnets (typically private) that you may want to designate for your backend RDS DB Instances.
A. DB Subnet Set
B. RDS Subnet Group
C. DB Subnet Group
D. DB Subnet Collection
```

```
123
Amazon Elastic Load Balancing is used to manage traffic on a fileet of Amazon EC2 instances, distributing traffic to instances across all availability zones within a
region. Elastic Load Balancing has all the advantages of an on-premises load balancer, plus several security benefits.
Which of the following is not an advantage of ELB over an on-premise load balancer?
A. ELB uses a four-tier, key-based architecture for encryption.
B. ELB offers clients a single point of contact, and can also serve as the first line of defense against attacks on your network.
C. ELB takes over the encryption and decryption work from the Amazon EC2 instances and manages it centrally on the load balancer.
D. ELB supports end-to-end traffic encryption using TLS (previously SSL) on those networks that use secure HTTP (HTTPS) connections.
```

```
124
You are setting up your first Amazon Virtual Private Cloud (Amazon VPC) network so you decide you should probably use the AWS Management Console and the
VPC Wizard. Which of the following is not an option for network architectures after launching the "Start VPC Wizard" in Amazon VPC page on the AWS
Management Console?
A. VPC with a Single Public Subnet Only
B. VPC with a Public Subnet Only and Hardware VPN Access
C. VPC with Public and Private Subnets and Hardware VPN Access
D. VPC with a Private Subnet Only and Hardware VPN Access
```

```
127
A user is trying to launch a similar EC2 instance from an existing instance with the option "Launch More like this". The AMI ofthe selected instance is deleted. What
will happen in this case?
A. AWS does not need an AMI for the "Launch more like this" option
B. AWS will launch the instance but will not create a new AMI
C. AWS will create a new AMI and launch the instance
D. AWS will throw an error saying that the AMI is deregistered
```

```
128
Your company has multiple IT departments, each with their own VPC. Some VPCs are located within the same AWS account, and others in a different AWS
account. You want to peer together all VPCs to enable the IT departments to have full access to each others' resources. There are certain limitations placed on
VPC peering. Which of the following statements is incorrect in relation to VPC peering?
A. Private DNS values cannot be resolved between instances in peered VPCs.
B. You can have up to 3 VPC peering connections between the same two VPCs at the same time.
C. You cannot create a VPC peering connection between VPCs in different regions.
D. You have a limit on the number active and pending VPC peering connections that you can have per VPC.
```

```
129
In the most recent company meeting, your CEO focused on the fact that everyone in the organization needs to make sure that all of the infrastructure that is built is
truly scalable. Which of the following statements is incorrect in reference to scalable architecture?
A. A scalable service is capable of handling heterogeneity.
B. A scalable service is resilient.
C. A scalable architecture won't be cost effective as it grows.
D. Increasing resources results in a proportional increase in performanc
```

```
130
After deploying a new website for a client on AWS, he asks if you can set it up so that if it fails it can be automatically redirected to a backup website that he has
stored on a dedicated server elsewhere. You are wondering whether Amazon Route 53 can do this. Which statement below is correct in regards to Amazon Route
53?
A. Amazon Route 53 can't help detect an outag
B. You need to use another service.
C. Amazon Route 53 can help detect an outage of your website and redirect your end users to alternate locations.
D. Amazon Route 53 can help detect an outage of your website but can't redirect your end users to alternate locations.
E. Amazon Route 53 can't help detect an outage of your website, but can redirect your end users to alternate locations.
Passing Certification Exams Made Easy
visit - https://www.2PassEasy.com
Welcome to download the Newest 2passeasy AWS-Solution-Architect-Associate dumps
https://www.2passeasy.com/dumps/AWS-Solution-Architect-Associate/ (1487 New Questions)
```

```
132
Which of the following statements is true of Amazon EC2 security groups?
A. You can change the outbound rules for EC2-Classi
B. Also, you can add and remove rules to a group at any time.
C. You can modify an existing rule in a grou
D. However, you can't add and remove rules to a group.
E. None of the statements are correct.
F. You can't change the outbound rules for EC2-Classi
G. However, you can add and remove rules to agroup at any tim
```

```
136
Your manager has asked you to set up a public subnet with instances that can send and receive internet traffic, and a private subnet that can't receive traffic
directly from the internet, but can initiate traffic to the internet (and receive responses) through a NAT instance in the public subnet. Hence, the following 3 rules
need to be allowed:
Inbound SSH traffic.
Web sewers in the public subnet to read and write to MS SQL servers in the private subnet Inbound RDP traffic from the Microsoft Terminal Services gateway in
the public private subnet What are the respective ports that need to be opened for this?
A. Ports 22,1433,3389
B. Ports 21,1433,3389
C. Ports 25,1433,3389
D. Ports 22,1343,3999
```

```
139
You want to establish a dedicated network connection from your premises to AWS in order to save money by transferring data directly to AWS rather than through
your internet service provider. You are sure there must be some other benefits beyond cost savings. Which of the following would not be considered a benefit if
you were to establish such a connection?
A. Elasticity
B. Compatibility with all AWS services.
C. Private connectMty to your Amazon VPC.
D. Everything listed is a benefi
```

```
144
You can seamlessly join an EC2 instance to your directory domain. What connectMty do you need to be able to connect remotely to this instance?
A. You must have IP connectMty to the instance from the network you are connecting from.
B. You must have the correct encryption keys to connect to the instance remotely.
C. You must have enough bandwidth to connect to the instance.
Passing Certification Exams Made Easy
visit - https://www.2PassEasy.com
Welcome to download the Newest 2passeasy AWS-Solution-Architect-Associate dumps
https://www.2passeasy.com/dumps/AWS-Solution-Architect-Associate/ (1487 New Questions)
D. You must use MFA authentication to be able to connect to the instance remotel
```

```
149
George has launched three EC2 instances inside the US-East-1a zone with his AWS account. Ray has launched two EC2 instances in the US-East-Ia zone with
his AWS account. Which of the below mentioned statements will help George and Ray understand the availability zone (AZ) concept better?
A. All the instances of George and Ray can communicate over a private IP with a minimal cost
B. The US-East-1a region of George and Ray can be different availability zones
C. All the instances of George and Ray can communicate over a private IP without any cost
D. The instances of George and Ray will be running in the same data centre
```

```
150
You are in the process of moving your friend's WordPress site onto AWS to try and save him some money, and you have told him that he should probably also
move his domain name. He asks why he can't leave
his domain name where it is and just have his infrastructure on AWS. What would be an incorrect response to his question ?
A. Route 53 offers low query latency for your end users.
B. Route 53 is designed to automatically answer queries from the optimal location depending on network conditions.
C. The globally distributed nature of AWS's DNS servers helps ensure a consistent ability to route your end users to your application.
D. Route 53 supports Domain Name System Security Extensions (DNSSEC).
```

```
155
Just when you thought you knew every possible storage option on AWS you hear someone mention Reduced Redundancy Storage (RRS) within Amazon S3.
What is the ideal scenario to use Reduced Redundancy Storage (RRS)?
A. Huge volumes of data
B. Sensitve data
C. Non-critical or reproducible data
D. Critical data
```

```
156
A user is making a scalable web application with compartmentalization. The user wants the log module to be able to be accessed by all the application
functionalities in an asynchronous way. Each module of the application sends data to the log module, and based on the resource availability it will process the logs.
Which AWS service helps this functionality?
A. AWS Simple Queue Service.
B. AWS Simple Notification Service.
C. AWS Simple Workflow Service.
D. AWS Simple Email Servic
Passing Certification Exams Made Easy
visit - https://www.2PassEasy.com
Welcome to download the Newest 2passeasy AWS-Solution-Architect-Associate dumps
https://www.2passeasy.com/dumps/AWS-Solution-Architect-Associate/ (1487 New Questions)
```

```
160
Your manager has come to you saying that he is very confused about the bills he is receMng from AWS as he is getting different bills for every user and needs you
to look into making it more understandable. Which of the following would be the best solution to meet his request?
A. AWS Billing Aggregation
B. Consolidated Billing
C. Deferred Billing
D. Aggregated Billing
```

```
161
You have written a CIoudFormation template that creates I Elastic Load Balancer fronting 2 EC2 Instances. Which section of the template should you edit so that
the DNS of the load balancer is returned upon creation of the stack?
A. Resources
B. Outputs
C. Parameters
D. Mappings
```

```
163
A user has hosted an application on EC2 instances. The EC2 instances are configured with ELB and Auto Scaling. The application server session time out is 2
hours. The user wants to configure connection draining to ensure that all in-flight requests are supported by ELB even though the instance is being deregistered.
What time out period should the user specify for connection draining?
A. 1 hour
B. 30 minutes
C. 5 minutes
D. 2 hours
```

```
164
How can you apply more than 100 rules to an Amazon EC2-Classic?
A. By adding more security groups
B. You need to create a default security group specifying your required rules if you need to use more than 100 rules per security group.
C. By default the Amazon EC2 security groups support 500 rules.
D. You can't add more than 100 rules to security groups for an Amazon EC2 instanc
```

```
167
You need to quickly set up an email-sending service because a client needs to start using it in the next hour. Amazon Simple Email Service (Amazon SES) seems
Passing Certification Exams Made Easy
visit - https://www.2PassEasy.com
Welcome to download the Newest 2passeasy AWS-Solution-Architect-Associate dumps
https://www.2passeasy.com/dumps/AWS-Solution-Architect-Associate/ (1487 New Questions)
to be the logical choice but there are several options available to set it up. Which of the following options to set up SES would best meet the needs of the client?
A. Amazon SES console
B. AWS CIoudFormation
C. SMTP Interface
D. AWS Elastic Beanstalk
```

```
171
You have a Business support plan with AWS. One of your EC2 instances is running Mcrosoft Windows Server 2008 R2 and you are having problems with the
software. Can you receive support from AWS for this software?
A. Yes
B. No, AWS does not support any third-party software.
C. No, Mcrosoft Windows Server 2008 R2 is not supported.
D. No, you need to be on the enterprise support pla
```

```
172
When controlling access to Amazon EC2 resources, each Amazon EBS Snapshot has a attribute that controls which AWS accounts can use the snapshot.
A. createVoIumePermission
B. LaunchPermission
C. SharePermission
D. RequestPermission
```

```
173
Your company plans to host a large donation website on Amazon Web Services (AWS). You anticipate a large and undetermined amount of traffic that will create
many database writes. To be certain that you do not drop any writes to a database hosted on AWS. Which service should you use?
A. Amazon RDS with provisioned IOPS up to the anticipated peak write throughput.
B. Amazon Simple Queue Service (SOS) for capturing the writes and draining the queue to write to the database.
C. Amazon EIastiCache to store the writes until the writes are committed to the database.
D. Amazon DynamoDB with provisioned write throughput up to the anticipated peak write throughpu
```

```
174
Your company hosts a social media site supporting users in multiple countries. You have been asked to provide a highly available design tor the application that
leverages multiple regions tor the most recently accessed content and latency sensitive portions of the wet) site The most latency sensitive component of the
Passing Certification Exams Made Easy
visit - https://www.2PassEasy.com
Welcome to download the Newest 2passeasy AWS-Solution-Architect-Associate dumps
https://www.2passeasy.com/dumps/AWS-Solution-Architect-Associate/ (1487 New Questions)
application involves reading user preferences to support web site personalization and ad selection. In addition to running your application in multiple regions, which
option will support this app|ication's requirements?
A. Serve user content from 53. CIoudFront and use Route53 latency-based routing between ELBs in each region Retrieve user preferences from a local
DynamoDB table in each region and leverage SQS to capture changes to user preferences with 505 workers for propagating updates to each table.
B. Use the 53 Copy API to copy recently accessed content to multiple regions and serve user content from 53. C|oudFront with dynamic content and an ELB in
each region Retrieve user preferences from an EIasticCache cluster in each region and leverage SNS notifications to propagate user preference changes to a
worker node in each region.
C. Use the 53 Copy API to copy recently accessed content to multiple regions and serve user content from 53 CIoudFront and Route53 latency-based routing
Between ELBs In each region Retrieve user preferences from a DynamoDB table and leverage SQS to capture changes to user preferences with 505 workers for
propagating DynamoDB updates.
D. Serve user content from 53. CIoudFront with dynamic content, and an ELB in each region Retrieve user preferences from an EIastiCache cluster in each region
and leverage Simple Workflow (SWF) to manage the propagation of user preferences from a centralized OB to each EIastiCache cluster.
```

```
179
A web company is looking to implement an external payment service into their highly available application deployed in a VPC Their application EC2 instances are
behind a public lacing ELB Auto scaling is used to add additional instances as traffic increases under normal load the application runs 2 instances in the
Auto Scaling group but at peak it can scale 3x in size. The application instances need to communicate with the payment service over the Internet which requires
whitelisting of all public IP addresses used to communicate with it. A maximum of 4 whitelisting IP addresses are allowed at a time and can be added through an
API.
How should they architect their solution?
A. Route payment requests through two NAT instances setup for High Availability and whitelist the Elastic IP addresses attached to the MAT instances.
B. Whitelist the VPC Internet Gateway Public IP and route payment requests through the Internet Gateway.
C. Whitelist the ELB IP addresses and route payment requests from the Application servers through the ELB.
D. Automatically assign public IP addresses to the application instances in the Auto Scaling group and run a script on boot that adds each instances public IP
address to the payment validation whitelist API.
```

```
181
You have deployed a three-tier web application in a VPC with a CIOR block of 10 0 0 0/ 28 You initially deploy two web servers, two application sewers, two
database sewers and one NAT instance tor a total of seven EC2 instances The web. Application and database servers are deployed across two availability zones
(AZs). You also deploy an ELB in front of the two web sewers, and use Route53 for DN5 Web (raffile gradually increases in the first few days following the
deployment, so you attempt to double the number of instances in each tier of the application to handle the new load unfortunately some of these new instances fail
to launch.
Which of the following could De the root caused? (Choose 2 answers)
A. AW5 resewes the first and the last private IP address in each subnet's CIDR block so you do not have enough addresses left to launch all of the new EC2
instances
B. The Internet Gateway (IGW) of your VPC has scaled-up, adding more instances to handle the traffic spike, reducing the number of available private IP
addresses for new instance launches
C. The ELB has scaled-up, adding more instances to handle the traffic spike, reducing the number of available private IP addresses for new instance launches
D. AW5 reserves one IP address in each subnet's CIDR block for Route53 so you do not have enough addresses left to launch all of the new EC2 instances
E. AW5 reserves the first four and the last IP address in each subnet's CIDR block so you do not haveenough addresses left to launch all of the new EC2
instances
```

```
183
You've been brought in as solutions architect to assist an enterprise customer with their migration of an e-commerce platform to Amazon Virtual Private Cloud
(VPC) The previous architect has already deployed a 3-tier VPC, The configuration is as follows:
VPC: vpc-2f8bc447 IGW: igw-2d8bc445 NACL: ad-208bc448
5ubnets and Route Tables: Web sewers: subnet-258bc44d
Application servers: subnet-248bc44c Database sewers: subnet-9189c6f9 Route Tables:
rrb-218bc449 rtb-238bc44b Associations:
subnet-258bc44d : rtb-218bc449 subnet-248bc44c : rtb-238bc44b subnet-9189c6f9 : rtb-238bc44b
You are now ready to begin deploying EC2 instances into the VPC Web servers must have direct access to the internet Application and database sewers cannot
have direct access to the internet.
Which configuration below will allow you the ability to remotely administer your application and database servers, as well as allow these sewers to retrieve updates
from the Internet?
A. Create a bastion and NAT instance in subnet-258bc44d, and add a route from rtb- 238bc44b to the NAT instance.
B. Add a route from rtb-238bc44b to igw-2d8bc445 and add a bastion and NAT instance within subnet-248bc44c.
C. Create a bastion and NAT instance in subnet-248bc44c, and add a route from rtb- 238bc44b to subneb258bc44d.
D. Create a bastion and NAT instance in subnet-258bc44d, add a route from rtb-238bc44b to Igw- 2d8bc445, and a new NACL that allows access between
subnet-258bc44d and subnet -248bc44c.
```

```
184
Your company has an on-premises multi-tier PHP web application, which recently experienced downtime due to a large burst In web traffic due to a company
announcement Over the coming days, you are expecting similar announcements to drive similar unpredictable bursts, and are looking to find ways to quickly
improve your infrastructures ability to handle unexpected increases in traffic.
The application currently consists of 2 tiers a web tier which consists of a load balancer and several Linux Apache web servers as well as a database tier which
hosts a Linux server hosting a MySQL database. Which scenario below will provide full site functionality, while helping to improve the ability of your application in
the short timeframe required?
Passing Certification Exams Made Easy
visit - https://www.2PassEasy.com
Welcome to download the Newest 2passeasy AWS-Solution-Architect-Associate dumps
https://www.2passeasy.com/dumps/AWS-Solution-Architect-Associate/ (1487 New Questions)
A. Failover environment: Create an 53 bucket and configure it for website hostin
B. Migrate your DNS to Route53 using zone file import, and leverage Route53 DNS failover to failover to the 53 hosted website.
C. Hybrid environment: Create an AMI, which can be used to launch web servers in EC2. Create an Auto Scaling group, which uses the AMI to scale the web tier
based on incoming traffi
D. Leverage Elastic Load Balancing to balance traffic between on-premises web servers and those hosted In AWS.
E. Offload traffic from on-premises environment: Setup a C|oudFront distribution, and configure CIoudFront to cache objects from a custom origi
F. Choose to customize your object cache behavior, and select a TIL that objects should exist in cache.
G. Migrate to AWS: Use VM Import/Export to quickly convert an on-premises web server to an AM
H. Create an Auto Scaling group, which uses the imported AMI to scale the web tier based on incoming traffi
I. Create an RDS read replica and setup replication between the RDS instance and on-premises MySQL server to migrate the database.
```

```
189
You've been hired to enhance the overall security posture for a very large e-commerce site They have a well architected multi-tier application running in a VPC that
uses ELBs in front of both the web and the app
tier with static assets served directly from 53 They are using a combination of RDS and DynamoOB for their dynamic data and then archMng nightly into 53 for
further processing with EMR
They are concerned because they found QUESTION able log entries and suspect someone is attempting to gain unauthorized access.
Which approach provides a cost effective scalable mitigation to this kind of attack?
A. Recommend that they lease space at a DirectConnect partner location and establish a IG DirectConnect connection to their vPC they would then establish
Internet connectMty into their space, filter the traffic in hardware Web Application Firewall (WAF). And then pass the traffic through the DirectConnect connection
into their application running in their VPC,
B. Add previously identified hostile source IPs as an explicit INBOUND DENY NACL to the web tier sub net.
C. Add a WAF tier by creating a new ELB and an AutoScaIing group of EC2 Instances running a host based WAF They would redirect Route 53 to resolve to the
new WAF tier ELB The WAF tier would thier pass the traffic to the current web tier The web tier Security Groups would be updated to only allow traffic from the
WAF tier Security Group
D. Remove all but TLS 1 2 from the web tier ELB and enable Advanced Protocol Filtering This will enable the ELB itself to perform WAF functionality.
```

```
192
An AWS customer is deploying an application mat is composed of an AutoScaIing group of EC2 Instances.
The customers security policy requires that every outbound connection from these instances to any other service within the customers Virtual Private Cloud must
be authenticated using a unique x 509 certificate that contains the specific instance-id.
In addition an x 509 certificates must Designed by the customer's Key management service in order to be trusted for authentication.
Which of the following configurations will support these requirements?
A. Configure an IAM Role that grants access to an Amazon 53 object containing a signed certificate and configure me Auto Scaling group to launch instances with
this role Have the instances bootstrap get the certificate from Amazon 53 upon first boot.
B. Embed a certificate into the Amazon Machine Image that is used by the Auto Scaling group Have the launched instances generate a certificate signature
request with the instance's assigned instance- id to the Key management service for signature.
C. Configure the Auto Scaling group to send an SNS notification of the launch of a new instance to the trusted key management servic
D. Have the Key management service generate a signed certificate and send it directly to the newly launched instance.
E. Configure the launched instances to generate a new certificate upon first boot Have the Key management service poll the AutoScaIing group for associated
instances and send new instances acertificate signature (hat contains the specific instance-i
```

```
195
You are designing an SSUTLS solution that requires HTIPS clients to be authenticated by the Web server using client certificate authentication. The solution must
be resilient.
Which of the following options would you consider for configuring the web server infrastructure? (Choose 2 answers)
A. Configure ELB with TCP listeners on TCP/4d3. And place the Web servers behind it.
B. Configure your Web servers with EIPS Place the Web servers in a Route53 Record Set and configure health checks against all Web servers.
C. Configure ELB with HTIPS listeners, and place the Web servers behind it.
D. Configure your web servers as the origins for a Cloud Front distributio
E. Use custom SSL certificates on your Cloud Front distribution.
```

```
200
You have an application running on an EC2 Instance which will allow users to download fl ies from a private 53 bucket using a pre-assigned URL. Before
generating the URL the application should verify the existence of the fi Ie in 53.
How should the application use AWS credentials to access the 53 bucket securely?
A. Use the AWS account access Keys the application retrieves the credentials from the source code of the application.
B. Create an IAM user for the application with permissions that allow list access to the 53 bucket launch the instance as the IAM user and retrieve the IAM user's
credentials from the EC2 instance user data.
C. Create an IAM role for EC2 that allows list access to objects in the 53 bucke
D. Launch the instance with the role, and retrieve the roIe's credentials from the EC2 Instance metadata
E. Create an IAM user for the application with permissions that allow list access to the 53 bucke
F. The application retrieves the IAM user credentials from a temporary directory with permissions that allow read access only to the application user.
```

```
201
A benefits enrollment company is hosting a 3-tier web application running in a VPC on AWS which includes a NAT (Network Address Translation) instance in the
public Web tier. There is enough provisioned capacity for the expected workload tor the new fiscal year benefit enrollment period plus some extra overhead
Enrollment proceeds nicely for two days and then the web tier becomes unresponsive, upon investigation using CIoudWatch and other monitoring tools it is
discovered that there is an extremely large and unanticipated amount of inbound traffic coming from a set of 15 specific IP addresses over port 80 from a country
where the benefits company has no customers. The web tier instances are so overloaded that benefit enrollment administrators cannot even SSH into them. Which
actMty would be useful in defending against this attack?
A. Create a custom route table associated with the web tier and block the attacking IP addresses from the IGW (Internet Gateway)
B. Change the EIP (Elastic IP Address) of the NAT instance in the web tier subnet and update the Main Route Table with the new EIP
C. Create 15 Security Group rules to block the attacking IP addresses over port 80
D. Create an inbound NACL (Network Access control list) associated with the web tier subnet with deny rules to block the attacking IP addresses
```

```
206
Your company policies require encryption of sensitive data at rest. You are considering the possible options for protecting data while storing it at rest on an EBS
data volume, attached to an EC2 instance. Which of these options would allow you to encrypt your data at rest? (Choose 3 answers)
A. Implement third party volume encryption tools
B. Do nothing as EBS volumes are encrypted by default
C. Encrypt data inside your applications before storing it on EBS
D. Encrypt data using native data encryption drivers at the file system level
E. Implement SSL/TLS for all services running on the server
```

```
211
To serve Web traffic for a popular product your chief financial officer and IT director have purchased 10 ml large heavy utilization Reserved Instances (Rls) evenly
spread across two availability zones:
Route 53 is used to deliver the traffic to an Elastic Load Balancer (ELB). After several months, the product grows even more popular and you need additional
capacity As a result, your company purchases two C3.2x|arge medium utilization Rls You register the two c3 2xIarge instances with your ELB and quickly find that
the ml large instances are at 100% of capacity and the c3 2xIarge instances have significant capacity that's unused Which option is the most cost effective and
uses EC2 capacity most effectively?
A. Use a separate ELB for each instance type and distribute load to ELBs with Route 53 weighted round robin
B. Configure Autoscaning group and Launch Configuration with ELB to add up to 10 more on-demand ml large instances when triggered by Cloudwatch shut off c3
2xIarge instances
C. Route traffic to EC2 ml large and c3 2xIarge instances directly using Route 53 latency based routing and health checks shut off ELB
D. Configure ELB with two c3 2xiarge Instances and use on-demand Autoscaling group for up to two additional c3.2x|arge instances Shut on mi .|arge instances.
```

```
215
A large real -estate brokerage is exploring the option o( adding a cost-effective location based alert to their existing mobile application The application backend
infrastructure currently runs on AWS Users who opt in to this service will receive alerts on their mobile device regarding real-estate otters in proximity to their
location. For the alerts to be relevant delivery time needs to be in the low minute count the existing mobile app has 5 million users across the us Which one of the
following architectural suggestions would you make to the customer?
A. The mobile application will submit its location to a web service endpoint utilizing Elastic Load Balancing and EC2 instances: DynamoDB will be used to store
and retrieve relevant otters EC2 instances will communicate with mobile earners/device providers to push alerts back to mobile application.
B. Use AWS DirectConnect or VPN to establish connectMty with mobile carriers EC2 instances will receive the mobile applications ' location through carrier
connection: ROS will be used to store and relevant relevant offers EC2 instances will communicate with mobile carriers to push alerts back to the mobile
application
C. The mobile application will send device location using SO
D. EC2 instances will retrieve the re Ievant others from DynamoDB AWS MobiIe Push will be used to send offers to the mobile application
E. The mobile application will send device location using AWS Nlobile Push EC2 instances will retrieve the relevant offers from DynamoDB EC2 instances will
communicate with mobile carriers/device providers to push alerts back to the mobile application.
```

```
216
A company is building a voting system for a popular TV show, viewers win watch the performances then visit the show's website to vote for their favorite performer.
It is expected that in a short period of time after the show has finished the site will receive millions of visitors. The visitors will first login to the site using their
Amazon.com credentials and then submit their vote. After the voting is completed the page will display the vote totals. The company needs to build the site such
that can handle the rapid influx of traffic while maintaining good performance but also wants to keep costs to a minimum. Which of the design patterns below
should they use?
A. Use Cloud Front and an Elastic Load balancer in front of an auto-scaled set of web servers, the web servers will first can the Login With Amazon service to
authenticate the user then process the users vote and store the result into a multi-AZ Relational Database Service instance.
B. Use CIoudFront and the static website hosting feature of 53 with the Javascript SDK to call the Login With Amazon service to authenticate the user, use IAM
Roles to gain permissions to a DynamoDB table to store the users vote.
C. Use Cloud Front and an Elastic Load Balancer in front of an auto-scaled set of web servers, the web servers will first call the Login with Amazon service to
Passing Certification Exams Made Easy
visit - https://www.2PassEasy.com
Welcome to download the Newest 2passeasy AWS-Solution-Architect-Associate dumps
https://www.2passeasy.com/dumps/AWS-Solution-Architect-Associate/ (1487 New Questions)
authenticate the user, the web servers will process the users vote and store the result into a DynamoDB table using IAM Roles for EC2 instances to gain
permissions to the DynamoDB table.
D. Use Cloud Front and an Elastic Load Balancer in front of an auto-scaled set of web servers, the web servers will first call the Logi
E. With Amazon service to authenticate the user, the web sewers win process the users vote and store the result into an SQS queue using IAM Roles for EC2
Instances to gain permissions to the SQS queu
F. A set of application sewers will then retrieve the items from the queue and store the result into a DynamoDB table.
```

```
220
You deployed your company website using Elastic Beanstalk and you enabled log file rotation to 53. An Elastic Map Reduce job is periodically analyzing the logs
on 53 to build a usage dashboard that you share with your CIO.
You recently improved overall performance of the website using Cloud Front for dynamic content delivery and your website as the origin.
After this architectural change, the usage dashboard shows that the traffic on your website dropped by an order of magnitude. How do you fix your usage
dashboard'?
A. Enable Cloud Front to deliver access logs to 53 and use them as input of the Elastic Map Reduce job.
B. Turn on Cloud Trail and use trail log tiles on 53 as input of the Elastic Map Reduce job
C. Change your log collection process to use Cloud Watch ELB metrics as input of the Elastic MapReducejob
D. Use Elastic Beanstalk "Rebuild Environment" option to update log delivery to the Elastic Map Reduce job.
E. Use Elastic Beanstalk 'Restart App server(s)" option to update log delivery to the Elastic Map Reduce job.
```

```
223
A web company is looking to implement an intrusion detection and prevention system into their deployed VPC. This platform should have the ability to scale to
thousands of instances running inside of the VPC, How should they architect t heir solution to achieve these goals?
A. Configure an instance with monitoring software and the elastic network interface (ENI) set to promiscuous mode packet sniffing to see an traffic across the VPC,
B. Create a second VPC and route all traffic from the primary application VPC through the second VPC where the scalable virtualized IDS/IPS platform resides.
C. Configure servers running in the VPC using the host-based 'route' commands to send all traffic through the platform to a scalable virtualized IDS/IPS.
D. Configure each host with an agent that collects all network traffic and sends that traffic to the IDS/IPS platform for inspection.
```

```
224
A web-startup runs its very successful social news application on Amazon EC2 with an Elastic Load Balancer, an Auto-Scaling group of Java/Tomcat application-
servers, and DynamoDB as data store. The main web-application best runs on m2 x large instances since it is highly memory- bound Each new deployment
requires semi-automated creation and testing of a new AM for the application servers which takes quite a while ana is therefore only done once per week.
Recently, a new chat feature has been implemented in nodejs and wails to be integrated in the architecture. First tests show that the new component is CPU
bound Because the company has some experience with using Chef, they decided to streamline the deployment process and use AWS Ops Works as an
application life cycle tool to simplify management of the application and reduce the deployment cycles.
What configuration in AWS Ops Works is necessary to integrate the new chat module in the most cost-efficient and filexible way?
A. Create one AWS OpsWorks stack, create one AWS Ops Works layer, create one custom recipe
B. Create one AWS OpsWorks stack create two AWS Ops Works layers create one custom recipe
C. Create two AWS OpsWorks stacks create two AWS Ops Works layers create one custom recipe
D. Create two AWS OpsWorks stacks create two AWS Ops Works layers create two custom recipe
```

```
227
If I want an instance to have a public IP address, which IP address should I use'?
A. Elastic I P Address
B. Class B IP Address
C. Class A IP Address
D. Dynamic IP Address
```

```
231
What does RRS stand for when talking about 53?
A. Redundancy Removal System
B. Relational Rights Storage
C. Regional Rights Standard
D. Reduced Redundancy Storage
```

```
233
All Amazon EC2 instances are assigned two IP addresses at launch, out of which one can only be reached from within the Amazon EC2 network?
A. Multiple IP address
B. Public IP address
C. Private IP address
Passing Certification Exams Made Easy
visit - https://www.2PassEasy.com
Welcome to download the Newest 2passeasy AWS-Solution-Architect-Associate dumps
https://www.2passeasy.com/dumps/AWS-Solution-Architect-Associate/ (1487 New Questions)
D. Elastic I P Address
```

```
235
Can you create IAM security credentials for existing users?
A. Yes, existing users can have security credentials associated with their account.
B. No, IAM requires that all users who have credentials set up are not existing users
C. No, security credentials are created within GROUPS, and then users are associated to GROUPS at a later time.
D. Yes, but only IAM credentials, not ordinary security credential
```

```
240
When you view the block device mapping for your instance, you can see only the EBS volumes, not the instance store volumes.
A. Depends on the instance type
B. FALSE
C. Depends on whether you use API call
D. TRUE
```

```
241
By default, EBS volumes that are created and attached t o an instance at launch are deleted when t hat instance is terminated. You can modify this behavior by
changing the value of the flag _ to false when you launch the instance
A. Delete On Termination
B. Remove On Deletion
C. Remove On Termination
D. Terminate On Deletion
```

```
245
True or False: When using IAM to control access to your RDS resources, the key names that can be used are case sensitive. For example, aws:CurrentTime is
NOT equivalent to AWS:currenttime.
A. TRUE
B. FALSE
```

```
248
True or False: Automated backups are enabled by default for a new DB Instance.
A. TRUE
B. FALSE
```

```
253
While creating the snapshots using the command line tools, which command should I be using?
A. ec2-deploy-snapshot
B. ec2-fresh-snapshot
C. ec2-create-snapshot
D. ec2-new-snapshot
```

```
254
Typically, you want your application to check whether a request generated an error before you spend any time processing results. The easiest way to find out if an
error occurred is to look for an _ node in the response from the Amazon RDS API.
A. Incorrect
B. Error
C. FALSE
```

```
255
Amazon RDS DB snapshots and automated backups are stored in
Passing Certification Exams Made Easy
visit - https://www.2PassEasy.com
Welcome to download the Newest 2passeasy AWS-Solution-Architect-Associate dumps
https://www.2passeasy.com/dumps/AWS-Solution-Architect-Associate/ (1487 New Questions)
A. Amazon 53
B. Amazon ECS Volume
C. Amazon RDS
D. Amazon EMR
```

```
260
What are the Amazon EC2 API tools?
A. They don't exis
B. The Amazon EC2 AMI tools, instead, are used to manage permissions.
C. Command-line tools to the Amazon EC2 web service.
D. They are a set of graphical tools to manage EC2 instances.
E. They don't exis
F. The Amazon API tools are a client interface to Amazon Web Senrice
```

```
264
Out of the stripping options available for the EBS volumes, which one has the following disadvantage : 'Doubles the amount of 1/0 required from the instance to
EBS compared to RAID 0, because you're mirroring all writes to a pair of volumes, limiting how much you can stripe.'?
A. Raid 0
B. RAID 1+0 (RAID 10)
C. Raid 1
D. Raid
```

```
267
Is creating a Read Replica of another Read Replica supported?
A. Only in certain regions
B. Only with MSSQL based RDS
C. Only for Oracle RDS types
D. No
```

```
271
Can Amazon 53 uploads resume on failure or do they need to restart?
A. Restart from beginning
B. You can resume them, if you flag the "resume on fai lure" option before uploading.
C. Resume on failure
D. Depends on the file size
```

```
272
How can I change the security group membership for interfaces owned by other AWS, such as Elastic Load Balancing?
A. By using the service specific console or API\CLI commands
B. None of these
C. Using Amazon EC2 API/CLI
D. using all these methods
```

```
274
What is the maximum write throughput I can provision for a single Dynamic DB table?
A. 1,000 write capacity units
B. 100,000 write capacity units
C. Dynamic DB is designed to scale without limits, but if you go beyond 10,000 you have to contact AWS first.
D. 10,000 write capacity units
```

```
275
What does the following command do with respect to the Amazon EC2 security groups? ec2-revoke RevokeSecurityGroup Ingress
A. Removes one or more security groups from a rule.
B. Removes one or more security groups from an Amazon EC2 instance.
Passing Certification Exams Made Easy
visit - https://www.2PassEasy.com
Welcome to download the Newest 2passeasy AWS-Solution-Architect-Associate dumps
https://www.2passeasy.com/dumps/AWS-Solution-Architect-Associate/ (1487 New Questions)
C. Removes one or more rules from a security group.
D. Removes a security group from our accoun
```

```
278
Can I move a Reserved Instance from one Region to another?
A. No
B. Only if they are moving into GovC|oud
C. Yes
D. Only if they are moving to US East from another region
```

```
282
True or False: When you perform a restore operation to a point in time or from a DB Snapshot, a new DB Instance is created with a new endpoint.
A. FALSE
B. TRUE
```

```
285
What does t he following command do with respect to the Amazon EC2 security groups? ec2-create-group CreateSecurityGroup
A. Groups the user created security groups in to a new group for easy access.
B. Creates a new security group for use with your account.
C. Creates a new group inside the security group.
D. Creates a new rule inside the security grou
```

```
289
How many types of block devices does Amazon EC2 support A
A. 2
B. 3
C. 4
D. 1
```

```
291
IAM provides several policy templates you can use to automatically assign permissions to the groups you create. The _ policy template gives the Admins group
permission to access all account resources,
except your AWS account information
A. Read Only Access
B. Power User Access
C. AWS Cloud Formation Read Only Access
D. Administrator Access
```

```
294
While performing the volume status checks, if the status is insufficient-data, what does it mean?
A. the checks may still be in progress on the volume
B. the check has passed
C. the check has failed
```

```
295
For each DB Instance class, what is the maximum size of associated storage capacity?
A. 5GB
B. 1 TB
C. 2TB
D. 500GB
```

```
298
What is an isolated database environment running in the cloud (Amazon RDS) called?
A. DB Instance
B. DB Sewer
C. DB Unit
D. DB Volume
```

```
302
In regards to IAM you can edit user properties later, but you cannot use the console to change the
A. user name
B. password
C. default group
```

```
306
Making your snapshot public shares all snapshot data with everyone. Can the snapshots with AWS Market place product codes be made public?
A. No
B. Yes
```

```
309
What does Amazon Cloud Formation provide?
A. The ability to setup Autoscaling for Amazon EC2 instances.
B. None of these.
C. A templated resource creation for Amazon Web Services.
D. A template to map network resources for Amazon Web Service
```

```
313
Please select the Amazon EC2 resource which cannot be tagged.
A. images (AM|s, kernels, RAM disks)
B. Amazon EBS volumes
C. Elastic IP addresses
D. VPCs
```

```
317
Can the string value of 'Key' be prefixed with :aws:"?
A. Only in GovC|oud
B. Only for 53 not EC2
C. Yes
D. No
```

```
322
Because of the extensibility limitations of striped storage attached to Windows Sewer, Amazon RDS does not currently support increasing storage on a _ DB
Instance.
A. SQL Sewer
B. MySQL
C. Oracle
```

```
326
Select the incorrect statement
A. In Amazon EC2, the private IP addresses only returned to Amazon EC2 when the instance is stopped or terminated
B. In Amazon VPC, an instance retains its private IP addresses when the instance is stopped.
C. In Amazon VPC, an instance does NOT retain its private IP addresses when the instance is stopped.
D. In Amazon EC2, the private IP address is associated exclusive ly with the instance for its lifetime
Passing Certification Exams Made Easy
visit - https://www.2PassEasy.com
Welcome to download the Newest 2passeasy AWS-Solution-Architect-Associate dumps
https://www.2passeasy.com/dumps/AWS-Solution-Architect-Associate/ (1487 New Questions)
```

```
328
Can I test my DB Instance against a new version before upgrading?
A. Only in VPC
B. No
C. Yes
```

```
332
What is a Security Group?
A. None of these.
B. A list of users that can access Amazon EC2 instances.
C. An Access Control List (ACL) for AWS resources.
D. A firewall for inbound traffic, built-in around every Amazon EC2 instanc
```

```
337
If an Amazon EBS volume is the root device of an instance, can I detach it without stopping the instance?
A. Yes but only if Windows instance
B. No
C. Yes
D. Yes but only if a Linux instance
```

```
340
A group can contain many users. Can a user belong to multiple groups?
A. Yes always
B. No
C. Yes but only if they are using two factor authentication
D. Yes but only in VPC
```

```
341
Is the encryption of connections between my application and my DB Instance using SSL for the MySQL server engines available?
A. Yes
B. Only in VPC
C. Only in certain regions
D. No
```

```
344
Which AWS instance address has the following characteristics? :" If you stop an instance, its Elastic IP address is unmapped, and you must remap it when you
restart the instance."
A. Both A and B
B. None of these
C. VPC Addresses
D. EC2 Addresses
```

```
346
Does Route 53 support MX Records?
A. Yes.
B. It supports CNAME records, but not MX records.
C. No
D. Only Primary MX record
E. Secondary MX records are not supporte
```

```
348
Passing Certification Exams Made Easy
visit - https://www.2PassEasy.com
Welcome to download the Newest 2passeasy AWS-Solution-Architect-Associate dumps
https://www.2passeasy.com/dumps/AWS-Solution-Architect-Associate/ (1487 New Questions)
Can the string value of 'Key' be prefixed with laws'?
A. No
B. Only for EC2 not 53
C. Yes
D. Only for 53 not EC
```

```
353
If I want my instance to run on a single-tenant hardware, which value do I have to set the instance's tenancy attribute to?
A. dedicated
B. isolated
C. one
D. reserved
```

```
358
What does Amazon RDS stand for?
A. Regional Data Sewer.
B. Relational Database Service.
C. Nothing.
D. Regional Database Service.
```

```
362
What does Amazon ELB stand for?
A. Elastic Linux Box.
B. Encrypted Linux Box.
C. Encrypted Load Balancing.
D. Elastic Load Balancin
```

```
365
What does Amazon Cloud Formation provide?
A. None of these.
B. The ability to setup Autoscaling for Amazon EC2 instances.
C. A template to map network resources for Amazon Web Services.
D. A templated resource creation for Amazon Web Service
```

```
369
What does Amazon SES stand for?
A. Simple Elastic Server
B. Simple Email Service
C. Software Email Solution
D. Software Enabled Sewer
```

```
373
Amazon 53 doesn't automatically give a user who creates _ permission to perform other actions on that bucket or object.
A. a file
B. a bucket or object
C. a bucket orfile
D. a object or file
```

```
374
What is the charge for the data transfer incurred in replicating data between your primary and standby?
A. No charg
B. It is free.
C. Double the standard data transfer charge
Passing Certification Exams Made Easy
visit - https://www.2PassEasy.com
Welcome to download the Newest 2passeasy AWS-Solution-Architect-Associate dumps
https://www.2passeasy.com/dumps/AWS-Solution-Architect-Associate/ (1487 New Questions)
D. Same as the standard data transfer charge
E. Half of the standard data transfer charge
```

```
379
Within the IAM service a GROUP is regarded as a:
A. A collection of AWS accounts
B. |t's the group of EC2 machines that gain t he permissions specified in the GROUP.
C. There's no GROUP in IAM, but only USERS and RESOURCES.
D. A collection of user
```

```
381
Do the system resources on the Micro instance meet the recommended configuration for Oracle?
A. Yes completely
B. Yes but only for certain situations
C. Not in any circumstance
```

```
383
Amazon RDS supports SOAP only through _ _
A. HTTP or HTTPS
B. TCP/IP
C. HTIP
D. HTIPS
```

```
387
embodies the "share-nothing" architecture and essentially involves breaking a large database into several smaller databases. Common ways to split a database
include
1) splitting tables that are notjoined in the same query onto different hosts or
2) duplicating a table across multiple hosts and then using a hashing algorithm to determine which host
receives a given update.
A. $harding
B. Fai lure recovery
C. Federation
D. DOL operations
```

```
390
Does Amazon Route 53 support NS Records?
A. Yes, it supports Name Service records.
B. No
C. It supports only MX records.
D. Yes, it supports Name Sewer record
```

```
392
The SQL Server _ feature is an efficient means of copying data from a source database to your DB Instance. It writes the data that you specify to a data file, such
as an ASCII file.
A. bulk copy
B. group copy
C. dual copy
D. mass copy
```

```
393
A _ is a document that provides a formal statement of one or more permissions.
A. policy
B. permission
C. Role
Passing Certification Exams Made Easy
visit - https://www.2PassEasy.com
Welcome to download the Newest 2passeasy AWS-Solution-Architect-Associate dumps
https://www.2passeasy.com/dumps/AWS-Solution-Architect-Associate/ (1487 New Questions)
D. resource
```

```
398
Regarding the attaching of ENI to an instance, what does 'warm attach' refer to?
A. Attaching an ENI to an instance when it is stopped.
B. This QUESTION doesn't make sense.
C. Attaching an ENI to an instance when it is running
D. Attaching an ENI to an instance during the launch process
```

```
402
A Provisioned IOPS volume must be at |east_ GB in size
A. 1
B. 50
C. 20
D. 10
```

```
403
Willi be alerted when automatic fail over occurs?
A. Only if SNS configured
B. No
C. Yes
D. Only if Cloudwatch configured
```

```
406
If you' re unable to connect via SSH to your EC2 instance, which of the following should you check and possibly correct to restore connectMty?
A. Adjust Security Group to permit egress traffic over TCP port 443 from your IP.
B. Configure the JAM role to permit changes to security group settings.
C. Modify the instance security group to allow ingress of ICMP packets from your IP.
D. Adjust the instance's Security Group to permit ingress traffic over port 22 from your IP.
E. Apply the most recently released Operating System security patche
```

```
407
After launching an instance that you intend to serve as a NAT (Network Address Translation) device in a public subnet you modify your route tables to have the
NAT device be the target of internet bound traffic of your private subnet. When you try and make an outbound connection to the internet from an instance in
the private subnet, you are not successful. Which of the following steps could resolve the issue?
A. Disabling the Source/Destination Check attribute on the NAT instance
B. Attaching an Elastic IP address to the instance in the private subnet
C. Attaching a second Elastic Network Interface (EN I) to the NAT instance, and placing it in the private sub net
D. Attaching a second Elastic Network Interface (ENI) to the instance in the private subnet, and placing it in the public subnet
```

```
412
You are building a solution for a customer to extend their on-premises data center to AWS. The customer
requires a 50-Mbps dedicated and private connection to their VPC. Which AWS product or feature satisfies this requirement?
A. Amazon VPC peering
B. Elastic IP Addresses
C. AWS Direct Connect
D. Amazon VPC virtual private gateway
```

```
414
Passing Certification Exams Made Easy
visit - https://www.2PassEasy.com
Welcome to download the Newest 2passeasy AWS-Solution-Architect-Associate dumps
https://www.2passeasy.com/dumps/AWS-Solution-Architect-Associate/ (1487 New Questions)
Which services allow the customer to retain full administrative prMleges of the underlying EC2 instances? Choose 2 answers
A. Amazon Relational Database Service
B. Amazon Elastic Map Reduce
C. Amazon EIastiCache
D. Amazon DynamoDB
E. AWS Elastic Beanstalk
```

```
416
When you put objects in Amazon 53, what is the indication that an object was successfully stored?
A. A HTIP 200 result code and MDS checksum, taken together, indicate that the operation was successful.
B. Amazon 53 is engineered for 99.999999999% durabilit
C. Therefore there is no need to confirm that data was inserted.
D. A success code is inserted into the 53 object metadata.
E. Each 53 account has a special bucket named _s3_1og
F. Success codes are written to this bucket with a timestamp and checksum.
```

```
421
A company has a workflow that sends video files from their on-premise system to AWS for transcoding. They use EC2 worker instances that pull transcoding jobs
from SQS. Why is SQS an appropriate service for this scenario?
A. SQS guarantees the order of the messages.
B. SQS synchronously provides transcoding output.
C. SQS checks the health of the worker instances.
D. SQS helps to facilitate horizontal scaling of encoding task
```

```
423
Which procedure for backing up a relational database on EC2 that is using a set of RAIDed EBS volumes for storage minimizes the time during which the
database cannot be written to and results in a consistent backup?
A. 1. Detach EBS volumes, 2. Start EBS snapshot of volumes, 3. Re-attach EBS volumes
B. 1. Stop the EC2 Instanc
C. 2. Snapshot the EBS volumes
D. 1. Suspend disk 1/0, 2. Create an image ofthe EC2 Instance, 3. Resume disk 1/0
E. 1. Suspend disk 1/0,2. Start EBS snapshot of volumes, 3. Resume disk 1/0
F. 1. Suspend disk 1/0, 2. Start EBS snapshot of volumes, 3. Wait for snapshots to complete, 4. Resume disk 1/0
```

```
424
You are configuring your company's application to use Auto Scaling and need to move user state information. Which of the following AWS services provides a
shared data store with durability and low latency?
A. AWS EIastiCache Memcached
B. Amazon Simple Storage Service
C. Amazon EC2 instance storage
D. Amazon DynamoDB
```

```
425
Which of the following are characteristics of a reserved instance? Choose 3 answers
A. It can be migrated across Availability Zones
B. It is specific to an Amazon Machine Image (AMI)
C. It can be applied to instances launched by Auto Scaling
D. It is specific to an instance Type
E. It can be used to lower Total Cost of Ownership (TCO) of a system
```

