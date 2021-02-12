#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scrapy


# In[2]:


class QuotesSpider(scrapy.Spider):
    name='quotesSpider'
    
    def start_requests(self):
        urls=[
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/'
        ]
        # generator 
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self,response):
        page_id = response.url.split("/")[-2]
        filename = f"quotes{page_id}.html"
        with open(filename,"wb") as f:
            f.write(response.body)


# In[ ]:




