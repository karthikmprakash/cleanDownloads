# Clean Downloads Folder

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/karthikmprakash/cleanDownloads">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Folder Automation - Auto Sorting</h3>

  <p align="center">
    Easy auto sorting any cluttered folder into descrete categories 
    <br />
    <a href="https://github.com/karthikmprakash/cleanDownloads/issues">Report Bug</a>
    ·
    <a href="https://github.com/karthikmprakash/cleanDownloads/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


We have all been through the most tiring and boring work looking for one important document through cluttered desktop or downloads folder! 
Yes, it can be partially if not fully solved by sorting the files into specific folder depending on the file extensions. But again, who has the time to sort stuff! Automation can help us here

Here's how:
* Python comes in for the rescue with its immense versatility and ease of use!
* Lets have a watchdog who waits for any changes in the target folder 
* Lets make a list of extensions we already know about and the designated folder it should end up in
* Loop through the files and move them with the `move` command of `shutil` library
* `pyinstaller` is used to create an executable to run the script without having to install any other dependancies 

A list of commonly used resources that I find helpful are listed in the acknowledgements.

### Built With

This section should list any major modules that is used in this project.
* [os](https://docs.python.org/3/library/os.html)
* [watchdog](https://pypi.org/project/watchdog/)
* [pyinstaller](https://pyinstaller.readthedocs.io/en/stable/)
* [shutil](https://docs.python.org/3/library/shutil.html)


<!-- GETTING STARTED -->
## Getting Started

If you want to test it out locally on your machine. Follow these steps below

### Prerequisites

Windows Machine : The code is written for windows machine. You can customize it by changing the directory path as required

### Installation

1.  Clone the repo
   ```sh
   git clone https://github.com/karthikmprakash/cleanDownloads.git
   ```
2. If you want to Install the executable
   ```sh
   cd cleanDownloads\build
   main.exe
   ```
3. Install all packages
   ```sh
   pip install -r requirements.txt
   ```
4. Check if your user directory name is same as your user name
   ```python
   import os
   os.getlogin()
   ```
5. To convert the python package into a executable 
  ```sh
  pip install pyinstaller
  pyinstaller --onefile -w your_python_file.py
  ```
  The ```--onefile``` bundles up everything into one file to be executed. ``` -w ``` is used to when your program does not require command prompt for execution


<!-- USAGE EXAMPLES -->
## Usage

The project can be reprogrammed to ones requirements, you can set up a routine or any action trigger like environment. for ex: 
* Rename files in a folder with a predefined structure. 
* For photographers, create folders automatically when you import photos into the coomputer.  



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/karthikmprakash/cleanDownloads/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Open! 



<!-- CONTACT -->
## Contact

Your Name - Karthik M Prakash [@karthikmprakash](https://twitter.com/your_username) - mkarthikprakash.work@gmail.com

Project Link: [https://github.com/karthikmprakash/cleanDownloads](https://github.com/karthikmprakash/cleanDownloads)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [File and Directory exisits](https://stackoverflow.com/questions/45113304/if-file-and-directory-exists)
* [To get current Windows User Name](https://stackoverflow.com/questions/13654122/how-to-make-python-get-the-username-in-windows-and-then-implement-it-in-a-script)
* [Watchdog integration](https://stackoverflow.com/questions/23479511/running-a-python-script-when-a-new-file-is-created)
* [code to cactegorize and move files](https://medium.com/swlh/automation-python-organizing-files-5d2b6b933402)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/karthikmprakash/cleanDownloads/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/karthikmprakash/cleanDownloads/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/karthikmprakash/cleanDownloads/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/karthikmprakash/cleanDownloads/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/karthikmprakash/cleanDownloads/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
