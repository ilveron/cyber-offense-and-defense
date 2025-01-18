from lxml import html

# Exercise Set 1 - Basic Selections
sample_html = '''
<html>
    <body>
        <div class="container">
            <h1>Welcome</h1>
            <p class="intro">This is an introduction</p>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </div>
    </body>
</html>
'''

tree = html.fromstring(sample_html)

# Exercise 1: Write an XPath to select the h1 element text
exercise1 = tree.xpath("/html/body/div/h1")[0]
print(f"Exercise 1: {exercise1.text}")

# Exercise 2: Write an XPath to select all li elements' text
exercise2 = tree.xpath("//li")
print(f"Exercise 2: {[elem.text for elem in exercise2]}")

# Exercise 3: Write an XPath to select the paragraph with class "intro"
exercise3 = tree.xpath('//p[@class="intro"]')[0]
print(f"Exercise 3: {exercise3.text}")

# Exercise Set 2 - Working with Attributes
sample_html_2 = '''
<html>
    <body>
        <div class="content">
            <article id="post-1">
                <h2>First Article</h2>
                <p class="description">Description 1</p>
                <span class="author">John Doe</span>
            </article>
            <article id="post-2">
                <h2>Second Article</h2>
                <p class="description">Description 2</p>
                <span class="author">Jane Smith</span>
            </article>
        </div>
    </body>
</html>
'''

tree2 = html.fromstring(sample_html_2)

# Exercise 4: Write an XPath to select the title of the article with id "post-1"
exercise4 = tree2.xpath('//article[@id="post-1"]/h2')[0]
print(f"Exercise 4: {exercise4.text}")

# Exercise 5: Write an XPath to select all description paragraphs
exercise5 = tree2.xpath('//p[@class="description"]')
print(f"Exercise 5: {[elem.text for elem in exercise5]}")

# Exercise 6: Write an XPath to select all author names
exercise6 = tree2.xpath('//span[@class="author"]')
print(f"Exercise 6: {[elem.text for elem in exercise6]}")

# Exercise Set 3 - Advanced Selections
sample_html_3 = '''
<html>
    <body>
        <div class="products">
            <div class="product">
                <h3>Laptop</h3>
                <p class="price">$999</p>
                <p class="stock">In Stock</p>
            </div>
            <div class="product">
                <h3>Phone</h3>
                <p class="price">$599</p>
                <p class="stock">Out of Stock</p>
            </div>
            <div class="product">
                <h3>Tablet</h3>
                <p class="price">$399</p>
                <p class="stock">In Stock</p>
            </div>
        </div>
    </body>
</html>
'''

tree3 = html.fromstring(sample_html_3)

# Exercise 7: Write an XPath to select names of all products that are "In Stock"
exercise7 = tree3.xpath('//div[@class="product"][.//p[@class="stock"][text()="In Stock"]]/h3')
print(f"Exercise 7: {[elem.text for elem in exercise7]}")

# Exercise 8: Write an XPath to select the second product's name
exercise8 = tree3.xpath('//div[@class="product"][2]/h3')[0]
print(f"Exercise 8: {exercise8.text}")

# Exercise 9: Write an XPath to select the price of the last product
exercise9 = tree3.xpath('//div[@class="product"][last()]/p[@class="price"]')[0]
print(f"Exercise 9: {exercise9.text}")