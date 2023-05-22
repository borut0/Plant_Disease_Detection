# Plant_Disease_Detection

Plant disease detection is the process of identifying and diagnosing diseases that
affect crops and plants. Early detection of plant diseases is crucial for effective
management and control, as it allows for timely intervention to prevent the spread
of the disease and minimize crop losses.

## Features 
  - Remote Monitoring
  - Early Detection and Diagnosis
  - Disease Managemengt and Decision Support 

## Tech Stack

**Client :** HTML, CSS

**Server :** Django

## Technologies
Python, CNN, Djnago, HTML and CSS

## Screenshots
- Home Page <br><br>
  ![home_page](https://github.com/borut0/Plant_Disease_Detection/assets/89539128/700d801b-364d-478b-9b81-88134405f280) 
- Particular Plant Page <br><br>
  ![leaf_image](https://github.com/borut0/Plant_Disease_Detection/assets/89539128/0d7215a8-e555-4a37-96ba-b93832bdede2) 
- Prediction and Solution Page <br><br>
  ![result_page](https://github.com/borut0/Plant_Disease_Detection/assets/89539128/96563b07-56a8-4627-ac94-99ac584b66e0)
- Error when user uploaded wrong file <br><br>
  ![error_page](https://github.com/borut0/Plant_Disease_Detection/assets/89539128/8fc55a29-7bb0-4468-bcb6-e4b011719dfc)
- Page Not Found 
  ![page_not_found](https://github.com/borut0/Plant_Disease_Detection/assets/89539128/e1865787-4791-4acc-ada7-581c550651b8)
  
## Model
- Structure <br><br>
![model_structure](https://github.com/borut0/Plant_Disease_Detection/assets/89539128/d58f6af3-2788-4d4f-bc50-74d0bca1c769)
- Accuracy <br><br>
![accuracy](https://github.com/borut0/Plant_Disease_Detection/assets/89539128/e2d8ac9e-a9ea-4088-9b3f-3035d31a119f)
- Loss <br><br>
![loss](https://github.com/borut0/Plant_Disease_Detection/assets/89539128/acf3b443-7480-4697-943e-e5c300c29365)
- Classification Report <br><br>
![classificatin_report](https://github.com/borut0/Plant_Disease_Detection/assets/89539128/e2eec1a3-6763-43fd-9188-df61e77259e9)

## Requirement 

| Package             | Version                                                          |
| ----------------- | ------------------------------------------------------------------ |
| Python | 3.9.16 |
| Tensorflow | 2.4.1 |
| Django | 4.1 |
| Numpy | 1.22.3 |

## Installation 

Clone the Repository

```bash
git clone https://github.com/borut0/Plant_Disease_Detection.git
```
Build the Model (sorry i didn't provide a model because it is too large(approx 900MB) and requirement.txt, I assure you it will not happend again)

```bash
cd Plant_Disease_Detection/Programming/final
```

Then run plant_disease_detection.ipynb
after couple of hours we got our model 

```bash
mkdir -p ../../website/models
cp best_model.h5 ../../website/models

```




