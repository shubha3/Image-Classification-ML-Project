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
---
### Discriminant Analysis
#### [Discriminant Analysis on unrotated data](https://github.com/shubha3/Senior-Mentorship-Summer-Project-2021/tree/main/Application-on-Unrotated-data/LDA-QDA)
* Trained the Linear and Quadratic Discriminant models on the unrotated training dataset.
* Tried to predict the labels of the observations in the **unrotated test dataset**.
* Tried to predict the labels of the observations in the **rotated test dataset**.
* Applied Principal Component Analysis (PCA) as a means of dimension reduction and then tried to repeat the above steps using the principal components as observations.

#### [Discriminant Analysis on merged data](https://github.com/shubha3/Senior-Mentorship-Summer-Project-2021/blob/main/Application-on-Merged-data/LDA-QDA/Merged_MNIST_LDA_QDA.ipynb)
* Merged the training sets of rotated and unrotated datasets.
* Trained LDA and QDA models on this merged dataset.
* Tried to predict the labels of the merged test dataset.
* Used PCA on this merged dataset to reduce the dimension of the feature space and tried to repeat the above steps using the principal components as observations.

---
### Decision Tree
#### [Decision Tree on unrotated data](https://github.com/shubha3/Senior-Mentorship-Summer-Project-2021/tree/main/Application-on-Unrotated-data/Decision%20Tree)
*
*
*

#### [Decision Tree on merged data](https://github.com/shubha3/Senior-Mentorship-Summer-Project-2021/tree/main/Application-on-Merged-data/Decision%20Tree)
*
*
*

---
### Support Vector Machine
#### [SVM on unrotated dataset](https://github.com/shubha3/Senior-Mentorship-Summer-Project-2021/tree/main/Application-on-Unrotated-data/SVM)
* Trained SVM model on the unrotated training dataset.
* Tried to predict the labels of the observations in the **unrotated test dataset**.
* Tried to predict the labels of the observations in the **rotated test dataset**.
* Applied Principal Component Analysis (PCA) as a means of dimension reduction and then tried to repeat the above steps using the principal components as observations.

#### [SVM on rotated dataset](https://github.com/shubha3/Senior-Mentorship-Summer-Project-2021/tree/main/Application-on-Merged-data/SVM)
* Merged the training sets of rotated and unrotated datasets.
* Trained SVM model on this merged dataset.
* Tried to predict the labels of the merged test dataset.
* Used PCA on this merged dataset to reduce the dimension of the feature space and tried to repeat the above steps using the principal components as observations.

---
### [Neural Network](https://github.com/shubha3/Senior-Mentorship-Summer-Project-2021/tree/main/Neural%20Network)
*
*
*

---
### Convolutional Neural Network
#### [CNN on unrotated data](https://github.com/shubha3/Senior-Mentorship-Summer-Project-2021/tree/main/Application-on-Unrotated-data/Convolutional%20Neural%20Network)
*
*
*

#### [CNN on merged data](https://github.com/shubha3/Senior-Mentorship-Summer-Project-2021/tree/main/Application-on-Merged-data/Convolutional%20Neural%20Network)
*
*
*

## Results
The following table shows the test accuracies of the different learning algorithms when the models have been trained on data obtained from the unrotated dataset.
<table>
<thead>
  <tr>
    <th colspan="2" rowspan="3">Learning Algorithms</th>
    <th colspan="4">Test accuracy</th>
  </tr>
  <tr>
    <td colspan="2">Model trained on<br>given data set</td>
    <td colspan="1">Model trained using<br>principal components</td>
  </tr>
  <tr>
    <td>Unrotated<br>test data</td>
    <td>Rotated<br>test data</td>
    <td>Unrotated<br>test data</td>
    <!--<td></td>-->
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2">Discriminant<br>Analysis</td>
    <td>LDA</td>
    <td>87.22%</td>
    <td>9.39%</td>
    <td>  87.22%</td>
    <!--<td></td>-->
  </tr>
  <tr>
    <td>QDA</td>
    <td>54.28%</td>
    <td>9.97%</td>
    <td>  13.63%</td>
    <!--<td></td>-->
  </tr>
  <tr>
    <td rowspan="3">Decision Tree</td>
    <td>Complete<br>decision tree</td>
    <td></td>
    <td></td>
    <td></td>
    <!--<td></td>-->
  </tr>
  <tr>
    <td>Cost complexity<br>pruing</td>
    <td></td>
    <td></td>
    <td>-</td>
    <!--<td></td>-->
  </tr>
  <tr>
    <td>Random forest</td>
    <td></td>
    <td></td>
    <td>-</td>
    <!--<td></td>-->
  </tr>
  <tr>
    <td colspan="2">Support Vector Machine</td>
    <td>97.88%</td>
    <td>9.96%</td>
    <td>96.85%</td>
    <!--<td></td>-->
  </tr>
  <tr>
    <td colspan="2">Neural Network</td>
    <td></td>
    <td></td>
    <td></td>
    <!--<td></td>-->
  </tr>
  <tr>
    <td colspan="2">Convoluted Neural Network</td>
    <td></td>
    <td></td>
    <td></td>
    <!--<td></td>-->
  </tr>
</tbody>
</table>

The following table shows the test accuracies of the different learning algorithms when the models have been trained on ***merged*** obtained from the unrotated and rotated datasets.
<table>
<thead>
  <tr>
    <th colspan="2" rowspan="2">Learning Algorithms</th>
    <th colspan="2">Test accuracy</th>
  </tr>
  <tr>
    <td>Model trained on<br>given data set</td>
    <td>Model trained using<br>principal components</td>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2">Discriminant<br>Analysis</td>
    <td>LDA</td>
    <td>58.41%</td>
    <td>56.76%</td>
  </tr>
  <tr>
    <td>QDA</td>
    <td>17.125%</td>
    <td>14.98%</td>
  </tr>
  <tr>
    <td rowspan="3">Decision Tree</td>
    <td>Complete<br>decision tree</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Cost complexity<br>pruing</td>
    <td></td>
    <td>-</td>
  </tr>
  <tr>
    <td>Random forest</td>
    <td></td>
    <td>-</td>
  </tr>
  <tr>
    <td colspan="2">Support Vector Machine</td>
    <td>90.25%</td>
    <td>88.51%</td>
  </tr>
  <tr>
    <td colspan="2">Neural Network</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td colspan="2">Convoluted Neural Network</td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>
