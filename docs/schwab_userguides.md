Introduction
Welcome to the Schwab Developer Portal. Here you will find information to support you on your journey towards consuming our suite of products. Explore our comprehensive resources and get started on your development journey today.

Get started with a few steps
1
Register: Create your account to being the development journey. After submitting the registration form you will receive an email that contains a time sensitive link to validate your email address; which, will then allow you to complete the registration process.

Note: If you already have an account, then sign in and proceed to step #2.

2
Choose your profile: Set up a company profile, join an existing company or register as an individual developer.

3
Discover: Review the API Product catalog to find and request access to the APIs that support your audience or use case.

4
Build: After you identify the API Product; you'll need to "Request Access" to that Line of Business. Upon approval, you'll be able to create your app to begin the development journey.

5
Deploy: For API Products that conduct testing in our lower environments; you will have the additional step to promote your app to production when it is ready to go live. Click on "Promote to Production", then a confirmation window pops up where you can promote your app.

User Registration
Registering a User Account will allow you to create a Company Profile, join an existing company, or register as an Individual Developer. At least one of these roles is required to request access to API Products.

Note:

For internal Schwab employees, you can skip the registration process.
To login in as a Schwab Employee, go directly to the Login and select the “Use your Schwab Credentials” option.
To register a User:

Select Register at the top right-hand corner of the site.
Complete User Registration form. All fields are required except where noted.
Read and agree to the Dev Portal's Terms of Use and Privacy Policy.
Submit the registration form.
You will receive an email that contains a link to complete registration and validate your account in the Dev Portal.
Note:

If you are joining an existing Company as a developer, you will need to contact your Company Administrator so they may send you an invitation to join that Company.
If your Company does not yet exist in the Dev Portal, you will need to create a Company Profile in order to request access to API Products and Docs.
Important:

Avoid duplicate Company Profile submissions by designating a Company Administrator that will own the Company Profile. This User can invite additional Company Developers who may view documentation, create, manage, and utilize Company applications.

How API Products are Organized
API Products are organized by Charles Schwab internal Line of Business (LOB). API Products are created, maintained and owned by Administrators from each LOB.

Each LOB has its own Access Request form, process for approval, and agreement to access their products. The documentation content and access to those products is provided by that LOB.

Requesting Product Access
API Products are organized by functional grouping or line of business. Company Administrators should first review Product overviews to determine what APIs they may require for Application development and submit an access request.

Once access has been granted, your Company may view API Product documentation, Support docs, and create Apps that subscribe to those API Products. 

Note:

Company Administrator is required to request access to Products on behalf of the Company. Company Developers should contact their Company Administrator if product access is required.
An Individual Developer role is required to access certain LOBs.

To request access to a specific Product:

Select API Products from the navigation menu to view a list of available LOBs and a short description of each.
Select the Learn More link for one of the LOB cards to read more detail.
After review and determination that access is required, select Request Access from the top of the LOB homepage.
Note:

LOBs listed on the site may have different requirements, approval workflows, access agreements, etc. If you do not see a Request Access button that LOB may not be available to your Company or Role.

Access Agreements

Access requirements and procedures may vary by API Product. In many cases, request forms and access agreements are click-through, however some Products may require custom agreements or forms that must be filled out offline. Each Product access request will provide instructions related to that specific process. Once a Company Administrator accepts an agreement, all members of that Company are bound to the terms of the agreement. 


Approval Process

Access requests are reviewed by Product or line of business administrators. Most requests are reviewed within two business days though this may be longer by Product or when a high volume of requests are experienced. If additional information is required to complete the request, a team member will contact the Company Administrator before approval.

Authenticate with OAuth
Schwab & API Security
Schwab is committed to providing the highest standards of digital security and privacy for our Clients. Using the OAuth 2 authorization framework, Schwab can provide secure, delegated access over HTTPS to devices, APIs, servers, and applications using access tokens in place of Client credentials.

 

OAuth 2 Overview
Schwab employs the OAuth 2 protocol to secure services from unauthorized access. OAuth 2 is the second iteration of this IETF traditional client-server authentication framework and a current standard for RESTful API security. Our implementation adheres to current IETF standards. This open standard framework operates over HTTPS, effectively replacing username+password with an encrypted token to access User data. Official IETF RFC articles may be found here:

OAuth 2 - https://tools.ietf.org/html/rfc6749
Bearer Token - https://tools.ietf.org/html/rfc6750
Bearer tokens are used for the OAuth authorization_code Grant Type.

 

Three-Legged Workflow
Three-Legged OAuth is a workflow (Flow) that allows Users to grant an App permission to access Protected Resources, such as their account information, without disclosing credentials. OAuth directs Users to Schwab's Login Micro Site (LMS) to perform the Consent and Grant (CAG) process. Here, the User may select and authorize the accounts they wish to be shared with the Third-Party Application (Application). Upon completion of the CAG process, the User is redirected back to the Application.

Key Terms
App

OAuth registration is managed by Apps on the Dev Portal. Here, these Apps are owned by a Company and used internally to manage Application access to Protected Resource data.

App elements and attributes include:

Client ID & Client Secret

These string values are unique to an App and are generated when it gets approved and registered with the OAuth server. When an App is authorized using the OAuth Flow, these elements help identify and control access that the App has to Protected Resources data going forward. Permissions to access an API Product are also tied to an App and its corresponding Client ID. The Client Secret will never be exposed outside of the OAuth Flow and App management in the Dev Portal. Client Secret values should always be kept confidential and stored securely by an Application.

Callback URL

OAuth uses the Callback URL ("redirect_uri") to redirect the User and OAuth Flow back to the Application when necessary. This will be used as the URL "host" of that Application's landing page:

Callback URLs must be HTTPS. There is a 255-character limit on this field including all URLs listed. Multiple URLs are supported by separating each with a comma.

Display Name

The Display Name is established when the App is created in the Dev Portal and shown on screen to the User performing CAG activities. This helps ensure that consent is granted to the appropriate App.

Environment

Apps may exist in either Sandbox (test data access) or the Production environment (live data access). See the “Creating an App” and “Promoting an App to Production” sections for more information.

Product Subscription

Apps may only subscribe to a single API Product, for example, Account Aggregation DDA.

Third-Party Application (User-Agent / "Application"):

This will represent any website, stand-alone application or other HTTP platform that uses an OAuth Bearer token to access Protected Resource data on behalf of a User.

Note: This is completely different than the “App” as defined here.
CAG - Consent and Grant

Using LMS, Schwab Users will provide their approval of Application access and select the accounts they wish to link.

LMS - Login Micro Site

A website for Users to log into Schwab directly from an Application to perform CAG activities.

LOB - Line of Business

Owner of an API Product or functional grouping of APIs in Schwab's Dev Portal. Examples: Data Aggregation Services, Tax Services, etc. Companies may request access to API Products owned by the LOB.

Roles

IETF's OAuth 2 framework defines four Roles, such as the Resource Owner (User), referenced throughout this OAuth documentation.

User

User is the Protected Resource Owner that authorizes Application access to their information. User may be referenced interchangeably with: a Schwab Client, the Resource Owner, End User, or App User.

More info?

Further IETF OAuth definition of Resource Owner can be found here: https://tools.ietf.org/html/rfc6749#section-1.1

Token

Several types of Tokens are used in OAuth 2 Flows. All Tokens are simply string values representing attributes such as scope, lifetime, and other information that is used for different purposes.

Access Token

To enhance API security, Apps will use an Access Token to access User's Protected Resources. This is used in place of their username+password combination.

Bearer Token

A Bearer token is the Access Token in the context of an API call for Protected Resource data. It is passed in the Authorization header as "Bearer {access_token_value}.

Refresh Token

The Refresh Token renews access to User’s Protected Resources. This may be done before, or at any point after the current, valid access_token expires. When it does expire, the corresponding Refresh Token is used to request a new Access Token as opposed to repeating the entire Flow. This token is provided along with the initial Access Token and should be stored for later use.

Three-Legged Flow Entities

The primary entities involved in the Three-Legged OAuth Flow are the following:

Resource Owner (User) - Schwab Client or User that owns and grants access to Protected Resources.
OAuth Client (App) - The App living in the Dev Portal. Using its Client ID and Client Secret, it requests access to Protected Resources on behalf of the User.
User-Agent (3rd-party application) - The Resource Owner will use this application, or website, to interact with Schwab APIs and access Protected Resources.
Authorization Server (OAuth server) - OAuth server that authenticates OAuth Clients and issues Tokens.
Resource Server - Schwab server that hosts our Users' Protected Resources, such as a financial account information.
OAuth Flow - Sequence Diagram
[Three Legged OAuth Flow](Schwab-OAuth-Flow.png)


About the Individual Developer Role
Becoming an Individual Developer will allow you access to Specific API Product(s) which will allow you create apps that will access to your existing Schwab brokerage account(s)

Note:

As an individual Developer, you are limited to creating a single App
A Schwab brokerage account is required to access Trader APIs

Become an Individual Developer
Becoming an Individual Developer will allow you access to the Trader APIs which will allow you access to your existing Schwab brokerage accounts.

To assign the Individual Developer Role to your Dev Portal Account:

From the Welcome Page

Register your account and Log In to the Dev Portal
On your first successful Log In, you will be directed to the Welcome Page.
Locate the Individual Developer card and click CONTINUE
The Individual Role will be added to your account
From your User Profile

Register your account and Log In to the Dev Portal
Click on the Profile link from the main menu.
Locate the section labeled Individual Developer
Click the Add Individual Developer Role button
The Individual Role will be added to your account.
Note:

You can manage your roles from your User Profile
A Schwab brokerage account is required to access Trader APIs
To remove the Individual Developer Role from your account:

Register your account and Log In to the Dev Portal
Click on the Profile link from the main menu.
Locate the Individual Developer Role from the Roles table
In the Actions Column, click the Remove button
Note:

Removing the Individual Developer role will remove any LOB subscriptions associated to the Individual Developer role.
All Apps created for that role will be deleted. This Action Cannot be undone.

Create an App
Apps allow your Company to interact with APIs. Once your Company has been granted access to an API Product, you can create a App.

Note:
Each Line of Business manages their own rules regarding the creation of apps. In some cases you may be required to create and test an app in the Sandbox Environment, then request approval to Promote that App to the Production Environment.

To Create an App:

Note:
You must either be a member of a company, or an Individual Developer and be approved to use the API Product.

Select Dashboard link in the main menu.
Select Apps from the navigation menu.
Select Create App.
Fill in App Name and Callback URL fields.
Select an API Product. This will subscribe your App to that API Product.
Submit.
App Field Guide

App Name is displayed to end users. Use a name that end users recognize and understand they will grant access to.

Callback URL is where end users will be returned to after authorizing your App access to data.

Some Lines of Business (LOBs) enforce restrictions to the URL protocol, such as requiring an HTTPS address, and may restrict special characters from being included in the callback URL field.
Multiple callback URLs are supported by separating each with a comma.
Field is restricted to 255 characters. Contact support if your URL exceeds limit.
App Approval and Status

Many API Products are configured to auto-approve Sandbox App creation. In cases where Sandbox Apps are not auto-approved, a Pending (approval) status will be displayed until approved.

App statuses you may experience include:

Pending- Awaiting Admin review and approval.

Sandbox - Approved Sandbox access. The App is ready for testing.

Rejected/Denied - App creation has not been approved. Contact Support for detail.

Upon successful creation and approval, the App’s Client ID and Client Secret will be found in the App Details.

Active (Approved) - The app has been approved and is available for use.

Inactive (Revoked) – The app has been disabled and will be unavailable for use until it has been re-activated.

Important:
App Key and Secret should be considered highly confidential and should only be used to authenticate your application and make requests to APIs.

Modify an App
How can I modify an existing App?

Follow the instructions below to modify an existing App:

Select Dashboard from the menu.
Select Apps from the secondary menu.
Locate the App you wish to modify and select View Details from the Actions column.
Select the Modify Button.
In the pop-up window, you can modify the “App Name” and “Callback URL” fields.
Once your modifications are complete, select “Modify” to save your changes.
Deactivate an App

In some instances you may want to deactivate an app to prevent it’s use. You can temporarily deactivate or “pause” and app:

Select Dashboard from the menu.
Select Apps from the secondary menu.
Locate the App you wish to deactivate and select View Details from the Actions column.
Select Deactivate App button.
On the Confirmation Screen select the Deactivate button to confirm the action.
Activate a Deactivated App.

Select Dashboard from the menu.
Select Apps from the secondary menu.
Locate the App you wish to Activate and select View Details from the Actions column.
Select Activate App button.
On the Confirmation Screen select the Activate button to confirm the action.

Test in Sandbox
Sandbox environment provides the ability to test API methods, or HTTP verbs, without touching live Production data. Technical and non-technical API documentation is provided alongside a full-featured testing platform hosted within the Developer Portal. The Sandbox provides the ability to verify an App's OAuth 2.0 credentials and investigate API resource functionality.

API Documentation Questions
Individual LOBs manage their own API documentation independently and may choose to publish their respective API Products in this API Explorer module.

Questions on specific API Product documentation should be directed to that specific API Product Owner.

Functionality

Sandbox testing provides visibility of inputs/outputs, or requests/responses, of data for each call. The data is rendered and persists within this module's UI until the next call is run. Like the leading HTTP post utilities, the full OAuth 2.0 workflow is replicated to include client (end-user) authorization steps. The resulting access token will automatically be used to authenticate API resource calls.

Schwab employs RESTful API design, architecture, and Swagger/OpenAPI specification framework to aid development efforts. Assets and artifacts such as API response object examples and API models alongside reference documentation are provided for technical teams’ development.

Sandbox Test Data

Sandbox data is carefully engineered to provide datasets for testing that simulate live Production environment data without exposing any actual live accounts or data. Using the resources described above along with your Company’s Sandbox App, you will be able to make calls and return sample responses. The test data represents an accurate cross-section of data commonly found in the live environment while implementing security and privacy policies to protect Schwab and our clients. The full featured testbed also includes error response scenarios where applicable.

Promoting Apps to Production
How do I create an App that consumes production (live) data?

Note:
Lines of Business (LOBs) may require that all Apps created against their API Products to first be created in a Sandbox Environment and require the App to be promoted to the Production Environment.

Once development and testing of a Sandbox App is complete, the App must be promoted to the Production environment to consume live data.

The promotion process creates a Production App while keeping the Sandbox App for future testing needs.

Promote a Sandbox App to Production:

Select Dashboard from the menu.
Select Apps from the secondary menu.
Locate the Sandbox App you wish to modify and select View Details from the Actions column.
Select the Promote to Production button.
Note:
Promoting an App from Sandbox to Production may require manual approval from an LOB admin and may take several days for an Admin to review and approve your request.

OAuth Restart vs. Refresh Token
When do I need to restart the OAuth Flow vs. use the Refresh Token step?

Restarting the OAuth Flow:

When a property change to an OAuth token is needed, the entire Flow must be restarted from the beginning and the User's CAG completed through LMS once again. Other conditions may also exist that require this restart as well.

Below are some of the most common reasons to restart the Flow as opposed to using the Refresh Token step:

The refresh_token is compromised or malfunctioning.
Note:
A compromised or missing access_token can be resolved using the simple Refresh Token step.
This will not require the full restart.
A scope value is needed and was not requested for the current access_token.
A new access_token is needed when different User accounts need to be authorized.
This could originate from a mistake during the User CAG activities or from a necessary change in the authorized accounts or other Protected Resources selected.
The OAuth Flow was accidentally restarted and aborted, after the first Authorize an App step was completed.
This automatically invalidates the current access_token.
Restart the OAuth flow and be sure to complete it as normal.
A User revokes a token’s access manually, changes account credentials or modifies the TFA (Two-Factor Authentication) setup.
In this case, the User might be expecting involvement to authorize different accounts or consent to continued access after a credentials change.
The User is always in control of access to their Protected Resources at Schwab.
Revoking a token can be done at any time and should terminate third-party access unless it’s explicitly granted again.
Changes are made to security or other policies affecting protected resources or other Schwab assets.
This ensures that the User or third-party agrees to the modified Terms of Service (TOS) or other policies changes.
This case is the standard protocol and doesn’t result from risk mitigation or other security-related actions.
Technical difficulties with the Refresh Token functionality or endpoint access occur.
This could be a documented or unknown error and cause.
Technical support should be engaged to assist with debugging when other attempts fail.
Using the Refresh Token

Under normal circumstances, the Refresh Token functionality can be used to renew Third-Party Application access to Protected Resources. Even returning sessions can be authenticated by refreshing an expired token. The Refresh Token functionality is usually sufficient; however, in some situations this functionality will not be able to generate a token with the properties currently needed. These edge-cases may only occasionally be encountered.

Below are the conditions where the Refresh Token step should be sufficient to renew Protected Resource access:

An access_token has expired normally.
The token's lifetime is returned expressed in seconds in the "expires_in" parameter
The access_token has been lost but not compromised.
This can occur when application logic fails to store the value in a variable or other memory location.
A developer programmatically determines that an access_token will be refreshed to mitigate “401 Unauthorized” failures preemptively.
It is quite common for developers to program the automatic refresh of an access_token - even before it expired.
If this is not done excessively frequently, this should not place excess strain on the OAuth resources.
The benefit to refreshing before expiration is the mitigation of unnecessary “401” errors.
These errors are often encountered when an API call is placed near the time that an access_token would normally expire.

App Callback URL Requirements and Limitations
What are the requirements for the Callback URL (redirect_uri)?

What errors are associated with Callback URLs?

A Callback URL (“redirect_uri” parameter) is required when creating an App on the Developer Portal. This URL will be utilized in the OAuth //authorize step to redirect the User from LMS, for “consent and grant,” back to the calling App.

Per OAuth 2 requirements, a Callback URL is only applicable for the “authorization_code” and implicit flows (“grant_type”). Currently, the only available OAuth flow for Schwab APIs is the “authorization_code” Grant Type.

Callback URL Requirements and Recommendations:

Callback URL requirements are configured by each Line of Business and may vary depending on the API Product being offered.

URL Scheme: Some LOBs require the Callback URL scheme to be secure (HTTPS). While other support HTTP or other URL schemes depending on specific business requirements.
All callback URLS will be validated to ensure it meets basic URL structure.
All callback URLS will be validated to ensure there are no special or unsupported characters in the address.
If no Callback URL is sent during the OAuth flow, the value will automatically default to the Callback URL registered when the App was created on Schwab’s Dev Portal.

In this scenario, if multiple Callback URLs were registered with the App, an error may be returned. The reason being the inability to determine which one use since none was specified in the API request.
The Callback URL sent during the OAuth flow must be identical to one of the Callback URL(s) registered with the App being used.
Note:

The table below will highlight some common permutations and the associated error reason information.

Adding Multiple Callback URLs for a single App

Multiple URLS are supported for a single app. This can be done on either on the Create App form or the Modify App forms.

To add multiple Callback URLS:

Enter Callback URLs by separating each with a comma. NOTE do not separate the comma and the next URL with a Space.

example https://www.example.com/path/page.etc, https://www.example.com/path2/page.etc
The field is currently limited at 256 characters max.

Contact support if a special use-cases occurs that exceed this limitation.
Common Callback URL Errors and Reasons:

Registered URL

URL Sent in OAuth //authorize

Response or Error

https://host/path

https://host/path

Successful response

https://host/path

myapp://blah/bam

Error - invalid URI specified

Reason: scheme sent does not match registered

myapp://blah/bam

https://host/path

Error - invalid URI specified

Reason: scheme sent does not match registered

https://host/path

http://host/path

Error - invalid URI specified

Reason: scheme sent does not match registered

(“https” vs. “http”)

myapp://this/that

myapp://host/path

Error - invalid URI specified

Reason: path sent does not match registered

myapp://this/that

myapp://this/that

Successful response

