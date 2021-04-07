# Created by CircuitHawk
# Last updates 2021-04-06

import os.path
import pcbnew
import json

class SaveReferencePositionPlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Reference Position -> Save"
        self.category = "Modify PCB"
        self.description = "Save reference positions"

    def Run(self):
        board = pcbnew.GetBoard()

        refList = {}

        for module in board.GetModules():
            if module.GetReference() != "REF**":
                # Get component footprint orientation
                footprintRot = module.GetOrientation()

                # Get reference position
                refPosX = module.Reference().GetPosition()[0]
                refPosY = module.Reference().GetPosition()[1]

                # Disable "Keep Upright"
                module.Reference().SetKeepUpright(False)

                # Get reference orientation when "Keep Upright" enabled
                refRot = module.Reference().GetDrawRotation()

                if footprintRot == 0:
                    refRelRot = refRot
                else:
                    refRelRot = refRot - footprintRot

                # Enable "Keep Upright"
                module.Reference().SetKeepUpright(True)

                refList[module.GetReference()] = refPosX, refPosY, refRelRot

        # Save reference positions to file
        cwd = os.path.dirname(pcbnew.GetBoard().GetFileName())
        refPositionFile = os.path.join(cwd, 'reference-positions.json')
        json.dump(refList, open(refPositionFile,'w'))

SaveReferencePositionPlugin().register()
