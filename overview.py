import  xenarix as xen
import model_generate as mg

scenSetID='scenSet1'
scenID='scenID'
resultID='resultID'

mg.generate(scenSet=scenSetID,
            scen=scenID,
            result=resultID)

result = xen.ResultObj()

result_multipath = result.get_multipath(scen_count=1)

calculated_result = []

for t, v in result.timegrid, result_multipath:

    v[0]
    calculated_result.append([])



