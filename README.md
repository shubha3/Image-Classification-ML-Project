# Machine Learning Project on Image Classification


## Data Description
The **[MNIST dataset](https://en.wikipedia.org/wiki/MNIST_database)** (Modified National Institute of Standards and Technology) is a large database of handwritten digits that has been chosen as our intended dataset for testing different Image Classification Techniques.

The data is present is present as MATLAB files which needs to be uploaded to the Jupiter notebook in due process.

The data is in two sets: Unrotated and Rotated.

The unrotated dataset as the name suggests consists of observation where the digits are not upright from the perspective of the viewer.
![unrotated image](https://github.com/shubha3/Senior-Mentorship-Summer-Project-2021/blob/main/data/image/unrotated%20image.jpeg)

The rotated dataset on the other hand consists of observations where the digits have been rotated clockwise or anti-clockwise.
![rotated image](https://github.com/shubha3/Senior-Mentorship-Summer-Project-2021/blob/main/data/image/Rotated%20image.png)
## Methodology
We have tried to check the efficacies of a variety of learning algorithms to judge their usability on this particular dataset.

In particular we have used the following learning algorithms:
1.  Discriminant Analysis
    * Linear Discriminant Analysis
    * Quadratic Discriminant Analysis
2.  Decision Trees
    * Application of Cost Complexity Pruning
    * Random Forest
3. Support Vector Machine
4. Neural Network
5. Convolutional Neural Network


In this project, we have first applied the above said learning algorithms to predict the labels of the observations both on unrotated and merged (unrotated+rotated) data.

## Brief Summary
### [Discriminant Analysis on unrotated data](https://github.com/shubha3/Senior-Mentorship-Summer-Project-2021/tree/main/Application-on-Unrotated-data/LDA-QDA)
We first trained the unrotated data using
