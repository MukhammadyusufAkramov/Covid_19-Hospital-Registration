#Akramov.Mukhammadyusuf
#TP059554


# imports
import os


# Return a list of each record
# def ParseFile( filename, sep = ',' ):
    tempList = []
    with open( filename, 'r' ) as dataFile:
        for line in dataFile:
            line[] = line.rstrip( '\n' ) # right strip any newline characters
            tempList.append( line.split( sep ) )
    return tempList


# To "write" to the "filename" file, using "sep" as separator 
def CreateText( filename, toWrite, sep = ',' ):
    with open( filename, 'w' ) as dataFile:
        for lines in toWrite:
            dataFile.write( ''.join( [ ( str( item ) + sep ) for item in lines ] ).rstrip( sep ) + '\n' )


# Display console
def ClearConsole():
    try:
        os.get_terminal_size()

        if( os.name == "nt" ):
            os.system( "cls" )
        else:
            os.system( "clear" )
    except:
        # do not do it
        pass


# Get a list of lists and search 
def Search( givenList, key = None, value = None, invalidInput = False, invalidText = "Invalid Input" ):
    if ( key == None or value == None ):
        print( "Search by? (PID/CID/Name/Group/Zone/Contact Number/Email/" )
        print( "Medical History/Blood Group/Height/Weight/Status/T1/T2/T3/Admission): " )
        enPut = input().lower()
        key = 0
        dataFields = ["PID", "CID", "Name", "Group", "Zone", "Contact Number", "Email", "Medical History", "Blood Group", "Height", "Weight", "Status", "T1", "T2", "T3", "Admission"]
        options = []
        sep = '/'
        
        if ( enPut == "pid" ):
            key = 0
        elif ( enPut == "cid" ):
            key = 1
        elif ( enPut == "name" ):
            key = 2
        elif ( enPut == "group" ):
            key = 3
            options = [ "ATO", "ACC", "AEO", "SID", "AHS" ]
        elif ( enPut == "zone" ):
            key = 4
            options = [ "A", "B", "C", "D" ]
        elif ( enPut == "contact Number" ):
            key = 5
        elif ( enPut == "email" ):
            key = 6
        elif ( enPut == "medical history" ):
            key = 7
        elif ( enPut == "blood group" ):
            key = 8
            options = [ "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-" ]
        elif ( enPut == "height" ):
            key = 9
        elif ( enPut == "weight" ):
            key = 10
        elif ( enPut == "status" ):
            key = 11
            options = [ "ACTIVE", "RECOVERED", "DECEASED" ]
        elif ( enPut == "t1" ):
            key = 12
            options = [ "QHNF", "QDFR", "HQFR", "HQNF", "CWFR" ]
        elif ( enPut == "t2" ):
            key = 13
            options = [ "QHNF", "QDFR", "HQFR", "HQNF", "CWFR" ]
        elif ( enPut == "t3" ):
            key = 14
            options = [ "QHNF", "QDFR", "HQFR", "HQNF", "CWFR" ]
        elif ( enPut == "admission" ):
            key = 15
            options = [ "Home", "NW", "ICU" ]
        else:
            #Invalid Input
            return False 
        
        possibleArgs = ''.join( [ item + sep for item in options ] ).rstrip( sep )
        if ( possibleArgs ):
            possibleArgs = " (" + possibleArgs + ")"
        
        print( f"Enter a {dataFields[key]}{possibleArgs}:" )
        value = input().lower()
    
    foundList = []
    count = 0
    for n in range( len( givenList ) ):
        
        # find out
        found = False
        if ( value.isdigit() ):
            if ( givenList[n][key].lower() == value ):
                found = True
        else: # .find() for lenient find, .startswith() for stricter find
            if ( givenList[n][key].lower().find( value ) != -1 ):
                found = True
        
        if ( found == True ):
            ClearConsole()
    
            if ( invalidInput ):
                print( "=============", invalidText, "=============")
                
            else:
                print( "\n\n\n" )            
            print( "COVID-19 PATIENT MANAGEMENT SYSTEM \n |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| \n Search \n" )
            print( " 1.  PID : ", givenList[n][0], "\n 2.  CID : ", givenList[n][1], "\n 3.  Name : ", givenList[n][2], "\n 4.  Group : ", givenList[n][3])
            print( " 5.  Zone : ", givenList[n][4], "\n 6.  Contact Number : ", givenList[n][5], "\n 7.  Email : ", givenList[n][6], "\n 8.  Medical History : ", givenList[n][7])
            print( " 9.  Blood Group : ", givenList[n][8], "\n 10. Height : ", givenList[n][9], "\n 11. Weight : ", givenList[n][10], "\n 12. Status : ", givenList[n][11])
            print( " 13. Test 1 : ", givenList[n][12], "\n 14. Test 2 : ", givenList[n][13], "\n 15. Test 3 : ", givenList[n][14], "\n 16. Admission : ", givenList[n][15])
            print( " 14. Test 2 : ", givenList[n][13] )
            print( "\n Is this entry what you were looking for? (\"Y\" to end search / \"N\" to go back):" )
            
            enPut = input().upper()
            
            if ( enPut == "Y" ):
                return givenList[n]
            elif ( enPut == "N" ):
                if not ( Search( givenList[ ( n + 1 ) : None ], key, value ) ):
                    return None
                else:
                    return givenList[n]
            else:
                if not ( Search( givenList[ n : None ], key, value, invalidInput = True ) ):
                    return None
                else:
                    return givenList[n]
            
    return None


def ChangeDetails( givenList, invalidInput = False, invalidText = "Invalid Input" ):
    ClearConsole()
    
    if ( invalidInput ):
        print( "=============", invalidText, "=============")
    else:
        print( "\n\n\n" )
        print( "COVID-19 PATIENT MANAGEMENT SYSTEM \n |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| \n Patient Details Input \n" )
        print( " 1.  PID : ", givenList[0], "\n 2.  Name : ", givenList[2], "\n 3.  Group : ", givenList[3])
        print( " 4.  Zone : ", givenList[4], "\n 5.  Contact Number : ", givenList[5], "\n 6.  Email : ", givenList[6], "\n 7.  Medical History : ", givenList[7] )
        print( " 8.  Blood Group : ", givenList[8], "\n 9. Height : ", givenList[9], "\n 10. Weight : ", givenList[10])
        print( " d.  Done \n x.  Cancel \n\n\n\n" )
        print( "Enter a number to modify its entry : " )
    
    enPut = input()

    # PID
    if ( enPut == "1" ):
        if not( ChangeDetails( givenList, invalidInput = True, invalidText = "PID cannot be modified" ) ):
            return False

    # Name
    elif ( enPut == "2" ):
        print( "Enter a new Name (x to cancel):" )
        enPut = input()
        noCommaInput = enPut.replace( ',', '' )
        
        if ( enPut == 'x' or enPut == 'X' ):
            if not( ChangeDetails( givenList ) ):
                return False
        elif not( enPut.isprintable() and enPut == noCommaInput ):
            if not( ChangeDetails( givenList, invalidInput = True, invalidText = "Invalid Input. No Commas allowed in Input." ) ):
                return False
        else:
            givenList[2] = enPut
            if not( ChangeDetails( givenList ) ):
                return False

    # Group
    elif ( enPut == "3" ):
        print( "Enter a new Group (ATO/ACC/AEO/SID/AHS) (x to cancel):" )
        enPut = input().upper()
        
        allowedGroups = [ "ATO", "ACC", "AEO", "SID", "AHS" ]
        if enPut == 'X':
            if not( ChangeDetails( givenList ) ):
                return False
        elif not( enPut in allowedGroups ):
            if not( ChangeDetails( givenList, invalidInput = True, invalidText = "Invalid Input. Groups must be ATO, ACC, AEO, SID, or AHS." ) ):
                return False
        else:
            givenList[3] = enPut
            if not( ChangeDetails( givenList ) ):
                return False

    # Zone
    elif ( enPut == "4" ):
        print( "Enter a new Zone (A/B/C/D) (x to cancel):" )
        enPut = input().upper()
        
       
        allowedZones = [ 'A', 'B', 'C', 'D' ]
        if enPut == 'X':
            if not( ChangeDetails( givenList ) ):
                return False
        elif not( enPut in allowedZones ):
            if not( ChangeDetails( givenList, invalidInput = True, invalidText = "Invalid Input. Zones must be A, B, C, or D." ) ):
                return False
        else:
            givenList[4] = enPut
            if not( ChangeDetails( givenList ) ):
                return False

    # Contact Number
    elif ( enPut == "5" ):
        print( "Enter a new Contact Number (x to cancel):" )
        enPut = input()
        digits = enPut.replace( '-', '' ).replace( '+', '' )
        
        if ( enPut == 'x' or enPut == 'X' ):
            if not( ChangeDetails( givenList ) ):
                return False
        elif not( digits.isdigit() and ( enPut.count( '+' ) <= 1 and enPut.count( '-' ) <= 1 ) ):
            if not( ChangeDetails( givenList, invalidInput = True, invalidText = "Invalid Input. Contact Number should only consist of digits, a dash and a plus symbol." ) ):
                return False
        else:
            givenList[5] = enPut
            if not( ChangeDetails( givenList ) ):
                return False

    # Email
    elif ( enPut == "6" ):
        print( "Enter a new Email (x to cancel):" )
        enPut = input()
        noCommaInput = enPut.replace( ',', '' )
        
        if ( enPut == 'x' or enPut == 'X' ):
            if not( ChangeDetails( givenList ) ):
                return False
        elif not( enPut.isprintable() and enPut == noCommaInput ):
            if not( ChangeDetails( givenList, invalidInput = True, invalidText = "Invalid Input. No Commas allowed in Input." ) ):
                return False
        else:
            givenList[6] = enPut
            if not( ChangeDetails( givenList ) ):
                return False

    # Medical History
    elif ( enPut == "7" ):
        print( "Enter a new Medical History (x to cancel):" )
        enPut = input()
        noCommaInput = enPut.replace( ',', '' )
        
        if ( enPut == 'x' or enPut == 'X' ):
            if not( ChangeDetails( givenList ) ):
                return False
        elif not( enPut.isprintable() and enPut == noCommaInput ):
            if not( ChangeDetails( givenList, invalidInput = True, invalidText = "Invalid Input. No Commas allowed in Input." ) ):
                return False
        else:
            givenList[7] = enPut
            if not( ChangeDetails( givenList ) ):
                return False

    # Blood Group
    elif ( enPut == "8" ):
        print( "Enter a new Blood Group (A+/A-/B+/B-/AB+/AB-/O+/O-) (x to cancel):" )
        enPut = input().upper()
        
       
        allowedBloodGroups = [ "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-" ]
        if enPut == 'X':
            if not( ChangeDetails( givenList ) ):
                return False
        elif not( enPut in allowedBloodGroups ):
            if not( ChangeDetails( givenList, invalidInput = True, invalidText = "Invalid Input. Blood Groups must be A+, A-, B+, B-, AB+, AB-, O+, or O-." ) ):
                return False
        else:
            givenList[8] = enPut
            if not( ChangeDetails( givenList ) ):
                return False

    # Height
    elif ( enPut == "9" ):
        print( "Enter a new Height (x to cancel):" )
        enPut = input()
        
    
        if ( enPut == 'x' or enPut == 'X' ):
            if not( ChangeDetails( givenList ) ):
                return False
        elif not( enPut.isdigit() ):
            if not( ChangeDetails( givenList, invalidInput = True, invalidText = "Invalid Input. Height must be a positive number." ) ):
                return False
        elif ( enPut.isdigit() ):
            if ( int( enPut ) <= 0 ):
                if not( ChangeDetails( givenList, invalidInput = True, invalidText = "Invalid Input. Height must be a positive number." ) ):
                    return False
            else:
                givenList[9] = enPut
                if not( ChangeDetails( givenList ) ):
                    return False

    # Weight
    elif ( enPut == "10" ):
        print( "Enter a new Weight (x to cancel):" )
        enPut = input()
        
        
        if ( enPut == 'x' or enPut == 'X' ):
            if not( ChangeDetails( givenList ) ):
                return False
        elif not( enPut.isdigit() ):
            if not( ChangeDetails( givenList, invalidInput = True, invalidText = "Invalid Input. Weight must be a positive number." ) ):
                return False
        else:
            givenList[10] = enPut
            if not( ChangeDetails( givenList ) ):
                return False

    elif ( enPut == "d" ):
        if ( givenList[3] == '-' or givenList[4] == '-' or ( givenList[5] == '-' and givenList[6] == '-' ) ):
            if not( ChangeDetails( givenList, invalidInput = True, invalidText = "Missing crucial information. Please check Group, Zone, and Contact Number or Email." ) ):
                return False
        else:
            pass
    elif ( enPut == 'x' or enPut == 'X' ):
        return False

    else:
        if not( ChangeDetails( givenList, invalidInput = True ) ):
            return False

    return givenList



def ChangeResults( givenList, invalidInput = False, invalidText = "Invalid Input" ):

    allowPreviousTestModification = False
    
    ClearConsole()
    
    if ( invalidInput ):
        print( "=============", invalidText, "=============")
    else:
        print( "\n\n\n" )
        print( " COVID-19 PATIENT MANAGEMENT SYSTEM \n |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| \n Test Result Details \n" )
        print( " 1.  PID : ", givenList[n][0], "\n 2.  CID : ", givenList[n][1], "\n 3.  Name : ", givenList[n][2], "\n 4.  Group : ", givenList[n][3])
        print( " 5.  Zone : ", givenList[n][4], "6.  Status : ", givenList[11], "7.  Test 1 : ", givenList[12], "8.  Test 2 : ", givenList[13])
        print( " 9.  Test 3 : ", givenList[14], "10.  Admission : ", givenList[15] )
        print( " d.  Done" , "x.  Cancel \n\n\n\n" )
        print( " Enter a number to modify its entry : " )
        
    enPut = input()
    
    if ( enPut == "1" ):
        if not( ChangeResults( givenList, invalidInput = True, invalidText = "PID cannot be modified" ) ):
            return False

    elif ( enPut == "2" ):
        if not( ChangeResults( givenList, invalidInput = True, invalidText = "CID cannot be modified" ) ):
            return False

    elif ( enPut == "3" ):
        if not( ChangeResults( givenList, invalidInput = True, invalidText = "Please use the Patient Details Modification interface to modify this field" ) ):
            return False

    elif ( enPut == "4" ):
        if not( ChangeResults( givenList, invalidInput = True, invalidText = "Please use the Patient Details Modification interface to modify this field" ) ):
            return False

    elif ( enPut == "5" ):
        if not( ChangeResults( givenList, invalidInput = True, invalidText = "Please use the Patient Details Modification interface to modify this field" ) ):
            return False

    # Status
    elif ( enPut == "6" ):
        if ( givenList[1] == "-" ):
            if not( ChangeResults( givenList, invalidInput = True, invalidText = "Status cannot be modified unless patient has been tested positive" ) ):
                return False
        else:
            print( "Enter a new Status (RECOVERED / DECEASED) (x to cancel):" )
            enPut = input().upper()
            
            if ( enPut == "RECOVERED" ):
                givenList[11] = "RECOVERED"
                if not( ChangeResults( givenList ) ):
                    return False
            elif ( enPut == "DECEASED" ):
                givenList[11] = "DECEASED"
                if not( ChangeResults( givenList ) ):
                    return False
            elif ( enPut == "X" ):
                if not( ChangeResults( givenList ) ):
                    return False
            else:
                if not( ChangeResults( givenList, invalidInput = True ) ):
                    return False

    # Test 1 / 12
    elif ( enPut == "7" ):
        validTestResults = []
        sep = '/'
        if ( givenList[3] == "ATO" or givenList[3] == "ACC" or givenList[3] == "AEO" ):
            validTestResults = [ "QHNF", "QDFR" ]
        elif ( givenList[3] == "SID" ):
            validTestResults = [ "QHNF", "HQFR" ]
        elif ( givenList[3] == "AHS" ):
            validTestResults = [ "HQNF", "CWFR" ]
        
        if ( allowPreviousTestModification ):
            # if either T2 or T3 is set
            if ( givenList[13] != "-" or givenList[14] != "-" ):
                print( "Modifying T1 will clear any preexisting data in T2 and T3. Proceed? (Y/N):" )
                enPut = input().upper()
                
                if ( enPut == "Y" ):
                    # clear T2 and T3, restore status
                    givenList[11] = "-"
                    givenList[13] = "-"
                    givenList[14] = "-"
                    
                    print( f"Enter a new Test Result( { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } ) (x to cancel):" )
                    enPut = input().upper()
                    
                    if ( enPut == validTestResults[0] ): # positive
                        givenList[12] = validTestResults[0]
                        givenList[11] = "ACTIVE"
                        
                        #suitable PID is found
                        tempList = ParseFile( "Data.txt" )
                        for lists in tempList:
                            if ( lists[0] == givenList[0] ):
                                givenList[1] = lists[1]
                                break
                        
                        #if empty CID, assign new CID                    
                        if ( givenList[1] == "-" ):
                            currentCID = 0
                            for items in ParseFile( "Data.txt" ):
                                if ( items[1] != "-" ):
                                    if ( int( items[1] ) > currentCID ):
                                        currentCID = int( items[1] )
                            currentCID += 1
                            givenList[1] = str( currentCID )
                        if not( ChangeResults( givenList ) ):
                            return False
                    elif ( enPut == validTestResults[1] ): # not positive
                        givenList[1] = "-" # retract CID
                        givenList[11] = "-" # retract Status
                        givenList[15] = "-" # retract Admission
                        givenList[12] = validTestResults[1]
                        if not( ChangeResults( givenList ) ):
                            return False
                    elif ( enPut == "X" ): # cancel
                        if not( ChangeResults( givenList ) ):
                            return False
                    else: # invalid input
                        if not( ChangeResults( givenList, invalidInput = True, invalidText = f"Tests can only be { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } for a patient of this group" ) ):
                            return False
                    
                elif ( enPut == "N" ):
                    if not( ChangeResults( givenList ) ):
                        return False
                else:
                    if not( ChangeResults( givenList, invalidInput = True ) ):
                        return False
            else:
                print( f"Enter a new Test Result( { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } ) (x to cancel):")
                enPut = input().upper()
                
                if ( enPut == validTestResults[0] ): # positive
                    givenList[12] = validTestResults[0]
                    givenList[11] = "ACTIVE"
                    
                    #find suitable PID
                    tempList = ParseFile( "Data.txt" )
                    for lists in tempList:
                        if ( lists[0] == givenList[0] ):
                            givenList[1] = lists[1]
                            break
                    
                    #if empty CID, assign new CID
                    if ( givenList[1] == "-" ):
                        # get newest CID to be used
                        currentCID = 0
                        for items in ParseFile( "Data.txt" ):
                            if ( items[1] != "-" ):
                                if ( int( items[1] ) > currentCID ):
                                    currentCID = int( items[1] )
                        currentCID += 1
                        givenList[1] = str( currentCID )
                    if not( ChangeResults( givenList ) ):
                        return False
                elif ( enPut == validTestResults[1] ): # not positive
                    givenList[1] = "-" # retract CID
                    givenList[11] = "-" # retract Status
                    givenList[15] = "-" # retract Admission
                    givenList[12] = validTestResults[1]
                    if not( ChangeResults( givenList ) ):
                        return False
                elif ( enPut == "X" ): # cancel
                    if not( ChangeResults( givenList ) ):
                        return False
                else: # invalid input
                    if not( ChangeResults( givenList, invalidInput = True, invalidText = f"Tests can only be { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } for a patient of this group" ) ):
                        return False
        else:
            if ( givenList[1] == "-" ):
                print( f"Enter a new Test Result( { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } ) (x to cancel):" )
                enPut = input().upper()
                
                if ( enPut == validTestResults[0] ): # positive
                    givenList[12] = validTestResults[0]
                    givenList[11] = "ACTIVE"
                    #if empty CID, assign new CID
                    if ( givenList[1] == "-" ):
                        # get newest CID to be used
                        currentCID = 0
                        for items in ParseFile( "Data.txt" ):
                            if ( items[1] != "-" ):
                                if ( int( items[1] ) > currentCID ):
                                    currentCID = int( items[1] )
                        currentCID += 1
                        givenList[1] = str( currentCID )
                    if not( ChangeResults( givenList ) ):
                        return False
                elif ( enPut == validTestResults[1] ): # not positive
                    givenList[12] = validTestResults[1]
                    if not( ChangeResults( givenList ) ):
                        return False
                elif ( enPut == "X" ): # cancel
                    if not( ChangeResults( givenList ) ):
                        return False
                else: # invalid input
                    if not( ChangeResults( givenList, invalidInput = True, invalidText = f"Tests can only be { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } for a patient of this group" ) ):
                        return False
            else:
                if not( ChangeResults( givenList, invalidInput = True, invalidText = "Cannot modify previously set results" ) ):
                    return False

    # Test 2 / 13
    elif ( enPut == "8" ):
        validTestResults = []
        sep = '/'
        if ( givenList[3] == "ATO" or givenList[3] == "ACC" or givenList[3] == "AEO" ):
            validTestResults = [ "QHNF", "QDFR" ]
        elif ( givenList[3] == "SID" ):
            validTestResults = [ "QHNF", "HQFR" ]
        elif ( givenList[3] == "AHS" ):
            validTestResults = [ "HQNF", "CWFR" ]
        
        # if T1 not set
        if ( givenList[12] == "-" ):
            if not( ChangeResults( givenList, invalidInput = True, invalidText = "Test 1 has not been performed yet" ) ):
                return False
        # if CID set(positive), T2 not executed
        elif ( givenList[1] != "-" and givenList[13] == "-" ):
            if not( ChangeResults( givenList, invalidInput = True, invalidText = "This patient has been tested positive. No further tests are needed." ) ):
                return False
        elif ( allowPreviousTestModification ):
            # if T3 is set
            if ( givenList[14] != "-" ):
                print( "Modifying T1 will clear any preexisting data in T3. Proceed? (Y/N):" )
                enPut = input().upper()
                
                if ( enPut == "Y" ):
                    # clear T3, check again Status
                    givenList[14] = "-"
                    if ( givenList[12] != "QHNF" and givenList[12] != "HQNF" ):
                        givenList[11] = "-"
                    
                    print( f"Enter a new Test Result( { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } ) (x to cancel):" )
                    enPut = input().upper()
                    
                    if ( enPut == validTestResults[0] ): # positive
                        givenList[13] = validTestResults[0]
                        givenList[11] = "ACTIVE"
                        
                        #find compability PID
                        tempList = ParseFile( "Data.txt" )
                        for lists in tempList:
                            if ( lists[0] == givenList[0] ):
                                givenList[1] = lists[1]
                                break
                        
                        #if empty CID, assign new CID
                        if ( givenList[1] == "-" ):
                            currentCID = 0
                            for items in ParseFile( "Data.txt" ):
                                if ( items[1] != "-" ):
                                    if ( int( items[1] ) > currentCID ):
                                        currentCID = int( items[1] )
                            currentCID += 1
                            givenList[1] = str( currentCID )
                        if not( ChangeResults( givenList ) ):
                            return False
                    elif ( enPut == validTestResults[1] ): # not positive
                        givenList[1] = "-" # retract CID
                        givenList[11] = "-" # retract Status
                        givenList[15] = "-" # retract Admission
                        givenList[13] = validTestResults[1]
                        if not( ChangeResults( givenList ) ):
                            return False
                    elif ( enPut == "X" ): # cancel
                        if not( ChangeResults( givenList ) ):
                            return False
                    else: # invalid input
                        if not( ChangeResults( givenList, invalidInput = True, invalidText = f"Tests can only be { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } for a patient of this group" ) ):
                            return False
                    
                elif ( enPut == "N" ):
                    if not( ChangeResults( givenList ) ):
                        return False
                else:
                    if not( ChangeResults( givenList, invalidInput = True ) ):
                        return False
            else:
                print( f"Enter a new Test Result( { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } ) (x to cancel):" )
                enPut = input().upper()
                
                if ( enPut == validTestResults[0] ): # positive
                    givenList[13] = validTestResults[0]
                    givenList[11] = "ACTIVE"
                    
                    
                    #searching for PID
                    tempList = ParseFile( "Data.txt" )
                    for lists in tempList:
                        if ( lists[0] == givenList[0] ):
                            givenList[1] = lists[1]
                            break
                    
                    #if empty CID, assign new CID
                    if ( givenList[1] == "-" ):
                        currentCID = 0
                        for items in ParseFile( "Data.txt" ):
                            if ( items[1] != "-" ):
                                if ( int( items[1] ) > currentCID ):
                                    currentCID = int( items[1] )
                        currentCID += 1
                        givenList[1] = str( currentCID )
                    if not( ChangeResults( givenList ) ):
                        return False
                elif ( enPut == validTestResults[1] ): # not positive
                    givenList[1] = "-" # retract CID
                    givenList[11] = "-" # retract Status
                    givenList[15] = "-" # retract Admission
                    givenList[13] = validTestResults[1]
                    if not( ChangeResults( givenList ) ):
                        return False
                elif ( enPut == "X" ): # cancel
                    if not( ChangeResults( givenList ) ):
                        return False
                else: # invalid input
                    if not( ChangeResults( givenList, invalidInput = True, invalidText = f"Tests can only be { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } for a patient of this group" ) ):
                        return False
        else:
            if ( givenList[1] == "-" ):
                print( f"Enter a new Test Result( { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } ) (x to cancel):" )
                enPut = input().upper()
                
                if ( enPut == validTestResults[0] ): # positive
                    givenList[13] = validTestResults[0]
                    givenList[11] = "ACTIVE"
                    #if empty CID, assign new CID
                    if ( givenList[1] == "-" ):
                        currentCID = 0
                        for items in ParseFile( "Data.txt" ):
                            if ( items[1] != "-" ):
                                if ( int( items[1] ) > currentCID ):
                                    currentCID = int( items[1] )
                        currentCID += 1
                        givenList[1] = str( currentCID )
                    if not( ChangeResults( givenList ) ):
                        return False
                elif ( enPut == validTestResults[1] ): # not positive
                    givenList[13] = validTestResults[1]
                    if not( ChangeResults( givenList ) ):
                        return False
                elif ( enPut == "X" ): # cancel
                    if not( ChangeResults( givenList ) ):
                        return False
                else: # invalid input
                    if not( ChangeResults( givenList, invalidInput = True, invalidText = f"Tests can only be { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } for a patient of this group" ) ):
                        return False
            else:
                if not( ChangeResults( givenList, invalidInput = True, invalidText = "Cannot modify previously set results" ) ):
                    return False

    # Test 3 / 14
    elif ( enPut == "9" ):
        validTestResults = []
        sep = '/'
        if ( givenList[3] == "ATO" or givenList[3] == "ACC" or givenList[3] == "AEO" ):
            validTestResults = [ "QHNF", "QDFR" ]
        elif ( givenList[3] == "SID" ):
            validTestResults = [ "QHNF", "HQFR" ]
        elif ( givenList[3] == "AHS" ):
            validTestResults = [ "HQNF", "CWFR" ]
        
        # if T1 not set
        if ( givenList[12] == "-" ):
            if not( ChangeResults( givenList, invalidInput = True, invalidText = "Test 1 has not been performed yet" ) ):
                return False
        # if T2 not set
        elif ( givenList[13] == "-" ):
            if not( ChangeResults( givenList, invalidInput = True, invalidText = "Test 2 has not been performed yet" ) ):
                return False
        # if CID set (positive), T3 not executed
        elif ( givenList[1] != "-" and givenList[14] == "-" ):
            if not( ChangeResults( givenList, invalidInput = True, invalidText = "This patient has been tested positive. No further tests are needed." ) ):
                return False
        elif ( allowPreviousTestModification or not ( givenList[1] != "-" ) ):
            print( f"Enter a new Test Result( { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } ) (x to cancel):" )
            enPut = input().upper()
            
            if ( enPut == validTestResults[0] ): # positive
                givenList[14] = validTestResults[0]
                givenList[11] = "ACTIVE"
                
                #find matching PID
                tempList = ParseFile( "Data.txt" )
                for lists in tempList:
                    if ( lists[0] == givenList[0] ):
                        givenList[1] = lists[1]
                        break
                
                #if empty CID, assign new CID
                if ( givenList[1] == "-" ):
                    currentCID = 0
                    for items in ParseFile( "Data.txt" ):
                        if ( items[1] != "-" ):
                            if ( int( items[1] ) > currentCID ):
                                currentCID = int( items[1] )
                    currentCID += 1
                    givenList[1] = str( currentCID )
                if not( ChangeResults( givenList ) ):
                    return False
            elif ( enPut == validTestResults[1] ): # not positive
                givenList[1] = "-" # retract CID
                givenList[11] = "-" # retract Status
                givenList[15] = "-" # retract Admission
                givenList[14] = validTestResults[1]
                if not( ChangeResults( givenList ) ):
                    return False
            elif ( enPut == "X" ): # cancel
                if not( ChangeResults( givenList ) ):
                    return False
            else: # invalid input
                if not( ChangeResults( givenList, invalidInput = True, invalidText = f"Tests can only be { ''.join( [ item + sep for item in validTestResults ] ).rstrip( sep ) } for a patient of this group" ) ):
                    return False
        else:
            if not( ChangeResults( givenList, invalidInput = True, invalidText = "Cannot modify previously set results" ) ):
                return False

    # Admission / 15
    elif ( enPut == "10" ):
        if ( givenList[1] != "-" ):
            if ( givenList[12] == "HQNF" or givenList[13] == "HQNF" or givenList[14] == "HQNF" ): # if HQNF, auto set to home
                givenList[15] = "Home"
            else:
                #take input
                print( f"Enter a new Admission location ( NW/ICU ) (x to cancel):" )
                enPut = input().upper()
                
                if ( enPut == "NW" ):
                    givenList[15] = "NW"
                    if not( ChangeResults( givenList ) ):
                        return False
                elif ( enPut == "ICU" ):
                    givenList[15] = "ICU"
                    if not( ChangeResults( givenList ) ):
                        return False
                elif ( enPut == "X" ):
                    if not( ChangeResults( givenList ) ):
                        return False
                else:
                    if not( ChangeResults( givenList, invalidInput = True ) ):
                        return False
        else:
            if not( ChangeResults( givenList, invalidInput = True, invalidText = "Patient is not tested positive. Cannot set Admission location" ) ):
                return False

    #check if Admission is filled
    elif ( enPut == "d" ):
        if ( givenList[11] != "-" ):
            if ( givenList[15] == "-" ):
                if not( ChangeResults( givenList, invalidInput = True, invalidText = "Missing crucial information. Please enter Admission location." ) ):
                    return False
                else:
                    return givenList

    elif ( enPut == "x" ):
        return False

    else:
        if not( ChangeResults( givenList, invalidInput = True ) ):
            return False

    return givenList



# Takes a list of lists
def CountResults( givenList ):
    T1 = 0
    T2 = 0
    T3 = 0
    for items in givenList:
        if( items[12] != "-" ):
            T1 += 1
        if( items[13] != "-" ):
            T2 += 1
        if( items[14] != "-" ):
            T3 += 1
    
    ClearConsole()
    print("\n\n\n")
    print( " COVID-19 PATIENT MANAGEMENT SYSTEM \n |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| \n Statistics \n 1. Total Test 1 Performed :", T1)
    print( " 2. Total Test 2 Performed :", T2, "\n 3. Total Test 3 Performed :", T3, "\n\n\n\n\n\n\n\n\n\n\n\n\n Press [ENTER] to return to Statistics menu")
    
    enPut = input()



# Returns True when done
def ShowLists( givenList, page, invalidInput = False, invalidText = "Invalid Input" ):
    maxPage = int( ( len( givenList ) - 1 ) / 15 ) + 1

    ClearConsole()
    if ( invalidInput ):
        print( "=============", invalidText, "=============")
        print( "" )
    else:
        print( "\n\n\n" )
        print( " COVID-19 PATIENT MANAGEMENT SYSTEM \n |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" )
        print( " Statistics (Data might be truncated for display purposes, please use Search for full data)")
    
    #print information
        print( "PID CID Name       Grp. Zne. Contact  Email    Med. Hist.   Bld. Ht.  Wt.  Sta. T1   T2   T3   Admission" )
    
    spacings = [ 3, 3, 10, 4, 4, 8, 8, 12, 4, 4, 4, 4, 4, 4, 4, 8 ]
    
    for n in range( ( page - 1) * 15, page * 15 ):
        if ( n >= len( givenList ) ):
            if ( n == 0 ):
                print( "\n\n ~~~~~~~~~~~~~~ NO DATA ~~~~~~~~~~~~~~" )
            else:
                print( "" )
        else:
            for o in range( 16 ):
                print( givenList[ n ][ o ][ 0 : spacings[ o ] ].ljust( spacings[ o ] ), end = '' )
                if ( o < 15 ):
                    print( ' ', end = '' )
                else:
                    print( '' )
                    print( "\n\n" )
                    print( f"[Page { page } of { maxPage }] \"<\" Previous Page | \">\" Next Page | \"x\" Done Viewing :", end = ' ' )
    
    enPut = input().upper()
    
    if ( enPut == "<" ):
        if ( page > 1 ):
            page -= 1
            if ( ShowLists( givenList, page ) ):
                return True
        else :
            if ( ShowLists( givenList, page, invalidInput = True, invalidText = "Cannot move page left" ) ):
                return True
    elif ( enPut == ">" ):
        if ( page < maxPage ):
            page += 1
            if ( ShowLists( givenList, page ) ):
                return True
        else :
            if ( ShowLists( givenList, page, invalidInput = True, invalidText = "Cannot move page right" ) ):
                return True
    elif ( enPut == "X" ):
        return True
    else:
        if ( ShowLists( givenList, page, invalidInput = True ) ):
            return True
    
    return True



# Returns True when done
def ShowStatistics( givenList, invalidInput = False, invalidText = "Invalid Input" ):
    ClearConsole()
    
    if ( invalidInput ):
        print( "=============", invalidText, "=============")
    else:
        print( "\n\n\n" )
        print( " COVID-19 PATIENT MANAGEMENT SYSTEM \n |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| \n Statistics \n" )
        print( " 1.  Tests Performed (for T1, T2, and T3) \n 2.  Patients Tested \n 3.  Recovered Cases" )
        print( " 4.  Positively Tested Patients (by group) \n 5.  Active Cases (by zone) \n 6.  Deceased Patients' Records" )
        print( " x.  Cancel \n\n\n\n\n\n\n\n\n" )
        print( "Enter a number : " )
    
    enPut = input()
    
    if ( enPut == "1" ):
        CountResults( givenList )
        if ( ShowStatistics( givenList ) ):
            return True
    elif ( enPut == "2" ):
        tempList = []
        for items in givenList:
            if ( items[12] != "-" ):
                tempList.append( items )
        
        ShowLists( tempList, 1 )
        if ( ShowStatistics( givenList ) ):
            return True
    elif ( enPut == "3" ):
        tempList = []
        for items in givenList:
            if ( items[11] == "RECOVERED" ):
                tempList.append( items )
        
        ShowLists( tempList, 1 )
        if ( ShowStatistics( givenList ) ):
            return True
    elif ( enPut == "4" ):
        print( "Enter a Group (ATO/ACC/AEO/SID/AHS) (x to cancel):" )
    
        enPut = input().upper()
        
        
        allowedGroups = [ "ATO", "ACC", "AEO", "SID", "AHS" ]
        if enPut == 'x':
            if ( ShowStatistics( givenList ) ):
                return True
        elif not( enPut in allowedGroups ):
            if ( ShowStatistics( givenList, invalidInput = True, invalidText = "Invalid Input. Groups must be ATO, ACC, AEO, SID, or AHS." ) ):
                return True
        else:
            tempList = []
            for items in givenList:
                if ( items[1] != "-" and items[3] == enPut ):
                    tempList.append( items )
            
            ShowLists( tempList, 1 )
        if ( ShowStatistics( givenList ) ):
            return True
    elif ( enPut == "5" ):
        print( "Enter a Zone (A/B/C/D) (x to cancel):" )
    
        enPut = input().upper()
        
        
        allowedZones = [ "A", "B", "C", "D" ]
        if enPut == 'x':
            if ( ShowStatistics( givenList ) ):
                return True
        elif not( enPut in allowedZones ):
            if ( ShowStatistics( givenList, invalidInput = True, invalidText = "Invalid Input. Zones must be A, B, C, or D." ) ):
                return True
        else:
            tempList = []
            for items in givenList:
                if ( items[11] == "ACTIVE" and items[4] == enPut ):
                    tempList.append( items )
            
            ShowLists( tempList, 1 )
        if ( ShowStatistics( givenList ) ):
            return True
    elif ( enPut == "6" ):
        tempList = []
        for items in givenList:
            if ( items[11] == "DECEASED" ):
                tempList.append( items )
        
        ShowLists( tempList, 1 )
        if ( ShowStatistics( givenList ) ):
            return True
    elif ( enPut == "x" ):
        return True
    else:
        ShowStatistics( givenList, invalidInput = True )
    
    return True



# menu interface
def Menu( invalidInput = False, invalidText = "Invalid Input" ):
    ClearConsole()
    
    if ( invalidInput ):
        print( "=============", invalidText, "=============")
    else:
        print( "\n\n\n" )
    
    print( " COVID-19 PATIENT MANAGEMENT SYSTEM \n |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" )
    print( " 1.  Add New Patient \n 2.  Change Patient Data \n 3.  Record/Update Test Details" )
    print( " 4.  Show Statistics \n 5.  Patient Data Search" )
    print( " x.  Exit \n" )
    print( " Enter a number : ")
    
    enPut = input()
    
    # check entered input
    if ( enPut == "1" ):
        currentPID = 0
        for items in ParseFile( "Data.txt" ):
            if ( int( items[0] ) > currentPID ):
                currentPID = int( items[0] )
        currentPID += 1
        
        # call ChangeDetails and add list to file
        tempList = ChangeDetails( [ currentPID, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-" ] )
        if ( tempList ):
            CreateText( "Data.txt", ParseFile( "Data.txt" ) + [ tempList ] )
            if not( Menu( invalidInput = True, invalidText = "Record successfully modified" ) ):
                return False
    elif ( enPut == "2" ):
        # search
        tempList = Search( ParseFile( "Data.txt" ) )
        
        if ( tempList ):
            # call ChangeDetails with list
            tempBigList = ParseFile( "Data.txt" )
            tempList = ChangeDetails( tempList )
            
            if ( tempList ):
                # replace list acordind to PID
                for n in range( len( tempBigList ) ):
                    if ( tempList[0] == tempBigList[n][0] ):
                        tempBigList[n] = tempList
                
                CreateText( "Data.txt", tempBigList )
                if not( Menu( invalidInput = True, invalidText = "Record successfully modified" ) ):
                    return False
        elif ( tempList == None ):
            if not( Menu( invalidInput = True, invalidText = "No Entries found for search term" ) ):
                return False
        elif ( tempList == False ):
            if not( Menu( invalidInput = True, invalidText = "Invalid search category" ) ):
                return False

    elif ( enPut == "3" ):
        # search
        tempList = Search( ParseFile( "Data.txt" ) )
        
        if ( tempList ):
            # call ChangeDetails with found list
            tempBigList = ParseFile( "Data.txt" )
            
            tempList = ChangeResults( tempList )
            
            if( tempList ):
                # replace list acordind to PID
                for n in range( len( tempBigList ) ):
                    if ( tempList[0] == tempBigList[n][0] ):
                        tempBigList[n] = tempList
                
                CreateText( "Data.txt", tempBigList )
        elif ( tempList == None ):
            if not( Menu( invalidInput = True, invalidText = "No Entries found for search term" ) ):
                return False
        elif ( tempList == False ):
            if not( Menu( invalidInput = True, invalidText = "Invalid search category" ) ):
                return False
        
    elif ( enPut == "4" ):
        ShowStatistics( ParseFile( "Data.txt" ) )
    elif ( enPut == "5" ):
        result = Search( ParseFile( "Data.txt" ) )
        
        if ( result == None ):
            if not( Menu( invalidInput = True, invalidText = "Reached end of data" ) ):
                return False
        elif ( result == False ):
            if not( Menu( invalidInput = True, invalidText = "Invalid search category" ) ):
                return False
    elif ( enPut == "x" ):
        print ("Thank you for using Management System! \n|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
        return False

    else:
        if not( Menu( invalidInput = True ) ):
            return False

    return True



# menu opens
while Menu():
    pass
