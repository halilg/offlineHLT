#!/usr/bin/env python3
import sys 
import json

#### Script configuration ########################################

jsonfile="Cert_314472-317591_13TeV_PromptReco_Collisions18_JSON.txt"
fnameTemplate = "mycert_hlt-{}_JSON.txt" 

#eras=["A", "B"]

# Bunlar datasetler
runlimits=["A_1", "A_2", "A_3", "B_1", "B_2", "C_1", "C_2", "C_3"]

runlimit={ "A_1":[315252, 316238],
           "A_2":[316239, 316568],
           "A_3":[316569, 317079],
           "B_1":[317080, 318069],
           "B_2":[318070, 319336],
           "C_1":[319337, 319446],
           "C_2":[319447, 319832],
           "C_3":[319833, 320393],
           "D_2":[320497, 322407],
         }

menus=["v1x", "v20", "v21", "v22", "v30", "v31", "v33", "v34"]

menulimit = { "v1x":[315252, 315973],
              "v20":[315974, 316271],
              "v21":[316361, 317488],
              "v22":[317509, 319579],
              "v30":[319527, 319912],
              "v31":[319913, 320065],
              "v33":[320500, 321396],
              "v34":[321397, 321990],
            }

parts = {  "v1x_2018A-v1" : [315252, 315973],
           "v20_2018A-v1" : [315974, 316238],
           "v20_2018A-v2" : [316239, 316271],
           "v21_2018A-v2" : [316361, 316568],
           "v21_2018A-v3" : [316569, 317079],
           "v21_2018B-v1" : [317080, 317488],
           "v22_2018B-v1" : [317509, 318069],
           "v22_2018B-v2" : [318070, 319336],
           "v22_2018C-v1" : [319337, 319446],
           "v22_2018C-v2" : [319447, 319579],
           "v30_2018C-v2" : [319527, 319832],
           "v30_2018C-v3" : [319833, 319912],
           "v31_2018C-v3" : [319913, 320065],
           "v33_2018D-v2" : [320500, 321396],
           "v34_2018D-v2" : [321397, 321990],        
        }



#####################################################################

def newJson(_jsondata, runs):
    jsonkeys = [int(x) for x in _jsondata]
    jsonkeys = sorted(jsonkeys)
    # print (jsonkeys, runs)
    runmin=runs[0]
    runmax=runs[1]
    outjson={}
    for key in jsonkeys:
        if key >= runmin and key <= runmax:
            outjson[str(key)]=_jsondata[str(key)]
    return outjson
try:
    with open(jsonfile) as f:
        jsondata = json.load(f)
except FileNotFoundError:
    print("JSON file not found:", jsonfile)
    sys.exit()

for jobname in parts:
    print (jobname)
    myjson = newJson(jsondata, parts[jobname])
    with open(fnameTemplate.format(jobname), "w") as f:
        f.write(json.dumps(myjson))
