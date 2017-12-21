# Projectile.nvim #

[![license](https://img.shields.io/github/license/dunstontc/projectile.nvim.svg)](https://github.com/dunstontc/projectile.nvim/blob/master/LICENSE)
[![Code Climate](https://img.shields.io/codeclimate/issues/github/me-and/mdf.svg)](https://github.com/dunstontc/projectile.nvim/issues)

> Collection of features for Vim similar to [bbatsov/projectile](https://github.com/bbatsov/projectile); using [Shougo/denite.nvim](https://github.com/Shougo/denite.nvim) for it's interfaces.  
> I wouldn't recommend using this quite yet, but if you do and you think of anything it needs that isn't already listed in [the todo file](todo.txt), let me know.

## Features ##

  - Projects
    - Keep a list of project locations with metadata
    - (WIP) Check version control status of Projects
    - List todos in a project
  - Bookmarks
    - Keep a list of bookmarked locations that can be jumped to
  - TODOs
    - List todos in the current project folder & jump to them
    - (WIP) List todos from a todo.txt file
    - (WIP) Append todos to the quickfix or location list


## Usage ##
### Requirements ###
  - [Shougo/denite.nvim](https://github.com/Shougo/denite.nvim)
  - Vim or Neovim with Python3 support

### Configuration ###
  - Data is persisted in in `$XDG_CACHE_HOME/projectile` or `~/.cache/projectile/`by default.  

```viml
let g:projectile#data_dir = '~/.cache/.projectile'
let g:projectile#directory_command = ''
let g:todo_plugin#todo_terms = ['TODO', 'FIXME', 'XXX']
let g:projectile#search_prog = 'grep'
let g:projectile#disable_devicons = 0
```


## Denite Sources ##
```viml
:Denite projectile
```
  - *Add*
  - *Remove*
  - *Open (default)*
  - *Cd*

```viml
:Denite bookmark
```
  - *Add*
  - *Remove*
  - *Open (default)*

```viml
:Denite todo
```
  - *Jump (default)*


## Related Projects ##
  - [projectile](https://github.com/bbatsov/projectile)
  - [vim-rooter](https://github.com/airblade/vim-rooter)
  - [vim-projectionist](https://github.com/tpope/vim-projectionist)
  - [vim-bookmarks](https://github.com/MattesGroeger/vim-bookmarks)
  - [TaskList.vim](https://github.com/vim-scripts/TaskList.vim)
  - [searchtasks.vim](https://github.com/gilsondev/searchtasks.vim)
  - [todolist.vim](vim-scripts/todolist.vim)
  - [vim-todo](https://github.com/codegram/vim-todo)
  - [gather-todo.txt-vim](https://github.com/lgalke/gather-todo.txt-vim)

## Credit & Thanks ##

- [Shougo/denite.nvim](https://github.com/Shougo/denite.nvim)
- [neoclide/denite-git](https://github.com/neoclide/denite-git)
- [chemzqm/denite-extra](https://github.com/chemzqm/denite-extra)
- [rafi/vim-denite-session](https://github.com/rafi/vim-denite-session)
- [SpaceVim](https://github.com/SpaceVim/SpaceVim)

