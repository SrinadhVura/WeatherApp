# WeatherApp
This repository is a submission to Github Copilot hackathon.
---
***About the hackathon:***
**GitHub Copilot** is powered by OpenAI Codex, a new AI system created by OpenAI. OpenAI Codex has a broad knowledge of how people use code and is significantly more capable than GPT-3 in code generation, in part, because it was trained on a data set that includes a much larger concentration of public source code. GitHub Copilot works with a broad set of frameworks and languages, but this technical preview works especially well for Python, JavaScript, TypeScript, Ruby and Go.

In simple words, GitHub Copilot is Artificial Intelligence that helps software developers write better code by providing valid and well-tested suggestions to the code they are currently working on. It can be seen as an AI assistant which provides developers with code based on the code they are currently writing.
---
The themes available are:
**Theme 1: Weather Forecasting Tool (Python)**

Create a command-line tool that accepts a city's name and returns the current weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse it using Python. Your solution should demonstrate how GitHub Copilot can help you with API usage, data parsing, and error handling.

**Theme 2: Simple E-commerce Inventory Management System (Java)**

Develop a simple inventory management system for an e-commerce platform using Java. The system should include basic functionalities such as adding, updating and removing products, and checking the available stock. Use GitHub Copilot to assist in generating code for implementing different operations and handling edge cases.

**Theme 3: Personal Finance Tracker (JavaScript)**

Create a web-based personal finance tracker using JavaScript, HTML, and CSS. The application should allow users to add, edit, and delete income and expense transactions and display the current balance. Use GitHub Copilot to guide you in implementing features, handling user input, and designing a responsive user interface.

**Theme 4: Task Management Application (.NET, C#)**

Develop a basic task management application using C# and .NET Framework. The application should allow users to create, update, and delete tasks, as well as mark them as completed. Show how GitHub Copilot can be used to generate code for implementing CRUD operations, input validation, and user interface design.

**Theme 5: URL Shortener Service (Ruby)**

Build a simple URL shortener service using Ruby and the Sinatra web framework. The service should accept a long URL as input, generate a unique short URL and store the mapping in a suitable data structure. Demonstrate how GitHub Copilot can provide suggestions for implementing the URL shortening algorithm, handling user input, and managing the data store.
---
This repository is based on theme 1.
Our solution to the problem statement makes use of the following :
* requests
* json
* argparse
* datetime
* opencage
* openweathermap API
1. *requests* is used to call the API endpoints of OpenCage and OpenWeather and return the results
2. *json* is used to format the retrieved results as json
3. *argparse* is used to read the provided city name from command-line as argument
4. *opencageAPI* is used to retrieve the geo co-ordinates of the city name provided by the user
5. *openweathermapAPI* is utilised to get the detailed weather of the thus found co-ordinates
* openweathermapAPI is capable of detecting upto 20,000 cities all round the world.
For a given city the tool retrieves various weather attributes like
* Weather description
* Temperature (current, day's minimum, day's maximum)
* Time of Sunrise
* Time of Sunset
* Wind speed and direction
* Humidity
# The code
The function get_coordinates() expects one argument i.e., city and with the help of opencageAPI retrieves latitude and longitude of the city and returns them
The city is determined by the program with the help of ArgumentParser from argparse library
The latitude and longitude are then sent to openweathermapAPI and the weather is then printed out.

# Running the program
1. Open any terminal
2. Navigate to the directory the WeatherApp.py is located
3. Use the command
   > python WeatherApp.py <CITY_NAME>
4. The output is printed in terminal
