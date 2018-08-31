#!/usr/bin/env python
import sys

template="""# https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile
from CRABClient.UserUtilities import config, getUsernameFromSiteDB

pd="$pd$"
version=$v$
era="$era$"
jsonurl="$jsonurl$"
tag="$tag$"

config = config()
config.General.requestName = 'DQM_{}_hlt-{}_{}-v{}'.format(pd, tag, era, version)
config.General.workArea = "crab_workspaces"
config.General.transferOutputs = True
config.General.transferLogs = False
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'dqm_step1.py'
config.JobType.maxJobRuntimeMin = 1379 #minutes
config.Data.inputDataset = '/{}/Run{}-PromptReco-v{}/AOD'.format(pd, era, version) 
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 130
config.Data.lumiMask=jsonurl
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = "hlt-{}_{}-v{}".format(tag, era, version)
config.Site.storageSite = 'T2_TR_METU'
"""

parts = ["v1x_2018A-v1", "v20_2018A-v1", "v20_2018A-v2", "v21_2018A-v2", "v21_2018A-v3", "v21_2018B-v1", "v22_2018B-v1", "v22_2018B-v2", "v22_2018C-v1", "v22_2018C-v2", "v30_2018C-v2", "v30_2018C-v3", "v31_2018C-v3" ]
datasets=["EGamma", "JetHT", "MET", "SingleMuon"]
#datasets=["MET"]

for dst in datasets:    
    for part in parts:
        hltv=part[:3]
        era=part[4:9]
        # erav = era[]
        pdver=part[-1]
        #print part, hltv, era, pdver
        jsonfname="mycert_hlt-{}_{}-v{}_JSON.txt".format(hltv, era, pdver)
        crabfname="crab_{}_hlt-{}_{}-v{}.py".format(dst, hltv, era, pdver)
        print(crabfname)
        # continue
        cfgtext=template.replace("$pd$", dst)
        cfgtext=cfgtext.replace("$v$", pdver)
        cfgtext=cfgtext.replace("$era$", era)
        cfgtext=cfgtext.replace("$jsonurl$", jsonfname)
        cfgtext=cfgtext.replace("$tag$", hltv+'_noEleRelIso')
        with open(crabfname, "w") as f:
            f.write(cfgtext)

