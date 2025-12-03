
![DL_Maya_Toolkit_intro-gif_v003](https://github.com/danilodelucio/DL_Maya_Toolkit/assets/47226196/adbe574b-46ce-4617-98f3-3e3fdfdbbf09)

**This tool is a collection of simple features to help 3D modellers in Maya speed up their workflows.**

___

This is a development project for the **Python Advanced** course taught by **Alexander Richter**.

I decided to create this tool for two main reasons:
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
It will highlight all the faces with more than 4 vertex (which are considered as Ngons).

> [!IMPORTANT]
> _For now, this feature does not have a progress bar, so keep in mind that this process can take some time depending on the selected 3D model, such as a dense mesh._

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
  <summary>2. Maya Setup [Option 1 - userSetup.py]</summary>
  <br>

  Copy the `userSetup.py` file and paste it into the Maya's Scripts directory (usually at `C:\Users\<username>\Documents\maya\<version>\scripts`).
  > _In case the file already exists, you can copy the entire content from one file and paste it at the end of another._

  <img width="400" alt="image" src="https://github.com/danilodelucio/DL_Maya_Toolkit/assets/47226196/9647985f-bd61-42e4-bb3b-0bf33e27f224">
<br>
<br>

  Open it with a text editor and replace the **DLMT_TOOL** path with where is located **DL_Maya_Toolkit** folder on your computer.

  > _Using a single backslash `\` can cause issues for the file path. Please use either a forward slash `/` or double backslash `\\`._
  
  <img width="659" alt="image" src="https://github.com/danilodelucio/DL_Maya_Toolkit/assets/47226196/d2ff7d3b-2261-4126-a33f-254840661aeb">
  <br>
  <br>
  
  Open Maya and you should see the **DL_Maya_Toolkit** shelf appear.
  
  <img width="757" alt="image" src="https://github.com/danilodelucio/DL_Maya_Toolkit/assets/47226196/1c77acb4-9e6e-4092-bc96-09050142ec8b">


</details>

<details>
  <summary>2. Maya Setup [Option 2 - Script Editor]</summary>
  <br>

  If you open Maya and the tool does not appear on the shelf after following the option 1 steps, it is possible that the `userSetup.py` file is being ignored by Maya.

  Copy the following code, paste it into the Script Editor and update the file path with where is located the tool.
  
  > _Using a single backslash `\` can cause issues for the file path. Please use either a forward slash `/` or double backslash `\\`._

  ```python
import sys
import importlib

app_module_path = 'put\\your\\file\\path\\here\\DL_Maya_Toolkit'
if app_module_path not in sys.path:
    sys.path.append(app_module_path)

from dlmt import dl_maya_toolkit_ui
importlib.reload(dl_maya_toolkit_ui)
ui = dl_maya_toolkit_ui.DlMayaToolkit()
ui.show()
```

<img width="800" alt="image" src="https://github.com/danilodelucio/DL_Maya_Toolkit/assets/47226196/e867425c-e9a5-4cd1-b228-307599c3737a">

<img width="350" alt="image" src="https://github.com/danilodelucio/DL_Maya_Toolkit/assets/47226196/7a1a29cb-ad12-46dd-be25-b132a027b854">

Now you should see a custom icon on your shelf and you can use it to open **DL_Maya_Toolkit**.

<img width="300" alt="image" src="https://github.com/danilodelucio/DL_Maya_Toolkit/assets/47226196/1df5a836-99da-4b6d-a405-7703ce0cbcd2">


</details>

<!-- ########################################################################## TROUBLESHOOTING ########################################################################## -->
___
# 🛠️ Troubleshooting
If you have feedback, suggestions, or feature requests, please visit the [Discussions](https://github.com/danilodelucio/DL_Maya_Toolkit/discussions) page and create a **New Discussion**.

For bugs, please go to the [Issues](https://github.com/danilodelucio/DL_Maya_Toolkit/issues) page and create a **New Issue**.

<!-- ########################################################################## SUPPORTERS ########################################################################## -->
___

# Support me! ☕

![Supporters Page](https://danilodelucio.com/wp-content/uploads/2025/12/supporter-badges.jpg)

## Enjoying this tool?
Support me with a coffee on my [Supporters](https://www.danilodelucio.com/supporters) page — get a badge and join the wall of supporters! 😎

You can also ⭐ _star this repository_ ⭐ — it helps a lot with visibility and motivates me to keep developing tools for VFX.

Sharing this project or sending me a positive message would help me in the same way.

___
Special thanks to **Luis Regalado**, **Vitor Borsato**, **Marco Antonio** and **Leticia Matsuoka** for providing suggestions for this tool.

Also, thanks to **Andrea Casati** for helping me with UI issues, **Juliana Chen** for her support and encouragement, and **Alexander Ritcher** for mentoring this awesome masterclass.

# Cheers! 🥂

