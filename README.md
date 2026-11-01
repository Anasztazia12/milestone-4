# The Old Ferryman

The Old Ferryman is a made-up gastropub in Norfolk, England. This project is its website, where customers can order pub food online, pay in advance and collect it at a time that suits them.

## Purpose

Ordering takeaway by phone is slow. Customers can wait on hold, they cannot see the full menu, and they do not know when their food will be ready. Staff have to stop working to answer the phone, and it is easy to get an order wrong.

The Old Ferryman solves this by putting the whole process online. Customers choose their food, pick a collection time, pay by card and then follow the status of their order. Staff can see all orders in one place and update them as they go.

The site is also a demo for my web design business, to show pubs, cafes and restaurants what an ordering system could look like for them.

## Target Audience

| User | What they want |
| --- | --- |
| New visitor | To see the menu and prices quickly |
| Returning customer | To order faster and see past orders |
| Customer with allergies | To check allergens before ordering |
| Restaurant staff | To see orders and update their status |
| Restaurant owner | To manage the menu and prices |

## Feature Priorities (MoSCoW)

### Must have

- Menu page with food categories and prices
- Food detail page with description and allergens
- Register, log in and log out
- Shopping bag where items can be added, changed and removed
- Stripe checkout in test mode
- Clear messages for successful and failed payments
- Order tracking page that is available after payment
- Reviews that customers can create, edit and delete
- Staff page to see orders and update their status

### Should have

- Search and filter by category or allergen
- Choice of collection time at checkout
- Order history in the user profile
- Saved contact details for faster checkout

### Could have

- Live order status without refreshing the page
- Average star rating on each food item
- Order confirmation emails

### Won't have (for now)

- Delivery by driver
- Table booking
- Loyalty points
- A mobile app

## Wireframes and Mockups

These boards show the planned pages. They were made before coding, using the placeholder name BistroBell and example dishes, so the finished site will use The Old Ferryman branding and pub food. Collection replaces the delivery tracking shown here, and Stripe is the only payment method.

- [Desktop wireframes and mockups](docs/wireframes/desktop-wireframes-and-mockups.png)
- [Mobile wireframes and mockups](docs/wireframes/mobile-wireframes-and-mockups.png)

Tablet wireframes are still to be added.

## Credits

### AI assistance

I used Claude (Anthropic) to help plan this project and to draft the text of this README, and to write the starter code for the home app and the environment variable settings, the base template and the first stylesheet.

### Libraries

- [Bootstrap 5.3.3](https://getbootstrap.com/) for layout and the navigation menu

### Design images

The wireframe and mockup boards in docs/wireframes were generated with ChatGPT (OpenAI).

### Photos

| Photo | Creator | Source | Licence |
| --- | --- | --- | --- |
| Pub interior | [Pexels](https://pixabay.com/users/pexels-2286921/) | [Pixabay](https://pixabay.com/photos/restaurant-furniture-interiors-1837150/) | [Pixabay Content License](https://pixabay.com/service/license-summary/) |
| Salmon teriyaki | [Wow_Pho](https://pixabay.com/users/wow_pho-916237/) | [Pixabay](https://pixabay.com/photos/food-salmon-teriyaki-fish-eat-712665/) | [Pixabay Content License](https://pixabay.com/service/license-summary/) |
| Pizza | [MatteoPhotoPro2020](https://pixabay.com/users/matteophotopro2020-11599221/) | [Pixabay](https://pixabay.com/photos/pizza-kitchen-pizzeria-food-tomato-5275191/) | [Pixabay Content License](https://pixabay.com/service/license-summary/) |
| Pizza and salad | [Sarda_Bamberg](https://pixabay.com/users/sarda_bamberg-32538049/) | [Pixabay](https://pixabay.com/photos/food-pizza-pizzeria-salad-7724008/) | [Pixabay Content License](https://pixabay.com/service/license-summary/) |
| Burger | [2SIF](https://pixabay.com/users/2sif-26811215/) | [Pixabay](https://pixabay.com/photos/burger-double-burger-hamburger-food-7323697/) | [Pixabay Content License](https://pixabay.com/service/license-summary/) |
| Chicken burger | [SylwesterL](https://pixabay.com/users/sylwesterl-34617078/) | [Pixabay](https://pixabay.com/photos/hamburger-sandwich-chicken-healthy-8026581/) | [Pixabay Content License](https://pixabay.com/service/license-summary/) |
| Blueberry cheesecake | [thezworld](https://pixabay.com/users/thezworld-13524303/) | [Pixabay](https://pixabay.com/photos/blue-berry-cheese-cake-blue-berry-4547988/) | [Pixabay Content License](https://pixabay.com/service/license-summary/) |
| Cheesecake | [matthiasboeckel](https://pixabay.com/users/matthiasboeckel-3930681/) | [Pixabay](https://pixabay.com/photos/cake-cheesecake-pastry-yummy-7796383/) | [Pixabay Content License](https://pixabay.com/service/license-summary/) |
| Chocolate cake | [Rbribella12](https://pixabay.com/users/rbribella12-52121918/) | [Pixabay](https://pixabay.com/photos/chocolate-cake-dessert-10261167/) | [Pixabay Content License](https://pixabay.com/service/license-summary/) |
| Fish and chips | [Timbigger](https://pixabay.com/users/timbigger-1333127/) | [Pixabay](https://pixabay.com/photos/fish-and-chips-cod-and-chips-8645438/) | [Pixabay Content License](https://pixabay.com/service/license-summary/) |
| Fish burger | [Abdullah_Shakoor](https://pixabay.com/users/abdullah_shakoor-5012922/) | [Pixabay](https://pixabay.com/photos/outback-steak-burger-khobar-fish-2492925/) | [Pixabay Content License](https://pixabay.com/service/license-summary/) |
| Shepherd's pie | [TehzeebNoah](https://pixabay.com/users/tehzeebnoah-56285559/) | [Pixabay](https://pixabay.com/photos/shepherds-pie-mashed-potato-meat-10366225/) | [Pixabay Content License](https://pixabay.com/service/license-summary/) |
| Meat pie | [tehzeebkazmii](https://pixabay.com/users/tehzeebkazmii-46957846/) | [Pixabay](https://pixabay.com/photos/meat-pie-pastry-crust-savory-beef-10366164/) | [Pixabay Content License](https://pixabay.com/service/license-summary/) |
| Roast duck | [RitaE](https://pixabay.com/users/ritae-19628/) | [Pixabay](https://pixabay.com/photos/roast-duck-roasted-duck-dumplings-1812345/) | [Pixabay Content License](https://pixabay.com/service/license-summary/) |
| Beef steak | [Rierosa222](https://pixabay.com/users/rierosa222-5673828/) | [Pixabay](https://pixabay.com/photos/beef-steak-meat-food-tenderloin-2509104/) | [Pixabay Content License](https://pixabay.com/service/license-summary/) |
| Sandwich | [rajdeepcraft](https://pixabay.com/users/rajdeepcraft-15019006/) | [Pixabay](https://pixabay.com/photos/sandwich-food-hamburger-burger-5930496/) | [Pixabay Content License](https://pixabay.com/service/license-summary/) |
| Salmon dish | [cattalin](https://pixabay.com/users/cattalin-560479/) | [Pixabay](https://pixabay.com/photos/new-years-eve-salmon-fish-seafood-518032/) | [Pixabay Content License](https://pixabay.com/service/license-summary/) |
