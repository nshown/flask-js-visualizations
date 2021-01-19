# Flask with JavaScript Visualizations

Flask is an excellent resource for generating webpages.  Using Flask's templating functionality you can edit the HTML content of a webpage based on data your Flask server accesses, including data stored in databases.

If your webpage needs charts or other data visualizations the best way to achieve this is through JavaScript.  JavaScript must be able to access the data in your databases in order to render these visualizations.  There are a couple of different methods to achieve this.  

The [first approach](templates/js-templating.html) is to use Flask's templating functionality to create objects in a JavaScript `<script>` tag that your code can access.

The [second approach](templates/js-using-web-api.html) is to create a Web API that you can then access using D3 or jQuery in your JavaScript code.  Once you have your Web API data you can then create your visualization.

In this repository I [create a sample database](db/setup.py) containing data about people's favorite colors in order to generate a Plotly Bar Chart using Flask templating to create a JavaScript object in addition to generating a visualization from a Web API.



![Sample Chart!](/images/sample-chart.png "A Sample Chart")