# sup-bot
Automated Supreme checkout bot
**CURRENTLY FUNCTIONAL ON CHROME ONLY, GECKODRIVER REJECTS CAPTCHA**

## How to setup
* Install chromedriver according to your version of chrome and add it to your PATH
> AppData/Local/Programs/Python
* Configure your info dictionary at the bottom of the file
* Run in terminal

## Product name/ color/ size
* Must be written with exact capitalization, no extra spacing and include special characters
* Consult a droplist site prior to use to ensure your configurations are 100% accurate

## Categories
* jackets
* shirts
* tops_sweaters
* sweatshirts
* t-shirts
* hats
* bags
* accessories
* skate

## Important note
* Certain input names (credit card number, etc) seem random, which could mean that Supreme updates these frequently to dissuade botting. Inspecting page elements before the drop is the best way to ensure your info is input ahead of time.

## Final implementation goals
- [X] refreshes product site close to drop time until available
- [X] automatically opens requested product page
- [X] adds product to cart
- [X] redirects to checkout page
- [X] passes inputs into request fields, awaits checkout click
