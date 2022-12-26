# Choose an Anime/Manga from MAL
This project was inspired by a video from a Data Science Youtuber Tina Huang who suggested writing a script to help choose an anime to watch.
My project takes a look at my personal Plan to Watch list on MyAnimeList and returns a random anime to watch. This was a big challenge for me 
because it was my first time trying to pull data from a website. I intially wanted to try web scraping but MAL has an API now so I tried using that,
but it was a big struggle trying to read the documentation when I'd never used an API before and I had difficulty parsing through the json file it returned.

I wrote this back in June 2022 but never really used it until this week (Dec 24ish 22) and it's been pretty helpful getting through my long list. 
After finishing the script I used something called auto-py-to-exe to convert the py file to a .exe so I can 
just have the icon on my desktop and use it whenever I want.

### 12/26/2022
I added a loop so that I can get another suggestion if I don't what it gives me and gives an option to request a manga from my manga Plan to Read list. 
For now if manga is selected it will just give a message saying that I am working on it.

### Possible future functionalities 

- [ ] Returning random manga from list
- [ ] Return random anime from current season
- [ ] Return random anime from top xx page