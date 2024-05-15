import os
import re
import zipfile
import numpy as np
import pandas as pd
from PIL import Image
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from matplotlib.backends.backend_pdf import PdfPages

def sort_list_of_fs_by_ascending_number(list_of_fs, r_pattern = ''):
    '''
    This function sorts a list of files/words by ascending order 
    E.g.(1): sort_list_of_fs_by_ascending_number(['Model_10.inp','Model_1.inp'])
    E.g.(2): sort_list_of_fs_by_ascending_number(['t_1 Model_10.inp','t_2 Model_1.inp'], 'Model_')
    ----------
    list_of_fs: [list of files/words]
    r_pattern: [str/regex] | regex pattern | Def. arg.: ''
    ----------
    the function modifies the list
    '''
    list_of_fs.sort(key=lambda el:int(re.search(f'{r_pattern}(\d+)',el).group(1)))

def save_images_to_pdf(pdf_name, images_folder = '.' ,  r_pattern = 'png', remove_imgs = False):
    image_files = [f for f in os.listdir(images_folder) if re.search(r_pattern, f)]
    sort_list_of_fs_by_ascending_number(image_files)

    pdf = canvas.Canvas(f'{pdf_name}.pdf', pagesize=letter)

    for image_file in image_files:
        image_path = os.path.join(images_folder, image_file) # Sacar directorio de cada imagen
        
        with Image.open(image_path) as img:
            img_width, img_height = img.size
            
            # Calculate aspect ratio to fit within the page size
            aspect_ratio = img_width / img_height
            target_width = letter[0]
            target_height = target_width / aspect_ratio

            # Ensure the image fits within the page size
            if target_height > letter[1]:
                target_height = letter[1]
                target_width = target_height * aspect_ratio

            # Calculate centering position
            x_offset = (letter[0] - target_width) / 2
            y_offset = (letter[1] - target_height) / 2
            
            # Draw the image on the PDF with correct size and position
            pdf.drawImage(image_path, x_offset, y_offset, width=target_width, height=target_height)
            pdf.showPage() 
            
    pdf.save()
    if remove_imgs:[os.remove(f'{images_folder}/{f}') for f in image_files]

def create_temp_imgs(f_list, path = None):
    if not path: path = Path('.')
    [fig.savefig(f'{path}/{i+1}_temp_img.png') for i, fig in enumerate(f_list)]

def save_figs_to_pdf(path, f_list): 
    '''
    This function generates a pdf with a given figure list.
    E.g.: save_figs_as_pdf('Imagenes/pdf_doc.pdf', f_list)
    ----------
    path: [str] | Name of the pdf to be saved with | Def. arg.:  'pdf_doc.pdf'
    f_list: [list of figures] | [f1, f2, ..., fn]
    '''
    with PdfPages(path) as pdf:
        for f in f_list:
            pdf.savefig(f)
            
def create_zip_given_f_l(zip_name, path = None,  r_pattern = 'png', remove_fs = False):
    '''
    This function generates a zip file given a folder and r_pattern.
    E.g.: create_zip_given_f_l('zip_file', path = Path('Results'),  r_pattern = 'png', remove_fs = True)            
    ----------
    zip_name: [str] | Name of the zip file
    path: [str] | path
    r_pattern: [str/regex] | regex pattern | Def. arg.: ''
    remove_fs: [True/False] | delete/don't delete  files  | Def. arg.: False
    '''
    if not path: path = Path('.')
    image_files = [f for f in os.listdir(path) if re.search(r_pattern, f)]
    sort_list_of_fs_by_ascending_number(image_files)
    
    with zipfile.ZipFile(path/f'{zip_name}.zip', 'w') as img_zip:
        for f in image_files:
            img_zip.write(path/f, f)
    if remove_fs:[os.remove(f'{path}/{f}') for f in image_files]

def filt_data_by_start_end_time(data, start_date, end_date):
    datetime_col = data.select_dtypes(include='datetime64').columns[0]
    return data[(data[datetime_col] >= start_date) & (data[datetime_col] <= end_date)]

def get_data_filter_between_vals(data, var, lims):
    data_mod = data.copy()
    a, b = lims
    if a is None:
        data_mod.loc[data[var] >= b, var]  = np.nan
    elif b is None:
        data_mod.loc[data[var] <= a, var]  = np.nan
    else:
        data_mod.loc[~data[var].between(a, b) , var]  = np.nan
    return data_mod

def save_dict_to_excel(data, file_name):
    df = pd.DataFrame(data)
    df.to_excel(f'{file_name}.xlsx', index=False)