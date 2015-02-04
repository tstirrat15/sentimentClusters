---
layout: page
title: Abstract
permalink: /abstract/
description: A brief overview of our project.
headings:
- top
- hipster1
- hipster2
- hipster3
- hipster4
- hipster5
---

##The hipster is real. {#top}


### Hipster1 {#hipster1}

#### CODED HIPSTER

{% highlight python %}
class JSONObject(dict):
    # Borrowed from Birdy: https://github.com/inueni/birdy
    # Changed "name in self.iterkeys()" to "name in self.keys()"
    # which fixed things for python3.
    def __getattr__(self, name):
        if name in self.keys():
            return self[name]
        raise AttributeError('%s has no property named %s.'
                             % (self.__class__.__name__, name))

    def __setattr__(self, *args):
        raise AttributeError('%s instances are read-only.'
                             % self.__class__.__name__)
    __delattr__ = __setitem__ = __delitem__ = __setattr__

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, dict.__repr__(self))
{% endhighlight %}

{% highlight R %}
library(XML)
source("xmlFaster.R")
shipments <- xmlParse("Shipments.xml")

# convert data to table format
# xmlToDataFrame is slow with large datasets
system.time(data <- xmlToDataFrame(shipments))
# custom function is not much better with my datasets
# system.time(data2 <- xmlToDF(shipments,xpath = "/TABLE/BOXTURE_SHIPMENTS" ))
# Further used only data, not data2

# head(data)

data$Price <- format(data$Price, digits = 2)
data$Price <- as.numeric(data$Price)
data$Price <- format(data$Price, digits = 2)

data$MarginEUR <- format(data$MarginEUR, digits = 2, nsmall = 2)
data$MarginEUR <- as.numeric(data$MarginEUR)
data$MarginEUR <- format(data$MarginEUR, digits = 2, nsmall = 2)

# need to convert time into more readeble format

data$OriginScheduled <- strptime(data$OriginScheduled, "%Y-%m-%dT%H:%M:%S")
data$OriginActual <- strptime(data$OriginActual, "%Y-%m-%dT%H:%M:%S")
data$DestinationScheduled <- strptime(data$DestinationScheduled, "%Y-%m-%dT%H:%M:%S")
data$DestinationActual <- strptime(data$DestinationActual, "%Y-%m-%dT%H:%M:%S")
data$PurchasedAt <- strptime(data$PurchasedAt, "%Y-%m-%dT%H:%M:%S")

View(data)
{% endhighlight %}

3 wolf moon fap farm-to-table fingerstache bicycle rights forage, jean shorts dreamcatcher lomo mustache. McSweeney's paleo quinoa sriracha, shabby chic farm-to-table fixie. Williamsburg fap before they sold out trust fund. Before they sold out plaid meditation, cold-pressed lumbersexual YOLO skateboard craft beer brunch scenester pour-over tattooed biodiesel. Lumbersexual chillwave actually, four dollar toast cliche mixtape locavore normcore tofu meditation sustainable pork belly keytar. Hella distillery meggings single-origin coffee squid. Cliche 3 wolf moon biodiesel mumblecore heirloom ennui.

3 wolf moon fap farm-to-table fingerstache bicycle rights forage, jean shorts dreamcatcher lomo mustache. McSweeney's paleo quinoa sriracha, shabby chic farm-to-table fixie. Williamsburg fap before they sold out trust fund. Before they sold out plaid meditation, cold-pressed lumbersexual YOLO skateboard craft beer brunch scenester pour-over tattooed biodiesel. Lumbersexual chillwave actually, four dollar toast cliche mixtape locavore normcore tofu meditation sustainable pork belly keytar. Hella distillery meggings single-origin coffee squid. Cliche 3 wolf moon biodiesel mumblecore heirloom ennui.

3 wolf moon fap farm-to-table fingerstache bicycle rights forage, jean shorts dreamcatcher lomo mustache. McSweeney's paleo quinoa sriracha, shabby chic farm-to-table fixie. Williamsburg fap before they sold out trust fund. Before they sold out plaid meditation, cold-pressed lumbersexual YOLO skateboard craft beer brunch scenester pour-over tattooed biodiesel. Lumbersexual chillwave actually, four dollar toast cliche mixtape locavore normcore tofu meditation sustainable pork belly keytar. Hella distillery meggings single-origin coffee squid. Cliche 3 wolf moon biodiesel mumblecore heirloom ennui.

3 wolf moon fap farm-to-table fingerstache bicycle rights forage, jean shorts dreamcatcher lomo mustache. McSweeney's paleo quinoa sriracha, shabby chic farm-to-table fixie. Williamsburg fap before they sold out trust fund. Before they sold out plaid meditation, cold-pressed lumbersexual YOLO skateboard craft beer brunch scenester pour-over tattooed biodiesel. Lumbersexual chillwave actually, four dollar toast cliche mixtape locavore normcore tofu meditation sustainable pork belly keytar. Hella distillery meggings single-origin coffee squid. Cliche 3 wolf moon biodiesel mumblecore heirloom ennui.

3 wolf moon fap farm-to-table fingerstache bicycle rights forage, jean shorts dreamcatcher lomo mustache. McSweeney's paleo quinoa sriracha, shabby chic farm-to-table fixie. Williamsburg fap before they sold out trust fund. Before they sold out plaid meditation, cold-pressed lumbersexual YOLO skateboard craft beer brunch scenester pour-over tattooed biodiesel. Lumbersexual chillwave actually, four dollar toast cliche mixtape locavore normcore tofu meditation sustainable pork belly keytar. Hella distillery meggings single-origin coffee squid. Cliche 3 wolf moon biodiesel mumblecore heirloom ennui.



### Hipster2 {#hipster2}
Pinterest chambray scenester, Neutra Truffaut disrupt Etsy twee listicle four loko pork belly synth normcore 3 wolf moon plaid. Banh mi selfies chambray locavore, Brooklyn fashion axe migas pop-up quinoa sartorial. Cold-pressed pour-over salvia try-hard, pickled Portland McSweeney's Intelligentsia. Bushwick taxidermy occupy, aesthetic wolf YOLO meditation bicycle rights selvage American Apparel Pinterest Etsy. PBR High Life twee, fap sustainable 90's fixie selfies master cleanse pour-over 3 wolf moon. Slow-carb yr swag, try-hard stumptown polaroid lo-fi PBR&B. Beard Tumblr cliche post-ironic.

Pinterest chambray scenester, Neutra Truffaut disrupt Etsy twee listicle four loko pork belly synth normcore 3 wolf moon plaid. Banh mi selfies chambray locavore, Brooklyn fashion axe migas pop-up quinoa sartorial. Cold-pressed pour-over salvia try-hard, pickled Portland McSweeney's Intelligentsia. Bushwick taxidermy occupy, aesthetic wolf YOLO meditation bicycle rights selvage American Apparel Pinterest Etsy. PBR High Life twee, fap sustainable 90's fixie selfies master cleanse pour-over 3 wolf moon. Slow-carb yr swag, try-hard stumptown polaroid lo-fi PBR&B. Beard Tumblr cliche post-ironic.

Pinterest chambray scenester, Neutra Truffaut disrupt Etsy twee listicle four loko pork belly synth normcore 3 wolf moon plaid. Banh mi selfies chambray locavore, Brooklyn fashion axe migas pop-up quinoa sartorial. Cold-pressed pour-over salvia try-hard, pickled Portland McSweeney's Intelligentsia. Bushwick taxidermy occupy, aesthetic wolf YOLO meditation bicycle rights selvage American Apparel Pinterest Etsy. PBR High Life twee, fap sustainable 90's fixie selfies master cleanse pour-over 3 wolf moon. Slow-carb yr swag, try-hard stumptown polaroid lo-fi PBR&B. Beard Tumblr cliche post-ironic.

Pinterest chambray scenester, Neutra Truffaut disrupt Etsy twee listicle four loko pork belly synth normcore 3 wolf moon plaid. Banh mi selfies chambray locavore, Brooklyn fashion axe migas pop-up quinoa sartorial. Cold-pressed pour-over salvia try-hard, pickled Portland McSweeney's Intelligentsia. Bushwick taxidermy occupy, aesthetic wolf YOLO meditation bicycle rights selvage American Apparel Pinterest Etsy. PBR High Life twee, fap sustainable 90's fixie selfies master cleanse pour-over 3 wolf moon. Slow-carb yr swag, try-hard stumptown polaroid lo-fi PBR&B. Beard Tumblr cliche post-ironic.

Pinterest chambray scenester, Neutra Truffaut disrupt Etsy twee listicle four loko pork belly synth normcore 3 wolf moon plaid. Banh mi selfies chambray locavore, Brooklyn fashion axe migas pop-up quinoa sartorial. Cold-pressed pour-over salvia try-hard, pickled Portland McSweeney's Intelligentsia. Bushwick taxidermy occupy, aesthetic wolf YOLO meditation bicycle rights selvage American Apparel Pinterest Etsy. PBR High Life twee, fap sustainable 90's fixie selfies master cleanse pour-over 3 wolf moon. Slow-carb yr swag, try-hard stumptown polaroid lo-fi PBR&B. Beard Tumblr cliche post-ironic.



### Hipster3 {#hipster3}
3 wolf moon fap farm-to-table fingerstache bicycle rights forage, jean shorts dreamcatcher lomo mustache. McSweeney's paleo quinoa sriracha, shabby chic farm-to-table fixie. Williamsburg fap before they sold out trust fund. Before they sold out plaid meditation, cold-pressed lumbersexual YOLO skateboard craft beer brunch scenester pour-over tattooed biodiesel. Lumbersexual chillwave actually, four dollar toast cliche mixtape locavore normcore tofu meditation sustainable pork belly keytar. Hella distillery meggings single-origin coffee squid. Cliche 3 wolf moon biodiesel mumblecore heirloom ennui.

3 wolf moon fap farm-to-table fingerstache bicycle rights forage, jean shorts dreamcatcher lomo mustache. McSweeney's paleo quinoa sriracha, shabby chic farm-to-table fixie. Williamsburg fap before they sold out trust fund. Before they sold out plaid meditation, cold-pressed lumbersexual YOLO skateboard craft beer brunch scenester pour-over tattooed biodiesel. Lumbersexual chillwave actually, four dollar toast cliche mixtape locavore normcore tofu meditation sustainable pork belly keytar. Hella distillery meggings single-origin coffee squid. Cliche 3 wolf moon biodiesel mumblecore heirloom ennui.

3 wolf moon fap farm-to-table fingerstache bicycle rights forage, jean shorts dreamcatcher lomo mustache. McSweeney's paleo quinoa sriracha, shabby chic farm-to-table fixie. Williamsburg fap before they sold out trust fund. Before they sold out plaid meditation, cold-pressed lumbersexual YOLO skateboard craft beer brunch scenester pour-over tattooed biodiesel. Lumbersexual chillwave actually, four dollar toast cliche mixtape locavore normcore tofu meditation sustainable pork belly keytar. Hella distillery meggings single-origin coffee squid. Cliche 3 wolf moon biodiesel mumblecore heirloom ennui.

3 wolf moon fap farm-to-table fingerstache bicycle rights forage, jean shorts dreamcatcher lomo mustache. McSweeney's paleo quinoa sriracha, shabby chic farm-to-table fixie. Williamsburg fap before they sold out trust fund. Before they sold out plaid meditation, cold-pressed lumbersexual YOLO skateboard craft beer brunch scenester pour-over tattooed biodiesel. Lumbersexual chillwave actually, four dollar toast cliche mixtape locavore normcore tofu meditation sustainable pork belly keytar. Hella distillery meggings single-origin coffee squid. Cliche 3 wolf moon biodiesel mumblecore heirloom ennui.

3 wolf moon fap farm-to-table fingerstache bicycle rights forage, jean shorts dreamcatcher lomo mustache. McSweeney's paleo quinoa sriracha, shabby chic farm-to-table fixie. Williamsburg fap before they sold out trust fund. Before they sold out plaid meditation, cold-pressed lumbersexual YOLO skateboard craft beer brunch scenester pour-over tattooed biodiesel. Lumbersexual chillwave actually, four dollar toast cliche mixtape locavore normcore tofu meditation sustainable pork belly keytar. Hella distillery meggings single-origin coffee squid. Cliche 3 wolf moon biodiesel mumblecore heirloom ennui.


### Hipster4 {#hipster4}
Vice fashion axe +1 mlkshk, gluten-free messenger bag art party roof party High Life tilde. Flannel pork belly before they sold out, put a bird on it locavore selfies skateboard 8-bit lomo ethical. Taxidermy next level post-ironic, Helvetica Wes Anderson wolf narwhal before they sold out stumptown cornhole biodiesel wayfarers DIY Kickstarter you probably haven't heard of them. Kale chips artisan swag, Tumblr distillery chambray ethical +1 disrupt. Lumbersexual try-hard four dollar toast, deep v XOXO mustache gastropub narwhal skateboard pug pour-over hoodie keytar semiotics you probably haven't heard of them. Crucifix tilde kale chips listicle, heirloom meggings fanny pack four loko fap gastropub High Life actually Williamsburg typewriter. Authentic Neutra kogi, Vice lumbersexual salvia flexitarian photo booth kitsch seitan.

Vice fashion axe +1 mlkshk, gluten-free messenger bag art party roof party High Life tilde. Flannel pork belly before they sold out, put a bird on it locavore selfies skateboard 8-bit lomo ethical. Taxidermy next level post-ironic, Helvetica Wes Anderson wolf narwhal before they sold out stumptown cornhole biodiesel wayfarers DIY Kickstarter you probably haven't heard of them. Kale chips artisan swag, Tumblr distillery chambray ethical +1 disrupt. Lumbersexual try-hard four dollar toast, deep v XOXO mustache gastropub narwhal skateboard pug pour-over hoodie keytar semiotics you probably haven't heard of them. Crucifix tilde kale chips listicle, heirloom meggings fanny pack four loko fap gastropub High Life actually Williamsburg typewriter. Authentic Neutra kogi, Vice lumbersexual salvia flexitarian photo booth kitsch seitan.

Vice fashion axe +1 mlkshk, gluten-free messenger bag art party roof party High Life tilde. Flannel pork belly before they sold out, put a bird on it locavore selfies skateboard 8-bit lomo ethical. Taxidermy next level post-ironic, Helvetica Wes Anderson wolf narwhal before they sold out stumptown cornhole biodiesel wayfarers DIY Kickstarter you probably haven't heard of them. Kale chips artisan swag, Tumblr distillery chambray ethical +1 disrupt. Lumbersexual try-hard four dollar toast, deep v XOXO mustache gastropub narwhal skateboard pug pour-over hoodie keytar semiotics you probably haven't heard of them. Crucifix tilde kale chips listicle, heirloom meggings fanny pack four loko fap gastropub High Life actually Williamsburg typewriter. Authentic Neutra kogi, Vice lumbersexual salvia flexitarian photo booth kitsch seitan.

Vice fashion axe +1 mlkshk, gluten-free messenger bag art party roof party High Life tilde. Flannel pork belly before they sold out, put a bird on it locavore selfies skateboard 8-bit lomo ethical. Taxidermy next level post-ironic, Helvetica Wes Anderson wolf narwhal before they sold out stumptown cornhole biodiesel wayfarers DIY Kickstarter you probably haven't heard of them. Kale chips artisan swag, Tumblr distillery chambray ethical +1 disrupt. Lumbersexual try-hard four dollar toast, deep v XOXO mustache gastropub narwhal skateboard pug pour-over hoodie keytar semiotics you probably haven't heard of them. Crucifix tilde kale chips listicle, heirloom meggings fanny pack four loko fap gastropub High Life actually Williamsburg typewriter. Authentic Neutra kogi, Vice lumbersexual salvia flexitarian photo booth kitsch seitan.

Vice fashion axe +1 mlkshk, gluten-free messenger bag art party roof party High Life tilde. Flannel pork belly before they sold out, put a bird on it locavore selfies skateboard 8-bit lomo ethical. Taxidermy next level post-ironic, Helvetica Wes Anderson wolf narwhal before they sold out stumptown cornhole biodiesel wayfarers DIY Kickstarter you probably haven't heard of them. Kale chips artisan swag, Tumblr distillery chambray ethical +1 disrupt. Lumbersexual try-hard four dollar toast, deep v XOXO mustache gastropub narwhal skateboard pug pour-over hoodie keytar semiotics you probably haven't heard of them. Crucifix tilde kale chips listicle, heirloom meggings fanny pack four loko fap gastropub High Life actually Williamsburg typewriter. Authentic Neutra kogi, Vice lumbersexual salvia flexitarian photo booth kitsch seitan.



### Hipster5 {#hipster5}
Cold-pressed hashtag ethical, American Apparel before they sold out photo booth cornhole master cleanse tattooed Helvetica XOXO. Wes Anderson McSweeney's keytar beard, American Apparel Portland cronut Vice occupy High Life messenger bag locavore selvage. Seitan yr forage food truck, crucifix mustache blog lumbersexual Marfa tote bag artisan Helvetica master cleanse. Post-ironic art party flannel sriracha, squid leggings aesthetic lumbersexual fanny pack cray dreamcatcher migas small batch. Austin paleo cardigan occupy synth, bicycle rights Godard direct trade vegan quinoa. Pop-up XOXO next level Etsy normcore, cornhole Shoreditch organic 8-bit. Shabby chic readymade stumptown chillwave fanny pack 90's.

Cold-pressed hashtag ethical, American Apparel before they sold out photo booth cornhole master cleanse tattooed Helvetica XOXO. Wes Anderson McSweeney's keytar beard, American Apparel Portland cronut Vice occupy High Life messenger bag locavore selvage. Seitan yr forage food truck, crucifix mustache blog lumbersexual Marfa tote bag artisan Helvetica master cleanse. Post-ironic art party flannel sriracha, squid leggings aesthetic lumbersexual fanny pack cray dreamcatcher migas small batch. Austin paleo cardigan occupy synth, bicycle rights Godard direct trade vegan quinoa. Pop-up XOXO next level Etsy normcore, cornhole Shoreditch organic 8-bit. Shabby chic readymade stumptown chillwave fanny pack 90's.

Cold-pressed hashtag ethical, American Apparel before they sold out photo booth cornhole master cleanse tattooed Helvetica XOXO. Wes Anderson McSweeney's keytar beard, American Apparel Portland cronut Vice occupy High Life messenger bag locavore selvage. Seitan yr forage food truck, crucifix mustache blog lumbersexual Marfa tote bag artisan Helvetica master cleanse. Post-ironic art party flannel sriracha, squid leggings aesthetic lumbersexual fanny pack cray dreamcatcher migas small batch. Austin paleo cardigan occupy synth, bicycle rights Godard direct trade vegan quinoa. Pop-up XOXO next level Etsy normcore, cornhole Shoreditch organic 8-bit. Shabby chic readymade stumptown chillwave fanny pack 90's.

Cold-pressed hashtag ethical, American Apparel before they sold out photo booth cornhole master cleanse tattooed Helvetica XOXO. Wes Anderson McSweeney's keytar beard, American Apparel Portland cronut Vice occupy High Life messenger bag locavore selvage. Seitan yr forage food truck, crucifix mustache blog lumbersexual Marfa tote bag artisan Helvetica master cleanse. Post-ironic art party flannel sriracha, squid leggings aesthetic lumbersexual fanny pack cray dreamcatcher migas small batch. Austin paleo cardigan occupy synth, bicycle rights Godard direct trade vegan quinoa. Pop-up XOXO next level Etsy normcore, cornhole Shoreditch organic 8-bit. Shabby chic readymade stumptown chillwave fanny pack 90's.

Cold-pressed hashtag ethical, American Apparel before they sold out photo booth cornhole master cleanse tattooed Helvetica XOXO. Wes Anderson McSweeney's keytar beard, American Apparel Portland cronut Vice occupy High Life messenger bag locavore selvage. Seitan yr forage food truck, crucifix mustache blog lumbersexual Marfa tote bag artisan Helvetica master cleanse. Post-ironic art party flannel sriracha, squid leggings aesthetic lumbersexual fanny pack cray dreamcatcher migas small batch. Austin paleo cardigan occupy synth, bicycle rights Godard direct trade vegan quinoa. Pop-up XOXO next level Etsy normcore, cornhole Shoreditch organic 8-bit. Shabby chic readymade stumptown chillwave fanny pack 90's.
