# This gets the text (raw html) of the first paragraph of the response.
myString = response.xpath('//p')[0].extract()

# Use HTML parsing library lxml
import lxml.html as lh

# Get the first sentence
firstSentence = myString.split('.')[0]

# Create element tree object
firstTree = lh.fromstring(firstSentence)

# Get the text content to write
firstText = firstTree.text_content()

# Get a list of relative links
myLinks = firstTree.xpath('a/@href')

# Get first link
firstLink = myLinks[0]

# Get new response (next page) URL
nextPage = response.urljoin(firstLink)

# Get new page!
scrapy.Request(nextPage) # There will be a 'callback' value here, as in the example.



### IMPORTANT ###
# Above, you will give a callback - the parse function!

# New page is now stored in response!



