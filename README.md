# Chess Tournament Manager

## Description

The Chess Tournament Manager is a Python-based application that helps manage chess tournaments. It allows users to create tournaments, add players, manage rounds and matches, and archive tournament and player data. The project follows an MVC (Model-View-Controller) architecture to separate business logic, data presentation, and user interaction control.

## Features

- **Create a Tournament**: Initialize a new tournament with a name, location, date, and description.
- **Add Players**: Add players to the ongoing tournament or archive them if no tournament is in progress.
- **Manage Matches**: Generate matches for each round, record match results, and update player scores.
- **Load a Tournament**: Load an unfinished tournament from the archive to resume it.
- **Display Archived Data**: View archived players and tournaments, as well as details of players and rounds for a specific tournament.
- **Update Player's National Chess ID**: Modify the national chess ID of an archived player.

## Installation

### Prerequisites

- Python 3.x must be installed on your machine.

### Installation Steps

1. Clone the GitHub repository:

    ```bash
    git clone https://github.com/your-username/chess-tournament-manager.git
    cd chess-tournament-manager
    ```

2. (Optional) Create a virtual environment for the project:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies (if any):

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:

    ```bash
    python controller.py
    ```

2. Follow the on-screen instructions to navigate through the menu options.

3. You can create new tournaments, add players, start and manage tournaments, and view or modify archived data.

## Project Structure

- **models/**: Contains the data models for the tournament, player, turn, and match.
- **views/**: Contains the view classes that handle user interaction and data presentation.
- **controller.py**: The main controller that ties together the models and views to manage the application's workflow.
- **README.md**: This file.

## Running Code Quality Checks with Flake8

To maintain code quality and adhere to PEP 8 standards, you can generate a Flake8 report for the project. Flake8 is a tool for checking the style guide enforcement of your Python code.

### Steps to Generate a Flake8 Report:

1. Install Flake8 if you haven't already:

    ```bash
    pip install flake8
    ```

2. Navigate to the project directory where `controller.py` is located.

3. Run the following command to generate a Flake8 report, with a maximum line length of 119 characters, and save the output to a file:

    ```bash
    flake8 --max-line-length=119 controller.py --output-file=flake8_report_file_name.txt
    ```

4. The report will be saved in `flake8_report_controller.txt`, detailing any style violations found in `controller.py`.

You can repeat this process for other files in the project by replacing `controller.py` with the desired file name.

## Saving and Loading Data

- Tournaments and players are saved in JSON format to files named `archived_tournaments.json` and `archived_players.json` respectively.
- When a tournament is created or a player is added, their data is automatically saved to these files.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request with your changes.

## License

This project is free of any kind of licence.

## Acknowledgments

Thanks to all contributors and anyone who provided feedback or assistance in the development of this project.