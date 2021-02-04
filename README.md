#Python scripts to clean and prepare data for training custom Azure Cognitive Services models


## Russian_speech_to_text
This folder contains scripts to prepare and clean data for training a custom Russian Speech-To-Text model.

*Russian_speech_to_text\01_Recovery_and_rename_data\01_recovery_unzip_in_place.py:* unzips all small individual archives to workaround issue with damaged .zip files.

*Russian_speech_to_text\01_Recovery_and_rename_data\02_recovery_move_rename.py:* extract and copy all useful data (.wav + .txt) from individual folders.

*Russian_speech_to_text\02_Cleaning_data\01_remove_empty_audio_train.py:* remove all .wav files less than 3 seconds length and corresponding lines in label.txt.

*Russian_speech_to_text\02_Cleaning_data\02_remove_empty_text.py:* remove all empty lines from the text transcript and corresponding .wav files.

*Russian_speech_to_text\02_Cleaning_data\03_replace_latin_symbols.py:* replace/transliterate all Latin symbols to avoid errors during training.
 
Now the dataset is ready to upload and train the model. If testing model for the accuracy needed, use *tools\split_train_test.py* to randomly split the dataset into train and test.


*Russian_speech_to_text\tools\extract_length.py:* extract audio files length for reference.

*Russian_speech_to_text\tools\find_latin_symbols.py:* extract Latin symbols for reference.

*Russian_speech_to_text\tools\split_train_test.py:* split the dataset into train and test.

*Russian_speech_to_text\tools\test_Speech2Text.py:* test speech to text model (using custom model).

*Russian_speech_to_text\tools\test_Text2Speech.py.py:* test text to speech model (using general model).


## Text_to_text

This folder contains scripts to prepare and clean data for training 4 custom text translations models: Tr-En; En-Ru; Ru-En; En-Tr.
Excel file with multiple or single sheet should be used as an input. 
Each sheet should contain data in the first three columns: 'Sentences_RU', 'Sentences_EN', 'Sentences_TR'.

*Text_to_text\extract_clean_split_data.py:* extract data from excel, clean and prepare aligned files for training and testing.

*Text_to_text\tools\translate_fill_test_dataset.py:* to improve the accuracy of the model it is essential to manually check custom translations, and add more data to the training dataset depending on results. This script will help to translate test data in all directions using general and custom models to test the model accuracy and find weak points. The Input structure is one-sheet excel file with three columns: 'Sentences_RU', 'Sentences_EN', 'Sentences_TR'; test file output from the extract_clean_split_data.py can be used for that.

*Text_to_text\tools\test_translate.py:* test text translations.

*Text_to_text\tools\search_for_symbols.py:* search for symbols [.;:] in text files, may be useful for prepare non-aligned files to avoid sentences splitting. Not necessary for aligned files.

*Text_to_text\tools\excel_macros_merge_multiple_files.txt:* excel macros for joining multiple files into one file with many worksheets, which can be used then as an input for extract_clean_split_data.py.




## Turkish_speech_to_text
This folder contains scripts to prepare and clean data for training a custom Russian Speech-To-Text model.


*Russian_speech_to_text\01_Recovery_and_rename_data\01_unzip_and_test_Powershell.txt:* because of the very mixed input data structure, I had to extract all relelevant archives with Powershell and then manually moving all the folders, with had location different than \<username>\voice\speech

*Russian_speech_to_text\01_Recovery_and_rename_data\02_recovery_move_rename.py:* extract and copy all useful data (.wav + .txt) from individual folders.

*Russian_speech_to_text\02_Cleaning_data\01_remove_empty_audio_train.py:* remove all .wav files less than 3 seconds length and corresponding lines in label.txt.

*Russian_speech_to_text\02_Cleaning_data\02_remove_empty_text.py:* remove all empty lines from the text transcript and corresponding .wav files.

*Russian_speech_to_text\02_Cleaning_data\03_replace_latin_symbols.py:* replace all incorrect symbols as line brakes or tabs to avoid errors during training.
 
Now the dataset is ready to upload and train the model. If testing model for the accuracy needed, use *tools\split_train_test.py* to randomly split the dataset into train and test.


*Russian_speech_to_text\tools\extract_length.py:* extract audio files length for reference.

*Russian_speech_to_text\tools\parsing_data_folder_to_sentences.py:* extract Latin symbols for reference.

*Russian_speech_to_text\tools\split_train_test.py:* split the dataset into train and test.

*Russian_speech_to_text\tools\test_Speech2Text.py:* test speech to text model (using custom or general model).

*Russian_speech_to_text\tools\test_Text2Speech.py.py:* test text to speech model (using general model).
