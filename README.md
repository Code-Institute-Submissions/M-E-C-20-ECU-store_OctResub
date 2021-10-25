# **ECU Store**: Code Institute MS4 Project

This project is a Full Stack e-commerce website using the Django web framework. Users can create a purchase without signing up, or can register and save their details to a personal profile and mark products as having fixed their vehicle.

View the deployed site: [ECU Store](https://ecu-store.herokuapp.com/).

# Table of contents

> 1.  [Overview](#overview)
> 2.  [UX](#ux)
>     1.  [Strategy](#strategy)
>     2.  [Scope](#scope)
>     3.  [Structure](#structure)
>     4.  [Skeleton](#skeleton)
>     5.  [Surface](#surface)
> 3.  [Features](#features)
>     1.  [Existing Features](#existing-features)
>     2.  [Future Feature Considerations](#future-feature-considerations)
> 4.  [Technologies Used](#technologies-used)
> 5.  [Testing](#testing)
> 6.  [Deployment](#deployment)
> 7.  [Credits](#credits)
>     1.  [Readme](#readme)
>     2.  [Content](#content)
>     3.  [Media](#media)
>     4.  [Code](#code)
> 8.  [Acknowledgements](#acknowledgements)
> 9.  [Disclaimer](#disclaimer)


# Overview

**ECU Store** is a full stack e-commerce store, which allows users to purchase automotive ECU's for specific vehicles. Unregistered users can purchase without needing to register, registered users can mark an item as "Fixed It!", which lets other users know that the product repaired their vehicle. The store is designed to be easy to navigate andintuitive for the user.

The project was developed using **Python** (Django), **HTML**, **CSS**, **JavaScript**, and utilises an SQL database via **PostreSQL**.

---

# UX

## Strategy

### User Stories  

| User Story ID                      | As A/An        | I want to be able to                                                                | So that I can                                                                                         |
|------------------------------------|----------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Viewing and Navigation**         |                |                                                                                     |                                                                                                       |
| 1                                 | Site User      | View a list of products                                      | Select some to purchase                                                             |
| 2                                 | Site User      | View individual product details                      | Identify the price, description, product rating, product image and availability                                                                          |
| 3                                 | Site User      | View how products worked for other users                                                 | Feel confident that the products are effective                                                                               |
| 4                                 | Site User      | Easily view the total of my purchases at any time                                                | Avoid overspending                                                                               |
| 5                                 | Site User      | Contact the store                                                | Make queries about a product, deliveries or to see if an item can be repaired                                                                               |
| **Registration and User Accounts** |                |                                                                                     |                                                                                                       |
| 6                                 | Site User      | Easily register for an account                                                             | Have a personal account and view my profile                                                                                       |
| 7                                 | Site User      | Log In and logout                                                                   | Access my personal account information                                                                 |
| 8                                 | Site User      | Recover my password                                                                 | Recover access to my account.                                                                         |
| 9                                 | Site User | Receive an email confirmation after registering                                                                   | Verify my account registration was successful                                                                         |                                                                                                      |
| 10                                | Site User      | Have a personalised user profile                                              | View my order history and order confirmations, and save my payment information                                               |
| **Sorting and searching**                           |                |                                                                                     |                                                                                                       |
| 11                                 | Site User      | Sort the list of available products                                                       | Easily identify the best rated, best priced and categorically sorted products                                                      |
| 12                                 | Site User | Sort a specific category of product                                                              | Find the best priced or best rated product in a specific category, or sort the products in that category by name                                                                               |
| 13                                 | Site User | Sort multiple categories of products simultaneously                                                        | Find the best priced or best rated products across broad categories                                                            |
| 14                                 | Site User | Search for a product by name or description                                                               | Find a specific product I'd like to purchase                                                                            |
| 15                                 | Site User | Easily see what I've searched for and the number of results                           | Quickly decide whether the product I want is available                                                                              |                                                                |
| **Purchasing and checkout**                    |                |                                                                                     |                                                                                                       |
| 16                                 | Site User      | Easily select the quantity of a product when purchasing it                                                                | Ensure I don't accidentally select the wrong product or quantity                                                                |
| 16                                 | Site User      | View items in my bag to be purchased                                                 | Identify the total cost of my purchase and all items I will receive                                                               |
| 18                                 | Site User      | Adjust the quantity of individual items in my bag                                                     | Easily make changes to my purchase before checkout                                                                      |
| 19                                 | Site User      | Easily enter payment information                                                  | Check out quickly and with no hassle |
| 20                                 | Site User      | Feel my personal and payment information is secure                                                  | Confidently provide the needed information to make a purchase |
| 21                                 | Site User      | View an order confirmation after checkout                                                  | Verify that I haven't made any mistakes |
| 22                                 | Site User      | Receive an email confirmation after checking out                                                  | Keep confirmation of what I've purchased for my records |
| **Admin and store management**                          |                |                                                                                     |                                                                                                       |
| 23                                 | Store owner      | Add a product                                                                      | Add new items to my store                                                                |
| 24                                 | Store owner      | Edit/update a product                                                           | Change product prices, descriptions, images and other product criteria         |
| 25                                 | Store owner          | Delete a product                                                            | Remove items that are no longer for sale                                                                              |
| 26                                 | Store owner          | View site user messages                                                         | Resond to their queries                                                                           |

## Scope

### Functional Requirements

#### Simple and Intuitive Interface

-   Users must be able to navigate, and interact with, the site with ease.
-   Ensure site is responsive to all device sizes.

#### User Management

-   Allow users to create an account, confirm their email address, change their
    password, log in, and log out.

#### Profile

-   Allow users to visit their profile.
-   Allow users to see their order history.
-   Allow users to edit their profile details and edit it if desired.

#### Products

-   Allow users to easily view available products.
-   Allow users to se what vehicles each product is available for.
-   Allow users to view if the product has helped other users.

#### Contact

-   Allow users to reach out to the store owners for product related queries.
-   Have a predefined structure to make it easier for the user to define their issue, and for the store owner to interpret.

#### Admin Tools

-   Allow the store owner to add new products to the database.
-   Allow the store owner to edit or delete existing products from the database.
-   Allow the store owner to view contact requests from site users, and to delete messages if necessary.

## Structure

### Informational Architecture

In order to create a simple interface for the user, each of the project’s core
functions will be isolated into different pages. In an attempt to implement an
intuitive navigation system, a persistent Navbar (Navbar) will be utilised. This will allow a user to navigate the
project with ease, spending minimal time finding attempting to make a purchase, which should help retain users.

#### Navbar

The Navbar will be present across the site and allow users to navigate across the site with ease.

<details>
  <summary>Show Details</summary>

>Applicable User Stories:
>-   1, 4, 6, 7, 14, 17, 18, 23, 26
>
>Applicable Functional Requirements:
>-   Simple, Intuitive, and Engaging Interface
>-   View Products
>-   View Profile
>-   Contact
>-   Register
>-   Login/Logout
>
>Navigational Routes:
>-   All logical pages.
  
</details>  
  

#### Home 

The home page is the initial landing page, and provides a brief overview of the
project’s concept and the appropriate CTAs.

<details>
  <summary>Show Details</summary>

>Applicable User Stories:
>-   1, 6, 7
>
>Applicable Functional Requirements:
>-   Direct users to view products.
>-   Prompt to register
>-   Prompt to login
>
>Navigational Routes:
>-   Products
>-   Log In (Logged Out)
>-   Register (Logged Out)

</details>  
  

#### Account Management

Account Management will allow users to register, create an account, log in, log
out,and reset their password.

<details>
  <summary>Show Details</summary>

>Applicable User Stories:
>-   6, 7, 8, 9, 10
>
>Applicable Functional Requirements:
>-   User Management
>
>Navigational Routes:
>-   Account verification
>-   Login Redirect

</details>  
  

#### Contact 

The will allow users to direct queries to the store manager.

<details>
  <summary>Show Details</summary>

>Applicable User Stories:
>-   5, 26
>
>Applicable Functional Requirements:
>-   Contact store owners.
>-   Predetermined subjects help both the owner and the user to narrow down the query.
>-   Contact admin will allow the store owner to view user messages.
>
>Navigational Routes:
>-   N/A

</details>  
  

#### Products

The products page will allow all users to view all products available in the store. From there the user can filter on category, price, manufacturer or ECU. Users can select products to view further information on them and decide to add to bag if a site user, or edit/delete items if a store owner.

<details>
  <summary>Show Details</summary>

>Applicable User Stories:
>-   1, 2, 3, 11, 12, 24, 25
>
>Applicable Functional Requirements:
>-   Simple, Intuitive, and Engaging Interface
>-   View products.
>-   Sort products.
>-   Add to bag.
>-   Edit/delete products.
>
>Navigational Routes:
>-   Bag
>-   Edit/delete products (Admin)

</details>  
  

#### Profile

The profile will allow users to see their account details and order history. A user can update their account details to enable faster checkout.

<details>
  <summary>Show Details</summary>

>Applicable User Stories:
>-   10, 19, 21
>
>Applicable Functional Requirements:
>-   Simple, Intuitive, and Engaging Interface
>-   User Management
>-   View order history
>
>Navigational Routes:
>-   N/A 

</details>  
  

#### Admin Tools

The admin tools page will allow the store owner to add products and to view messages from site users.

<details>
  <summary>Show Details</summary>

>Applicable User Stories:
>-   23, 26
>
>Applicable Functional Requirements:
>-   Simple and Intuitive Interface
>-   Add new products
>-   View messages
>
>Navigational Routes:
>-   N/A

</details>  
 
 ### Design

The following considerations were made when planning the project’s design.

#### Navigation

-   It should be simple and intuitive for a new user to land on the site and navigate it without confucion.
-   All text sould be clear in purpose to a user and positioned to allow a user to understand the site navigation.

#### Visual 

-   Products should contain images to identify to the customer the accuracy of the product.
-   Each image will be appropriately sized and positioned, allowing a user to
    understand their relationship to the products, yet not overwhelm or misuse the available screen space.
-   Text should be clear, appropriately sized and coloured.

#### Physical

-   All features will be available to all screen sizes and devices.
-   Users will be able to access and engage with this project anywhere with an
    internet connection.

#### Time

-   The site is designed to allow quick and easy purchasing of products.
-   A user will be able to log out of website at any point, and log back in on any other device and resume where they left off.

## Skeleton

### Wireframes

**Due to the resolution of the wireframe documents, it is recommended that these PDFs 
are downloaded to be viewed in the browser, rather than using GitHub’s native PDF viewer.**

-   All Wireframes: [Link]()
-   Navbar Wireframe: [Link]()
-   Home Wireframe: [Link]()
-   Products Wireframe: [Link])
-   Profile Wireframe: [Link]()
-   Login/Register Wireframe: [Link]()
-   Contact Wireframe: [Link]()
-   Product Management Wireframe: [Link]()
-   Contact Admin Wireframe: [Link]()

### Database

This project utilises a Relational Database via PostgreSQL for storing User
Credentials, User Profiles, Products, Categories,  and Contacts. The Database went follwed a similar schema to the Boutique Ado project, as I thought it was a solid and logical place to build an e-commerce site from.

**Schema**

<details>
  <summary>Final DB Schema</summary>

![Final DB Schema]()

</details>

## Surface

This project utilises a
simple colour scheme, designed for a visually soft style.

### Colour Scheme

The primary colour scheme, utilised for the layout, framework, and text of the
website, focuses on a off-white to almost black colour scheme.

![Primary Colour Scheme]()

The variations of white were implemented in the navbar and backgrounds, and as text on buttons and the footer.

The shades of black were used on buttons, to signal their purpose by contrasting with the white background.

<details>
  <summary>Contrast Results</summary>

**Chalk on Raisin**  

![Contrast – Chalk on Raisin](https://res.cloudinary.com/bak2k3/image/upload/v1628878126/CIRPG/Contrast_-_Chalk_on_Raisin_bejrgd.jpg)


**Chalk on Rich**  

![Contrast – Chalk on Rich](https://res.cloudinary.com/bak2k3/image/upload/v1628878126/CIRPG/Contrast_-_Chalk_on_Rich_bqfoal.jpg)

</details>

### Typography

The font [Lato](https://fonts.google.com/specimen/Lato) was used across the whole project, as I think it suits the simple and minimalistic purpose o fthe site, and is easily readable.

#### Underlined Links

The navbar within the project produce an underlined effect when hovered (desktop) or pressed (mobile). This helps communicate that the elements
are interactive, and produces appropriate user feedback when a user engages with
these elements.

![Visual Effects – Underline]()

#### Button Effect 

When a user hovers (desktop) or pressed (mobile) buttons, the colour is changed slightly to indicate this event.

![Visual Effects – Buttons]()

---

# Features

## Existing Features

### General

1. Navigation bar on top of each page that consists of:
    * Site logo
    * Search bar
    * Main manvigation menu
    * Menu entries to Login/Register for anonymous users
    * My Account menu entry with a dropdown sub menu for authorized users
    * Shopping bag menu entry with a total amount displayed
2. Footer with social links and copyright message.
2. Responsive layout that is adapted to desktop and mobile screen sizes.
3. Supported by all of the most popular web browsers.
4. Instant feedback from the site to the user with the help of pop-up messages when important actions take place.

### Products

1. View multiple products on single page.
2. View each product on separate page.
3. Search box where products can be found by name or description.
4. Sort products by price, name and categories, both ascending and descending.
5. Filter products by categories.
6. Add product to the shopping bag with specified quantity.

### Bag

1. View shopping bag.
2. Update quantity or Remove product(s) from the shopping bag.
3. View checkout page.

### Checkout
1. Submit delivery information and payment details on checkout page.
2. Complete an order and make a payment.
3. View order details on payment completion.
4. Receive an email with order details on payment completion.

### Profile
1. Update personal delivery information that will be used to prefill checkout form
2. View order history
3. Logout from the site

### Contact
1. Contact store owners.

### Admin
1. Execute all the feautures of users mentioned above.
2. Add new product(s) to the site.
3. Modify or delete existing products on the site.
4. View contact forms submitted by users.

### Future features
1. Add possibility for authorised users to create a wishlist.
2. Add a newsletter signup.
3. Add a product testimones page.

---

# Technologies Used

## Development

-   The project was written and tested in
    [gitpod](https://www.gitpod.io/).
-   The project was debugged using Google
    Chrome [Dev
    Tools](https://developer.chrome.com/docs/devtools/).
-   The project uses [GitHub](https://github.com/) for hosting source code and utilising git version control.

## Design

-   The project's wireframes were designed in
    [Balsamiq](https://balsamiq.com/wireframes/).

## HTML/CSS

HTML5 and CSS3 are used throughout this project.

-   The project uses [Bootstrap](https://getbootstrap.com/) 5 as the HTML/CSS Framework..
-   The project uses [FontAwesome](https://fontawesome.com/) v5.15.4, for the site icons.
-   The project uses [Google Fonts](https://fonts.google.com/) for typography.

## Python

This project uses Python version 3.9.6 for back-end infrastructure and data
pre-processing.

A list of the packages dependencies can be found at [requirements.txt](requirements.txt).

## JavaScript

This project uses JavaScript ES6.

-   The project uses [jQuery](https://jquery.com/), a JavaScript library, for
    DOM Traversal, HTML Manipulation, and Event Handling.
-   The project uses the [Stripe.js](https://stripe.com/docs/js) library for
    handling Stripe payment objects.

## Hosting
-   This project is hosted through [Heroku](https://www.heroku.com/).
-   This project’s images are hosted via [AWS S3](https://aws.amazon.com/s3/).

## Database

The project uses [PosteSQL](https://www.postgresql.org/), a relational Database,
for data storage, and this is managed via
[Heroku](https://www.heroku.com/postgres).

## Testing Technologies

-   The project's HTML was validated using [W3C HTML Markup Validator](https://validator.w3.org/).
-   The project's CSS was validated using [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/).
-   The project's JS was validated using [JSHint](https://jshint.com/).
-   The project’s Python was validated using [Pylint](https://pylint.org/).
-   The project's accessibility was assessed via Google Chrome's [Lighthouse](https://developers.google.com/web/tools/lighthouse).