# What are SSH keys?

In the physical world, we keep things secure by using locks that are opened by keys.  In cyberspace, we secure things by _SSH keypairs_ that work the same way.  A keypair consists of two files:
1. **A public key** – This is like the lock on the box. You can share this lock with anyone because they can’t open the box with just the lock.
2. **A private key** – This is your key that opens the lock. You keep it secret and safe.

When working with GitHub (or any similar service), **SSH keys** work as follows:
- Your **public key** is uploaded to GitHub.
- Your **private key** stays on your computer or container.
- When you try to connect to GitHub using your account, it will present you with a challenge that is encrypted using the public key. Your computer will then decrypt this using the private key, and GitHub will check if the challenge matches before you’re allowed in.

SSH keys are both secure and convenient -- no need to enter a password every time you connect.

---

# Why use SSH keys with Docker and GitHub?

To access GitHub from inside a **Docker container** you need to set up SSH keys so the container can communicate securely with GitHub.

By storing your keys in a **persistent volume**, you can avoid regenerating keys every time you start the container.

This builds on your understanding of connecting VSCode to containers ([003-connect-with-vscode](003-connect-with-vscode.md)) and starting your class container ([002-start-the-class-container](002-start-the-class-container.md)).

---

# Installing an SSH keypair in a Docker container with a persistent volume

Here’s a step-by-step guide:

## 1. Set up a persistent volume for keys

When creating your container, make sure to add a volume -- a shared folder between the container and your computer.  In our [original docker setup](002-start-the-class-container.md), we called it `/workspace`. This directory can store SSH keys persistently.

---

## 2. Generate SSH keys inside the Docker container

1. Start your Docker container and mount the persistent volume.

2. Inside the container, generate a new SSH keypair:
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com" -f /workspace/id_ed25519
   ```
   - **Options explained:**
     - `-t ed25519` specifies the key type.
     - `-C "your_email@example.com"` adds a comment for identification.
     - `-f /workspace/id_ed25519` saves the keypair in the mounted folder for persistence.

3. The command creates two files in `/workspace`:
   - `id_ed25519` (private key)
   - `id_ed25519.pub` (public key)

4. Print the public key:
   ```bash
   cat /workspace/id_ed25519.pub
   ```
   Copy the output.

---

## 3. Add the public key to GitHub

1. Go to [GitHub SSH settings](https://github.com/settings/keys).
2. Click **New SSH Key**.
3. Paste the public key you copied and save it.
    - Make sure you don't copy line breaks.

---

## 4. Configure the Docker container to use the key

1. Link the private key to the SSH directory:
   ```bash
   mkdir -p ~/.ssh
   cp /workspace/id_ed25519 ~/.ssh/id_ed25519
   chmod 600 ~/.ssh/id_ed25519
   ```

2. Add GitHub’s public keys (for verification):
   ```bash
   ssh-keyscan github.com >> ~/.ssh/known_hosts
   ```

---

## 5. Test the connection

Inside the container, test the SSH connection:
```bash
ssh -T git@github.com
```
If it works, you’ll see a message like:
```
Hi username! You've successfully authenticated.
```

---

# Summary

By generating SSH keys inside the Docker container and saving them in a persistent volume:
- You’ve enabled secure access to GitHub without needing passwords.
- The keys are saved outside the container, so they remain available even if the container is restarted or recreated.
- You’re now set up to clone, pull, and push repositories from inside the Docker container.

Feel free to refer back to your knowledge of containerization from the introductory guide ([001-introduction-to-containerization](001-introduction-to-containerization.md)) and VSCode setup to enhance this workflow ([003-connect-with-vscode](003-connect-with-vscode.md)).

---

Previous: [Connecting VSCode to your Docker container](003-connect-with-vscode.md)
