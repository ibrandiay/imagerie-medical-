

import matplotlib.pyplot as plt
import pydicom
from pydicom.data import get_testdata_files

# Il faut changer le chemin de l'image selon le path ou elle se trouve

base = "/home/zoheir/Documents/Imageire médicale/Projet/AAA/DICOM/S00001/SER00001/"
pass_dicom = "I00002"
filename= pydicom.data.data_manager.get_files(base,pass_dicom)[0]

dataset = pydicom.dcmread(filename)

# Mode normal:
print()
print("Nom de Fichier.........:", filename)
print("Type de sauvegarde.....:", dataset.SOPClassUID)
print()

pat_name = dataset.PatientName
display_name = pat_name.family_name + ", " + pat_name.given_name
print("Nom du Patient...:", display_name)
print("Id du Patient.......:", dataset.PatientID)
print("Modalité.........:", dataset.Modality)
print("Date de passage.......:", dataset.StudyDate)

if 'PixelData' in dataset:
    rows = int(dataset.Rows)
    cols = int(dataset.Columns)
    print("Image size.......: {rows:d} x {cols:d}, {size:d} bytes".format(
        rows=rows, cols=cols, size=len(dataset.PixelData)))
    if 'PixelSpacing' in dataset:
        print("Pixel spacing....:", dataset.PixelSpacing)

# use .get() if not sure the item exists, and want a default value if missing
print("Slice location...:", dataset.get('SliceLocation', "(missing)"))

# Afficher l'image en utilisant matplotlib
plt.imshow(dataset.pixel_array, cmap=plt.cm.bone)
plt.show()


