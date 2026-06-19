class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)

        return list(groups.values())
        
        
        
        """
        checkHash = {x: False for x in strs}
        valids = []
        charCount1 = {}    
        charCount2 = {}
        #print(checkHash)
        for fromCheck in strs:
            
            if checkHash[fromCheck] == False:
                tempStoreArray = [fromCheck]
            charCount1 = {char: fromCheck.count(char) for char in set(fromCheck)}
            checkHash[fromCheck] = True
            #  Made Hashmap of item and Made it True so that it is not checked further in the process

            for toCheck in strs:
                #if checkHash[toCheck] == True :
                    #print("Checked", fromCheck, toCheck)
                    #print(" ")
                if checkHash[toCheck] == False :
                    charCount2 = {char: toCheck.count(char) for char in set(toCheck)}
                    if charCount1 == charCount2:
                        tempStoreArray.append(toCheck)
                        checkHash[toCheck] = True
                        #print("CheckHash at INSIDE IF For ", fromCheck, checkHash)
                        #print("")
                        #print("TEMP ARRAY AT ",fromCheck, toCheck, tempStoreArray)

            if len(tempStoreArray) != 0:
                valids.append(tempStoreArray)
            tempStoreArray = []

        return valids
        """

