# Getting Started with AI Coding Tools

A step-by-step guide for people who have never used a terminal or coding tools before. You do not need to be a developer to follow this guide.

---

## What you will set up

By the end of this guide you will have an AI coding assistant running on your computer that can coach you through startup exercises, generate documents, and challenge your thinking. Think of it as a very smart, very direct co-founder who lives in your terminal.

---

## Step 0: Understand the basics

**What is a terminal?**
A terminal (also called command line or shell) is a text-based way to talk to your computer. Instead of clicking buttons, you type commands. It looks like a black or white window with text. Every Mac and Windows computer has one built in.

- **Mac:** Open the app called "Terminal" (search for it in Spotlight with Cmd + Space)
- **Windows:** Open "PowerShell" (search for it in the Start menu)

**What is a repository (repo)?**
A repository is a folder of files stored on GitHub (a website for sharing code). You will download ("clone") this folder to your computer so the AI can read the files inside it.

**What is an API key?**
An API key is like a password that lets software use an online service. You will need one to use Claude (the AI). It costs money based on usage, but a typical workshop session costs less than USD 1.

---

## Step 1: Install Node.js

Node.js is a tool that many coding applications need to run. You only need to install it once.

1. Go to [nodejs.org](https://nodejs.org/)
2. Click the big green button that says **LTS** (Long Term Support)
3. Run the installer that downloads. Click "Next" through all the steps. Accept the defaults.
4. To check it worked, open your terminal and type:
   ```
   node --version
   ```
   You should see a version number like `v20.x.x` or `v22.x.x`. If you see an error, restart your terminal and try again.

---

## Step 2: Install Git

Git is the tool that downloads repositories from GitHub.

**Mac:** Git is usually pre-installed. To check, type this in your terminal:
```
git --version
```
If you see a version number, you are good. If not, your Mac will prompt you to install developer tools. Click "Install" and wait.

**Windows:** Download Git from [git-scm.com](https://git-scm.com/downloads). Run the installer with all default settings.

---

## Step 3: Get an Anthropic API key

This is the key that lets you use Claude, the AI that powers the coaching experience.

1. Go to [console.anthropic.com](https://console.anthropic.com/)
2. Create an account (email and password)
3. Add a payment method (Settings > Billing). You will only be charged for what you use. A workshop session typically costs USD 0.50-2.00.
4. Go to **API Keys** and click **Create Key**
5. Give it a name like "hub201-workshop"
6. Copy the key. It starts with `sk-ant-`. **Save it somewhere safe. You will not be able to see it again.**

Now set the key in your terminal so Claude Code can use it:

**Mac:**
```
export ANTHROPIC_API_KEY=sk-ant-your-key-here
```

**Windows (PowerShell):**
```
$env:ANTHROPIC_API_KEY="sk-ant-your-key-here"
```

Note: This only lasts for the current terminal session. If you close and reopen your terminal, you will need to set it again. To make it permanent:

**Mac:** Add the export line to your `~/.zshrc` file:
```
echo 'export ANTHROPIC_API_KEY=sk-ant-your-key-here' >> ~/.zshrc
```

**Windows:** Search for "Environment Variables" in the Start menu, click "Edit the system environment variables", click "Environment Variables", and add a new user variable called `ANTHROPIC_API_KEY` with your key as the value.

---

## Step 4: Install Claude Code

Claude Code is the AI assistant that reads the workshop files and coaches you through the exercises.

In your terminal, type:
```
npm install -g @anthropic-ai/claude-code
```

This may take a minute. When it finishes, check it worked:
```
claude --version
```

You should see a version number. If you get a "permission denied" error on Mac, try:
```
sudo npm install -g @anthropic-ai/claude-code
```
It will ask for your computer password (the one you use to log in to your Mac).

---

## Step 5: Download the workshop

In your terminal, type these two commands one at a time:
```
git clone https://github.com/TheGinjaNinja/hub201-workshop.git
```
```
cd hub201-workshop
```

The first command downloads the workshop files. The second command moves you into the workshop folder.

---

## Step 6: Start the AI coach

Type:
```
claude
```

That is it. The AI coach will introduce itself, ask about your startup, and guide you through the exercises. It will challenge your thinking, rate your evidence, and generate professional outputs using your own branding.

---

## Tips for using Claude Code

**How to talk to it:** Just type naturally. "Let's work on our value proposition" or "I want to do the competition matrix" or "Can you explain what a beachhead is?"

**How to share files:** If the coach asks you to share your pitch deck or branding materials, you can drag files into the terminal window or paste file paths.

**How to stop:** Press `Ctrl + C` to stop Claude Code at any time. Your progress is saved in the `/outputs/` folder.

**How to restart:** Navigate back to the workshop folder (`cd hub201-workshop`) and type `claude` again.

**If something goes wrong:** Close the terminal, open a new one, set your API key again (Step 3), navigate to the folder (Step 5), and type `claude`.

---

## Alternative: Use Claude without installing anything

If you cannot or do not want to install software, you can use the workshop through a web browser:

1. Go to [claude.ai](https://claude.ai) and create a free account (or log in)
2. Start a new conversation
3. Open the file `CLAUDE.md` from this repository on GitHub: [view CLAUDE.md](https://github.com/TheGinjaNinja/hub201-workshop/blob/main/CLAUDE.md)
4. Copy the entire contents of that file
5. Paste it into the Claude chat as your first message
6. The AI coach will start guiding you through the exercises

The web version works well for the coaching conversation but cannot generate files on your computer. You will need to copy the outputs manually.

---

## Alternative: Use a different AI coding tool

The workshop works with any AI coding tool that can read project files. If you already use one of these, you do not need Claude Code:

- **Cursor:** Open the `hub201-workshop` folder. Cursor reads `CLAUDE.md` automatically.
- **Windsurf:** Open the folder. Same behaviour as Cursor.
- **GitHub Copilot (VS Code):** Open the folder and paste the contents of `CLAUDE.md` into the Copilot chat.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "command not found: node" | Restart your terminal after installing Node.js. If still broken, reinstall from nodejs.org. |
| "command not found: git" | On Mac, accept the developer tools install prompt. On Windows, install from git-scm.com. |
| "command not found: claude" | Run `npm install -g @anthropic-ai/claude-code` again. On Mac, try with `sudo` in front. |
| "Invalid API key" or "authentication error" | Check your API key is set correctly. Run `echo $ANTHROPIC_API_KEY` (Mac) or `echo $env:ANTHROPIC_API_KEY` (Windows) to see if it is set. |
| "Permission denied" on Mac | Add `sudo` before the command. Example: `sudo npm install -g @anthropic-ai/claude-code` |
| Terminal shows weird characters or looks broken | Close the terminal and open a new one. |
| "Repository not found" when cloning | Check your internet connection. The repo URL is `https://github.com/TheGinjaNinja/hub201-workshop.git` |

---

## Cost guide

Claude Code charges based on usage. Here is a rough guide:

| Activity | Estimated cost |
|----------|---------------|
| One exercise (30-45 minutes of coaching) | USD 0.25-0.50 |
| All 6 exercises in one session | USD 1.50-3.00 |
| Generating the HTML presentation | USD 0.25-0.50 |
| A full workshop day | USD 2.00-5.00 |

You can check your usage at [console.anthropic.com](https://console.anthropic.com/) under Billing.
