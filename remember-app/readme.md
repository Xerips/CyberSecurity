# Remember-app

![showcase]()

**Description**: A simple app to write down and recall useful commands from the command line.

If you're like me, you run through HackTheBox machines, books, and other training resources taking notes of commands to use on live targets in Obsidian or CherryTree. These get bloated, you have to search through them for what you're looking for and it can take some time. It also takes you out of the command line, and fills more of your screen(s) with yet another window for your note taking app.

I didn't like this! I've lost those note files, or have different notes on different machines or note taking apps, and it's generally a pain.  
Even autosuggest for the command line doesn't always find what you're actually looking for and I found myself typing and retyping commands to try and populate the one obscure command I was hoping to find!

So! I've created this little app to help me quickly add useful commands to a file from the command line, then search those commands when I'm trying to remember them.

## remember_this.py

- Use this to write commands or notes into a file that will be located in the directory of the script.
- I recommend using an alias for this: Instead of writing out `python3 /PATH/TO/remember_this.py <arguments>` set an alias to something like `rememberthis` for easier usage.
- There is no set convention for what you put in headers, descriptions, or commands.
  - Create your own system by adding keywords to the description that help you find what you're looking for.

**Usage:**

- Use with command line arguments:
  `python3 remember_this.py -H <Header/Title you want to use> -D <Description of the command or note> -C <Command or note>`

- Use with interactive mode:
  `python3 remember_this.py -i`

  - This will prompt you for a header, then a description, then the command.

- Add the `-v` flag for verbose. This will print out the entire contents found under the Header you've added to.

  - Works with both interactive mode and with command line arguments.

## remember.py

- Use this to "remember" what you've added with `remember_this.py`.
- I recommend using an alias for this as well and setting it to something like `remember`.

**Usage:**

- List all of the content in the directory:
  `python3 remember.py --all`

- Search for keywords in the description:
  `python3 remember.py --search <keyword>`

  - Searches are not case sensitive.

- Print the contents of a Header:
  `python3 remember.py <Header>`
  - ex.
    `python3 remember.py Nmap`

I hope you find this useful!
