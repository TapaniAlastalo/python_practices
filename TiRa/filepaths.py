# Data Folder
DATA_FOLDER = 'data/'
RESULTS_FOLDER = 'results/'
TEXT_FOLDER = 'texts/'

# Test Data
TEST_DATA_PATH = DATA_FOLDER + 'rsa_test_data-'

# Encrypt
ENC_RESULTS_PATH = RESULTS_FOLDER + 'rsa_enc_results-'
ENC_POINTS_PATH = TEXT_FOLDER + 'rsa_enc_points-'
ENC_TEXT_PATH = TEXT_FOLDER + 'rsa_enc_texts-'

# Decrypt
DEC_RESULTS_PATH = RESULTS_FOLDER + 'rsa_dec_results-'
DEC_POINTS_PATH = TEXT_FOLDER + 'rsa_dec_points-'
DEC_TEXT_PATH = TEXT_FOLDER + 'rsa_dec_texts-'

# Types
CSV = '.csv'
TXT = '.txt'

# File sets
def getTestDataFiles():
    TEST_DATA_FILES = [   TEST_DATA_PATH + '0' + TXT,
                    TEST_DATA_PATH + '1' + TXT,
                    TEST_DATA_PATH + '10' + TXT,
                    TEST_DATA_PATH + '100' + TXT,
                    TEST_DATA_PATH + '1000' + TXT,
                    TEST_DATA_PATH + '10000' + TXT ]
    return TEST_DATA_FILES

def getTestDataFilesRT(runTime):
    TEST_DATA_FILES = [   TEST_DATA_PATH + '0' + '_' + runTime + TXT,
                    TEST_DATA_PATH + '1' + '_' + runTime + TXT,
                    TEST_DATA_PATH + '5' + '_' + runTime + TXT,
                    TEST_DATA_PATH + '10' + '_' + runTime + TXT,
                    TEST_DATA_PATH + '50' + '_' + runTime + TXT,
                    TEST_DATA_PATH + '100' + '_' + runTime + TXT ]
    return TEST_DATA_FILES

def getENCPointsFiles(runTime):
    ENC_POINTS_FILES = [   ENC_POINTS_PATH + '0' + '_' + runTime + TXT,
                    ENC_POINTS_PATH + '1' + '_' + runTime + TXT,
                    ENC_POINTS_PATH + '2' + '_' + runTime + TXT,
                    ENC_POINTS_PATH + '3' + '_' + runTime + TXT,
                    ENC_POINTS_PATH + '4' + '_' + runTime + TXT,
                    ENC_POINTS_PATH + '5' + '_' + runTime + TXT ]
    return ENC_POINTS_FILES



def getENCTextFiles(runTime):
    ENC_TEXT_FILES = [   ENC_TEXT_PATH + '0' + '_' + runTime + TXT,
                    ENC_TEXT_PATH + '1' + '_' + runTime + TXT,
                    ENC_TEXT_PATH + '2' + '_' + runTime + TXT,
                    ENC_TEXT_PATH + '3' + '_' + runTime + TXT,
                    ENC_TEXT_PATH + '4' + '_' + runTime + TXT,
                    ENC_TEXT_PATH + '5' + '_' + runTime + TXT ]
    return ENC_TEXT_FILES