d3.json("/raw-web-api", function (myData) { 
  console.log(myData); 
    
  var myXData = [];
  var myYData = [];

  myData.forEach(votes_color => {
      myXData.push(votes_color.color);
      myYData.push(votes_color.votes);
  });

  var data = [
      {
        x: myXData,
        y: myYData,
        marker:{
          color: myXData,
        },
        type: 'bar'
      }
    ];
    
  Plotly.newPlot('my-chart', data);

  //console.log the time
  var tempDate = new Date();
  console.log("finished retrieving web api data and plotting it", 
    tempDate.toLocaleTimeString(), 
    tempDate.getMilliseconds(),
    "MS");
}); 

//console.log the time
var tempDate = new Date();
console.log("finished running js-using-web-api.js file", 
  tempDate.toLocaleTimeString(), 
  tempDate.getMilliseconds(),
  "MS");