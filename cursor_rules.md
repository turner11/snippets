# based on [mberman84](https://gist.github.com/mberman84/98fa7d02a2d4c11071bf2bf63faa4713)


# Coding pattern preferences

– Always prefer simple solutions  
– Avoid duplication of code whenever possible, which means checking for other areas of the codebase that might already have similar code and functionality  
– Write code that takes into account the different environments: dev, test, and prod  
– You are careful to only make changes that are requested or you are confident are well understood and related to the change being requested  
– When fixing an issue or bug, do not introduce a new pattern or technology without first exhausting all options for the existing implementation. And if you finally do this, make sure to remove the old implementation afterwards so we don’t have duplicate logic.  
– Keep the codebase very clean and organized  
– Avoid writing scripts in files if possible, especially if the script is likely only to be run once  
– Avoid having files over 200–300 lines of code. Refactor at that point.  
– Mocking data is only needed for tests, never mock data for dev or prod  
– Never add stubbing or fake data patterns to code that affects the dev or prod environments  
– Never overwrite my .env file without first asking and confirming
– Always prefer python types over typing-types when possible (e.g. list vs List)
– Always prefer pipes (|) over typing.Optional 
– Always prefer using f-strings for string formatting and interpolation in Python, as they are more readable and efficient than older methods like % formatting or str.format()

# Coding Workflow preferences

- Focus on the areas of code relevant to the task
- Do not touch code that is unrelated to the task
- Write thorough tests for all major functionality
- Avoid making major changes to the patterns and architecture of how a feature works, after it has shown to work well, unless explicitly instructed
- Always think about what other methods and areas of code might be affected by code changes


# Technichal stack

- Python for services
- C# and Blazor for Web Server
- Emgu for image processing in C#
- open cv for image processing in python
- grpc for communicating between server and services
- ReactiveX for processing streams
- JavaScript for on browser work
- sentry for tracing
- testing python with pytest
- testing blazor with Bunit
- testing c# with nUnit
