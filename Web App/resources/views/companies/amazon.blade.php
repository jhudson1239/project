<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    <!-- Styles -->
    <link rel="stylesheet" href="/css/company.css">

    <!-- Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,700" rel="stylesheet">
    <script defer src="https://use.fontawesome.com/releases/v5.0.10/js/all.js" integrity="sha384-slN8GvtUJGnv6ca26v8EzVaR9DC58QEwsIk9q1QXdCU8Yu8ck/tL/5szYlBbqmS+" crossorigin="anonymous"></script>

    <!-- Chart -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.css">
    <script src="https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.js"></script>  
    <title>Amazon</title>
</head>

<body>
    <nav>
        
        <div id="logo"><img src="images/logo.png" alt=""></div>
        <div id="links">
            <ul>
            <li> <a href="/">Home</a> </li>
                <li>About</li>
                <li>Contact</li>
            </ul>
        </div>      
    </nav>

    
    <div class="container">
        <section id="section-a">
            <h1>{{$company->name}}</h1>
            <div id="company-logo">
                <img src="/images/a-logo.jpg" alt="">
            </div>
            
            <div id="company-info">
                <div id="info-container">
                    <h2>Company Information</h2>
                    <ul>
                        <li>Address : {{$company->address}}</li>
                        <li>Founders : {{$company->founded}}</li>
                        <li>Company CEO(s): {{$company->ceo}}</li>
                        <li>General Information : {{$company->information}}</li>
                    </ul>
                </div>
            </div>
        </section>
        <hr>    
    </div>

    <div class="container">
        <section id="section-b">
            <h1>Sentiment Analysis</h1>
            <div id="chart-1">
                <div style="height:400px; width:400px;" class="ct-chart ct-perfect-fourth chart-format" id="chart1"><h2>Project Classifier</h2></div>
            </div>
            <div id="chart-2">
                <div style="height:400px; width:400px;" class="ct-chart ct-perfect-fourth chart-format" id="chart2"><h2>Textblob Classifier</h2></div>
            </div>

            

            <div id="info">

                <span class="fas fa-circle" style="color:#D70206; font-size:1.5em"></span> Positive <span class="fas fa-circle" style="color:#F05B4F; font-size:1.5em"></span> Negative
                
            <h2 style="margin-top:20px;">What does this mean?</h2>
            <p>The two charts above show the sentiment of tweet that where
                collected by using the companys name. The tweets where then analyzed
                by a machine learning algorithm for their sentiment, this was either 
                postive or negative. The chart on the left shows the predictions from
                the classfier made for this project. Its accuracy when tested was around 74%. 
                The chart on the right is a classifer know as TextBlob, their accuracy was
                around 40%.
            </p>
            </div>
            
        </section>
    </div>

        

    
<script>
  new Chartist.Pie('#chart1', {
  series: [{{$positive}}, {{$negative}}]
}, {
  chartPadding: 30,
  labelOffset: 50,
  labelDirection: 'explode'
});

new Chartist.Pie('#chart2', {
  series: [{{$t_negative}}, {{$t_positive}}]
}, {
  chartPadding: 30,
  labelOffset: 50,
  labelDirection: 'explode'
});
</script>
    
</body>
</html>