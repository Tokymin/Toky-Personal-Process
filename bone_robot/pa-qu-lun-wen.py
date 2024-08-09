import requests
from bs4 import BeautifulSoup
import os

# Example list of titles
titles = [
    '1. Incorporating the Hybrid Deformable Model for Improving the Performance of Abdominal CT Segmentation via Multi-Scale Feature Fusion Network',
    '2. Fiber Bragg Grating-Based Force Sensing in Robot-Assisted Cardiac Interventions: A Review',
    '3. Towards real time guide wire shape extraction in fluoroscopic sequences: A two phase deep learning scheme to extract sparse curvilinear structures.',
    '4. Iterative stripe artifact correction framework for TOF-MRA',
    '5. A Novel Method of Using Bifilar Spiral Resonator for Designing Thin Robust Flexible Glucose Sensors',
    '6. Automatic tool segmentation and tracking during robotic intravascular catheterization for cardiac interventions',
    '7. Towards Faster and More Accurate Target Localization on Intrafraction X-Ray Fluoroscopy for Lung Radiotherapy Using Modified YoloV3 Detector',
    '8. Gradient Variability Coefficient A Novel Method for Assessing Glycemic Variability and Risk of Hypoglycemia',
    '9. Nonlinear dynamics of a conical dielectric elastomer oscillator with switchable mono to bi-stability',
    '10. Preliminary Feasibility Study of Imaging Registration Between Supine and Prone Breast CT in Breast Cancer Radiotherapy Using Residual Recursive Cascaded Networks',
    '11. A novel multi-DoF surgical robotic system for brachytherapy on liver tumor: Design and control',
    '12. A Soft Wearable and Fully-Textile Piezoresistive Sensor for Plantar Pressure Capturing',
    '13. Radiographical assessment of tumour stroma and treatment outcomes using deep learning: a retrospective multicohort study',
    '14. Noninvasive Prediction of Occult Peritoneal Metastasis in Gastric Cancer Using Deep Learning',
    '15. Fully-automated functional region annotation of liver via a 2.5D class-aware deep neural network with spatial adaptation',
    '16. Self-supervised CT Super-Resolution with Hybrid Model',
    '17. LSTformer: Long Short-term Transformer for Real Time Respiratory Prediction',
    '18. A parametric study on the subharmonic isolas in a bistable dielectric elastomer actuator',
    '19. Weighting-Based Deep Ensemble Learning for Recognition of Interventionalists’ Hand Motions During Robot-Assisted Intravascular Catheterization',
    '20. Adapting Neural-Based Models for Position Error Compensation in Robotic Catheter Systems',
    '21. Topological EEG Nonlinear Dynamics Analysis for Emotion Recognition',
    '22. Exploring Operators’ Natural Behaviors to Predict Catheterization Trial Outcomes in Robot-Assisted Intravascular Interventions',
    '23. Context-aware network fusing transformer and V-Net for semi-supervised segmentation of 3D left atrium',
    '24. A Soft Robotic Balloon Endoscope for Airway Procedures',
    '25. Online Hard Patch Mining Using Shape Models and Bandit Algorithm for Multi-Organ Segmentation',
    '26. A deep unsupervised learning framework for the 4D CBCT artifact correction',
    '27. Guidewire simulation of endovascular intervention: A systematic review',
    '28. A statistical deformation model-based data augmentation method for volumetric medical image segmentation',
    '29. Volumetric tumor tracking from a single cone-beam X-ray projection image enabled by deep learning',
    '30. Deep Multi-Magnification Similarity Learning for Histopathological Image Classification',
    '31. ARR-GCN: Anatomy-Relation Reasoning Graph Convolutional Network for Automatic Fine-Grained Segmentation of Organs Surgical Anatomy',
    '32. An attention-based deep convolutional neural network for ultra-sparse-view CT reconstruction',
    '33. Sinogram domain metal artifact correction of CT via deep learning',
    '34. Semi-supervised segmentation of coronary DSA using mixed networks and multi-strategies',
    '35. An unsupervised dual contrastive learning framework for scatter correction in cone-beam CT image',
    '36. Ultra-tunable bistable structures for universal robotic applications',
    '37. An Unsupervised Learning-Based Regional Deformable Model for Automated Multi-Organ Contour Propagation',
    '38. Guidewire Endpoint Detection Based on Pixeladjacent-relation During Robot-assisted Intravascular Catheterization: In vivo mammalian models',
    '39. Volumetric feature points integration with bio-structure-informed guidance for deformable multi-modal CT image registration',
    '40. Development of an Intuitive Interface with Haptic Enhancement for Robot-Assisted Endovascular Intervention',
    '41. A Soft Robot Driven by a Spring-Rolling Dielectric Elastomer Actuator with Two Bristles',
    '42. Technical and Clinical Progress on Robot-Assisted Endovascular Interventions: A Review'
]


# Function to search for paper and download
def download_paper(title, save_path):
    search_url = f"https://scholar.google.com/scholar?q={title}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Example selector for the first PDF link (this may need to be adjusted based on the site structure)
    link_tag = soup.select_one("a[href$='.pdf']")

    if link_tag:
        pdf_url = link_tag["href"]
        pdf_response = requests.get(pdf_url)

        # Save the PDF
        with open(save_path, "wb") as file:
            file.write(pdf_response.content)
        print(f"Downloaded: {title}")
    else:
        print(f"PDF not found for: {title}")


# Directory to save the papers
save_dir = "downloaded_papers"
os.makedirs(save_dir, exist_ok=True)

# Loop over titles and download papers
for title in titles:
    number, paper_title = title.split('. ', 1)
    safe_title = paper_title.replace('/', '_')  # Make title file system safe
    save_path = os.path.join(save_dir, f"{number} {safe_title}.pdf")
    download_paper(paper_title, save_path)
