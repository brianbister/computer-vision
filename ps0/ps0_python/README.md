# Report

`Which looks more like what you’d expect a monochrome image to look like? Would you expect a computer vision algorithm to work on one better than the other?`

It's difficult to say but the red channel looks more monochrome than the green. With the image I chose the red channel has more distinct edges, the green feels like there are several more shades of green in the picture which is why it feels like red may be better suited for computer vision algorithms. However, I feel these results may vary based on the contents of your image.

`What is the min and max of the pixel values of img1_green? What is the mean? What is the standard deviation?  And how did you compute these?`

I ran this numbers for house.tiff. It had a min of 0, max of 242, mean of ~168, and standard deviation of 48.72. The code can be found in `arithmetic_and_geometric_ops`.

`What do negative pixel values mean anyways?`

Negative pixel values are ignored and considered 0.
