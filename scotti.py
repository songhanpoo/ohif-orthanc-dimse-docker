import json
import orthanc

def OnChange(changeType, level, resource):
    if changeType == orthanc.ChangeType.ORTHANC_STARTED:
        print('Started')
        mwlquery = dict()
        mwlquery["AccessionNumber"] = '00007'
        MWL = orthanc.RestApiPost('/modalities/PACS1/find-worklist', json.dumps(mwlquery))
        print(MWL)

orthanc.RegisterOnChangeCallback(OnChange)
