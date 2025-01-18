from lxml import html

sample_bookstore = '''
<html>
    <body>
        <div class="bookstore">
            <div class="category" id="fiction">
                <h2>Fiction Books</h2>
                <div class="book" rating="4.5">
                    <h3 class="title">The Great Adventure</h3>
                    <p class="author">Sarah Wilson</p>
                    <div class="details">
                        <span class="price">$24.99</span>
                        <span class="pages">320 pages</span>
                        <span class="published">2023</span>
                        <div class="availability">
                            <span class="status available">In Stock</span>
                            <span class="copies">5 copies</span>
                        </div>
                    </div>
                    <ul class="tags">
                        <li>adventure</li>
                        <li>fantasy</li>
                    </ul>
                </div>
                <div class="book" rating="4.8">
                    <h3 class="title">Mystery Manor</h3>
                    <p class="author">John Smith</p>
                    <div class="details">
                        <span class="price">$19.99</span>
                        <span class="pages">280 pages</span>
                        <span class="published">2022</span>
                        <div class="availability">
                            <span class="status unavailable">Out of Stock</span>
                            <span class="copies">0 copies</span>
                        </div>
                    </div>
                    <ul class="tags">
                        <li>mystery</li>
                        <li>thriller</li>
                    </ul>
                </div>
            </div>
            
            <div class="category" id="non-fiction">
                <h2>Non-Fiction Books</h2>
                <div class="book" rating="4.2">
                    <h3 class="title">Science Today</h3>
                    <p class="author">Dr. Emily Brown</p>
                    <div class="details">
                        <span class="price">$29.99</span>
                        <span class="pages">400 pages</span>
                        <span class="published">2023</span>
                        <div class="availability">
                            <span class="status available">In Stock</span>
                            <span class="copies">3 copies</span>
                        </div>
                    </div>
                    <ul class="tags">
                        <li>science</li>
                        <li>education</li>
                    </ul>
                </div>
            </div>
        </div>
    </body>
</html>
'''

tree = html.fromstring(sample_bookstore)

# Exercise 1: Select all book titles published in 2023
exercise1 = tree.xpath('//div[@class="book"]/h3[@class="title"][following-sibling::div/span[@class="published"][number()=2023]]')
print(f"Exercise 1: {[elem.text for elem in exercise1]}")

# Exercise 2: Find all books with a rating higher than 4.5
exercise2 = tree.xpath('//div[@class="book" and @rating > 4.5]/h3[@class="title"]')
print(f"Exercise 2: {[elem.text for elem in exercise2]}")

# Exercise 3: Select the authors of books that are currently in stock
exercise3 = tree.xpath('//div[@class="book"]/p[@class="author"][../div/div/span[@class="status unavailable"]]')
print(f"Exercise 3: {[elem.text for elem in exercise3]}")

# Exercise 4: Select all tags from books in the fiction category
exercise4 = tree.xpath('//div[@id="fiction"]//ul[@class="tags"]/li')
print(f"Exercise 4: {[elem.text for elem in exercise4]}")

# Exercise 5: Find books that have both 'available' status and cost less than $25
exercise5 = tree.xpath('//div[@class="book"]/h3[..//span[@class="status available"] and ../div/span[@class="price"][number(substring(text(),2)) < 25]]')
print(f"Exercise 5: {[elem.text for elem in exercise5]}")