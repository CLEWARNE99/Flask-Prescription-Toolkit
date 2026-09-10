# Eyeglass Prescription Toolkit
## 👓[Live Flask Demo](https://flask-prescription-toolkit.onrender.com/)👓
<img width="398" height="242" alt="tenor" src="https://github.com/user-attachments/assets/fe206e98-be76-48d0-a440-9501a422092c" />


After many years of working in the optical field, I've run countless calculations when dealing with patient prescriptions, and quality checking orders. As much as doing these calculations repeatedly has kept me sharp and on my feet, there are sometimes I wish I could just plug these numbers in somewhere and get
a quick result! Thus, the Eyeglass Prescription Toolkit was born.

This app can take a user-entered prescription, and depending on what the user wants, it can transpose the format of the prescription, find the power of the lens in a specified meridian, or convert a multifocal prescription into a single vision 
prescription.

## Some Eyeglass Prescription Jargon
Anytime you see OD, this is referring to the right eye (oculus dexter). OS refers to the left eye (oculus sinister).

There are a few parts to an eyeglass prescription:
- SPH: You can think of the SPH number as the baseline "strength" of your prescription. This number comes after a '+' or a '-'. If your prescription is minus, you are nearsighted, if it is plus, you are farsighted.
- CYL: This is the amount of astigmatism correction in your prescription. Astigmatism refers to when the eye is not shaped perfectly spherical, the more astigmatism, the more oval or football-shaped your eye is. This causes light to focus at multiple points rather than one, causing additional visual blur.
- AXIS: This is the degree of rotation the lens sits in your prescription. Only included when there is a CYL value, as SPH only lenses have the same power correction at every axis.
- ADD: This is included if you need reading correction in addition to distance correction. Think of bifocals or progressives. This is the power "added" to your SPH correction in the bottom of the lens (in other words the distance power is reduced by this much to accommodate for up-close vision.)

## Tech Stack:
Python, HTML, Flask, Jinja2

## About the Project:
- app.py contains the Flask app. There are routes going to each of the 3 pages of the app. Functions for the routes also use requests to retrieve user-inputted data from the fields on each page. It also uses logic from the 4 core .py files to transform the user's prescription values depending on which
tool is being used.
- The templates folder contains each of the .html pages utilized by the app. These html pages use Jinja2 to dynamically render the output on each page.

I decided to separate the python logic into separate files for readability and organization. Rather than one big logic file that would be long and messy, these map nicely to each page of the app.

For the CSS, I used Bootstrap, and made some small tweaks to adjust to my vision of the app.

<img width="981" height="514" alt="Screenshot_10-9-2026_0262_flask-prescription-toolkit onrender com" src="https://github.com/user-attachments/assets/c77508be-4c47-459c-a8d1-37ebbbf182fe" />
(A screenshot of the Cyl Transposition page!)

## How to Use
- Cyl Transpose:

This page of the app takes each part of your prescription, and transposes it to "plus cyl" format or "minus cyl" format. Plus cyl and minus cyl are two different ways of writing the same prescription, minus cyl mostly used by optometrists, and plus cyl mostly used by opthamologists.

Converting the prescription can make it easier to compare to another prescription or an older prescription if each prescription is written in a different format.

- Power at 90/180

This page of the app takes each part of your prescription, and then find the power in either the horizontal meridian of the lens (180), or the vertical meridian of the lens (90). This is useful for determining how precisely the lens needs to be centered for the patient, and for calculating induced prism in
 lenses when the lens centers are misaligned with the patient's pupils.

- Multifocal to Single Vision

This page of the app takes each part of a multifocal prescription, and converts it into single vision. Sometimes when someone has a multifocal prescription, they want to use the distance-only part of it, or the reading-only part of it. They can also use the intermediate-only for computer usage or reading sheet music!

## Installation
1. Clone the repository
```   
git clone https://github.com/CLEWARNE99/Flask-Prescription-Toolkit.git
```
2. Install dependencies
```
pip install -r requirements.txt
```

## Running the Flask App locally
To run the flask app locally, run:
```
python app.py
```

## Some Reflection:
I started writing this project with tkinter. I actually wrote a completely functional version using tkinter, but using it, I realized it would be complicated to share the project with others. After doing some research I familiarized myself with Flask, which ended up being a perfect medium for this project: more modern,
 and able to be shared simply by clicking a link!

For future development on this project, implementing an ANSI Standards checker for orders would be another useful addition. This page could take details from an order, vs how the order was manufactured to determine if the prescription lenses fall within ANSI tolerance standards, and are able to be dispensed to a
 patient.
