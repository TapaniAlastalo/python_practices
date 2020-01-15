import rsa_gendata
import rsa_enc
import rsa_dec
import rsa_key_builder
# File paths
import filepaths

import time
    

def main():
    #tests1()
    tests2()
    tests3()

def tests3():
    print("Test3. Test big preset value speed")
    constant = 1
    #rsa_gendata.generateTestDataWithConstant(constant)
    
    try:
        runTime = time.time()
        
        # Pick Secret pre values p & q. Could be any prime numbers.
        # use preset values
        p = rsa_key_builder.DEFAULT_P
        q = rsa_key_builder.DEFAULT_Q
        print("Secret p & q are [" + str(p) + "," + str(q) + "]")

        # Calculate n, e, d
        # Public keys
        n = p*q
        # Calculate public key e # or use preset value
        e = rsa_key_builder.DEFAULT_E
        print("Public key pair is [" + str(n) + "," + str(e) + "]")

        # Calculate secret key # or use preset value
        d = rsa_key_builder.DEFAULT_D
        # no d found
        print("Secret key is " + str(d))

        # PICK TEST DATA FILES      
        default_files = filepaths.getTestDataFiles()
        # shortest are enough
        files = [ default_files[1] ]
        executeTest(n, e, d, files, runTime, 1)
    
    except ValueError as error:
        print(error.args)


def tests2():
    print("Test2. Test long message speed.")
    constant = 10000
    #rsa_gendata.generateTestDataWithConstant(constant)

    try:
        runTime = time.time()
        
        # Pick Secret pre values p & q. Could be any prime numbers.
        # use preset values
        p = rsa_key_builder.FAST_P
        q = rsa_key_builder.FAST_Q
        print("Secret p & q are [" + str(p) + "," + str(q) + "]")

        # Calculate n, e, d
        # Public keys
        n = p*q
        # Calculate public key e # or use preset value
        e = rsa_key_builder.FAST_E
        print("Public key pair is [" + str(n) + "," + str(e) + "]")

        # Calculate secret key # or use preset value
        d = rsa_key_builder.FAST_D
        # no d found
        print("Secret key is " + str(d))

        # PICK TEST DATA FILES      
        default_files = filepaths.getTestDataFiles()
        # shortest are enough
        files = [ default_files[5] ]
        executeTest(n, e, d, files, runTime, 1)
    
    except ValueError as error:
        print(error.args)
    

def tests1():
     # Use only if want to regenerate test data.
    #rsa_gendata.generateTestData()

    # test with fast preset values. Test all generated data. Print only results.
    testFASTPresetValues()
    # test with bigger preset values. Test only shortest generated datas[0, 1, 2]. Print all.
    testDEFAULTPresetValues()
    # test with generated preset values. Test only shortest generated data[0, 1, 2]. Print all.
    testGeneratedValues()



def testFASTPresetValues():
    try:
        print("Prepare test for FAST preset values")
        runTime = time.time()
        
        # Pick Secret pre values p & q. Could be any prime numbers.
        # use preset values
        p = rsa_key_builder.FAST_P
        q = rsa_key_builder.FAST_Q
        print("Secret p & q are [" + str(p) + "," + str(q) + "]")

        # Calculate n, e, d
        # Public keys
        n = p*q
        # Calculate public key e # or use preset value
        e = rsa_key_builder.FAST_E
        print("Public key pair is [" + str(n) + "," + str(e) + "]")

        # Calculate secret key # or use preset value
        d = rsa_key_builder.FAST_D
        print("Secret key is " + str(d))

        # PICK TEST DATA FILES
        files = filepaths.getTestDataFiles()
        executeTest(n, e, d, files, runTime, 1)
    
    except ValueError as error:
        print(error.args)


# takes app. 5 mins
def testDEFAULTPresetValues():
    try:
        print("Prepare test for FAST preset values")
        runTime = time.time()
        
        # Pick Secret pre values p & q. Could be any prime numbers.
        # use preset values
        p = rsa_key_builder.DEFAULT_P
        q = rsa_key_builder.DEFAULT_Q
        print("Secret p & q are [" + str(p) + "," + str(q) + "]")

        # Calculate n, e, d
        # Public keys
        n = p*q
        # Calculate public key e # or use preset value
        e = rsa_key_builder.DEFAULT_E
        print("Public key pair is [" + str(n) + "," + str(e) + "]")

        # Calculate secret key # or use preset value
        d = rsa_key_builder.DEFAULT_D
        # no d found
        print("Secret key is " + str(d))

        # PICK TEST DATA FILES      
        default_files = filepaths.getTestDataFiles()
        # shortest are enough
        files = [ default_files[0], default_files[1], default_files[2] ]
        executeTest(n, e, d, files, runTime, 3)
    
    except ValueError as error:
        print(error.args)


def testGeneratedValues():
    try:
        runTime = time.time()
        # Pick Secret pre values p & q. Could be any prime numbers.
        # use prime generator
        p = rsa_key_builder.generateRandomPrimeNumber(17, 999)
        q = rsa_key_builder.generateRandomPrimeNumber(17, 999, p)
        print("Secret p & q are [" + str(p) + "," + str(q) + "]")

        # Calculate n, e, d
        # Public keys
        n = p*q
        # Calculate public key e # or use preset value
        e = rsa_key_builder.calculatePublicKey(p, q)
        print("Public key pair is [" + str(n) + "," + str(e) + "]")

        # Calculate secret key # or use preset value
        d = rsa_key_builder.calculateSecretKey(p, q, e)
        # no d found
        if d == -1:
            raise ValueError('No secret key d couldn\'t be determinated')
        print("Secret key is " + str(d))

        # PICK TEST DATA FILES      
        default_files = filepaths.getTestDataFiles()
        # shortest are enough
        files = [ default_files[0], default_files[1], default_files[2] ]
        executeTest(n, e, d, files, runTime, 3)
        
    except ValueError as error:
        print(error.args)



# LOOP TEST DATA AND RUN ENCS AND DECS   
def executeTest(n, e, d, files, runTime, printFlags = 1):
    counter = 0
    for filePath in files:  
        print("Starting File-" + str(counter) + " handling..")
        file_start_time = time.process_time()      
        with open(filePath, 'r') as f:   
            for line in f:
                # runs RSA encrypt
                encodedPoints = rsa_enc.encrypt(n, e, line, counter, runTime, printFlags)            
                # runs rsa_dec
                rsa_dec.decrypt(n, d, encodedPoints, counter, runTime, printFlags)
        file_total_time = time.process_time() - file_start_time
        print("File-" + str(counter) + " total handling time " + str(file_total_time))
        counter += 1



main()