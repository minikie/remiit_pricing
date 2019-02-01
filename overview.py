import xenarix as xen
import xenarix.results as xen_r

import model_generate as mg

scenSetID='scenSet1'
scenID='scenID'
resultID='resultID'

mg.generate(scenSetID=scenSetID,
            scenID=scenID,
            resultID=resultID)

result = xen_r.ResultObj(scenSetID, scenID, resultID)

multipath = result.get_multipath(scen_count=1)

calculated_result = []

for t, v in result.timegrid, multipath:

    v[0]
    calculated_result.append([])



