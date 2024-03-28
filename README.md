# ui-automation-testing

## Setup runtime environment
1. Install Python  
    supports Python 3.11.5
2. Install dependencies  
    After the python installed, please install dependencies by command:  
    ```
    pip install -r <project_folder>/requirements.txt
   ```
    
    *Tips: If there are multiple versions on your jump host, please make sure dependencies are installed with the version you used.  
    For example, your jump host configured as below:*
    ``` 
    root@jumphost01:~# python --version
    Python 3.6.8
    root@jumphost01:~# python3 --version
    Python 3.7.2
    ```
    *Please install dependencies and run scrips by commands:*
    ```
    python3 -m pip install -r <project_folder>/requirements.txt
    python3 <project_folder>/main.py
    ```
 
 3. Download code  
    Download a copy or git clone the source code to your local directory.
    
 4. Download webdriver   
    Webdriver is required since the script is based on selenium. Chrome and Firefox are supported now. Please download it according to your browser type and version.   
    [Chrome Webdriver](https://chromedriver.chromium.org/downloads) | [Firefox Webdriver](https://github.com/mozilla/geckodriver/releases)  
    *Tips: Place the webdriver in your project root folder please, or you need to specify its path in config.yaml*

## Configure testbed info
Please fill in your testbed info in <project_folder>/settings/config.yaml
 
## Update test data
Test data is configured in file '<project_folder>/tests/data.yaml'  
Please update the value according to your requirements.

## Add cases to test suite
Test suite is defined in file '<project_folder>/main.py'.  
Because the testing objects are related, strongly recommend keeping the case order and running related cases together.  

## Run cases
Run script '<project_folder>/main.py' using the command-line or other python IDE.  
The framework is based on unittest, please refer to official document for updating it if you want.

## Test report
Report file location and filename are configured in <project_folder>/settings/config.yaml.  
*Tips: It will be overwritten if the setting is not updated, please take a copy manually if you need.*
