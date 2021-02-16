# Python Datascience Template

## Template Setup
1. Clone this template via 
```
git clone <RepoUrl> <YOUR_PROJECT_NAME>
```
2. Navigate into the just cloned project via
```
cd <YOUR_PROJECT_NAME>
```
3. Run main.py stepwise and familiarise yourself with features provided by this template: 
   - Config Setup
   - Logging Setup 
   - Debug_toggle
    
## Configuration Parameters
- **project_name**: The name of the Project
- **logging_dir**: The path to the logging directory. If an relative path is provided it is assumed to be relative to the project directory. - logging_info_name: null 
- **logging_info_name**: The file name of the "info" logs, i.e. a file into which logs of all log levels are written
- **logging_error_name**: The name of the "error" logs, i.e a file into which logs equal or above the warning log level are written
- **logging_file_mode**: Either "a" (Append to log file) or "w" (Overwrite existing log file)
- **debug_default**: Boolean value that set the initial DEBUG variable setting
     
