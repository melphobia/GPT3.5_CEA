import pandas as pd
import re
import traceback
import os
import sys
import pandas as pd
from typing import List, Dict
from datetime import datetime
import csv

def final_df_creation(preds,final_dict,letter_pattern):
    pred_entities = []

    for pred in preds:
        match = re.search(fr':\s({letter_pattern}\s.*)$', pred)
        match2 = re.search(fr'({letter_pattern}\s.*)$', pred)
    
        if match or match2:
            # Use match2 instead of match in the else block
            entity_with_letter = match.group(1) if match else match2.group(1)
            letter_pattern_removed = re.sub(fr'^{letter_pattern}\s', '', entity_with_letter)
            pred_entities.append(letter_pattern_removed)
        else:
            pred_entities.append(pred)
    
    entities = []

    for key, value in final_dict.items():
        entities.append(key[1])
        if len(entities) == len(pred_entities):
            break
            
    locations = []
    for key, value in final_dict.items():
            locations.append(key[0])
            if len(locations) == len(pred_entities):
                break

   
    pred_df = pd.DataFrame({'entity': entities , 'prediction': pred_entities,'location':locations})

    links = []
    for key_0, key_1, value in zip(pred_df['location'], pred_df['entity'], pred_df['prediction']):
        if (key_0, key_1) in final_dict:
            link = final_dict[(key_0, key_1)].get(value)
            if link:
                links.append(link)
            else:
                links.append(None)
        else:
            links.append(None)

    # Creating the final DataFrame
    final_pred_df = pd.DataFrame({'entity': entities, 'prediction': pred_entities, 'location': locations, 'link': links})
    final_pred_df[['dataset', 'column', 'row']] = final_pred_df['location'].str.split('_', expand=True)
    # Drop the original 'location' column if you no longer need it
    final_pred_df = final_pred_df.drop('location', axis=1)
    return final_pred_df



def prediction_submission_MC_Row(final_df,timestamp,prompt_number):
    predictions = []
    for index, row in final_df.iterrows():
        dataset = row['dataset'] if row['dataset'] is not None else "NIL"
        column = row['column'] if row['column'] is not None else "NIL"
        row_value = row['row'] if row['row'] is not None else "NIL"
        link = row['link'] if row['link'] is not None else "NIL"

        prediction = [dataset, column,row_value, link]
        predictions.append(prediction)
    
    prediction_df = pd.DataFrame(predictions, columns=['Dataset', 'Column','Row', 'Link'])
  

    csv_file_path = f'../evaluation/prediction_submissions/HardTables/HT_row_multiple_choice_prompt_{prompt_number}_{timestamp}.csv'
    os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)
    with open(csv_file_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for pred in predictions:
            csv_writer.writerow(pred)


def prediction_submission_Comma_Row(final_df,timestamp,prompt_number):
    predictions = []
    for index, row in final_df.iterrows():
        dataset = row['dataset'] if row['dataset'] is not None else "NIL"
        column = row['column'] if row['column'] is not None else "NIL"
        row_value = row['row'] if row['row'] is not None else "NIL"
        link = row['link'] if row['link'] is not None else "NIL"

        prediction = [dataset, column,row_value, link]
        predictions.append(prediction)
    
    prediction_df = pd.DataFrame(predictions, columns=['Dataset', 'Column','Row', 'Link'])
  

    csv_file_path = f'../evaluation/prediction_submissions/HardTables/HT_row_comma_prompt_{prompt_number}_{timestamp}.csv'
    os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)
    with open(csv_file_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for pred in predictions:
            csv_writer.writerow(pred)


def prediction_submission_MC_Cell(final_df,timestamp,prompt_number):
    predictions = []
    for index, row in final_df.iterrows():
        dataset = row['dataset'] if row['dataset'] is not None else "NIL"
        column = row['column'] if row['column'] is not None else "NIL"
        row_value = row['row'] if row['row'] is not None else "NIL"
        link = row['link'] if row['link'] is not None else "NIL"

        prediction = [dataset, column,row_value, link]
        predictions.append(prediction)
    
    prediction_df = pd.DataFrame(predictions, columns=['Dataset', 'Column', 'Row', 'Link'])
  

    csv_file_path = f'../evaluation/prediction_submissions/HardTables/HT_cell_multiple_choice_prompt_{prompt_number}_{timestamp}.csv'
    os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)
    with open(csv_file_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for pred in predictions:
            csv_writer.writerow(pred)


def prediction_submission_Comma_Cell(final_df,timestamp,prompt_number):
    predictions = []
    for index, row in final_df.iterrows():
        dataset = row['dataset'] if row['dataset'] is not None else "NIL"
        column = row['column'] if row['column'] is not None else "NIL"
        row_value = row['row'] if row['row'] is not None else "NIL"
        link = row['link'] if row['link'] is not None else "NIL"

        prediction = [dataset, column,row_value, link]
        predictions.append(prediction)
    
    prediction_df = pd.DataFrame(predictions, columns=['Dataset', 'Column','Row', 'Link'])
  

    csv_file_path = f'../evaluation/prediction_submissions/HardTables/HT_cell_comma_prompt_{prompt_number}_{timestamp}.csv'
    os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)
    with open(csv_file_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for pred in predictions:
            csv_writer.writerow(pred)
