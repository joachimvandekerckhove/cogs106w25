# Command Line Functions for Ubuntu

Slightly advanced use of the bash shell.

## `sudo`
Running commands with administrative privileges:

- **`sudo`**: Execute a command as the superuser.
  ```bash
  sudo command
  sudo apt update
  ```

> [!CAUTION]
> Superuser privileges are normally password protected because you can brick your system with them.

## Package Management (APT and Snap)

### APT

- **`apt update`**: Update the package list.
  ```bash
  sudo apt update
  ```
- **`apt upgrade`**: Upgrade all packages.
  ```bash
  sudo apt upgrade
  ```
- **`apt install`**: Install a package.
  ```bash
  sudo apt install package_name
  ```
- **`apt remove`**: Remove a package.
  ```bash
  sudo apt remove package_name
  ```

### Snap
- **`snap install`**: Install a Snap package.
  ```bash
  sudo snap install package_name
  ```
- **`snap remove`**: Remove a Snap package.
  ```bash
  sudo snap remove package_name
  ```
- **`snap list`**: List installed Snap packages.
  ```bash
  snap list
  ```

## Accessing Manuals and Help

- **`man` (manual):** View the manual for a command.
  ```bash
  man command_name
  ```
  Example:
  ```bash
  man ls
  ```
  Press `q` to quit the manual.

- **`--help`:** Many commands provide a quick help summary.
  ```bash
  command_name --help
  ```
  Example:
  ```bash
  ls --help
  ```
- **`info`:** Access detailed documentation for certain commands.
  ```bash
  info command_name
  ```
  Example:
  ```bash
  info coreutils
  ```

- **Searching Manuals:**
  Use `man -k` to search the manual pages for a keyword.
  ```bash
  man -k keyword
  ```
  Example:
  ```bash
  man -k copy
  ```

## Common Shortcuts for Efficiency

- **Tab Completion:** Use the `Tab` key to auto-complete file names, commands, or directories.
- **Command History:** Use the `Up` and `Down` arrow keys to browse previous commands. You can also search with `Ctrl + R` (reverse search).
- **Cancel a Command:** Press `Ctrl + C` to stop a running command.

## `alias`

The `alias` command in Linux allows you to create shortcuts for frequently used commands, making them easier and faster to type.

### Syntax
```bash
alias name='command'
```

### Example
Create a shortcut for a long command:
```bash
alias ll='ls -alF'
```
- Now, typing `ll` runs the `ls -alF` command, which lists all files in long format and classifies file types.

Create a shortcut for a command that makes me feel icky:
```bash
alias boop='touch'
```

They can get more complex
```bash
alias please='sudo $(fc -ln -1)'
```

#### Viewing Existing Aliases
To see all current aliases:
```bash
alias
```

#### Removing an Alias
To remove an alias, use the `unalias` command:
```bash
unalias name
```
Example:
```bash
unalias ll
```

#### Making Aliases Permanent
Aliases created in a terminal session are temporary. To make them permanent, add them to your shell configuration file:
- For `bash`: Add to `~/.bashrc`
- For `zsh`: Add to `~/.zshrc`

Example:
```bash
echo "alias ll='ls -alF'" >> ~/.bashrc
source ~/.bashrc
```

This ensures the alias is available every time you open a new terminal session.


## Cron
Automating tasks with `cron`:

- **`crontab -e`**: Edit the crontab file to schedule tasks.
  ```bash
  # Example crontab entry
  0 5 * * * /path/to/script.sh  # Run daily at 5 AM
  ```
- **`crontab -l`**: List current cron jobs.
  ```bash
  crontab -l
  ```

## SSH
Securely connecting to remote machines:

- **`ssh`**: Open an SSH session.
  ```bash
  ssh user@hostname_or_IP
  ```
- **`scp`**: Copy files over SSH.
  ```bash
  scp file.txt user@hostname:/remote/path/
  ```

## Git
Version control and collaboration:

- **`git clone`**: Clone a repository.
  ```bash
  git clone https://github.com/user/repository.git
  ```
- **`git add`**: Stage changes.
  ```bash
  git add file.txt
  ```
- **`git commit`**: Commit staged changes.
  ```bash
  git commit -m "Descriptive message"
  ```
- **`git push`**: Push changes to a remote repository.
  ```bash
  git push origin branch_name
  ```
- **`git pull`**: Pull updates from a remote repository.
  ```bash
  git pull origin branch_name
  ```
- **`git status`**: Check the status of the repository.
  ```bash
  git status
