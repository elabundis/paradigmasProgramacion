" Plugins (downloaded under the specified directory)
call plug#begin(has('nvim') ? stdpath('data') . '/plugged' : '~/.vim/plugged')

" Color Schemes
Plug 'jnurmine/Zenburn'
Plug 'ellisonleao/gruvbox.nvim'

" Status bar with useful information
" Plug 'vim-airline/vim-airline'
Plug 'nvim-lualine/lualine.nvim'
" If you want to have icons in your statusline choose one of these
Plug 'nvim-tree/nvim-web-devicons'

" Fancy file browser
Plug 'scrooloose/nerdtree'

" Fuzzy finder of files and their contents
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'

" Display indentation
Plug 'lukas-reineke/indent-blankline.nvim'

" Improve indentation-based code folding
Plug 'tmhedberg/SimpylFold'

" Improve auto indentation of python files
Plug 'vim-scripts/indentpython.vim'

" Automatically close parenthesis and the like
Plug 'jiangmiao/auto-pairs'

" Easily surround with parenthesis or tags
Plug 'tpope/vim-surround'

" Delete or change surrounding functions (dsf or csf)
Plug 'AndrewRadev/dsf.vim'

" Repeat commands from plugins with . (not just built-in ones)
Plug 'tpope/vim-repeat'

" Syntax highliting for many languages
Plug 'sheerun/vim-polyglot'

" PEP 8 checking (backend for syntastic)
Plug 'nvie/vim-flake8'

" Comment stuff up with a key stroke for all languages
Plug 'tpope/vim-commentary'

" Send code to a REPL
Plug 'jpalardy/vim-slime'

" Indentation motion and selection (extremely useful in python)
Plug 'jessekelighine/vindent.vim'

" Preview HTML (CSS and JavaScript), Markdown, AsciiDoc y SVG
" (LivePreview start)
Plug 'brianhuster/live-preview.nvim'

" Preview markdown in your browser
" (MarkdownPreview)
Plug 'iamcco/markdown-preview.nvim', { 'do': 'cd app && npx --yes yarn install' }

" Preview github flavor Markdown (requires bun) 
" (GithubPreviewStart)
" Plug 'wallpants/github-preview.nvim'

" Snippets for html code
Plug 'mattn/emmet-vim'

" Close html tags
Plug 'alvan/vim-closetag'

" When a tag is modified, it updates the correspondind closing (opening) tag
Plug 'AndrewRadev/tagalong.vim'

" CSS color highlighter
Plug 'ap/vim-css-color'

" Latex syntax, snippets, and more
Plug 'lervag/vimtex'

" Snippets engine. YouCompleteMe adds autocompletion.
" I prefer to use coc-snippets since I use coc for autocompletion. 
" Uncomment if not planning to use coc. 
" Plug 'SirVer/ultisnips'

" Good initial set of snippets
Plug 'honza/vim-snippets'

" Use git within the editor with extra features
Plug 'tpope/vim-fugitive'

" Improve git log in fugitive: uses --graph with syntax highliting and
" fugitive features (move among commits, open them, etc)
Plug 'junegunn/gv.vim'

" Completions based on Language Server Protocols
Plug 'neoclide/coc.nvim', {'branch': 'release'}

" List ends here. Plugins become visible to Vim after this call.
call plug#end()


" My Leader character
let mapleader = ","

" Colors 
" Enable 256 colors palette in Gnome Terminal
if $COLORTERM == 'gnome-terminal'
    set t_Co=256
endif
colorscheme gruvbox
set background=light

" set mouse=a               	     " Enable mouse on all modes
set clipboard=unnamed,unnamedplus    " Use the OS clipboard

" Keep 'so' lines of context around cursor
set so=0

set number
set cursorline

set nohls

" Browse through help more easily by moving words to next line
" when they don't fit on screen
autocmd FileType help setlocal linebreak breakindent

" Easily move to alternate file
nnoremap <F1> :b#<CR>

" When editing a file, always jump to the last known cursor position.
" Don't do it when the position is invalid, when inside an event handler
autocmd BufReadPost *
\ if line("'\"") >= 1 && line("'\"") <= line("$") && &ft !~# 'commit'
\ |   exe "normal! g`\""
\ | endif

" Indentation for full stack development
au BufNewFile,BufRead *.js,*.html,*.css,*.php
    \ set tabstop=2       |
    \ set softtabstop=2   |
    \ set shiftwidth=2    |
    \ set expandtab

" Keep VisualMode after indent with > or <
vmap < <gv
vmap > >gv

"split navigations
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" Spelling
autocmd FileType markdown,gitcommit setlocal spell spelllang=en_us

" Highlight extra white space
highlight BadWhitespace ctermbg=red guibg=darkred
fun! HighlightExtraSpaces()
    match BadWhitespace /\s\+$/
endfun

" Automatically flag unnecessary whitespace on desired filetypes
au BufRead,BufNewFile *.pyw,*.c,*.h :call HighlightExtraSpaces()

" Delete trailing white space on save, useful for some filetypes ;)
fun! CleanExtraSpaces()
    let save_cursor = getpos(".")
    let old_query = getreg('/')
    silent! %s/\s\+$//e
    call setpos('.', save_cursor)
    call setreg('/', old_query)
endfun

if has("autocmd")
    autocmd BufWritePre *.txt,*.js,*.wiki,*.sh,*.coffee :call CleanExtraSpaces()
endif

" Enable folding
set foldmethod=indent
set foldlevel=99
" Enable folding with the spacebar
nnoremap <space> za
" Show docstring for folded code 
let g:SimpylFold_docstring_preview=1

" Have :grep use ripgrep instead of the command line grep
set grepprg=rg\ --vimgrep\ --smart-case\ --follow

" Allow to add project especific configurations on top of global and filetype settings
" (add .exrc file at project root)
set exrc

" Allow plugins that depend on python (autocompletion usually depends on it)
let g:python3_host_prog = '/Users/jesus/.pyenv/versions/py3nvim/bin/python'

" -------------------------------------------------------------
" Settings for correct functioning of coc
" -------------------------------------------------------------
" " Some servers have issues with backup files
set nobackup
set nowritebackup

" Having longer updatetime (default is 4000 ms = 4s) leads to noticeable
" delays and poor user experience
set updatetime=300

" Always show the signcolumn, otherwise it would shift the text each time
" diagnostics appear/become resolved
set signcolumn=yes


" Plugin settings (individual files are used for plugins that require much
" configuration)

" -------------------------------------------------------------
" => Vim-slime
" -------------------------------------------------------------
" Configure vim-slime to work with tmux (use ctrl+c+c)
let g:slime_target = "tmux"
let g:slime_default_config = {"socket_name": "default", "target_pane": "{last}"}
let g:slime_bracketed_paste = 1  " copy correct indentation onto ipython

" -------------------------------------------------------------
" => emmet-vim
" -------------------------------------------------------------
let g:user_emmet_install_global = 0
autocmd FileType html,htmldjango,css,php EmmetInstall
" To trigger emmet we use the vim <leader> followed by the emmet <leader>
let g:user_emmet_leader_key=','

" -------------------------------------------------------------
" => ultisnips 
" (when plugin is installed. I use  coc-snippets instead)
" -------------------------------------------------------------
" let g:UltiSnipsExpandTrigger="<tab>"
" let g:UltiSnipsJumpForwardTrigger="<tab>"
" let g:UltiSnipsJumpBackwardTrigger="<s-tab>"  " shift + tab

" Directories to read the snippets from
" let g:UltiSnipsSnippetDirectories=[$HOME.'/.config/nvim/UltiSnips']

" -------------------------------------------------------------
" => coc-snippets
" -------------------------------------------------------------
let g:coc_snippet_next = '<tab>'

" Use <leader>x to convert visually selected code into snippet
xmap <leader>x  <Plug>(coc-convert-snippet)


" Start lualine statusline
lua << END
require('lualine').setup {
	options = {
		icons_enabled = true,
		theme = 'gruvbox',
		section_separators = '',
		component_separators = ''
	},
  extensions = {'quickfix', 'fugitive', 'fzf'},
}

require("ibl").setup()
END

