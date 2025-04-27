| Test Case ID | Title | Test Procedure | Expected Results | Status |
| ------------ | ------ | --------| ------------ | ------- |
| TC_001 | Home Page Route (/) | Click on the “Home” tab to trigger “Get / HTTP/1.1”. Click on the “Athletica Sportswear” to trigger “Get /HTTP/1.1”. | 200 OK, renders “home.html” and static images. | Pass |
| TC_002 | Women’s Clothing Route (/) | Hover over the “Women” tab and click on the “Clothing” tab to trigger “GET /women/clothing HTTP/1.1”. | 200 OK, renders “women_clothing.html” and static images. | Pass |
| TC_003 | Women’s Shoes Route (/) | Hover over the “Women” tab and click on the “Shoes” tab to trigger “GET /women/shoes HTTP/1.1”. | 200 OK, renders “women_shoes.html” and static images. | Pass |
| TC_004 | Women’s Accessory Route (/) | Hover over the “Women” tab and click on the “Accessory” tab to trigger “GET /women/accessory HTTP/1.1”. | 200 OK, renders “women_accessory.html” and static images. | Pass |
| TC_005 | Men’s Clothing Route (/) | Hover over the “Men” tab and click on the “Clothing” tab to trigger “GET /men/clothing HTTP/1.1”. | 200 OK, renders “men_clothing.html” and static images. | Pass |
| TC_006 | Men’s Shoes Route (/) | Hover over the “Men” tab and click on the “Shoes” tab to trigger “GET /men/shoes HTTP/1.1”. | 200 OK, renders “men_shoes.html” and static images. | Pass |
| TC_007 | Men’s Accessory Route (/) | Hover over the “Men” tab and click on the “Accessory” tab to trigger “GET /men/accessory HTTP/1.1”. | 200 OK, renders “men_accessory.html” and static images. | Pass |
| TC_008 | Search Items by Name | Input “Relay Sneakers” into search bar | 200 OK, results containing “Relay Sneakers,” static image render, option to add to cart appears. | Pass|
| TC_009 | Search Items by Color | Input “Red” into search bar | 200 OK, results containing “red” in their description, static images render, option to add to cart appears. | Pass|
| TC_010 | Search Items by Category | Input “Women” into search bar | 200 OK, results for Women clothing, shoes, accessories, static images render, option to put items into cart appears. | Pass |
| TC_011 | Search Items by Subcategory | Input “Shoes” into search bar | 200 OK, results for shoes under Men and Women category, static images render, option to put items into cart appears. | Pass |


