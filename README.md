# OOP-Python-Project
A skeleton for an online store, which could be used in text mode. The suggested store will be one that sells electronics, but basically, it could sell anything else. Like in a real store, this one will contain some categories of products and for each category. It is also able to manage the categories and the products (add, remove, list). 

Objects of the project: 

Categories - will contain a collection of all categories we enter. Examples of categories: Amplifiers,
Receivers, Speakers, Turntables, and so on;

Category - describes a single category;

Product - base class for all the products;

Amplifier - inherits the Product class and will contain info specific for that kind of product (power,
number of channels, size);

Receiver - inherits the Products class and contains info specific to that kind of product (number of
channels, color, size);

Turntable - inherits the Product class and contains specific info for that kind of product (speed,
connection type (wired, Bluetooth), size);

Products - contains a collection of all the products in the store;

Orders - models an order to be placed in the store. 

All these components of our store will persist on the disk.
