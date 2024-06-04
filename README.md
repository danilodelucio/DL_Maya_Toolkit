![dl_maya_toolkit_cover01](https://github.com/danilodelucio/DL_Maya_Toolkit/assets/47226196/f2735ce1-4612-43d9-890f-d11d19297d84)

**This tool is a collection of simple features to help Maya users speed up their workflows.**

___

This is a development project for the **Python Advanced** course taught by **Alexander Richter**.

I decided to create it for two main reasons:
- To become familiar with Maya's API;
- To develop simple automated tasks based on suggestions from Maya users;

<img width="480" alt="dlmt_app1" src="https://github.com/danilodelucio/DL_Maya_Toolkit/assets/47226196/1caa1769-7428-4183-b34d-93d2a4a122fc">

Features:
- Duplicate Faces;
- Extract Faces;
- Combine Objects;
- Separate Objects;
- Outliner Renamer;
- Check Ngons;

<!-- ########################################################################## DUPLICATE/EXTRACT FACES | COMBINE/SEPARATE OBJECTS ########################################################################## -->
___
  # :ice_cube: Duplicate/Extract Faces | Combine/Separate Objects
  These features are similar to the default ones in Maya, with a few differences:
  - No history;
  - Moving the 3D Pivot to the center of the object/face;

<img width="400" alt="image" src="https://github.com/danilodelucio/DL_Maya_Toolkit/assets/47226196/abddf431-4e30-4fdb-83b4-c3ee728085cc">

<!-- ########################################################################## OUTLINER RENAMER ########################################################################## -->
___
# :memo: Outliner Renamer
This feature allows you to rename multiple selected items in the **Outliner** panel.
Optionally, you can add padding by using "#", which will be replaced by sequence numbers.
> The increment value will be used if the padding is provided.

<img width="942" alt="image" src="https://github.com/danilodelucio/DL_Maya_Toolkit/assets/47226196/d683ea2d-74e9-4e02-8c30-3808f610de68">

<img width="500" alt="image" src="https://github.com/danilodelucio/DL_Maya_Toolkit/assets/47226196/288b9e1a-30e2-4a40-918d-b3d2cb830e3e">

<!-- ########################################################################## CHECK NGONS ########################################################################## -->
___
# :white_check_mark: Check Ngons
It will highlight all the Ngons if they were found.
> [!IMPORTANT]
> For now, this feature does not have a progress bar, so keep in mind that this process can take some time depending on the selected 3D model, such as a dense mesh.

<img width="400" alt="image" src="https://github.com/danilodelucio/DL_Maya_Toolkit/assets/47226196/cbe9ae38-b79d-4bb7-99a0-d62c3ea6a797">

<img width="700" alt="image" src="https://github.com/danilodelucio/DL_Maya_Toolkit/assets/47226196/12e4b002-82eb-4e04-864b-090b6dbeda74">

<!-- ########################################################################## HOW TO INSTALL ########################################################################## -->
___
# ⚙️ How to Install

<details>
  <summary>1. Downloading the tool</summary>
  <br>
  
At the top of this page, click on the green button and download the **zip** file.
<br>
  
<img width="400" alt="dlmt-github-download" src="https://github.com/danilodelucio/DL_Maya_Toolkit/assets/47226196/1e959bd7-21c0-4a1b-a164-4aab4b9bf7e5">
<br>
  
Save it anywhere on your computer, then extract its content. For better convenience, I suggest renaming the folder by removing the "**-master**" from the filename.

<br>
<img width="300" alt="dlmt extracting zip" src="https://github.com/danilodelucio/DL_Maya_Toolkit/assets/47226196/0cfbf992-0246-45f5-8640-be45562f114a">
<img width="150" alt="dlmt extracting zip2" src="https://github.com/danilodelucio/DL_Maya_Toolkit/assets/47226196/9bf69a05-220a-46f4-92c9-b6f95bf97552">

</details>

<details>
  <summary>2. Maya Setup</summary>
  <br>
  
  From the image below, follow the following steps (you will only need to do this process once):

  1. Open the Script Editor;
  2. Open a Python tab;
  3. Copy/Paste the code below and replace the file path with where is located **DL_Maya_Toolkit** folder on your computer;
  4. Save it to your Shelf;

<img width="882" alt="dlmt-shelf-maya" src="https://github.com/danilodelucio/DL_Maya_Toolkit/assets/47226196/3c3b8cbb-e6d2-436e-869a-552acda24c28">

```python
import sys
import importlib

app_module_path = 'D:\\your\\path\\here\\DL_Maya_Toolkit'
if app_module_path not in sys.path:
    sys.path.append(app_module_path)

from dlmt import dl_maya_toolkit_ui
importlib.reload(dl_maya_toolkit_ui)
ui = dl_maya_toolkit_ui.DlMayaToolkit()
ui.show()
```
> Using a single backslash `\` can cause issues for the file path. Please use either a forward slash `/` or double backslash `\\`.

</details>


<!-- ########################################################################## TROUBLESHOOTING ########################################################################## -->
___
# 🛠️ Troubleshooting
![I can fix it, if I dont know it is broken](https://github.com/danilodelucio/DL_Maya_Toolkit/assets/47226196/db7fdbbc-4327-4be7-9dae-124baf40f892)

If you have feedback, suggestions, or feature requests, please visit the [Discussions](https://github.com/danilodelucio/DL_Maya_Toolkit/discussions) page and create a **New Discussion**.

For bugs, please go to the [Issues](https://github.com/danilodelucio/DL_Maya_Toolkit/issues) page and create a **New Issue**.

<!-- ########################################################################## SUPPORT ME ########################################################################## -->
___
# 🥺 Support me
![image](https://github.com/danilodelucio/DL_Maya_Toolkit/assets/47226196/a7f890f4-05e6-4f28-ab11-2ce42651075e)

This project required significant time and extra hours of hard work to make it available to everyone.

If you find this tool useful, please consider supporting me on [Buy Me A Coffee](https://buymeacoffee.com/danilodelucio). ☕

You can also share this tool or send me a positive message, it would help me in the same way.

___
Special thanks to **Luis Regalado**, **Vitor Borsato**, **Marco Antonio** and **Leticia Matsuoka** for providing suggestions for this tool.

Also, thanks to **Andrea Casati** for helping me with UI issues, and **Juliana Chen** for her support and encouragement.

# Cheers! 🥂
