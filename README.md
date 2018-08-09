# Final Project

Web Programming with Python and JavaScript

In this project, I aimed to make an artist website for my own independent music project The plan is to modify this project once the course is over - removing account functionality, and with it, comments - and host it onto a webhost such as heroku. Within the templates directory, there is index.html but also, index2.html, this is due to the fact that I decided to render a different template when a user logged into the website - the template contains a logout button instead. index.html and index2.html both fetch the latest upload from the artist's youtube channel using the YouTube API. Once the data is fetched, it is then used to render the latest youtube video from the channel, and the title of it as well.

Furthermore, the music.html template contains images of some of the music that I have previous produced, this template will only render if the user is not logged in. If the user is logged in, music2.html will be rendered. In music2.html, clicking on any of the artworks on the page will automatically begin playing the song that the artwork belongs to, furthermore, a volume fader will appear at the top of the page in the navivation bar. If a user is logged in, they are also granted the ability to comment of any of the tracks, this can be done by clicking on the song names that highlight in white when hovered over in the music2.html template. Once a user clicks on a song title, they will be redirected to a specific template made for the song they clicked on, on this page, they will be able to comment through a form. At the bottom of every page - with the exception of terms.html - is a "Terms & Conditions" hyperlink that renders the terms.html template which currently contains example text from (https://www.bmi.com/legal/entry/terms_and_conditions_of_use) for the scope of this project. Also in the bottom navbar, there is also a contact link to the artist's email.

At the top of every page is a navbar that contains social media logos that redirect the user to the artist's page on the social media platform related to the logo that was clicked. In the background of every page is a design I created using Photoshop to help improve the overall style of the website UI. Lastly, viewing this page with Chrome's device toolbar will reveal that I opted to remove account functionality for phone users to make the website look cleaner. However, it would be ideal to spend more time designing the overall website with the ultimate goal of giving mobile visiters the same user functionality that laptop and computer visiters have.

# Sources
Youtube API: https://developers.google.com/apis-explorer/#search/youtube/youtube/v3/youtube.playlistItems.list?part=snippet&maxResults=50&playlistId=UUzAjvFPO5L8aEdHbb8DafeQ&_h=5&

BMI Terms and Conditions of Use: https://www.bmi.com/legal/entry/terms_and_conditions_of_use

Media Queries: http://www.stephen.io/mediaqueries


# Superuser

Username: admin

Password: testtest
