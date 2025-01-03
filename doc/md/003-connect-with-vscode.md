# Connecting VSCode to your Docker container

This guide will help you set up Visual Studio Code (VSCode) to connect to your running Docker container. This will allow you to edit and execute code inside the container seamlessly.

---

## Prerequisites

Before you begin, ensure that you have:

1. **VSCode** installed on your computer.

   - Download it from [Visual Studio Code](https://code.visualstudio.com/).
   - Install the "Remote - SSH" and "Remote - Containers" extensions from the Extensions Marketplace.

2. A **running Docker container** with SSH enabled.

   - Follow the steps in the "Start the class Docker container" guide to set up and start the container.

![](p/vscode-1.png)

---

## Connect using the Remote - Containers Extension

You can use the "Remote - Containers" extension to connect directly to the running container:

1. **Attach to the container**:

   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open the command palette.
   - Type `Remote-Containers: Attach to Running Container` and select it.
   - Choose `class-container` from the list.

![](p/vscode-2.png)

A new window will pop up with a different message in the bottom left.

![](p/vscode-3.png)

2. **Open the workspace**:

   - VSCode will open a new window where you can find the container's `/workspace` directory.
   - You can now edit, debug, and execute code directly inside the container.
   - You will have to install other extensions as needed, such as the Python one and the Jupyter one.

![](p/vscode-4.png)

![](p/vscode-5.png)

---

## Test your setup

1. **Create a Python file**:

   - Inside the container, create a file named `test.py`:

     ```python
     print("Hello from Docker!")
     ```

2. **Run the file**:

   - Use the integrated terminal in VSCode to run:

     ```bash
     python3 test.py
     ```
   - Verify that the output is `Hello from Docker!`.

---

## Troubleshooting

1. **No container found**:

   - Verify the container is running using `docker ps`.

2. **VSCode cannot attach to container**:

   - Check that the "Remote - Containers" extension is installed.
   - Ensure Docker Desktop is running.

3. **Python not found**:

   - Verify Python is installed in the container:

     ```bash
     python3 --version
     ```

---

## Summary

This setup allows you to use a full-featured development environment while keeping your code and dependencies isolated in a container.

---

Previous: [Start the class Docker container](002-start-the-class-container.md)

Next: [What are SSH keys?](004-ssh-keys.md)
