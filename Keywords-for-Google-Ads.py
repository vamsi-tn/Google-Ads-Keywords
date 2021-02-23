1. The brief
Imagine working for a digital marketing agency, and the agency is approached by a massive online retailer of furniture. They want to test our skills at creating large campaigns for all of their website. We are tasked with creating a prototype set of keywords for search campaigns for their sofas section. The client says that they want us to generate keywords for the following products:

sofas
convertible sofas
love seats
recliners
sofa beds
The brief: The client is generally a low-cost retailer, offering many promotions and discounts. We will need to focus on such keywords. We will also need to move away from luxury keywords and topics, as we are targeting price-sensitive customers. Because we are going to be tight on budget, it would be good to focus on a tightly targeted set of keywords and make sure they are all set to exact and phrase match.

Based on the brief above we will first need to generate a list of words, that together with the products given above would make for good keywords. Here are some examples:

Products: sofas, recliners
Words: buy, prices
The resulting keywords: 'buy sofas', 'sofas buy', 'buy recliners', 'recliners buy', 'prices sofas', 'sofas prices', 'prices recliners', 'recliners prices'.

As a final result, we want to have a DataFrame that looks like this:

Campaign	Ad Group	Keyword	Criterion Type
Campaign1	AdGroup_1	keyword 1a	Exact
Campaign1	AdGroup_1	keyword 1a	Phrase
Campaign1	AdGroup_1	keyword 1b	Exact
Campaign1	AdGroup_1	keyword 1b	Phrase
Campaign1	AdGroup_2	keyword 2a	Exact
Campaign1	AdGroup_2	keyword 2a	Phrase
The first step is to come up with a list of words that users might use to express their desire in buying low-cost sofas.

P
# List of words to pair with products
words = ['Price', 'discount', 'Promotion', 'Sale', 'return', 'Best value',
        'Shop', 'Products', 'Inventory']
​
# Print list of words
print(words)
['Price', 'discount', 'Promotion', 'Sale', 'return', 'Best value', 'Shop', 'Products', 'Inventory']
2. Combine the words with the product names
Imagining all the possible combinations of keywords can be stressful! But not for us, because we are keyword ninjas! We know how to translate campaign briefs into Python data structures and can imagine the resulting DataFrames that we need to create.

Now that we have brainstormed the words that work well with the brief that we received, it is now time to combine them with the product names to generate meaningful search keywords. We want to combine every word with every product once before, and once after, as seen in the example above.

As a quick reminder, for the product 'recliners' and the words 'buy' and 'price' for example, we would want to generate the following combinations:

buy recliners
recliners buy
price recliners
recliners price
…

and so on for all the words and products that we have.

from pprint import pprint
pprint(keywords_list)
products = ['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds']
​
# Create an empty list
keywords_list = []
​
# Loop through products
for product in products:
    # Loop through words
    for word in words:
        # Append combinations
        keywords_list.append([product, product + ' ' + word])
        keywords_list.append([product, word + ' ' + product])
        
# Inspect keyword list
from pprint import pprint
pprint(keywords_list)
[['sofas', 'sofas Price'],
 ['sofas', 'Price sofas'],
 ['sofas', 'sofas discount'],
 ['sofas', 'discount sofas'],
 ['sofas', 'sofas Promotion'],
 ['sofas', 'Promotion sofas'],
 ['sofas', 'sofas Sale'],
 ['sofas', 'Sale sofas'],
 ['sofas', 'sofas return'],
 ['sofas', 'return sofas'],
 ['sofas', 'sofas Best value'],
 ['sofas', 'Best value sofas'],
 ['sofas', 'sofas Shop'],
 ['sofas', 'Shop sofas'],
 ['sofas', 'sofas Products'],
 ['sofas', 'Products sofas'],
 ['sofas', 'sofas Inventory'],
 ['sofas', 'Inventory sofas'],
 ['convertible sofas', 'convertible sofas Price'],
 ['convertible sofas', 'Price convertible sofas'],
 ['convertible sofas', 'convertible sofas discount'],
 ['convertible sofas', 'discount convertible sofas'],
 ['convertible sofas', 'convertible sofas Promotion'],
 ['convertible sofas', 'Promotion convertible sofas'],
 ['convertible sofas', 'convertible sofas Sale'],
 ['convertible sofas', 'Sale convertible sofas'],
 ['convertible sofas', 'convertible sofas return'],
 ['convertible sofas', 'return convertible sofas'],
 ['convertible sofas', 'convertible sofas Best value'],
 ['convertible sofas', 'Best value convertible sofas'],
 ['convertible sofas', 'convertible sofas Shop'],
 ['convertible sofas', 'Shop convertible sofas'],
 ['convertible sofas', 'convertible sofas Products'],
 ['convertible sofas', 'Products convertible sofas'],
 ['convertible sofas', 'convertible sofas Inventory'],
 ['convertible sofas', 'Inventory convertible sofas'],
 ['love seats', 'love seats Price'],
 ['love seats', 'Price love seats'],
 ['love seats', 'love seats discount'],
 ['love seats', 'discount love seats'],
 ['love seats', 'love seats Promotion'],
 ['love seats', 'Promotion love seats'],
 ['love seats', 'love seats Sale'],
 ['love seats', 'Sale love seats'],
 ['love seats', 'love seats return'],
 ['love seats', 'return love seats'],
 ['love seats', 'love seats Best value'],
 ['love seats', 'Best value love seats'],
 ['love seats', 'love seats Shop'],
 ['love seats', 'Shop love seats'],
 ['love seats', 'love seats Products'],
 ['love seats', 'Products love seats'],
 ['love seats', 'love seats Inventory'],
 ['love seats', 'Inventory love seats'],
 ['recliners', 'recliners Price'],
 ['recliners', 'Price recliners'],
 ['recliners', 'recliners discount'],
 ['recliners', 'discount recliners'],
 ['recliners', 'recliners Promotion'],
 ['recliners', 'Promotion recliners'],
 ['recliners', 'recliners Sale'],
 ['recliners', 'Sale recliners'],
 ['recliners', 'recliners return'],
 ['recliners', 'return recliners'],
 ['recliners', 'recliners Best value'],
 ['recliners', 'Best value recliners'],
 ['recliners', 'recliners Shop'],
 ['recliners', 'Shop recliners'],
 ['recliners', 'recliners Products'],
 ['recliners', 'Products recliners'],
 ['recliners', 'recliners Inventory'],
 ['recliners', 'Inventory recliners'],
 ['sofa beds', 'sofa beds Price'],
 ['sofa beds', 'Price sofa beds'],
 ['sofa beds', 'sofa beds discount'],
 ['sofa beds', 'discount sofa beds'],
 ['sofa beds', 'sofa beds Promotion'],
 ['sofa beds', 'Promotion sofa beds'],
 ['sofa beds', 'sofa beds Sale'],
 ['sofa beds', 'Sale sofa beds'],
 ['sofa beds', 'sofa beds return'],
 ['sofa beds', 'return sofa beds'],
 ['sofa beds', 'sofa beds Best value'],
 ['sofa beds', 'Best value sofa beds'],
 ['sofa beds', 'sofa beds Shop'],
 ['sofa beds', 'Shop sofa beds'],
 ['sofa beds', 'sofa beds Products'],
 ['sofa beds', 'Products sofa beds'],
 ['sofa beds', 'sofa beds Inventory'],
 ['sofa beds', 'Inventory sofa beds']]
3. Convert the list of lists into a DataFrame
Now we want to convert this list of lists into a DataFrame so we can easily manipulate it and manage the final output.

)
# Load library
import pandas as pd
​
# Create a DataFrame from list
keywords_df = pd.DataFrame.from_records(keywords_list)
​
# Print the keywords DataFrame to explore it
print(keywords_df.head())
       0                1
0  sofas      sofas Price
1  sofas      Price sofas
2  sofas   sofas discount
3  sofas   discount sofas
4  sofas  sofas Promotion
4. Rename the columns of the DataFrame
Before we can upload this table of keywords, we will need to give the columns meaningful names. If we inspect the DataFrame we just created above, we can see that the columns are currently named 0 and 1. Ad Group (example: "sofas") and Keyword (example: "sofas buy") are much more appropriate names.

keywords_df = ...
# Rename the columns of the DataFrame
keywords_df = keywords_df.rename(columns={0: "Ad Group", 1: "Keyword"})
5. Add a campaign column
Now we need to add some additional information to our DataFrame. We need a new column called Campaign for the campaign name. We want campaign names to be descriptive of our group of keywords and products, so let's call this campaign 'SEM_Sofas'.

# ... YOUR CODE FOR TASK 5 ...
# Add a campaign column
keywords_df['Campaign'] = 'SEM_Sofas'
6. Create the match type column
There are different keyword match types. One is exact match, which is for matching the exact term or are close variations of that exact term. Another match type is broad match, which means ads may show on searches that include misspellings, synonyms, related searches, and other relevant variations.

Straight from Google's AdWords documentation:

In general, the broader the match type, the more traffic potential that keyword will have, since your ads may be triggered more often. Conversely, a narrower match type means that your ads may show less often—but when they do, they’re likely to be more related to someone’s search.

Since the client is tight on budget, we want to make sure all the keywords are in exact match at the beginning.

# ... YOUR CODE FOR TASK 6 ...
# Add a criterion type column
keywords_df['Criterion Type'] = 'Exact'
7. Duplicate all the keywords into 'phrase' match
The great thing about exact match is that it is very specific, and we can control the process very well. The tradeoff, however, is that:

The search volume for exact match is lower than other match types
We can't possibly think of all the ways in which people search, and so, we are probably missing out on some high-quality keywords.
So it's good to use another match called phrase match as a discovery mechanism to allow our ads to be triggered by keywords that include our exact match keywords, together with anything before (or after) them.

Later on, when we launch the campaign, we can explore with modified broad match, broad match, and negative match types, for better visibility and control of our campaigns.

# Make a copy of the keywords DataFrame
keywords_phrase = keywords_df.copy()
​
# Change criterion type match to phrase
keywords_phrase['Criterion Type'] = 'Phrase'
​
# Append the DataFrames
keywords_df_final = keywords_df.append(keywords_phrase)
8. Save and summarize!
To upload our campaign, we need to save it as a CSV file. Then we will be able to import it to AdWords editor or BingAds editor. There is also the option of pasting the data into the editor if we want, but having easy access to the saved data is great so let's save to a CSV file!

Looking at a summary of our campaign structure is good now that we've wrapped up our keyword work. We can do that by grouping by ad group and criterion type and counting by keyword. This summary shows us that we assigned specific keywords to specific ad groups, which are each part of a campaign. In essence, we are telling Google (or Bing, etc.) that we want any of the words in each ad group to trigger one of the ads in the same ad group. Separately, we will have to create another table for ads, which is a task for another day and would look something like this:

Campaign	Ad Group	Headline 1	Headline 2	Description	Final URL
SEM_Sofas	Sofas	Looking for Quality Sofas?	Explore Our Massive Collection	30-day Returns With Free Delivery Within the US. Start Shopping Now	DataCampSofas.com/sofas
SEM_Sofas	Sofas	Looking for Affordable Sofas?	Check Out Our Weekly Offers	30-day Returns With Free Delivery Within the US. Start Shopping Now	DataCampSofas.com/sofas
SEM_Sofas	Recliners	Looking for Quality Recliners?	Explore Our Massive Collection	30-day Returns With Free Delivery Within the US. Start Shopping Now	DataCampSofas.com/recliners
SEM_Sofas	Recliners	Need Affordable Recliners?	Check Out Our Weekly Offers	30-day Returns With Free Delivery Within the US. Start Shopping Now	DataCampSofas.com/recliners
Together, these tables get us the sample keywords -> ads -> landing pages mapping shown in the diagram below.

Keywords-Ads-Landing pages flow

# Save the final keywords to a CSV file
# ... YOUR CODE FOR TASK 8 ...
keywords_df_final.to_csv('keywords.csv',index=False)
# View a summary of our campaign work
summary = keywords_df_final.groupby(['Ad Group', 'Criterion Type'])['Keyword'].count()
print(summary)
Ad Group           Criterion Type
convertible sofas  Exact             18
                   Phrase            18
love seats         Exact             18
                   Phrase            18
recliners          Exact             18
                   Phrase            18
sofa beds          Exact             18
                   Phrase            18
sofas              Exact             18
                   Phrase            18
Name: Keyword, dtype: int64
