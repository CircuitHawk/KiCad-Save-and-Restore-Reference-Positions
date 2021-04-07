# KiCad-Save-and-Restore-Reference-Positions
Save/Restore reference designator position and orientations in KiCad

For those that modify library symbols and footprints often, pulling a new netlist file into a board layout can result in reference designators resetting to their default positions. This simple plugin allows a user to save and restore all reference designators positions and orientations. 

To install the plugin download the two Python files and place in the KiCad plugins directory (e.g., on Windows C:\Program Files\KiCad\share\kicad\scripting\plugins). Restart KiCad and you're good to go.

Quick usage guide:

Starting with our target design, let's save the reference positions:

![Imgur Image](https://i.imgur.com/vzvGiUN.png)

This creates "reference-positions.json" in the KiCad project directory. The JSON file stores the position of each valid reference designator and orientation:

![Imgur Image](https://i.imgur.com/tfv1w0H.png[/img])

After pulling changes into the board layout some reference designators are relocated. Let's restore the positions/orientations from the previously saved states:

![Imgur Image](https://i.imgur.com/lde66Dl.png[/img])

You can see the designators are back to their saved positions:

![Imgur Image](https://i.imgur.com/vzvGiUN.png[/img])
