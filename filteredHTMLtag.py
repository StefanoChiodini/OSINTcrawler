# in this class we will filter the html tags from the text extracted from the html page
# I think that all this filtered tags are useless for a person that wants to read the page
#filter out style and class inside attrs, skip all the symbol, path, svg tags 

def removeUselessTags(tag):

    # The <script> tag is used to define a client-side script (JavaScript). The <script> element either contains scripting statements, or it points to an external script file through the src attribute. The <script> element is used in conjunction with the HTML DOM to interact with the user.
    if tag.name == 'script':
        return "to be removed"

    # if tag.name == 'link' and in the attributes there is "as": "script" it means that the link is a script or refers to a js file so i can remove it
    if tag.name == 'link':
        if 'as' in tag.attrs :
            if tag.attrs['as'] == 'script':
                return "to be removed"

    
    # if tag.name == 'link' and in the attributes there is "rel": "stylesheet" it means that the link is a stylesheet or refers to a css file so i can remove it
    if tag.name == 'link':
        if 'rel' in tag.attrs:
            if "stylesheet" in tag.attrs['rel']:
                return "to be removed"
            

    # The <style> tag is used to define style information for an HTML document. The <style> element should contain one or more CSS rules.
    if tag.name == 'style':
        return "to be removed"

    # The <symbol> tag is used to define a graphic symbol that can be reused on a page or across a website
    if tag.name == 'symbol':
        return "to be removed"

    #The <path> tag is used to draw shapes such as lines, rectangles, circles, and polygons. It can also be used to create complex curves and shapes.
    if tag.name == 'path':
        return "to be removed"
    
    #The <svg> tag is used to draw graphics on a web page. The <svg> tag is used to define a container
    if tag.name == 'svg':
        return "to be removed"
    
    #<rect> tag is used to draw a rectangle in an SVG image
    if tag.name == 'rect':
        return "to be removed"
    
    #The "use" tag in HTML is used to insert and reuse SVG graphics into an HTML document. It allows you to reference an SVG file or an SVG element from within the same document or from a different file,
    if tag.name == 'use':
        return "to be removed"
    
    #The <g> tag is used to group SVG shapes together. It is used to apply the same style properties to multiple shapes.
    if tag.name == 'g':
        return "to be removed"
    
    #The <defs> tag is used to define SVG graphics that can be used later in the document. The <defs> tag is used to group SVG shapes together. It is used to apply the same style properties to multiple shapes.
    if tag.name == 'defs':
        return "to be removed"
    
    #The <clipPath> tag is used to define a clipping path. A clipping path is used to restrict the region to which paint can be applied. A clipping path is used to restrict the region to which paint can be applied.
    if tag.name == 'clippath':
        return "to be removed"
    
    if tag.name == 'meta':
        return "to be removed"

    return "to be kept"
