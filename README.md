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
