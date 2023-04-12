# in this class i filter and trasform the html page in a readable format
# TODO: use this link for testing "https://0x00sec.org/t/malware-development-1-password-stealers-chrome/33571"
def obtainReadableFormat(htmlPage):

   # filter out every tag that is not an article
   data = []
   dataTimes = [] # i use this list to store the timestamps
   i = 0
   timeHtmlElements = htmlPage.findAll("time")
   for timeHtmlElement in timeHtmlElements:
      dataTimes.append(timeHtmlElement.get_text(strip=True))

   for tag in htmlPage.descendants:

      if tag.name == "head":
         data1 = {
                  'name': tag.name,
                  'text': tag.get_text(strip=True),
                  }
         data.append(data1)        
 
      elif tag.name == "article":
            try:
               data1 = {
                     'name': tag.name,
                     'text': tag.get_text(strip=True),
                     'attrs': {},
                     'timestamp': dataTimes[i]
                     }
               i = i + 1
               for attr, value in tag.attrs.items():

                  if attr not in ['class', 'style', 'width', 'height', 'loading', 'role']: # here i remove the useless attributes
                     data1['attrs'][attr] = value

               data.append(data1)
            # now i catch index out of range exception
            except IndexError:
               data1 = {
                     'name': tag.name,
                     'text': tag.get_text(strip=True),
                     'attrs': {},
                     'timestamp': "timestamp not found"
                     }
               for attr, value in tag.attrs.items():

                  if attr not in ['class', 'style', 'width', 'height', 'loading', 'role']:
                     data1['attrs'][attr] = value

   i = 0
   return data