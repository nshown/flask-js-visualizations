var myXData = [];
var myYData = [];

my_color_data.forEach(votes_color => {
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