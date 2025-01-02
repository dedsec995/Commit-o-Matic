# Commit-o-Matic

Commit-o-Matic is an automated script that updates a counter stored in a text file and commits the changes to a GitHub repository. It is designed to display the power of cron jobs, clever python scripting and how to rules the machines (be lazy :P).

---

## A Personal Note

When everyone was making their New Year’s resolutions, I decided that I wanted to achieve an entirely green commit history this year. So, I created this fun little project, Commit-o-Matic, to ensure I have a daily commit for every single day of the year. Join me in the fun, and let’s make GitHub greener together!

---

## Requirements# Commit-o-Matic

Linux or macOS (Only powerful Doors, No Windows)

- Python 3.x
- Git
- SSH or Personal Access Token for GitHub authentication

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone git@github.com:dedsec995/Commit-o-Matic.git
   cd Commit-o-Matic
   ```
2. **Set Up Git Authentication:**

   - **Option 1: SSH (Recommended)**
     - [Generate and add an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).
   - **Option 2: HTTPS with Personal Access Token**
     - [Generate a personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).

3. **Create the Counter File:**
   Ensure there’s a `counter.txt` file in the project directory. The script will create it automatically if it doesn’t exist.

4. **Test the Script:**

   ```bash
   python3 auto_commit.py
   ```

---

## Usage

### Manual Execution

Run the Python script manually to update the counter and commit changes:

```bash
python3 auto_commit.py
```

### Automate with Cron Job

1. Open the crontab editor:

   ```bash
   crontab -e
   ```

2. Add the following line to schedule the script to run every 5 minutes:

   ```bash
   */5 * * * * /usr/bin/python3 /path/to/auto_commit.py >> /path/to/logfile.log 2>&1
   ```

   Replace `/path/to/auto_commit.py` and `/path/to/logfile.log` with the absolute paths.

3. Save and exit. The script will now run automatically as per the schedule.

---

## How It Works

1. The script reads the current value from `counter.txt`.

2. Increments the counter by 1.

3. Writes the new value back to the file.

4. Commits the change to the GitHub repository with a commit message:

   ```
   Auto-update counter to <counter> at <timestamp>
   ```

5. Pushes the changes to the repository.

---

## Forking and Setting Up Your Own Commit-o-Matic

Want to create your own Commit-o-Matic? Here’s how:

1. **Fork the Repository:**

   - Go to the [Commit-o-Matic GitHub repository](https://github.com/dedsec995/Commit-o-Matic).
   - Click the **Fork** button in the top-right corner to create your own copy of the repository.

2. **Clone Your Fork:**

   ```bash
   git clone git@github.com:dedsec995/commit-o-matic.git
   cd Commit-o-Matic
   ```

3. **Set Up Authentication:**

   - Follow the instructions in the [Set Up Git Authentication](#set-up-git-authentication) section.

4. **Customize Your Repository:**

   - Update the script or counter file as needed.
   - Modify the cron job schedule if desired.

5. **Start Committing:**

   - Run the script manually or set up a cron job to automate your commits. Enjoy watching your green GitHub contribution graph fill up!

---

## Example Output

### `counter.txt`

```
42
```

### Commit Message

```
Auto-update counter to 42 at 2025-01-02 14:30:15
```

---

## Contribution

Feel free to fork this repository and submit pull requests for improvements or additional features.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For any questions or issues, feel free to reach out:

- GitHub: [dedsec995](https://github.com/dedsec995)
- Email: [amitluhar49@gmail.com](mailto\:amitluhar49@gmail.com)
