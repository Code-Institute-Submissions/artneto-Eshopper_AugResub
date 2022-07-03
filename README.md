# E-shopperonline

## About

**E-shopperonline** 
Is an online store that offers to customers who are looking for food or supplements, from athletes to anyone who wants to get fit. This website has functions to make it easily available our range of products to all users, the website is made to be responsive and simple to use on a range of devices.

Please note: This site was created solely for educational purposes.
Link to the [site](http://e-shopperonline.herokuapp.com//)

## Table of Contents

- [UX (User Experience)]
- [User Stories]
- [Design Choices]
  - [Fonts](https://github.com/)
  - [Colors](https://github.com/)
  - [Imagery](https://github.com/)
  - [Wireframes](https://github.com/)
- [Features](https://github.com/)
  - [Site Navigation](https://github.com/)
  - [Features Implemented](https://github.com/)
  - [Future Features](https://github.com/)
- [Web Marketing & Business]()
  - [Responsive Design](https://github.com/)
  - [Defensive Design](https://github.com/)
  - [Database Schema](https://github.com/)
- [Technologies](https://github.com/)
  - [Languages](https://github.com/)
  - [Frameworks and Libraries](https://github.com/)
  - [Tools](https://github.com/)
- [Testing](https://github.com/)
- [Deployment](https://github.com/)
- [Credits](https://github.com/)
  - [Code](https://github.com/)
  - [Content](https://github.com/)
  - [Media](https://github.com/)
  - [Acknowledgements](https://github.com/)


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

[Back to contents](#contents)

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

-   ### Wireframes
    -   [View Mockups](https://github.com/\\\\\)The wireframes, for desktop and mobile, were created using Balsamiq and can be found bellow:



[Back to contents](#contents)
## Features

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
 
### Features Left to Implement

- Integrate OAuth app to add Google login for quick user registration and login.
- A star rating or upvote feature for the products.
- Implement a space where users can discuss diet or training tips with other users.

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
  
  - SQLite: A cloud-based database that stores fields for products, users, orders..
  
- The Database schema is below:


