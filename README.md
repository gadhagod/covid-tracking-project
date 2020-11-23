# covid-tracking-project
![](https://img.shields.io/pypi/v/covid-tracking-project?color=dark%20green) \
A python wrapper for the Covid Tracking Project API.

### Installation

    pip3 install covid-tracking-project

### Importing

    import ctp

### Functions

- **Class**: `us()`
    - **Function**: `history()`
        - Description: Get US historical data
        - Parameters: 
            - day (description: Get data on a specific day, type: string/int, requirement: optional, defaults: all days, example: `20200501`)
    - **Function**: `current()`
        - Description: Get current US data
- **Class**: `states()`
    - **Function**: `metadata()`
        - Description: Get state metadata
        - Parameters:
            - state (description: Get data on a specific state, type: string, requirement: optional, default: all states, example: `ca`)
    - **Function**: `history()`    
        - Description: Get state historical data
        - Parameters:
            - day (description: Get data on a specific day, type: string/int, requirement: optional, defaults: all days, example: `20200501`)
            - state (description: Get data on a specific state, type: string, requirement: optional, default: all states, example: `ca`)
    - **Function**: `current()`
        - Description: Get state current data
        - Parameters:
            - state (description: Get data on a specific state, type: string, requirement: optional, default: all states, example: `ca`)