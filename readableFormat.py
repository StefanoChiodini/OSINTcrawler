# in this class i filter and trasform the html page in a readable format

def obtainReadableFormat(htmlPage):
    # TODO: take for every post and comment the one with tag div and attributes like this:
    #          "attrs": {
    #        "itemprop": "articleBody"
    #     }

    '''
          {
         "name": "span",
         "text": "Cromical",
         "attrs": {
            "itemprop": "author", -> use this to find the author of the post
            "itemscope": "",
            "itemtype": "http://schema.org/Person"
         }
      },

            {
         "name": "time",
         "text": "May 8, 2016,  9:29pm",
         "attrs": {
            "itemprop": "datePublished", -> use this to find the date of the post
            "datetime": "2016-05-08T21:29:20Z"
         }
      },

      this maybe inlcude a lot of data:
            {
         "name": "article",
         "text": "SeaFirst 100May '16I\u2019d like to challenge some things.99% of the Managers
           that I have attended a lecture at say that skill > educationcOne very well to do 
           manager said he hires people from small colleges more than larger collegesAt the 
           recent conference I was at the actual demographics were 95%white, 75% male, ages 
           between 20-80.  (Estimates)The industry has been shaped by people without degrees 
           and this will only get more true.1Reply",
         "attrs": {
            "id": "post_2",
            "aria-label": "post #2 by @Sea",
            "role": "region",
            "data-post-id": "880",
            "data-topic-id": "245",
            "data-user-id": "24"
         }
      },
    '''
    # filter out every tag that is not an article
    data = []
    for tag in htmlPage.find_all("article"):

        if tag.name == "article":
            data1 = {
                    'name': tag.name,
                    'text': tag.get_text(strip=True),
                    'attrs': {}
                    }
            for attr, value in tag.attrs.items():

                if attr not in ['class', 'style', 'width', 'height', 'loading']: # here i remove the useless attributes
                    data1['attrs'][attr] = value

            data.append(data1)        

    return data