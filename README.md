SKU Pricing Rule Project
==========================

DiUS is starting a computer store. You have been engaged to build the checkout system. We will start with the following products in our catalogue

SKU	Name	Price
ipd	Super iPad	$549.99
mbp	MacBook Pro	$1399.99
atv	Apple TV	$109.50
vga	VGA adapter	$30.00
As we're launching our new computer store, we would like to have a few opening day specials.

we're going to have a 3 for 2 deal on Apple TVs. For example, if you buy 3 Apple TVs, you will pay the price of 2 only
the brand-new Super iPad will have a bulk discounted applied, where the price will drop to $499.99 each, if someone buys more than 4
we will bundle in a free VGA adapter free of charge with every MacBook Pro sold
As our Sales manager is quite indecisive, we want the pricing rules to be as flexible as possible as they can change in the future with little notice.

Our checkout system can scan items in any order.

Features:
* Checkout
* PricingRule
* UnitTests

# Getting Started

The project is ready to run as is. You will need Python 3.x or later.

## Create a Virtual Environment

After cloning or downloading the repo, create a Python virtual environment with:

```
python -m venv myvirtualenv
```

for Python 3.x.

For Python 2.7, use the `virtualenv` command:

```
virtualenv myvirtualenv
```

This will create the virtual environment in the current directory as `myvirtualeenv`. You can place the virtual environment in any location. Alternative, you can use any of a number of tools for managing Python virtual environments. See note below on `pipenv`, a popular option.


## Testing

You can run unit tests in test folder:
```
python -m unittest discover .\test\
```

