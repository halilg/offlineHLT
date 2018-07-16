checkGridProxy() {
    temp=$(voms-proxy-info --all)
    if [[ $? -ne 0 ]]; then
       voms-proxy-init --voms cms --valid 168:00
       if [[ $? -ne 0 ]]; then
           exit
       fi
    fi
}

checkCMSEnvironment() {
    temp=$(which cmsRun)
    if [[ $? -ne 0 ]]; then
       echo 'cmsRun not in path. Forgot to cmsenv?'
       exit
    fi
}
