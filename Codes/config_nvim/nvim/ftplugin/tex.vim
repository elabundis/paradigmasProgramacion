let maplocalleader = "_"

setlocal spell spelllang=en_us
call HighlightExtraSpaces()

"------------------------------------------------
" vimtex
"------------------------------------------------
nmap <localleader>c <plug>(vimtex-compile)
nmap <localleader>C <plug>(vimtex-compile-ss)
nmap <localleader>v <plug>(vimtex-view)
nmap <localleader>i <plug>(vimtex-info)
nmap <localleader>s <plug>(vimtex-status)

" Redefine some mappings
"------------------------
" Motions
" Move across environments
nmap ]e <plug>(vimtex-]m)
xmap ]e <plug>(vimtex-]m)
omap ]e <plug>(vimtex-]m)
nmap ]E <plug>(vimtex-]M)
xmap ]E <plug>(vimtex-]M)
omap ]E <plug>(vimtex-]M)
nmap [e <plug>(vimtex-[m)
xmap [e <plug>(vimtex-[m)
omap [e <plug>(vimtex-[m)
nmap [E <plug>(vimtex-[M)
xmap [E <plug>(vimtex-[M)
omap [E <plug>(vimtex-[M)

" Move across math zones
nmap ]m <plug>(vimtex-]n)
xmap ]m <plug>(vimtex-]n)
omap ]m <plug>(vimtex-]n)
nmap ]M <plug>(vimtex-]N)
xmap ]M <plug>(vimtex-]N)
omap ]M <plug>(vimtex-]N)
nmap [m <plug>(vimtex-[n)
xmap [m <plug>(vimtex-[n)
omap [m <plug>(vimtex-[n)
nmap [M <plug>(vimtex-[N)
xmap [M <plug>(vimtex-[N)
omap [M <plug>(vimtex-[N)

" Text objects
" items inside a list (inside enumerate or itemize)
" (ai and ii mapping are taken by Vindent plugin (also useful))
omap al <Plug>(vimtex-am)
xmap al <Plug>(vimtex-am)
omap il <Plug>(vimtex-im)
xmap il <Plug>(vimtex-im)

" Sections and its variants
omap aS <Plug>(vimtex-aP)
xmap aS <Plug>(vimtex-aP)
omap iS <Plug>(vimtex-iP)
xmap iS <Plug>(vimtex-iP)

"------------------------------------------------
" surround.vim
"------------------------------------------------
" Surround with commands or environments via: 'ysc' and 'yse'
let b:surround_{char2nr("e")} 
  \ = "\\begin{\1environment: \1}\n\t\r\n\\end{\1\1}" 
let b:surround_{char2nr("c")} = "\\\1command: \1{\r}"

"------------------------------------------------
" auto-pairs
"------------------------------------------------
" Add a closing pair for $
let b:AutoPairs = AutoPairsDefine({'$' : '$'})
