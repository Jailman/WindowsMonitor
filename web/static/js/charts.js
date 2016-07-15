function charts(){
  $(function () {
      //CPU
      $.getJSON('/cpu?callback=?', function (data) {
          // Create the chart
          $('#cpu').highcharts('StockChart', {
            rangeSelector: {
                inputEnabled: $('#cpu').width() > 480,
                selected: 1
            },
              title : {
                  text : 'Windows CPU Monitor (单位：%)'
              },
              credits: {
                  enabled: true,
                  text: 'wanmei.com',
                  href: 'http://www.wanmei.com'
              },
              series : [{
                  name : 'Windows CPU Monitor',
                  data : data,
                  type : 'areaspline',
                  threshold : null,
                  tooltip : {
                      valueDecimals : 2
                  },
                  fillColor : {
                      linearGradient : {
                          x1: 0,
                          y1: 0,
                          x2: 0,
                          y2: 1
                      },
                      stops : [
                          [0, Highcharts.getOptions().colors[0]],
                          [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                      ]
                  }
              }]
          });
      });

      //RAM
      $.getJSON('/mem?callback=?', function (data) {
          // Create the chart
          $('#mem').highcharts('StockChart', {
            rangeSelector: {
                inputEnabled: $('#mem').width() > 480,
                selected: 1
            },
              title : {
                  text : 'Windows RAM Monitor (单位：MB)'
              },
              credits: {
                  enabled: true,
                  text: 'wanmei.com',
                  href: 'http://www.wanmei.com'
              },
              series : [{
                  name : 'Windows RAM Monitor',
                  data : data,
                  type : 'areaspline',
                  threshold : null,
                  tooltip : {
                      valueDecimals : 2
                  },
                  fillColor : {
                      linearGradient : {
                          x1: 0,
                          y1: 0,
                          x2: 0,
                          y2: 1
                      },
                      stops : [
                          [0, Highcharts.getOptions().colors[0]],
                          [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                      ]
                  }
              }]
          });
      });

      //Disk C:
      $.getJSON('/diskc?callback=?', function (data) {
      		Highcharts.getOptions().colors = Highcharts.map(Highcharts.getOptions().colors, function(color) {
          return {
              radialGradient: { cx: 0.5, cy: 0.3, r: 0.7 },
              stops: [
                  [0, color],
                  [1, Highcharts.Color(color).brighten(-0.3).get('rgb')] // darken
              ]
          };
      });
          $('#diskc').highcharts({
              chart: {
                  plotBackgroundColor: null,
                  plotBorderWidth: null,
                  plotShadow: false
              },
              title: {
                  text: 'Disk C: Usage'
              },
              credits: {
                  enabled: true,
                  text: 'wanmei.com',
                  href: 'http://www.wanmei.com'
              },
              tooltip: {
          	    pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
              },
              plotOptions: {
                  pie: {
                      allowPointSelect: true,
                      cursor: 'pointer',
                      dataLabels: {
                          enabled: true,
                          color: '#000000',
                          connectorColor: '#000000',
                          formatter: function() {
                              return '<b>'+ this.point.name +'</b>: '+ this.percentage +' %';
                          }
                      }
                  }
              },
              series: [{
                  type: 'pie',
                  name: 'Browser share',
                  data: data
                  // [
                  //     ['Firefox',   45.0],
                  //     ['IE',       26.8],
                  //     {
                  //         name: 'Chrome',
                  //         y: 12.8,
                  //         sliced: true,
                  //         selected: true
                  //     },
                  //     ['Safari',    8.5],
                  //     ['Opera',     6.2],
                  //     ['Others',   0.7]
                  // ]
              }]
          });
      });
  });
}


charts()

//每3秒刷新图表
// $(document).ready(function() {
//   window.setInterval(charts,15000);
// });
