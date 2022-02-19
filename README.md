# NomeQualquer API



<h1><b>API Reference</b></h1>
    <br>
    <p>The API is organized around Fast API. Our API is oriented so that events can provide user the best experience.</p>
    <br>
    <p>You can test using our API in your Website Event, and we guarantee your client will get one of the best experiences of his life.</p>
    <br>
    <p> The API differs for every account as we release new versions and tailor functionality, watch our GitHub frequently. </p>
    <br>

<h2><b>Faq</b></h2>
 <p><b>1º</b> What will we have to do to use your API ?</p>
 <p> You just have to submit a request to API (using fetch or something else) with your schedule and tags in a dictionary and then, ask for your user "tag" preferences so the API will automatic give the Best Schedule he could get according to his preferences.
<br>
<h5>Example:</h5>
 <p>
 {<br>
```json
  "horario": [
    {
      "title": "Opening Time,
      "date_start": "1641027600",
      "date_end": "1641031200",
      "tags": []
    },
    {
      "title": "Timmy Trumpet",
      "date_start": "1641031200",
      "date_end": "1641038400",
      "tags": [<br>
        "eletronica"
       ]
    },
    {
      "title": "Metallica",<br>
      "date_start": "1641031200",
      "date_end": "1641038400",
      "tags": [
        "rock"
      ]
    },
`   {
      "title": "Dzrt",
      "date_start": "1641031200",
      "date_end": "1641038400",
      "tags": [
        "pop"
      ]
    },
    {
      "title": "Lunch",
      "date_start": "1641038400",
      "date_end": "1641045600",
      "tags": []
    }
      ]
        }
```
<p> You can use https://www.epochconverter.com/ as a time converter to date_start and date_end </p>

<p><b>2º</b> Do we have to pay something to use it? </p>
<p> No, this is a free open-source API made in @Sei Hackathon </p>
