# E-shopperonline

![](static/docs/images/mockup.PNG)


## About

**E-shopperonline** 
Is an online store that offers to customers who are looking for food or supplements, from athletes to anyone who wants to get fit. This website has functions to make it easily available our range of products to all users, the website is made to be responsive and simple to use on a range of devices.

**Please note**: This site was created solely for educational purposes.
[Click here for a live demo version of this project.](http://e-shopperonline.herokuapp.com/)

## Table of Contents


- [**UX (User Experience)**](#ux-user-experience)
  - [**User Stories**](#user-stories)
- [**Design Choices**](#design-choices)
  - [**Typography**](#Typography)
  - [**Colour Scheme**](#colour-scheme)
  - [**Wireframes**](#wireframes)
- [**Features**](#features)
  - [**Site Navigation**](#site-navigation)
  - [**Future Features**](#feature-features)
  - [**Error Page**](#error-page)
  - [**Responsive Design**](#responsive-design)
  - [**Defensive Design**](#defensive-design)
- [**Database Schema**](#database-schema)
- [**Technologies**](#technologies)
  - [**Languages**](#languages)
  - [**Frameworks**](#frameworks)
  - [**Libraries**](#libraries)
  - [**Tools**](#tools)
- [**Manual Testing**](#manual-testing)
- [**Bugs**](#bugs)
  - [**Bugs fixed**](#bugs-fixed)
  - [**Known Bugs**](#known-bugs)
- [**Deployment**](#deployment)
  - [**Running Locally**](#forking-the-gitHub-repository)
- [**Web Marketing & Business**](#web-marketing-&-business)
- [**Credits**](#credits)
  - [**Media**](#media)
  - [**Acknowledgements**](#acknowledgements)



## **UX (User Experience)**

### **User Stories**

| User Story ID  | As a/an  | I want to be able to...  | So that I can... |
|---|---|---|---|
| Viewing Products & Navigation |
| 1  | User/Shopper | view the website from any device (mobile, desktop, tablet) | identify their qualities and compare. |
| 2  | User/Shopper   |to be able to navigate through the menu bar | to browse products. |
| 3  | User/Shopper    | to be able to find products by categories| to purchase products according to your interest. |
| Registration and Accounts |
| 4  | User/Shopper | register for an account | keep track of my orders and check my personal details. |
| 5  | User/Shopper   | receive email confirmation upon signing up | verify my set up was successful. |
| 6  |  User/Shopper  | be able to reset my password in case I forget it | gain access to my account. |
| 7  | User/Shopper   | have the ability to log in to the site with my details | view my orders and personal details |
| 8  | User/Shopper   | update my personal details | keep them up to date. |
| 9 | User/Shopper   | purchase from the site without having to register an account all the time| check out quickly and easily. |
| Searching products |
| 10  | User/Shopper   | to search product in the search tool | find product according to brand, type or key words. |
|11 | User/Shopper  | sort by price, name, category and rating  | view a wide range and choose which to buy. |
|12 | User/Shopper  | view the best sellers products on the home page  | choose the best range according to best sold products. |
| Checkout  |
| 13  | User/Shopper | have a total amount for selected products | stay within my budget.|
| 14 | User/Shopper  | view my bag contents |track of which products I have selected for purchase. 
| 15 | User/Shopper | adjust the quantity of products before the payment | stay on the page without being redirected to the home page. |
| 16  | User/Shopper  |  enter my payment details | to complete the purchase quickly. |
| 17  |  User/Shopper | view the full order before entering card details | check it before confirmation. |
| 18  | User/Shopper  | receive email notifications when I make an order | confirm my order has been placed and refer back to. |
| Admin/Management  |
| 19 | Admin/Management  | add products to the website | add new products and pictures for other users purchase. through user account. |
| 20 | Admin/Management  | remove or edit products to the website | remove or edit products and pictures for products posted by the main account. through user account. |
|  21 | User/Shopper | sign up for newsletter  | and receive emails with newsletter from the website |
|  22 | Admin/Management | create comments for each products  | leave my review about the products for future users. |

[Back to contents](#table-of-contents)

## **Design Choices**

### **Typography**

- The navigation bar, page titles, and buttons are all in the "'Open Sans'" font family. This design has a very become and neutral, yet friendly appearance, and even though the website is dedicated to health and fitness, it just seemed appropriate to employ.
- And for Logo I decided to apply 'Roboto' to allows letters to take up the space needed to give power aspect to logo. 


### **Colour Scheme**

The colors used in this project are:
- (#BB390F) - Rust
- (#EAE7EA )- Platinum
- (#D8B34E) - Metallic gold
  - The combination of these colors gave a very attractive look to the site. I decided go for rust for the buttons because stand out and packs an energetic punch.

  ![](static/docs/images/color.PNG)

-   ### Wireframes
    - The wireframes, for desktop and mobile, were created using Balsamiq and can be found bellow:

  [wireframe](https://github.com/artneto/Eshopper/blob/main/static/docs/images/wireframe.png)

  

[Back to contents](#table-of-contents)
## Features


### Site Navigation

Links essential for ease of access are displayed in the navigation bar.

| Link | Not logged in  | Logged in | Logged in as super user |
|---------------|---------------|---------------|-------------|
| Home | &#10003;| &#10003; | &#10003; |
| Log In  | &#10003;  | &#10007;  | &#10007;  |
| Register | &#10003;  | &#10007;  | &#10007;  |
| Profile  | &#10007;  | &#10003;  | &#10003;  |
| Log Out  | &#10007;  | &#10003;  | &#10003;  |
| Search  | &#10003;  | &#10003;  | &#10003;  |
| Add Product | &#10007; |&#10007;  |  &#10003; |
| edit/remove Product | &#10007; |&#10007;  |  &#10003; |
| Add Comment | &#10007; |&#10003;  |  &#10003; |

### Exisiting Features

#### Register an account
- Anyone can register free of charge and make their own account with their essential information. In the navigation bar, there is a registration button. Only a username, email address and password are required.

#### Log In/ Log Out to/from Account
- Registered users can securely log in and out using the login/logout buttons on the navigation bar.

#### View, search and sort products 
- The "Shop Now" button on the home page and the navigation bar both provide access to the products. By clicking on the image of the product they to give more information about the product, users may view detailed information such as cost, brand, and product ratings.
Users can search for a specific product by name or by keyword using the search box at the top of the page.
A search box at the top of the screen allows you to filter products by category, and a dropdown selector on the right of the screen allows you to sort by price, classification as A-Z products, or low-to-high pricing.

#### Add/remove products to/from cart and update quantity
- On the product detail page, unregistered users can add items to their shopping cart.
Once logged in, customers can add items from the detailed product page to their bag and choose how many of that particular item to add to their cart. The user must click on the cart information to be taken to the cart page, where there will be action buttons to remove items from the cart and entries to change the quantity.

#### Payment, save information and confirmation email 
  - Users with and without accounts can buy products. When the user is ready to proceed with the  payment and is on the cart page, they can click the "checkout" button to be taken to the payment page, that they can fill out the required fields that really are missing (users can choose to store the information), and then complete their order. Users are routed to a success page where order information is available after the order has indeed been completed. When an order is completed, users are automatically sent a confirmation email including the order details.



#### Profiles 
  - The user can modify the delivery details under the profile page management.

#### Review

  - The product details tab allows users who are logged in to leave reviews for each item. The user will view a message asking for his login in order to submit a comment if he is not currently logged in.

#### Admin Superuser
To access the admin interface by adding /admin to the end of the Eshopper URL.

  In the admin interface, a superuser or administrator can:
  -  View the list of categories and goods and create, update, or delete them.
  -  Product and its information may be edited, deleted, or added.
  -  View the whole list of users and remove any you want.
  -  View the order history and all associated details. Which user, when, how much, what order number, etc.
 
### Feature Features

- Integrate OAuth app to add Google login for quick user registration and login.
- A star rating or upvote feature for the products.
- Implement a space where users can discuss diet or training tips with other users.
- Adding a Sold Out option to price field.

### Error Page

 - 404 page created to redirect users back to the main site in case of an error

  ![](static/docs/images/404error.PNG)

 - 500 error page created to redirect users to the main site after a server error

 ![](static/docs/images/500error.PNG)

### Responsive Design

- The application has been developed for mobile devices but it has been adjusted to provide such a wonderful experience for desktop and tablet users too though.

### Defensive Design

 - Form Validation

    - All forms also have form validation to help ensure the required information is entered        before    submission.
    If incorrect data is entered, a warning message will be displayed to advise the user on how to proceed.

    - A default image will be added if a product is added without an associated image, however form ’ll work this unlikely.

 - Unauthorised Attempts

    - If a user attempts to access a section of the website for that they're not permitted, they will receive an error 404 message when the page is loaded.

 - @login_required

   -  Addition of the login required decorator to prohibit access to specific pages. Only users     who've been granted approval can add, edit, delete, and edit products.
    A user whom have logged out would be sent to the login page if they attempt to access a restricted page.

 - Review

    - Only users who have received approval can leave a review about the available product. The comment box will be available on the products details page.

  - Bag 

   - Validation has been put in place to ensure sure that it only 99 items at the most can be put there in bag.
    If 0 is selected, the item is taken out of the bag.
    The user will have access to the necessary information, such as the front addition for purchases under 50 euros.




[Back to contents](#contents)

#### Database Schema

  - PostgreSQL: SQL triught  PostgreSQL was used for fixtures categories.json and products.json
  
  - SQLite: A cloud-based database that stores fields for products, users, orders.
  

  The ER diagram schema is below:

![](static/docs/images/ERdiagram.PNG)
  

[Back to contents](#table-of-contents)
## Technologies


### **Languages**

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
  - Used as the main markup language for the website content.
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
  - Used to style the individual webpages.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - Used to show the questions through pagination and for the game play.
- [Python 3](https://www.python.org/)
    - Used to run the site and database

[Back to contents](#table-of-contents)
    
### **Frameworks**

- [Bulma](https://bulma.io/)

- [Django](https://www.djangoproject.com/)

[Back to contents](#table-of-contents)

### **Libraries**

  - Panda: Built on top of the Python programming language, Panda Library is an open source data analysis  and manipulation tool that is quick, strong, adaptable, and simple to use. On the home page, it was utilized to create a section listing the best sold products.

  - OS: included in this website in order to provide basic utility modules for Python.

  - SYS: functions and variables that was used to manipulate different parts of the Python runtime environment.

[Back to contents](#table-of-contents)

### **Tools**

  - [Git](https://git-scm.com/)

  - [GitHub](https://github.com/)
  
  - [Gitpod](https://www.gitpod.io/)
  
  - [Heroku](https://www.heroku.com/home)

  - [AWS](https://aws.amazon.com/)

  - [Stripe](https://stripe.com/)

  - [Google fonts](https://fonts.google.com/)

  - [Htmlcolorcodes](https://htmlcolorcodes.com/)

  - [Favicons](https://favicon.io/)
  
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse)

  - [Website Mockup Generator](https://websitemockupgenerator.com/)

  - [JSHint](https://jshint.com/)

  -  [Balsamiq](https://balsamiq.cloud/)
  
  -  [Mailchimp](https://mailchimp.com/)

  - [PEP8 Online](http://pep8online.com/)

  - [W3C Markup Validator](https://validator.w3.org/)

  - [Jigsaw Validator](https://jigsaw.w3.org/css-validator/)

  - [web page mobile friendly ](https://www.google.com/search?q=mobile+friendly+test/)

  - [Lucidchart](https://www.lucidchart.com/pages/)

[Back to contents](#table-of-contents)

## Manual Testing

  ## Home Page

  - The user is given an introductory text and a "Shop Now" button on the homepage. The user will be directed to the products page by this.


  ![](static/docs/images/home.PNG)

  - The header area also provides access to the products page for the user. The user can choose from a variety of categories from which the products are then sorted. 

  ![](static/docs/images/navbar.PNG)

  - The user can utilise the search bar in the header area to look up products. By entering different keywords, brand or sku, the search bar will provide a filtered list of results for those that do.

  ![](static/docs/images/topnav.PNG)

  - Testing product search bar. 

  ![](static/docs/images/test01.PNG)

 - The homepage also includes a newsletter signup area that will appear on desktop computers and other devices.

 ![](static/docs/images/newsletter.PNG)

 - Last but not least, I also developed a function that displays the best-selling items depending on the transactions handled throughout the test period.

 ![](static/docs/images/home1.PNG)

 ## Products

 - The user is presented with a list of products from the products page, each of which includes an image, the product name, category, price, brand, and rating. The top left corner also shows the overall number of goods. Using the filter bar in the upper right corner, the user can also continue to filter the products. The user can choose the headline choice and the level of filtering specificity from the dropdown menus to filter for particular categories.

 ![](static/docs/images/productsearch.png)


 - Only registered user will be allowed to leave a review for the product.

  ![](static/docs/images/review01.PNG)

 - User logged he can pick any product and write a review

 ![](static/docs/images/reviw2.PNG)

 - Once submitted an alert message will be displayed to indicate that the comment has been posted.

  ![](static/docs/images/review3.PNG)

 - By selecting the product, the user will receive a notice that the product has been added to the  bag. The customer will see the value of the product, the current offer and will have the option to view bag or finalizing the purchase.

 ![](static/docs/images/bag1.PNG)

  The user has the option to change the quantity and contents of their bag. The + and - icons can be used by the user to raise or reduce the product amount. By clicking the update button, the user can then update their bag with the necessary quantity adjustment, which also updates the overall bag total. The user also has the option of manually entering the quantity they want to change. By choosing the remove button, the user can also take the item out of the bag. The object in the bag will be fully removed as a result. A fresh alert message containing the changes will appear each time a change is made to the bag.

 - Only the admin or the person who added the product on the Eshopper website can edit or delete the selected product, this function is not available for non-users.

 ![](static/docs/images/admin01.PNG)

 - To edit the product you need the information needed to complete the form in the Porduct Management area.

 ![](static/docs/images/editpro.PNG)

 - This non-image image will be displayed by default if the product doesn't have a picture.

  ![](static/docs/images/no-img.PNG)


 ## Purchase 

 - The user will be asked to provide the delivery details along with the complete list of the purchase's items. The "Adjust Bag" button allows the user to return to the shopping bag and make additional changes. Otherwise, the user may choose to pay by clicking the "Complete Order" button. Through Stripe, which uses a secure way, the payment is handled.

 ![](static/docs/images/bag02.PNG)

 - The user is redirected to the confirmation page, where the order confirmation is displayed, after the order has been submitted.

  ![](static/docs/images/bag3.PNG)

 - Email confirmation:

  ![](static/docs/images/eshopperemail.PNG)

### Creating an account

  Along with the superuser account (/admin), I've made a personal account for myself. Verify that authentication went smoothly.

  ![](static/docs/images/register.PNG)

### Logging in to an account

  There were several attempts to log in and out. It performed as intended.

  ![](static/docs/images/signin.PNG)


### Journal 
 
  User/Admin can create journal post with this model. 

 ![](static/docs/images/blog.PNG)


### Contact 
 
  User/Shopper can contact website admin in case needs help with your order or website access. The user received a confirmation or error message if the form is invalid.

 ![](static/docs/images/form1.PNG)

### Validators

- [W3C HTML Validator](https://validator.w3.org) 
  - checkout_success.html
  - checkout_success.html
  - checkout.html
  - index.html
  - add_products.html
  - edit_product.html
  - product_detail.html
  - products.html
  - quantity_input_script.html
  - profile.html
  - 404.html
  - 500.html
  - base.html
  - main-nav.html
  - mobile_top_header.html
  - toast_error.html
  - toast_info.html
  - toast_success.html
  - toast_warning.html
  - authentication_error.html
  - connections.html
  - login_cancelled.html
  - signup.html
  - blog.html
  - add_blog.html
  - edit_blog.html
  - contact.html 


- [W3C CSS Validator](http://jigsaw.w3.org/css-validator/)
 - base.css
 - profile.css

### Other testing 
- Google Chrome, and Safari, were among the browsers on which the project was evaluated.
- The project was tested on the iPad, iPhone 12 Pro Max, Iphone 10 mini, MacBook Air, and Samsung galaxy a32.
- To get user feedback, enhance the user experience, and find any potential problems, Eshopper was put to the test among friends and family.


### Bugs fixed

- I needed to remove to add review in the product_detail view but the solution was to define in the product_detail view.

### Know Bugs 

- Home page hero image is not rendered on Iphone 12 pro Max.


[Back to contents](#table-of-contents)

## Deployment

### Deployment to Heroku

This project was deployed to [Heroku](https://www.heroku.com/). Find the steps bellow:

1. Go to Heroku webpage and create a new app
1. Click on "Resources" tab and provision a new PostgreSQL database.
1. In order to use PostgreSQL, both packages `dj_database_url` and `psycopg2` have to be installed on Gitpod.
1. Import `dj_database_url` into the project's [`settings.py`](/eshopper/settings.py) to setup new database.
1. Disable the default database(SQLite) in the project's [`settings.py`](/eshopper/settings.py) and add the PostgreSQL database URL stored in the variable `DATABASE_URL`(can be found by clicking on the "settings" tab followed by clicking on "reveal config vars") in order to connect to PostgreSQL.
1. Run migrations (due to the use of PostreSQL) on Gitpod.

    ```
    $ python3 manage.py migrate
    ```

1. Load data (Categories and Products JSON files in the [`fixtures`](/products/fixtures) folder).
- Load categories first 

    ```
    $ python3 manage.py loaddata categories
    ```

- Then load products

    ```
    $ python3 manage.py loaddata products
    ```

1. Create superuser:

    ```
    $ python3 manage.py createsuperuser 
    ```

1. In the project's [`settings.py`](/eshopper/settings.py), re-enable the projec's default database(disabled in step number 5) and with an if statment make sure that when the app is running on Heroku the connection is made to PostgreSQL or otherwise to default database (SQLite).
1. Install `gunicorn` package on Gitpod
1. Create Procfile
1. Set `DISABLE_COLLECTSTATIC` to `1` on Heroku (so heroku does not collect static files during deployment).

    ```
    $ heroku config:set DISABLE_COLLECTSTATIC=1 --app e-shopperonline
    ```

1. Add `ALLOWED_HOSTS` variable(containing host name of the premiumbody app and the localhost) to project's [`settings.py`](/eshopper/settings.py) file.
1. Commit and Push to Github
1. Since the app was created via the Heroku webpage, initializing heroku git remote is necessary before pushing to Heroku

    ```
    $ heroku git:remote -a e-shopperonline
    ```

1. Push to Heroku

    ```
    $ git push heroku master
    ```

1. Finally, enable automatic deployment to Heroku when pushing to Github by going to Heroku webpage, clicking on the "Deploy" tab and then on "Connect to Github" button. Search for the eshopper repo and click on "Connect". Scroll down to the "Automatic deploys" section and click on "Enable Automatic Deploys".

[Back to contents](#table-of-contents)


### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
1. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
1. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/artneto/Eshopper)
1. Under the repository name, click "Clone or download".
1. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
1. Open Git Bash
1. Change the current working directory to the location where you want the cloned directory to be made.
1. Type "git clone", and then paste the URL you copied in Step 3.

    ```
    $ git clone https://github.com/artneto/Eshopper
    ```
    
 ### Amazon Services (S3)
 
 After the deployment to Heroku, Amazon Web Services(AWS) - S3 was used to store all the media and static files in Eshopper app.

 ## Web Marketing & Business

 A Facebook page for Eshopper was made as part of the website marketing campaign.
 Please take note that I made a fake Facebook page using the Code Institute template.

 ![](static/docs/images/facebook.PNG)

## Credits

### Media

-   The hero image is from the free stock image library [Pexels](https://pexels.com/).
-   The product pictures came from Amazon [Amazon](https://amazon.co.uk/).

### Acknowledgements


-   A major part of the logic and web application structure used in the Eshopper project is from a Code Institute tutorial that can be found in this [GitHub repository](https://github.com/ckz8780/boutique_ado_v1). 

- My Family for testing the site and giving feedback on different devices.

- Code Institute slack channel for porviding further information and support. 

- My friend and collegue Beatriz Amorim for supporting me and providing me feedback.

[Back to contents](#table-of-contents)


