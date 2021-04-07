# Created by CircuitHawk
# Last updates 2021-04-06

import os.path
import pcbnew
import json

class RestoreReferencePositionPlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Reference Position -> Restore"
        self.category = "Modify PCB"
        self.description = "Restore reference positions"

    def Run(self):
        board = pcbnew.GetBoard()

        # Restore reference positions from file
        cwd = os.path.dirname(pcbnew.GetBoard().GetFileName())
        refPositionFile = os.path.join(cwd, 'reference-positions.json')
        refList = json.load(open(refPositionFile))

        for module in board.GetModules():
            if module.GetReference() != "REF**" and module.GetReference() in refList.keys():
                module.Reference().SetKeepUpright(False)
                refPosX, refPosY, refRot = refList[module.GetReference()]
                refPos = pcbnew.wxPoint(refPosX, refPosY)
                module.Reference().SetPosition(refPos)
                module.Reference().SetTextAngle(refRot)
                module.Reference().SetKeepUpright(True)

RestoreReferencePositionPlugin().register()
